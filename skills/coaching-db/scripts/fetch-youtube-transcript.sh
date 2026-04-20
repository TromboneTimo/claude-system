#!/bin/bash
# Fetch YouTube auto-captions + metadata JSON for a single video URL.
#
# Usage: fetch-youtube-transcript.sh <url> [output-dir]
#
# Output: <output-dir>/<video-id>.en.vtt and <output-dir>/<video-id>.info.json
# Expects yt-dlp installed at the Python user site. Adjust the binary path if needed.

set -eu

URL="${1:-}"
OUT="${2:-/tmp/coaching-db-yt}"

if [[ -z "$URL" ]]; then
  echo "Usage: fetch-youtube-transcript.sh <youtube-url> [output-dir]" >&2
  exit 1
fi

YTDLP="${YT_DLP_BIN:-/Users/air/Library/Python/3.10/bin/yt-dlp}"

if [[ ! -x "$YTDLP" ]]; then
  # Fallback to PATH lookup
  if command -v yt-dlp >/dev/null 2>&1; then
    YTDLP="$(command -v yt-dlp)"
  else
    echo "yt-dlp not found. Install: pip install --user yt-dlp" >&2
    exit 1
  fi
fi

mkdir -p "$OUT"
cd "$OUT"

"$YTDLP" --skip-download \
         --write-auto-subs \
         --sub-lang "en-orig,en" \
         --sub-format vtt \
         --write-info-json \
         -o "%(id)s.%(ext)s" \
         "$URL"

echo "Fetched: $URL -> $OUT"
