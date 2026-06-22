#!/usr/bin/env python3
"""
Build an errata PDF where each error has a thumbnail crop of the approximate
area from the page PNG, so the user can visually verify each finding isn't
a hallucination. Radiology-report style.

Crop strategy: use staff_y (reliable from vision) for vertical center.
For horizontal, use an order-based spread across errors on the same staff.
Crop window is generous (45% of page width, 20% of page height) so even
a rough position gives enough context to judge.

Usage:
  build_errata_with_crops.py annotations.json pngs_dir/ out_errata.pdf [--limit N]
"""
import argparse
import json
from pathlib import Path
from io import BytesIO

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader

SEVERITY_FILL = {
    "BLOCKER": Color(0.85, 0.10, 0.10),
    "HIGH":    Color(0.95, 0.55, 0.10),
    "MEDIUM":  Color(0.10, 0.40, 0.85),
    "LOW":     Color(0.45, 0.45, 0.45),
}

POSITION_Y_FRAC = {
    "top":           0.12,
    "upper-middle":  0.30,
    "middle":        0.48,
    "lower-middle":  0.66,
    "bottom":        0.84,
}

CROP_W_FRAC = 0.45  # 45% of page width
CROP_H_FRAC = 0.22  # 22% of page height (slightly bigger than one system)


def crop_for_error(page_img, err, same_staff_errors, err_idx):
    """Return a PIL crop positioned at approximate staff+measure location."""
    W, H = page_img.size
    y_frac = POSITION_Y_FRAC.get((err.get("staff_position") or "middle").lower(), 0.5)

    # Horizontal: spread this staff's errors across 15%-85% of page width.
    n = len(same_staff_errors)
    if n == 1:
        x_frac = 0.5
    else:
        x_frac = 0.15 + (err_idx / (n - 1)) * 0.70

    crop_w = int(W * CROP_W_FRAC)
    crop_h = int(H * CROP_H_FRAC)
    cx = int(W * x_frac)
    cy = int(H * y_frac)

    left = max(0, cx - crop_w // 2)
    top = max(0, cy - crop_h // 2)
    right = min(W, left + crop_w)
    bottom = min(H, top + crop_h)
    return page_img.crop((left, top, right, bottom))


def wrap(text, width):
    words = text.split()
    if not words:
        return [""]
    lines = []
    cur = words[0]
    for w in words[1:]:
        if len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def build(ann_path, pngs_dir, out_path, limit=None):
    data = json.loads(Path(ann_path).read_text())
    errors = data.get("errors", [])
    if limit:
        errors = errors[:limit]

    page_w, page_h = 612, 792  # letter
    c = canvas.Canvas(str(out_path), pagesize=(page_w, page_h))

    margin = 36
    y = page_h - margin

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, f"Engraving Errata: {data.get('score_title','Score')}")
    y -= 16
    c.setFont("Helvetica", 9)
    c.drawString(margin, y, f"Arranger: {data.get('arranger','')}  |  "
                           f"Total: {len(errors)} errors shown (with visual evidence)")
    y -= 20

    # Pre-group by page+staff for the horizontal-spread calc
    by_page_staff = {}
    for e in errors:
        key = (e.get("page"), e.get("staff_position", "middle"))
        by_page_staff.setdefault(key, []).append(e)

    # Cache open PNGs
    png_cache = {}
    def get_page_png(pnum):
        if pnum not in png_cache:
            path = Path(pngs_dir) / f"page-{pnum:02d}.png"
            if not path.exists():
                return None
            png_cache[pnum] = Image.open(path)
        return png_cache[pnum]

    ENTRY_HEIGHT = 130  # per-error row height

    for err in errors:
        # New page if we run out of space
        if y < margin + ENTRY_HEIGHT:
            c.showPage()
            y = page_h - margin

        pnum = err.get("page")
        page_img = get_page_png(pnum) if isinstance(pnum, int) else None
        sev = err.get("severity", "LOW")

        # Severity color bar
        c.setFillColor(SEVERITY_FILL.get(sev, SEVERITY_FILL["LOW"]))
        c.rect(margin, y - ENTRY_HEIGHT + 4, 4, ENTRY_HEIGHT - 6, fill=1, stroke=0)

        # Thumbnail crop (left column, below bar)
        thumb_x = margin + 12
        thumb_y = y - ENTRY_HEIGHT + 4
        thumb_w = 230
        thumb_h = ENTRY_HEIGHT - 10

        if page_img:
            same_staff = by_page_staff.get(
                (pnum, err.get("staff_position", "middle")), [err]
            )
            try:
                idx = same_staff.index(err)
            except ValueError:
                idx = 0
            crop = crop_for_error(page_img, err, same_staff, idx)
            # Fit crop into thumb box preserving aspect
            thumb_buf = BytesIO()
            crop.save(thumb_buf, format="PNG")
            thumb_buf.seek(0)
            c.drawImage(
                ImageReader(thumb_buf),
                thumb_x, thumb_y, width=thumb_w, height=thumb_h,
                preserveAspectRatio=True, anchor="sw",
            )
            # Thin border around thumbnail
            c.setStrokeColor(Color(0.7, 0.7, 0.7))
            c.setLineWidth(0.5)
            c.rect(thumb_x, thumb_y, thumb_w, thumb_h, fill=0, stroke=1)
        else:
            c.setFillColor(Color(0.95, 0.95, 0.95))
            c.rect(thumb_x, thumb_y, thumb_w, thumb_h, fill=1, stroke=0)
            c.setFillColor(Color(0.5, 0.5, 0.5))
            c.setFont("Helvetica", 8)
            c.drawCentredString(thumb_x + thumb_w/2, thumb_y + thumb_h/2, "[no page image]")

        # Right column: header + description + fix
        text_x = thumb_x + thumb_w + 16
        text_y = y - 12

        # Header
        c.setFillColor(SEVERITY_FILL.get(sev, SEVERITY_FILL["LOW"]))
        c.setFont("Helvetica-Bold", 11)
        c.drawString(text_x, text_y,
                     f"#{err.get('id','?')}  p.{pnum}  {err.get('staff','?')}  m.{err.get('measure','?')}")
        text_y -= 14
        c.setFont("Helvetica-Bold", 9)
        c.drawString(text_x, text_y, f"[{sev}  {err.get('category','')}]")
        text_y -= 12

        # Description
        c.setFillColor(Color(0, 0, 0))
        c.setFont("Helvetica", 8.5)
        for line in wrap(err.get("description", ""), 60):
            if text_y < thumb_y + 30:
                break
            c.drawString(text_x, text_y, line)
            text_y -= 10

        # Fix
        if err.get("fix"):
            c.setFillColor(Color(0.3, 0.3, 0.3))
            c.setFont("Helvetica-Oblique", 8.5)
            text_y -= 4
            for line in wrap("FIX: " + err["fix"], 60):
                if text_y < thumb_y + 5:
                    break
                c.drawString(text_x, text_y, line)
                text_y -= 10

        y -= ENTRY_HEIGHT + 8

    c.save()
    print(f"Wrote {out_path} with {len(errors)} visually-evidenced errors")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("annotations_json", type=Path)
    ap.add_argument("pngs_dir", type=Path)
    ap.add_argument("out_pdf", type=Path)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    build(args.annotations_json, args.pngs_dir, args.out_pdf, args.limit)
