#!/usr/bin/env python3
"""Подготовка фотографий к вёрстке.

Что делает с каждым файлом:
  • разворачивает по EXIF (фото с телефона часто лежат «на боку»);
  • переводит в sRGB;
  • ужимает до разумного размера — 300 dpi хватает для печати,
    а PDF не раздувается до сотни мегабайт;
  • складывает результат в build/img/.
"""
from __future__ import annotations

import hashlib
import pathlib

from PIL import Image, ImageOps

MAX_PX = 2400          # длинная сторона после сжатия
JPEG_QUALITY = 86


def prepare(src: pathlib.Path, out_dir: pathlib.Path) -> pathlib.Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    key = hashlib.md5(
        f"{src.resolve()}:{src.stat().st_mtime_ns}:{MAX_PX}".encode()
    ).hexdigest()[:10]

    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    has_alpha = im.mode in ("RGBA", "LA") or "transparency" in im.info

    if max(im.size) > MAX_PX:
        scale = MAX_PX / max(im.size)
        im = im.resize((round(im.width * scale), round(im.height * scale)),
                       Image.LANCZOS)

    if has_alpha:
        dst = out_dir / f"{src.stem}-{key}.png"
        im.convert("RGBA").save(dst, "PNG", optimize=True)
    else:
        dst = out_dir / f"{src.stem}-{key}.jpg"
        im.convert("RGB").save(dst, "JPEG", quality=JPEG_QUALITY,
                               optimize=True, progressive=True)
    return dst
