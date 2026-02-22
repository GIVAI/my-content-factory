#!/bin/bash
# Timelapse keyframe generator — Nano Banana Pro
# Usage: ./generate-frames.sh <project-name> <anchor-prompt> <frame1-desc> <frame2-desc> ...
#
# Example:
#   ./generate-frames.sh seat-restore \
#     "Interior of a dark gray sedan, front passenger seat, shot from open driver door at 3/4 angle. Workshop fluorescent lighting." \
#     "Severely cracked brown leather with foam showing through tears" \
#     "Completely stripped, bare yellow foam padding exposed" \
#     "Being reupholstered, backrest done, seat bottom in progress" \
#     "Fully reupholstered with premium black diamond-quilted leather"

set -euo pipefail

API_KEY="${NANO_BANANA_API_KEY:?Set NANO_BANANA_API_KEY env variable (see TOOLS.md)}"
API_URL="https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent"
RATIO="9:16"
SIZE="2K"

PROJECT="$1"
ANCHOR="$2"
shift 2

# Output to factory project folder
OUTDIR="[YOUR_OUTPUT_DIR]/timelapse/${PROJECT}"
mkdir -p "$OUTDIR"

FRAME_NUM=1
for DESC in "$@"; do
  FULL_PROMPT="${ANCHOR} ${DESC}"
  OUTPUT="${OUTDIR}/frame-${FRAME_NUM}.jpg"
  
  echo "🎨 Generating frame ${FRAME_NUM}: ${DESC:0:60}..."
  
  PAYLOAD=$(python3 -c "
import json, sys
data = {
    'contents': [{'parts': [{'text': sys.argv[1]}]}],
    'generationConfig': {
        'responseModalities': ['IMAGE'],
        'imageConfig': {
            'aspectRatio': '${RATIO}',
            'imageSize': '${SIZE}'
        }
    }
}
print(json.dumps(data))
" "$FULL_PROMPT")

  RESPONSE=$(curl -s -X POST "$API_URL" \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

  python3 -c "
import sys, json, base64
data = json.loads(sys.argv[1])
try:
    b64 = data['candidates'][0]['content']['parts'][0]['inlineData']['data']
    with open('${OUTPUT}', 'wb') as f:
        f.write(base64.b64decode(b64))
    print(f'  ✅ Saved: ${OUTPUT}')
except Exception as e:
    print(f'  ❌ ERROR: {e}', file=sys.stderr)
    print(json.dumps(data, indent=2)[:500], file=sys.stderr)
    sys.exit(1)
" "$RESPONSE"

  FRAME_NUM=$((FRAME_NUM + 1))
  sleep 1
done

echo ""
echo "🎬 All ${#@} frames generated in: ${OUTDIR}/"
ls -la "$OUTDIR/"
