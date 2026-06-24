---
name: Harrison scripts archive location
description: Canonical folder for all filming-ready scripts. Save here every time a new script is generated.
type: project
originSessionId: 96d24bc4-360e-4d3e-b566-fcab2c713a01
---
All Harrison filming-ready scripts live at `/Users/air/Desktop/Precision-Brass/scripts/`. Naming: `YYYY-MM-DD_topic-slug.{html,pdf}`.

**Why:** Without a dedicated archive, scripts were scattered across `output/`, `references/`, `~/Downloads/`, and skill folders. This is the single source of truth.

**How to apply:** When `pb-script-write` runs, it must save the deliverable to all three of:
1. `Precision-Brass/scripts/YYYY-MM-DD_slug.{html,pdf}` (canonical archive)
2. `Precision-Brass/output/YYYY-MM-DD_slug.{html,pdf}` (working copy)
3. `~/Downloads/YYYY-MM-DD_slug.{html,pdf}` (fast handoff)

To recall a past script in a future session: `ls Precision-Brass/scripts/` or grep the folder. The `README.md` inside that folder maintains a per-script index with topic + status.
