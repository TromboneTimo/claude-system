---
name: PDFs and exported deliverables always go to Downloads (also)
description: When generating any PDF or exported deliverable in Precision-Brass workspace, save BOTH to project output folder AND to ~/Downloads/
type: feedback
originSessionId: 96d24bc4-360e-4d3e-b566-fcab2c713a01
---
When generating any PDF, exported document, or shareable deliverable in the Precision-Brass workspace, save it to BOTH:
1. The project's appropriate folder (usually `Precision-Brass/output/`)
2. `~/Downloads/` (always)

**Why:** Timo grabs deliverables from Downloads to send to Harrison or upload elsewhere. Having to dig into the project folder every time slows him down.

**How to apply:** After writing a PDF (or similar exported file) to the project folder, immediately `cp` it to `~/Downloads/` with the same filename. Do this without asking. Confirm both paths in the response.

**Does NOT apply to:** the dashboard (`Precision-Brass/dashboard/index.html`. that has its own rule in `project_dashboard_location.md` saying Downloads is wrong for that). Source code, raw data, intermediate working files. Only finished deliverables.
