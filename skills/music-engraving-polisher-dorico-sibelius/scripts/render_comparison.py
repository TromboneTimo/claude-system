#!/usr/bin/env python3
"""
Merge an original PDF and polished PDF into a single side-by-side comparison
PDF. Each output page = original page on left, polished page on right,
at letter-landscape dimensions (17 x 11).

Usage: render_comparison.py original.pdf polished.pdf out.pdf
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter, PageObject, Transformation


def build(original, polished, out):
    r_orig = PdfReader(str(original))
    r_poly = PdfReader(str(polished))

    writer = PdfWriter()
    n = min(len(r_orig.pages), len(r_poly.pages))

    # Letter landscape target
    W = 17 * 72  # 17 inches
    H = 11 * 72  # 11 inches

    for i in range(n):
        p_orig = r_orig.pages[i]
        p_poly = r_poly.pages[i]

        # Scale each source page to half-width, full-height
        orig_w = float(p_orig.mediabox.width)
        orig_h = float(p_orig.mediabox.height)
        poly_w = float(p_poly.mediabox.width)
        poly_h = float(p_poly.mediabox.height)

        half_w = W / 2
        sx_o = half_w / orig_w
        sy_o = H / orig_h
        s_o = min(sx_o, sy_o)

        sx_p = half_w / poly_w
        sy_p = H / poly_h
        s_p = min(sx_p, sy_p)

        new_page = PageObject.create_blank_page(width=W, height=H)

        # Left: original
        tx_o = (half_w - orig_w * s_o) / 2
        ty_o = (H - orig_h * s_o) / 2
        new_page.merge_transformed_page(p_orig, Transformation().scale(s_o).translate(tx_o, ty_o))

        # Right: polished
        tx_p = half_w + (half_w - poly_w * s_p) / 2
        ty_p = (H - poly_h * s_p) / 2
        new_page.merge_transformed_page(p_poly, Transformation().scale(s_p).translate(tx_p, ty_p))

        writer.add_page(new_page)

    with open(out, "wb") as f:
        writer.write(f)
    print(f"Wrote {out} ({n} comparison pages)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("original", type=Path)
    ap.add_argument("polished", type=Path)
    ap.add_argument("out", type=Path)
    args = ap.parse_args()

    if not args.original.exists() or not args.polished.exists():
        print("ERROR: missing input PDF(s)", file=sys.stderr)
        sys.exit(1)

    build(args.original, args.polished, args.out)


if __name__ == "__main__":
    main()