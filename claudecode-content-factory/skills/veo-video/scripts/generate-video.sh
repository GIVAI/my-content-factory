#!/bin/bash
# Timelapse video generator — Veo 3.1 Sync API (first/last frame)
# Usage: ./generate-video.sh <project-name> <prompt> <start-frame.jpg> <end-frame.jpg> <output-name>
#
# For production use, prefer async-video.py (no charge on failure)
#
# Example:
#   ./generate-video.sh seat-restore \
#     "Smooth timelapse of leather being stripped from a car seat" \
#     frame-1.jpg frame-2.jpg segment-1-2

set -euo pipefail

API_KEY="${VEO_API_KEY:?Set VEO_API_KEY env variable (see TOOLS.md)}"
API_URL="https://api.laozhang.ai/v1/chat/completions"
MODEL="veo-3.1-fast-fl"

PROJECT="$1"
PROMPT="$2"
START_FRAME="$3"
END_FRAME="$4"
OUTPUT_NAME="$5"

# Output to factory project folder
OUTDIR="/Users/user/claudecode/projects/nano_img/timelapse/${PROJECT}"
mkdir -p "$OUTDIR"

echo "🎬 Generating video: ${OUTPUT_NAME}"
echo "   Start: ${START_FRAME}"
echo "   End:   ${END_FRAME}"
echo "   Prompt: ${PROMPT:0:80}..."

# Encode frames to base64
START_B64=$(base64 -i "$START_FRAME" | tr -d '\n')
END_B64=$(base64 -i "$END_FRAME" | tr -d '\n')

# Build request
PAYLOAD=$(python3 -c "
import json, sys
data = {
    'messages': [{'role': 'user', 'content': [
        {'type': 'text', 'text': sys.argv[1]},
        {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{sys.argv[2]}'}},
        {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{sys.argv[3]}'}}
    ]}],
    'model': '${MODEL}',
    'stream': False
}
print(json.dumps(data))
" "$PROMPT" "$START_B64" "$END_B64")

echo "   ⏳ Sending to Veo 3.1 (this may take 1-3 min)..."

RESPONSE=$(curl -s -X POST "$API_URL" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

# Extract video URL and download
VIDEO_URL=$(python3 -c "
import json, sys, re
data = json.loads(sys.argv[1])
try:
    content = data['choices'][0]['message']['content']
    urls = re.findall(r'https?://[^\s\)]+\.mp4', content)
    if urls:
        print(urls[0])
    else:
        links = re.findall(r'\[.*?\]\((https?://[^\)]+)\)', content)
        if links:
            print(links[0])
        else:
            print('NO_URL', file=sys.stderr)
            print(f'Response content: {content[:500]}', file=sys.stderr)
            sys.exit(1)
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
    print(json.dumps(data, indent=2)[:500], file=sys.stderr)
    sys.exit(1)
" "$RESPONSE")

OUTPUT_PATH="${OUTDIR}/${OUTPUT_NAME}.mp4"
echo "   📥 Downloading: ${VIDEO_URL:0:80}..."
curl -s -o "$OUTPUT_PATH" "$VIDEO_URL"

echo "   ✅ Saved: ${OUTPUT_PATH}"
echo "   📏 Size: $(du -h "$OUTPUT_PATH" | cut -f1)"
