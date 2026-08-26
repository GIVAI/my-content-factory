#!/usr/bin/env python3
"""YAML с содержанием  →  HTML-макет рабочей тетради (A4).

Каждое поле для заполнения помечается невидимой ссылкой
https://field.local/<имя>?t=<тип>. Chromium превращает такие ссылки
в link-аннотации PDF, а build.py заменяет их на настоящие поля формы.
"""
from __future__ import annotations

import html
import pathlib
import re
from typing import Any

import images

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FIELD_HOST = "https://field.local"
PHOTO_OUT = ROOT / "build" / "img"


def photo_url(src: str) -> str:
    """Путь к фотографии → готовый к вёрстке file://-адрес."""
    path = pathlib.Path(src)
    if not path.is_absolute():
        path = ROOT / path
    if not path.exists():
        raise FileNotFoundError(f"Не найдена фотография: {src}")
    return images.prepare(path, PHOTO_OUT).as_uri()


def photo_bg(photo) -> str:
    """Инлайн-стиль: фотография как фон с бордовой заливкой поверх."""
    if not photo:
        return ""
    if isinstance(photo, str):
        photo = {"src": photo}
    tint = float(photo.get("tint", 0.82))
    pos = photo.get("position", "center 30%")
    return (
        ' style="background-image:'
        f"linear-gradient(168deg, rgba(90,14,30,{tint}) 0%, rgba(59,7,19,{min(tint + .08, 1):.2f}) 100%),"
        f"url({photo_url(photo['src'])});"
        f'background-size:cover;background-position:{pos}"'
    )


# --------------------------------------------------------------------------- утилиты
def esc(text: Any) -> str:
    """Экранирует текст, но оставляет простую разметку: **жирный**, *курсив*, ==выделение==."""
    s = html.escape(str(text if text is not None else ""))
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"==(.+?)==", r'<span class="hl">\1</span>', s)
    s = s.replace(" — ", "&nbsp;— ").replace("\n", "<br>")
    return s


def slug(text: str, fallback: str) -> str:
    tr = str.maketrans(
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "abvgdeejzijklmnoprstufhccss_y_eua",
    )
    s = str(text).lower().translate(tr)
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")[:40]
    return s or fallback


class FieldNamer:
    """Гарантирует уникальные имена полей формы."""

    def __init__(self) -> None:
        self.used: set[str] = set()
        self.n = 0

    def make(self, hint: str = "") -> str:
        self.n += 1
        base = f"{self.n:03d}_{slug(hint, 'pole')}"
        name = base
        i = 2
        while name in self.used:
            name, i = f"{base}_{i}", i + 1
        self.used.add(name)
        return name


def anchor(name: str, kind: str, style: str = "inset:0") -> str:
    """Невидимая ссылка-маркер будущего поля формы."""
    return (
        f'<a class="pdf-field" style="{style}" '
        f'href="{FIELD_HOST}/{name}?t={kind}">&nbsp;</a>'
    )


# --------------------------------------------------------------------------- блоки
def render_block(b: dict, fn: FieldNamer) -> str:
    t = b.get("type", "text")

    if t == "text":
        return f'<p>{esc(b["text"])}</p>'

    if t == "lead":
        return f'<p class="lead">{esc(b["text"])}</p>'

    if t == "note":
        return f'<p class="note">{esc(b["text"])}</p>'

    if t == "heading":
        return f'<h3 class="subtitle">{esc(b["text"])}</h3>'

    if t in ("list", "numbered"):
        tag = "ul" if t == "list" else "ol"
        items = "".join(f"<li>{esc(i)}</li>" for i in b["items"])
        return f'<{tag} class="list">{items}</{tag}>'

    if t == "quote":
        cite = f'<cite>{esc(b["author"])}</cite>' if b.get("author") else ""
        return f'<blockquote class="quote"><p>{esc(b["text"])}</p>{cite}</blockquote>'

    if t == "callout":
        title = (
            f'<div class="callout__title">{esc(b["title"])}</div>'
            if b.get("title")
            else ""
        )
        body = "".join(f"<p>{esc(p)}</p>" for p in as_list(b.get("text", "")))
        return f'<div class="callout">{title}{body}</div>'

    if t == "panel":
        inner = "".join(render_block(x, fn) for x in b.get("blocks", []))
        return f'<div class="panel">{inner}</div>'

    if t == "spacer":
        return f'<div class="spacer" style="height:{b.get("size", 6)}mm"></div>'

    if t == "field":
        return render_field(b, fn)

    if t == "box":
        return render_box(b, fn)

    if t == "checklist":
        return render_checklist(b, fn)

    if t == "grid":
        return render_grid(b, fn)

    if t == "scale":
        return render_scale(b, fn)

    if t == "duo":
        return render_duo(b, fn)

    if t == "image":
        style = f'height:{b["height"]}mm' if b.get("height") else ""
        radius = b.get("radius", 2)
        caption = (
            f'<figcaption class="photo__caption">{esc(b["caption"])}</figcaption>'
            if b.get("caption") else ""
        )
        fit = b.get("fit", "cover")
        pos = b.get("position", "center 30%")
        return (
            f'<figure class="photo" style="{style};border-radius:{radius}mm">'
            f'<img src="{photo_url(b["src"])}" alt="" '
            f'style="object-fit:{fit};object-position:{pos}">'
            f"{caption}</figure>"
        )

    if t == "card":
        nums = f'<div class="card__num">{esc(b["number"])}</div>' if b.get("number") else ""
        body = "".join(f"<p>{esc(x)}</p>" for x in as_list(b.get("text", [])))
        return (
            f'<div class="card">{nums}<div class="card__body">'
            f'<div class="card__title">{esc(b["title"])}</div>{body}</div></div>'
        )

    if t == "options":
        return render_options(b, fn)

    if t == "numbered_lines":
        return render_numbered_lines(b, fn)

    if t == "cols":
        cols = "".join(
            f'<div>{"".join(render_block(x, fn) for x in col)}</div>'
            for col in b["columns"]
        )
        return f'<div class="cols">{cols}</div>'

    raise ValueError(f"Неизвестный тип блока: {t}")


def as_list(v: Any) -> list:
    return v if isinstance(v, list) else [v]


def field_head(b: dict) -> str:
    out = ""
    if b.get("label"):
        q = f'<span class="q">{esc(b["q"])}</span>' if b.get("q") else ""
        out += f'<div class="field__label">{q}<span>{esc(b["label"])}</span></div>'
    if b.get("ask"):
        out += f'<p class="field__ask">{esc(b["ask"])}</p>'
    if b.get("hint"):
        out += f'<p class="field__hint">{esc(b["hint"])}</p>'
    return out


def render_field(b: dict, fn: FieldNamer) -> str:
    """Подпись + N линеек, на каждой — отдельное однострочное поле."""
    n = int(b.get("lines", 3))
    base = b.get("label") or b.get("ask") or "otvet"
    lines = ""
    for i in range(n):
        name = fn.make(f"{slug(base, 'otvet')}_{i + 1}")
        lines += (
            '<div class="line">'
            + anchor(name, "line", "left:1mm;right:1mm;top:1mm;bottom:.6mm")
            + "</div>"
        )
    return f'<div class="field">{field_head(b)}<div class="lines">{lines}</div></div>'


def render_box(b: dict, fn: FieldNamer) -> str:
    """Подпись + рамка для свободного текста (многострочное поле)."""
    h = float(b.get("height", 34))
    ruled = " boxfield--ruled" if b.get("ruled", True) else ""
    name = fn.make(slug(b.get("label") or b.get("ask") or "blok", "blok"))
    grow = b.get("grow", False)
    cls = "field field--grow" if grow else "field"
    style = "" if grow else f'style="height:{h}mm"'
    return (
        f'<div class="{cls}">{field_head(b)}'
        f'<div class="boxfield{ruled}" {style}>'
        + anchor(name, "multiline", "left:1.5mm;right:1.5mm;top:1.5mm;bottom:1.5mm")
        + "</div></div>"
    )


def render_checklist(b: dict, fn: FieldNamer) -> str:
    items = ""
    for i, text in enumerate(b["items"]):
        name = fn.make(f"chk_{slug(b.get('label', ''), 'sp')}_{i + 1}")
        items += (
            '<li><span class="checkbox">'
            + anchor(name, "check", "inset:0")
            + f"</span><span>{esc(text)}</span></li>"
        )
    return f'<div class="field">{field_head(b)}<ul class="checklist">{items}</ul></div>'


def render_grid(b: dict, fn: FieldNamer) -> str:
    cols = b["columns"]
    rows = int(b.get("rows", 4))
    height = b.get("row_height", 11)
    head = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = ""
    for r in range(rows):
        tds = ""
        for c in range(len(cols)):
            name = fn.make(f"{slug(b.get('label', 'tab'), 'tab')}_{r + 1}_{c + 1}")
            tds += (
                f'<td style="height:{height}mm">'
                + anchor(name, "line", "left:1.5mm;right:1.5mm;top:0;bottom:0")
                + "</td>"
            )
        body += f"<tr>{tds}</tr>"
    return (
        f'<div class="field">{field_head(b)}'
        f'<table class="grid"><thead><tr>{head}</tr></thead>'
        f"<tbody>{body}</tbody></table></div>"
    )


def render_scale(b: dict, fn: FieldNamer) -> str:
    lo, hi = int(b.get("min", 1)), int(b.get("max", 10))
    dots = ""
    for v in range(lo, hi + 1):
        name = fn.make(f"{slug(b.get('label', 'shkala'), 'shkala')}_{v}")
        dots += (
            f'<div class="scale__dot">{v}' + anchor(name, "check", "inset:0") + "</div>"
        )
    ends = (
        f'<div class="scale__ends"><span>{esc(b.get("min_label", ""))}</span>'
        f'<span>{esc(b.get("max_label", ""))}</span></div>'
    )
    return (
        f'<div class="field scale">{field_head(b)}'
        f'<div class="scale__row">{dots}</div>{ends}</div>'
    )


def render_options(b: dict, fn: FieldNamer) -> str:
    """Вопрос + варианты ответа с галочками (Да / Иногда / Нет)."""
    rows = ""
    for i, item in enumerate(b["items"]):
        opts = ""
        for j, choice in enumerate(item.get("choices", ["Да", "Нет"])):
            name = fn.make(f"opt_{slug(b.get('label', 'v'), 'v')}_{i + 1}_{j + 1}")
            opts += (
                '<span class="opt"><span class="checkbox">'
                + anchor(name, "check", "inset:0")
                + f"</span>{esc(choice)}</span>"
            )
        rows += (
            f'<li><p class="options__q">{esc(item["text"])}</p>'
            f'<div class="options__row">{opts}</div></li>'
        )
    return f'<div class="field">{field_head(b)}<ul class="options">{rows}</ul></div>'


def render_numbered_lines(b: dict, fn: FieldNamer) -> str:
    """Пронумерованные строчки для списка ответов (1…5)."""
    n = int(b.get("count", 5))
    base = slug(b.get("label") or b.get("ask") or "spisok", "spisok")
    rows = ""
    for i in range(n):
        name = fn.make(f"{base}_{i + 1}")
        rows += (
            f'<div class="nline"><span class="nline__num">{i + 1}</span>'
            '<span class="nline__rule">'
            + anchor(name, "line", "left:1mm;right:1mm;top:1mm;bottom:.6mm")
            + "</span></div>"
        )
    return f'<div class="field">{field_head(b)}<div class="nlines">{rows}</div></div>'


def render_duo(b: dict, fn: FieldNamer) -> str:
    sides = ""
    for side in b["sides"]:
        n = int(side.get("lines", 5))
        lines = ""
        for i in range(n):
            name = fn.make(f"{slug(side.get('label', 'duo'), 'duo')}_{i + 1}")
            lines += (
                '<div class="line">'
                + anchor(name, "line", "left:1mm;right:1mm;top:1mm;bottom:.6mm")
                + "</div>"
            )
        sides += (
            '<div class="duo__side">'
            f'<div class="duo__cap">{esc(side["label"])}</div>'
            f'<div class="lines">{lines}</div></div>'
        )
    return f'<div class="field">{field_head(b)}<div class="duo">{sides}</div></div>'


# --------------------------------------------------------------------------- страницы
def render_offer(offer) -> str:
    """Блок с ценой на финальной странице.

    offer: строка (простой текст) либо словарь
    {note, price, old_price, caption}.
    """
    if not offer:
        return ""
    if isinstance(offer, str):
        return f'<div class="offer"><div class="offer__caption">{esc(offer)}</div></div>'

    parts = ""
    if offer.get("note"):
        parts += f'<div class="offer__note">{esc(offer["note"])}</div>'
    row = ""
    if offer.get("price"):
        row += f'<span class="offer__price">{esc(offer["price"])}</span>'
    if offer.get("old_price"):
        row += f'<span class="offer__old">{esc(offer["old_price"])}</span>'
    if row:
        parts += f'<div class="offer__row">{row}</div>'
    if offer.get("caption"):
        parts += f'<div class="offer__caption">{esc(offer["caption"])}</div>'
    return f'<div class="offer">{parts}</div>'


def render_page(p: dict, meta: dict, folio: int, fn: FieldNamer) -> str:
    t = p.get("type", "content")

    if t == "cover":
        title = esc(p.get("title", meta.get("title", "")))
        title_style = f' style="font-size:{p["title_size"]}"' if p.get("title_size") else ""
        cover_bg = photo_bg(p.get("photo"))
        seal = p.get("seal", "Рабочая\nтетрадь").replace("\n", "<br>")
        return f"""
<section class="page page--cover">
  <div class="cover__top"{cover_bg}>
    <div>
      <div class="cover__head">
        <div class="cover__eyebrow">{esc(p.get('eyebrow', 'Рабочая тетрадь'))}</div>
        <div class="cover__note">{esc(p.get('note', ''))}</div>
      </div>
      <div class="cover__rule"></div>
    </div>
    <div>
      <h1 class="cover__title"{title_style}>{title}</h1>
      <p class="cover__sub">{esc(p.get('subtitle', ''))}</p>
    </div>
  </div>
  <div class="cover__bottom">
    <div class="cover__for">{esc(p.get('for_whom', ''))}</div>
    <div class="cover__sign">
      <div>
        <p class="cover__author">{esc(meta.get('author', ''))}</p>
        <p class="cover__role">{esc(meta.get('role', ''))}</p>
      </div>
      <div class="cover__seal">{seal}</div>
    </div>
  </div>
</section>"""

    if t == "divider":
        divider_bg = photo_bg(p.get("photo"))
        return f"""
<section class="page page--divider"{divider_bg}>
  <div class="divider__num">{esc(p.get('number', ''))}</div>
  <h2 class="divider__title">{esc(p.get('title', ''))}</h2>
  <p class="divider__caption">{esc(p.get('caption', ''))}</p>
  <div class="divider__foot">
    <span class="brand">{esc(meta.get('brand', ''))}</span>
    <span class="folio">{folio:02d}</span>
  </div>
</section>"""

    if t == "outro":
        contacts = "".join(
            f"<div>{esc(c)}</div>" for c in p.get("contacts", [])
        )
        outro_bg = photo_bg(p.get("photo"))
        cta = (
            f'<a class="cta" href="{html.escape(p["cta_url"])}">{esc(p["cta"])}</a>'
            if p.get("cta")
            else ""
        )
        offer = render_offer(p.get("offer"))
        return f"""
<section class="page page--outro"{outro_bg}>
  <h2>{esc(p.get('title', ''))}</h2>
  <p>{esc(p.get('text', ''))}</p>
  {offer}
  {cta}
  <div class="outro__contacts">{contacts}</div>
  <div class="divider__foot">
    <span class="brand">{esc(meta.get('brand', ''))}</span>
    <span class="folio">{folio:02d}</span>
  </div>
</section>"""

    # обычная страница
    body = "".join(render_block(b, fn) for b in p.get("blocks", []))
    title = f'<h2 class="title">{esc(p["title"])}</h2>' if p.get("title") else ""
    body_cls = "page__body page__body--fill" if p.get("fill") else "page__body"
    return f"""
<section class="page page--content">
  <header class="page__head">
    <span class="kicker">{esc(p.get('kicker', meta.get('brand', '')))}</span>
    <span class="kicker">{esc(p.get('kicker_right', ''))}</span>
  </header>
  <div class="{body_cls}">{title}{body}</div>
  <footer class="page__foot">
    <span class="brand">{esc(meta.get('brand', ''))}</span>
    <span class="folio">{folio:02d}</span>
  </footer>
</section>"""


def render_document(doc: dict, *, measure: bool = False) -> str:
    meta = doc.get("meta", {})
    fn = FieldNamer()
    pages = []
    for i, p in enumerate(doc["pages"]):
        pages.append(render_page(p, meta, i + 1, fn))

    fonts_css = (ASSETS / "fonts" / "fonts.css").read_text(encoding="utf-8")
    styles_css = (ASSETS / "styles.css").read_text(encoding="utf-8")

    # скрипт замера переполнения — используется только в режиме проверки
    measure_js = """
<script>
window.addEventListener('load', function () {
  var report = [];
  document.querySelectorAll('.page').forEach(function (pg, i) {
    var body = pg.querySelector('.page__body') || pg;
    var over = body.scrollHeight - body.clientHeight;
    if (over > 1) report.push((i + 1) + ':' + Math.round(over));
  });
  var d = document.createElement('div');
  d.id = 'overflow-report';
  d.textContent = report.join(',') || 'ok';
  document.body.appendChild(d);
});
</script>""" if measure else ""

    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<title>{html.escape(meta.get('title', 'Рабочая тетрадь'))}</title>
<style>{fonts_css}</style>
<style>{styles_css}</style>
</head><body>
{''.join(pages)}
{measure_js}
</body></html>"""
