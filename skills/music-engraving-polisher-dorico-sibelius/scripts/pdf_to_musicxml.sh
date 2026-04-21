#!/usr/bin/env bash
# PDF/image to MusicXML via Audiveris OMR. Auto-installs Audiveris if missing.
# Usage: pdf_to_musicxml.sh <input.pdf> <out_dir>
# Writes <out_dir>/<basename>.musicxml

set -euo pipefail

INPUT="$1"
OUT_DIR="$2"
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$OUT_DIR"

AUDIVERIS_APP=""
for CAND in "$HOME/Applications/Audiveris.app" "/Applications/Audiveris.app"; do
    if [ -d "$CAND" ]; then
        AUDIVERIS_APP="$CAND"
        break
    fi
done

if [ -z "$AUDIVERIS_APP" ]; then
    echo "Audiveris not installed. Running one-time installer..."
    bash "$SKILL_DIR/scripts/install_audiveris.sh"
    for CAND in "$HOME/Applications/Audiveris.app" "/Applications/Audiveris.app"; do
        if [ -d "$CAND" ]; then
            AUDIVERIS_APP="$CAND"
            break
        fi
    done
fi

if [ -z "$AUDIVERIS_APP" ]; then
    echo "ERROR: Audiveris install failed. Please install manually or export MusicXML from Dorico/Sibelius directly." >&2
    exit 1
fi

AUDIVERIS_BIN=""
for CAND in "$AUDIVERIS_APP/Contents/MacOS/Audiveris" "$AUDIVERIS_APP/Contents/MacOS/audiveris"; do
    if [ -x "$CAND" ]; then
        AUDIVERIS_BIN="$CAND"
        break
    fi
done

if [ -z "$AUDIVERIS_BIN" ]; then
    echo "ERROR: Could not find Audiveris executable inside $AUDIVERIS_APP" >&2
    exit 1
fi

echo "Running Audiveris OMR on $INPUT..."
"$AUDIVERIS_BIN" -batch -export -output "$OUT_DIR" "$INPUT"

BASE=$(basename "$INPUT" | sed 's/\.[^.]*$//')
OUT_XML="$OUT_DIR/${BASE}.mxl"
if [ ! -f "$OUT_XML" ]; then
    OUT_XML="$OUT_DIR/${BASE}.musicxml"
fi

if [ ! -f "$OUT_XML" ]; then
    echo "ERROR: Audiveris did not produce expected MusicXML output at $OUT_XML" >&2
    ls -la "$OUT_DIR" >&2
    exit 1
fi

echo "OMR complete: $OUT_XML"
echo "WARNING: OMR-derived MusicXML may contain transcription errors. Review before re-engraving."