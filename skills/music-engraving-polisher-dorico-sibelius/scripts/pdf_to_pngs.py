#!/usr/bin/env python3
"""
Convert a PDF score into page PNGs at a resolution safe for Claude vision.

Why 150 DPI (≈1240px wide for letter/A4)?
- Claude vision token cost scales with area. At 1024px long edge an image is
  ~680 tokens high-detail; at 2000px it's 5k+. Sheet music at 150 DPI keeps
  stave lines crisp for engraving error detection (collisions, spacing,
  articulation overlaps) while staying near the efficient token band.
- If you're hitting token pressure on a 200+ page score, drop to 120 DPI.

Usage:
  python pdf_to_pngs.py input.pdf out_dir/ [--dpi 150] [--pages 1-20]
"""
import argparse
import subprocess
import sys
from pathlib import Path


def extract(pdf_path: Path, out_dir: Path, dpi: int, page_range: str | None) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    # pdftoppm auto-zero-pads; we ask for 'page' prefix → page-01.png, page-02.png...
    cmd = ["pdftoppm", "-png", "-r", str(dpi)]
    if page_range:
        first, last = page_range.split("-") if "-" in page_range else (page_range, page_range)
        cmd += ["-f", first, "-l", last]
    cmd += [str(pdf_path), str(out_dir / "page")]
    subprocess.run(cmd, check=True)
    return sorted(out_dir.glob("page-*.png"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--pages", type=str, default=None, help="e.g. 10-20 or 5")
    args = ap.parse_args()

    if not args.pdf.exists():
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        sys.exit(1)

    pages = extract(args.pdf, args.out_dir, args.dpi, args.pages)
    print(f"Extracted {len(pages)} pages at {args.dpi} DPI to {args.out_dir}")
    for p in pages:
        print(p)


if __name__ == "__main__":
    main()
