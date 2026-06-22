#!/usr/bin/env python3
"""
Margin-ribbon + errata annotator (v2).

Instead of drawing shapes over the score (which requires reliable bounding box
coordinates the vision model cannot provide), this overlays:

- A RIGHT-margin ribbon on each page with small severity-colored numbered dots,
  placed at the vertical level of the affected staff (derived from staff_position).
- A FOOTER text strip on each page listing every error on that page in the form
  "#N Ob m.3-6 collision". So the engraver can find the issue from the semantic
  description, not a fuzzy circle.

The companion errata PDF (generated separately) carries the full fix text.

JSON schema expected (v2):
  {
    "page": int,
    "measure": str,                    # e.g. "10-12" or "rehearsal E"
    "staff": str,                      # instrument name
    "staff_position": str,             # top, upper-middle, middle, lower-middle, bottom
    "category": str,
    "severity": str,
    "description": str,
    "fix": str,
    "id": int
  }

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

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color

SEVERITY_FILL = {
    "BLOCKER": Color(0.85, 0.10, 0.10, alpha=0.95),
    "HIGH":    Color(0.95, 0.55, 0.10, alpha=0.95),
    "MEDIUM":  Color(0.10, 0.40, 0.85, alpha=0.95),
    "LOW":     Color(0.45, 0.45, 0.45, alpha=0.95),
}
SEVERITY_LABEL = {
    "BLOCKER": "B",
    "HIGH":    "H",
    "MEDIUM":  "M",
    "LOW":     "L",
}

# Staff position to vertical fraction of the page (0=top, 1=bottom).
POSITION_Y_FRAC = {
    "top":           0.12,
    "upper-middle":  0.30,
    "middle":        0.48,
    "lower-middle":  0.66,
    "bottom":        0.84,
}
DEFAULT_Y_FRAC = 0.50

# Measure position to horizontal fraction of the page (0=left, 1=right).
# The music content area is typically ~12% from left edge to ~95% from left edge.
POSITION_X_FRAC = {
    "left":         0.20,
    "center-left":  0.35,
    "center":       0.52,
    "center-right": 0.70,
    "right":        0.88,
}
DEFAULT_X_FRAC = 0.52


def staff_y(page_h, position):
    frac = POSITION_Y_FRAC.get((position or "").lower(), DEFAULT_Y_FRAC)
    return page_h * (1.0 - frac)


def measure_x(page_w, position):
    frac = POSITION_X_FRAC.get((position or "").lower(), DEFAULT_X_FRAC)
    return page_w * frac


def make_overlay_page(page_w, page_h, errors_for_page):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(page_w, page_h))

    # === SMALL NUMBERED CIRCLES ON THE PAGE ===
    # Each error gets a small circle on the page. Y is from staff_position
    # (reliable: the vision model knows which staff). X is from
    # measure_position if present, otherwise we spread errors on the same
    # staff horizontally by their order in the list so they don't stack.
    dot_radius = 11

    # Group errors by staff so we can spread them horizontally within each staff.
    by_staff = {}
    for err in errors_for_page:
        key = (err.get("staff_position") or "middle")
        by_staff.setdefault(key, []).append(err)

    placed = []
    for staff_key, staff_errors in by_staff.items():
        n = len(staff_errors)
        for idx, err in enumerate(staff_errors):
            y = staff_y(page_h, err.get("staff_position"))

            # If the model provided measure_position, use it. Otherwise
            # distribute this staff's errors evenly across the content area.
            mp = err.get("measure_position")
            if mp:
                x = measure_x(page_w, mp)
            else:
                # Spread n errors across 15%-90% of page width.
                if n == 1:
                    x_frac = 0.5
                else:
                    x_frac = 0.15 + (idx / (n - 1)) * 0.75
                x = page_w * x_frac

            # De-collide if two circles still land too close.
            while any(abs(x - px) < 24 and abs(y - py) < 24 for (px, py) in placed):
                y -= 24
            placed.append((x, y))

        sev = err.get("severity", "LOW")
        stroke_color = SEVERITY_FILL.get(sev, SEVERITY_FILL["LOW"])

        # Outline-only circle so the music underneath stays visible.
        c.setStrokeColor(stroke_color)
        c.setFillColor(Color(1, 1, 1, alpha=0.85))  # pale white center for contrast
        c.setLineWidth(2.0)
        c.circle(x, y, dot_radius, fill=1, stroke=1)

        # Numbered label in the center of the circle, in severity color.
        c.setFillColor(stroke_color)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(x, y - 3, str(err.get("id", "")))

    # === FOOTER STRIP ===
    # One-line summary of all errors on this page, left-aligned at the bottom.
    footer_y = 16
    c.setFillColor(Color(0, 0, 0, alpha=1))
    c.setFont("Helvetica", 7)

    if errors_for_page:
        parts = []
        for err in errors_for_page:
            sev = err.get("severity", "LOW")
            parts.append(
                f"#{err.get('id','')}[{SEVERITY_LABEL.get(sev,'?')}] "
                f"{err.get('staff','?')} m.{err.get('measure','?')} "
                f"{err.get('category','?')}"
            )
        footer_text = "  |  ".join(parts)
        # Clip to page width with ellipsis if too long.
        max_chars = int((page_w - 72) / 3.5)  # ~3.5pt per char at 7pt font
        if len(footer_text) > max_chars:
            footer_text = footer_text[: max_chars - 1] + "..."
        c.drawString(36, footer_y, footer_text)

    # Legend in the footer right-aligned
    c.setFont("Helvetica-Bold", 6)
    legend_x = page_w - 180
    c.setFillColor(SEVERITY_FILL["BLOCKER"]); c.circle(legend_x, footer_y + 2, 3, fill=1, stroke=0)
    c.setFillColor(Color(0,0,0)); c.drawString(legend_x + 5, footer_y, "BLOCKER")
    c.setFillColor(SEVERITY_FILL["HIGH"]); c.circle(legend_x + 45, footer_y + 2, 3, fill=1, stroke=0)
    c.setFillColor(Color(0,0,0)); c.drawString(legend_x + 50, footer_y, "HIGH")
    c.setFillColor(SEVERITY_FILL["MEDIUM"]); c.circle(legend_x + 80, footer_y + 2, 3, fill=1, stroke=0)
    c.setFillColor(Color(0,0,0)); c.drawString(legend_x + 85, footer_y, "MED")
    c.setFillColor(SEVERITY_FILL["LOW"]); c.circle(legend_x + 115, footer_y + 2, 3, fill=1, stroke=0)
    c.setFillColor(Color(0,0,0)); c.drawString(legend_x + 120, footer_y, "LOW")

    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def annotate(input_pdf, annotations_path, output_pdf):
    data = json.loads(Path(annotations_path).read_text())
    errors = data.get("errors", [])
    errors_by_page = {}
    for err in errors:
        page = err.get("page")
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


def build_errata(annotations_path, errata_pdf):
    """Generate a standalone errata PDF with the full error table."""
    data = json.loads(Path(annotations_path).read_text())
    errors = data.get("errors", [])
    title = data.get("score_title", "Score")
    arranger = data.get("arranger", "")
    counts = data.get("severity_counts", {})

    buf = BytesIO()
    c = canvas.Canvas(str(errata_pdf), pagesize=(612, 792))  # letter
    page_w, page_h = 612, 792
    margin_left = 48
    margin_right = 48
    margin_top = 48
    text_y = page_h - margin_top

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin_left, text_y, f"Engraving Errata: {title}")
    text_y -= 18
    c.setFont("Helvetica", 10)
    if arranger:
        c.drawString(margin_left, text_y, f"Arranger: {arranger}")
        text_y -= 14
    c.drawString(
        margin_left, text_y,
        f"Total: {len(errors)} errors "
        f"(BLOCKER: {counts.get('BLOCKER',0)}, HIGH: {counts.get('HIGH',0)}, "
        f"MEDIUM: {counts.get('MEDIUM',0)}, LOW: {counts.get('LOW',0)})"
    )
    text_y -= 22

    # Render each error
    for err in errors:
        if text_y < 100:
            c.showPage()
            c.setFont("Helvetica", 9)
            text_y = page_h - margin_top

        sev = err.get("severity", "LOW")
        # Severity dot
        c.setFillColor(SEVERITY_FILL.get(sev, SEVERITY_FILL["LOW"]))
        c.circle(margin_left + 4, text_y + 3, 5, fill=1, stroke=0)
        c.setFillColor(Color(1, 1, 1))
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(margin_left + 4, text_y + 0.5, str(err.get("id", "")))

        # Header line
        c.setFillColor(Color(0, 0, 0))
        c.setFont("Helvetica-Bold", 10)
        header = (
            f"  #{err.get('id','?')}  p.{err.get('page','?')}  "
            f"{err.get('staff','?')}  m.{err.get('measure','?')}  "
            f"[{sev}  {err.get('category','?')}]"
        )
        c.drawString(margin_left + 12, text_y, header)
        text_y -= 12

        # Description
        c.setFont("Helvetica", 9)
        desc = err.get("description", "")
        for line in wrap(desc, 95):
            if text_y < 60:
                c.showPage()
                text_y = page_h - margin_top
            c.drawString(margin_left + 20, text_y, line)
            text_y -= 11

        # Fix
        if err.get("fix"):
            c.setFont("Helvetica-Oblique", 9)
            c.setFillColor(Color(0.2, 0.2, 0.2))
            for line in wrap("FIX: " + err["fix"], 95):
                if text_y < 60:
                    c.showPage()
                    text_y = page_h - margin_top
                c.drawString(margin_left + 20, text_y, line)
                text_y -= 11
            c.setFillColor(Color(0, 0, 0))

        text_y -= 8

    c.save()
    print(f"Wrote {errata_pdf}")


def wrap(text, width):
    """Dumb word-wrap that respects word boundaries."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    current = words[0]
    for w in words[1:]:
        if len(current) + 1 + len(w) <= width:
            current += " " + w
        else:
            lines.append(current)
            current = w
    lines.append(current)
    return lines


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: annotate_pdf.py input.pdf annotations.json output.pdf [errata.pdf]",
              file=sys.stderr)
        sys.exit(1)
    input_pdf = sys.argv[1]
    ann_path = sys.argv[2]
    output_pdf = sys.argv[3]
    errata_pdf = sys.argv[4] if len(sys.argv) > 4 else None

    annotate(input_pdf, ann_path, output_pdf)
    if errata_pdf:
        build_errata(ann_path, errata_pdf)
