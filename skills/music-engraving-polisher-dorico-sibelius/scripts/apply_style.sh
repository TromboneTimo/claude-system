#!/usr/bin/env bash
# Apply a MuseScore .mss style to a MusicXML and export both PDF and polished MusicXML.
# Usage: apply_style.sh <input.musicxml> <style.mss> <out.pdf> <out.musicxml>

set -euo pipefail

INPUT="$1"
STYLE="$2"
OUT_PDF="$3"
OUT_MUSICXML="$4"

MSCORE="/Applications/MuseScore 4.app/Contents/MacOS/mscore"

if [ ! -x "$MSCORE" ]; then
    echo "ERROR: MuseScore 4 not found at $MSCORE" >&2
    echo "Install it from https://musescore.org or via Homebrew Cask." >&2
    exit 1
fi

# Convert to PDF with style applied.
"$MSCORE" "$INPUT" -S "$STYLE" -o "$OUT_PDF"

# Convert to polished MusicXML (round-trip through MuseScore with the same style).
"$MSCORE" "$INPUT" -S "$STYLE" -o "$OUT_MUSICXML"

echo "Applied $(basename "$STYLE") to $(basename "$INPUT")"
echo "  PDF:      $OUT_PDF"
echo "  MusicXML: $OUT_MUSICXML"