#!/usr/bin/env python3
"""
Reads annotations.json + input PDF, produces annotated PDF with colored
rectangles around each visual error and a numbered margin callout.

Severity colors:
  BLOCKER: red
  HIGH:    orange
  MEDIUM:  blue
  LOW:     gray
"""
import json
import sys
from pathlib import Path
from io import BytesIO

from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter

SEVERITY_COLORS = {
    "BLOCKER": Color(0.85, 0.10, 0.10, alpha=0.35),
    "HIGH":    Color(0.95, 0.55, 0.10, alpha=0.35),
    "MEDIUM":  Color(0.10, 0.40, 0.85, alpha=0.30),
    "LOW":     Color(0.45, 0.45, 0.45, alpha=0.25),
}
SEVERITY_STROKE = {
    "BLOCKER": Color(0.75, 0.05, 0.05, alpha=0.9),
    "HIGH":    Color(0.85, 0.45, 0.05, alpha=0.9),
    "MEDIUM":  Color(0.05, 0.30, 0.75, alpha=0.9),
    "LOW":     Color(0.30, 0.30, 0.30, alpha=0.8),
}


def make_overlay_page(page_w, page_h, errors_for_page):
    """Create a transparent overlay PDF page with annotation boxes."""
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(page_w, page_h))
    for err in errors_for_page:
        region = err["region"]
        x = (region["x_pct"] / 100.0) * page_w
        # flip y: JSON uses top-left origin, PDF uses bottom-left
        y_top = (region["y_pct"] / 100.0) * page_h
        w = (region["w_pct"] / 100.0) * page_w
        h = (region["h_pct"] / 100.0) * page_h
        y = page_h - y_top - h

        sev = err["severity"]
        c.setFillColor(SEVERITY_COLORS[sev])
        c.setStrokeColor(SEVERITY_STROKE[sev])
        c.setLineWidth(2.0)
        # Ellipse circumscribing the error region, with 15% padding so it
        # circles around (not crops) the defect. reportlab ellipse takes
        # the bounding box (x1, y1, x2, y2) in PDF coords.
        pad_x = w * 0.15
        pad_y = h * 0.15
        c.ellipse(x - pad_x, y - pad_y, x + w + pad_x, y + h + pad_y,
                  fill=0, stroke=1)

        # numbered badge near the top-left of the circle
        badge_x = x - pad_x
        badge_y = y + h + pad_y - 14
        c.setFillColor(SEVERITY_STROKE[sev])
        c.circle(badge_x + 8, badge_y + 4, 9, fill=1, stroke=0)
        c.setFillColor(Color(1, 1, 1))
        c.setFont("Helvetica-Bold", 10)
        label = str(err["id"])
        c.drawCentredString(badge_x + 8, badge_y + 1, label)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def annotate(input_pdf, annotations_path, output_pdf):
    data = json.loads(Path(annotations_path).read_text())
    errors = data["errors"]
    errors_by_page = {}
    for err in errors:
        page = err["page"]
        # handle "1-20" or "throughout" entries: skip per-page drawing
        if isinstance(page, str):
            continue
        errors_by_page.setdefault(page, []).append(err)

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        pnum = i + 1
        w = float(page.mediabox.width)
        h = float(page.mediabox.height)
        if pnum in errors_by_page:
            overlay = make_overlay_page(w, h, errors_by_page[pnum])
            page.merge_page(overlay)
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Wrote {output_pdf}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: annotate_pdf.py input.pdf annotations.json output.pdf")
        sys.exit(1)
    annotate(sys.argv[1], sys.argv[2], sys.argv[3])
