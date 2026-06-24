---
name: PDF only to Downloads (not HTML)
description: For deliverables, only the PDF copies to ~/Downloads/. HTML stays in scripts/ and output/ archive only. Timo only needs the PDF for review.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
When pb-script-write (or any deliverable skill) saves to multiple locations, the HTML file does NOT go to ~/Downloads/. Only the PDF goes there.

**Why:** Timo reviews PDFs, not HTML files. An HTML file in Downloads is noise. He's never going to open it. The HTML belongs in the scripts archive (canonical) and output/ (working copy). Downloads is for the one file he actually needs to read.

**How to apply:**
- `scripts/YYYY-MM-DD_slug.html` and `.pdf` (canonical archive)
- `output/YYYY-MM-DD_slug.html` and `.pdf` (working copy)
- `~/Downloads/YYYY-MM-DD_slug.pdf` (PDF ONLY)

This overrides the prior rule in `feedback_pdfs_to_downloads.md` for the HTML half. From 2026-05-06.
