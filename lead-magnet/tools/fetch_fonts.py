#!/usr/bin/env python3
"""Скачивает нужные подмножества шрифтов Google Fonts и собирает
самодостаточный assets/fonts/fonts.css с base64-встраиванием.

Запускается один раз (или после изменения списка FAMILIES).
Дальше сборка PDF работает полностью офлайн.
"""
import base64
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "assets" / "fonts"

# Подмножества, которые реально нужны для русского текста
KEEP = {"cyrillic", "cyrillic-ext", "latin", "latin-ext"}

FAMILIES = [
    "Playfair+Display:ital,wght@0,500;0,600;0,700;1,500",
    "Inter:wght@300;400;500;600;700",
]

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main() -> None:
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    faces: dict[tuple, dict] = {}

    for fam in FAMILIES:
        url = f"https://fonts.googleapis.com/css2?family={fam}&display=swap"
        css = get(url).decode("utf-8")
        blocks = re.findall(r"/\* ([a-z\-]+) \*/\s*@font-face \{(.*?)\}", css, re.S)
        for subset, body in blocks:
            if subset not in KEEP:
                continue
            family = re.search(r"font-family: '([^']+)'", body).group(1)
            style = re.search(r"font-style: (\w+)", body).group(1)
            weight = int(re.search(r"font-weight: (\d+)", body).group(1))
            rng = re.search(r"unicode-range: ([^;]+);", body).group(1).strip()
            woff_url = re.search(r"url\((https://[^)]+\.woff2)\)", body).group(1)

            name = woff_url.rsplit("/", 1)[-1]
            path = FONT_DIR / name
            if not path.exists():
                path.write_bytes(get(woff_url))
                print("↓", name, path.stat().st_size, "b")

            # один @font-face на файл: веса схлопываем в диапазон (шрифты variable)
            key = (family, style, name)
            face = faces.setdefault(
                key, {"min": weight, "max": weight, "range": rng, "path": path}
            )
            face["min"] = min(face["min"], weight)
            face["max"] = max(face["max"], weight)

    css_out = ["/* Сгенерировано tools/fetch_fonts.py — не редактировать вручную */"]
    for (family, style, _), f in faces.items():
        data = base64.b64encode(f["path"].read_bytes()).decode("ascii")
        w = str(f["min"]) if f["min"] == f["max"] else f'{f["min"]} {f["max"]}'
        css_out.append(
            "@font-face{"
            f"font-family:'{family}';font-style:{style};font-weight:{w};"
            "font-display:block;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');"
            f"unicode-range:{f['range']};"
            "}"
        )

    out = FONT_DIR / "fonts.css"
    out.write_text("\n".join(css_out), encoding="utf-8")
    print("✓ fonts.css:", round(out.stat().st_size / 1024), "KB,", len(faces), "начертаний")


if __name__ == "__main__":
    main()
