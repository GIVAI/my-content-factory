#!/bin/bash
# Скачать субтитры YouTube видео и очистить
# Usage: get_transcript.sh <youtube_url> <output_file>
set -e

URL="$1"
OUT="$2"
TMPBASE="/tmp/yt_swipefile_$$"

if [ -z "$URL" ] || [ -z "$OUT" ]; then
  echo "Usage: $0 <youtube_url> <output_file>"
  exit 1
fi

yt-dlp --write-auto-sub --sub-lang ru,en --skip-download -o "$TMPBASE" "$URL" 2>&1

if [ -f "${TMPBASE}.ru.vtt" ]; then
  SUBFILE="${TMPBASE}.ru.vtt"
  echo "LANG=ru"
elif [ -f "${TMPBASE}.en.vtt" ]; then
  SUBFILE="${TMPBASE}.en.vtt"
  echo "LANG=en"
else
  echo "ERROR: No subtitles found"
  exit 1
fi

cat "$SUBFILE" | \
  sed '/^WEBVTT/d;/^Kind:/d;/^Language:/d;/^$/d;/-->/d' | \
  sed 's/<[^>]*>//g' | \
  awk '!seen[$0]++' > "$OUT"

LINES=$(wc -l < "$OUT")
echo "OK: $LINES lines → $OUT"
rm -f "${TMPBASE}"*.vtt
