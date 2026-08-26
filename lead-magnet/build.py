#!/usr/bin/env python3
"""Сборка PDF рабочей тетради.

    python3 build.py                      # собрать out/<файл>.pdf
    python3 build.py --preview            # + PNG-превью страниц в build/preview
    python3 build.py --content другой.yaml

Этапы:
  YAML → HTML (tools/render.py) → Chromium → design.pdf
  → из ссылок-маркеров достаём координаты → ReportLab делает слой полей формы
  → pypdf кладёт дизайн под слой полей → готовый заполняемый PDF.
"""
from __future__ import annotations

import argparse
import glob
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.parse

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
import render  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent
BUILD = ROOT / "build"
OUT = ROOT / "out"

INK = (0.298, 0.039, 0.102)      # #4C0A1A — цвет, которым «пишет» пользователь


# --------------------------------------------------------------------- chromium
def chromium() -> str:
    env = shutil.which("chromium") or shutil.which("google-chrome")
    if env:
        return env
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium/chrome-linux/chrome"):
        found = sorted(glob.glob(pat))
        if found:
            return found[-1]
    sys.exit("Не найден Chromium — укажите путь через переменную CHROME.")


def run_chromium(args: list[str]) -> str:
    cmd = [chromium(), "--headless", "--disable-gpu", "--no-sandbox",
           "--disable-dev-shm-usage", "--virtual-time-budget=4000", *args]
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.stdout + p.stderr


def html_to_pdf(html_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    log = run_chromium([
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path.as_uri(),
    ])
    if not pdf_path.exists():
        sys.exit("Chromium не создал PDF:\n" + log)


def check_overflow(doc: dict) -> list[str]:
    """Считает, не вылезает ли содержимое за границы страниц."""
    probe = BUILD / "_measure.html"
    probe.write_text(render.render_document(doc, measure=True), encoding="utf-8")
    dom = run_chromium(["--dump-dom", probe.as_uri()])
    m = re.search(r'id="overflow-report">([^<]*)<', dom)
    if not m or m.group(1) == "ok":
        return []
    return [x for x in m.group(1).split(",") if x]


# --------------------------------------------------------------------- поля формы
def collect_fields(pdf_path: pathlib.Path):
    """Достаёт из design.pdf ссылки-маркеры → список описаний полей."""
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        box = page.mediabox
        size = (float(box.width), float(box.height))
        fields = []
        for ref in (page.get("/Annots") or []):
            a = ref.get_object()
            uri = (a.get("/A") or {}).get("/URI", "")
            if not str(uri).startswith(render.FIELD_HOST):
                continue
            parsed = urllib.parse.urlparse(str(uri))
            name = parsed.path.lstrip("/")
            kind = urllib.parse.parse_qs(parsed.query).get("t", ["line"])[0]
            x0, y0, x1, y1 = (float(v) for v in a["/Rect"])
            fields.append({
                "name": name, "kind": kind,
                "x": min(x0, x1), "y": min(y0, y1),
                "w": abs(x1 - x0), "h": abs(y1 - y0),
            })
        pages.append({"size": size, "fields": fields})
    return pages


def build_field_layer(pages, layer_path: pathlib.Path, meta: dict) -> int:
    """Прозрачный PDF того же формата, где живут настоящие поля формы."""
    from reportlab.lib.colors import Color
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas

    # ReportLab умеет ставить в поля формы только стандартные PDF-шрифты.
    # Helvetica + NeedAppearances: просмотрщик сам подставит начертание
    # с кириллицей, когда пользователь начнёт печатать.
    font_name = "Helvetica"

    ink = Color(*INK)
    c = canvas.Canvas(str(layer_path), pagesize=pages[0]["size"])
    c.setTitle(meta.get("title", "Рабочая тетрадь"))
    c.setAuthor(meta.get("author", ""))
    c.setSubject(meta.get("subtitle", ""))
    total = 0

    for page in pages:
        c.setPageSize(page["size"])
        form = c.acroForm
        for f in page["fields"]:
            total += 1
            if f["kind"] == "check":
                size = min(f["w"], f["h"])
                form.checkbox(
                    name=f["name"], x=f["x"] + (f["w"] - size) / 2,
                    y=f["y"] + (f["h"] - size) / 2, size=size,
                    buttonStyle="check", borderWidth=0, forceBorder=False,
                    borderColor=None, fillColor=None, textColor=ink,
                    checked=False,
                )
            else:
                multiline = f["kind"] == "multiline"
                form.textfield(
                    name=f["name"], x=f["x"], y=f["y"],
                    width=f["w"], height=f["h"],
                    borderWidth=0, forceBorder=False,
                    borderColor=None, fillColor=None, textColor=ink,
                    fontName=font_name, fontSize=10.5,
                    fieldFlags="multiline" if multiline else "",
                    relative=False,
                )
        c.showPage()
    c.save()
    return total


def compose(design: pathlib.Path, layer: pathlib.Path, out: pathlib.Path, meta: dict) -> None:
    """Кладёт дизайн под слой с полями и сохраняет результат."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import BooleanObject, NameObject

    writer = PdfWriter(clone_from=str(layer))
    design_reader = PdfReader(str(design))

    for i, page in enumerate(writer.pages):
        page.merge_page(design_reader.pages[i], over=False)

    root = writer._root_object
    if "/AcroForm" in root:
        root["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)

    writer.add_metadata({
        "/Title": meta.get("title", "Рабочая тетрадь"),
        "/Author": meta.get("author", ""),
        "/Subject": meta.get("subtitle", ""),
        "/Keywords": meta.get("keywords", ""),
        "/Creator": meta.get("brand", ""),
    })
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as fh:
        writer.write(fh)


def make_preview(pdf: pathlib.Path, out_dir: pathlib.Path, dpi: int = 90) -> None:
    if not shutil.which("pdftoppm"):
        print("· pdftoppm не установлен — превью пропущено")
        return
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(pdf),
                    str(out_dir / "page")], check=True)
    print(f"· превью: {out_dir}")


# --------------------------------------------------------------------- main
def main() -> None:
    ap = argparse.ArgumentParser(description="Сборка PDF рабочей тетради")
    ap.add_argument("--content", default="content/workbook.yaml")
    ap.add_argument("--out", default=None, help="путь к итоговому PDF")
    ap.add_argument("--preview", action="store_true", help="сделать PNG-превью страниц")
    ap.add_argument("--no-fields", action="store_true", help="без интерактивных полей")
    args = ap.parse_args()

    BUILD.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)

    src = (ROOT / args.content) if not pathlib.Path(args.content).is_absolute() else pathlib.Path(args.content)
    doc = yaml.safe_load(src.read_text(encoding="utf-8"))
    meta = doc.get("meta", {})

    html_path = BUILD / "workbook.html"
    html_path.write_text(render.render_document(doc), encoding="utf-8")
    print(f"· макет: {html_path.name} ({len(doc['pages'])} стр.)")

    over = check_overflow(doc)
    if over:
        for item in over:
            page, px = item.split(":")
            print(f"  ⚠ страница {page}: содержимое не помещается (+{px}px)")
    else:
        print("· проверка вёрстки: всё помещается")

    design = BUILD / "design.pdf"
    html_to_pdf(html_path, design)

    out_path = pathlib.Path(args.out) if args.out else OUT / (
        render.slug(meta.get("file_name") or meta.get("title", "workbook"), "workbook") + ".pdf"
    )

    if args.no_fields:
        shutil.copy(design, out_path)
        print(f"· без полей формы → {out_path}")
    else:
        pages = collect_fields(design)
        layer = BUILD / "fields.pdf"
        n = build_field_layer(pages, layer, meta)
        compose(design, layer, out_path, meta)
        print(f"· интерактивных полей: {n}")

    size_kb = round(out_path.stat().st_size / 1024)
    print(f"✓ готово: {out_path}  ({size_kb} KB)")

    if args.preview:
        make_preview(out_path, BUILD / "preview")


if __name__ == "__main__":
    main()
