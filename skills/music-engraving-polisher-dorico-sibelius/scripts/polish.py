#!/usr/bin/env python3
"""
Main orchestrator for the music-engraving-polisher skill.

Loads a MusicXML (or PDF via OMR fallback), re-engraves through MuseScore
with a strict style, and emits polished MusicXML + PDF + before/after
comparison + diff JSON + residual validation issues + Dorico/Sibelius
instructions.

Usage:
  polish.py <input> <out_dir> [--style moderate|strict|conservative]
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATES = SKILL_DIR / "templates"
SCRIPTS = SKILL_DIR / "scripts"

STYLE_MAP = {
    "moderate": "moderate-engraving.mss",
    "strict": "strict-engraving.mss",
    "conservative": "conservative-engraving.mss",
}


def run(cmd, check=True):
    print(f"$ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(cmd, check=check)


def ensure_musicxml(input_path, work_dir):
    """Return path to a MusicXML. If input is a PDF/image, run OMR first."""
    ext = input_path.suffix.lower()
    if ext in (".musicxml", ".mxl", ".xml"):
        return input_path
    if ext in (".pdf", ".png", ".jpg", ".jpeg"):
        print(f"Input is {ext}, running OMR fallback...")
        omr_script = SCRIPTS / "pdf_to_musicxml.sh"
        run(["bash", str(omr_script), str(input_path), str(work_dir)])
        base = input_path.stem
        for candidate in (
            work_dir / f"{base}.mxl",
            work_dir / f"{base}.musicxml",
            work_dir / f"{base}.xml",
        ):
            if candidate.exists():
                return candidate
        raise RuntimeError(f"OMR did not produce MusicXML for {input_path}")
    raise RuntimeError(f"Unsupported input extension: {ext}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path, help="MusicXML, MXL, or PDF")
    ap.add_argument("out_dir", type=Path, help="Output directory")
    ap.add_argument("--style", choices=list(STYLE_MAP.keys()), default="moderate",
                    help="Engraving style preset (default: moderate)")
    args = ap.parse_args()

    if not args.input.exists():
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    work_dir = args.out_dir / "_work"
    work_dir.mkdir(exist_ok=True)

    style_file = TEMPLATES / STYLE_MAP[args.style]
    if not style_file.exists():
        print(f"ERROR: style file not found: {style_file}", file=sys.stderr)
        sys.exit(1)

    # Step 1: ensure we have a MusicXML (OMR if needed)
    musicxml_in = ensure_musicxml(args.input, work_dir)
    print(f"Using MusicXML: {musicxml_in}")

    # Step 2: render original PDF without style application (as baseline)
    mscore = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"
    original_pdf = args.out_dir / "original.pdf"
    run([mscore, str(musicxml_in), "-o", str(original_pdf)])

    # Step 3: apply style + re-engrave to polished MusicXML + PDF
    polished_xml = args.out_dir / "polished.musicxml"
    polished_pdf = args.out_dir / "polished.pdf"
    run([mscore, str(musicxml_in), "-S", str(style_file), "-o", str(polished_pdf)])
    run([mscore, str(musicxml_in), "-S", str(style_file), "-o", str(polished_xml)])

    # Step 4: content-level diff (before vs after)
    changes_json = args.out_dir / "changes.json"
    run(["python3", str(SCRIPTS / "diff_xml.py"),
         str(musicxml_in), str(polished_xml), str(changes_json)])

    # Step 5: validation pass for residual issues
    residual_json = args.out_dir / "residual_issues.json"
    run(["python3", str(SCRIPTS / "validation_pass.py"),
         str(polished_xml), str(residual_json)])

    # Step 6: side-by-side before/after PDF
    comparison_pdf = args.out_dir / "before-after.pdf"
    run(["python3", str(SCRIPTS / "render_comparison.py"),
         str(original_pdf), str(polished_pdf), str(comparison_pdf)])

    # Step 7: Dorico + Sibelius instructions
    run(["python3", str(SCRIPTS / "write_instructions.py"),
         str(changes_json), str(residual_json), args.style, str(args.out_dir)])

    print()
    print("=" * 60)
    print(f"Polish complete. Outputs in {args.out_dir}:")
    print(f"  polished.musicxml    - clean MusicXML, re-import into Dorico/Sibelius")
    print(f"  polished.pdf         - publication-ready PDF")
    print(f"  original.pdf         - baseline (for comparison)")
    print(f"  before-after.pdf     - side-by-side landscape comparison")
    print(f"  changes.json         - content-level diff (should be small)")
    print(f"  residual_issues.json - what re-engraving could not fix")
    print(f"  dorico-instructions.md")
    print(f"  sibelius-instructions.md")


if __name__ == "__main__":
    main()