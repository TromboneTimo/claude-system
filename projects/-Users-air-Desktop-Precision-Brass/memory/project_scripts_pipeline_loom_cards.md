---
name: project-scripts-pipeline-loom-cards
description: "scripts.html pipeline status->column map, and how to add a Loom-brief filming card (the content-suggestion-as-card pattern Timo wants). Also how the script modal + content_items tiles render."
metadata: 
  node_type: memory
  type: project
  originSessionId: defd3a9f-9783-4b7f-ac74-e4760a101955
---

dashboard/scripts.html pipeline columns (STAGES) and their backing status:
- Ideas Pending  = `ideas.status` idea_pending
- Script Pending = `scripts.status` pending
- **Ready To Film = `scripts.status` approved**  (Harrisson films it; this is the "filmed list" Timo usually means)
- Ideas Approved  = `ideas.status` idea_approved
- Changes         = `scripts.status` changes
- Filmed (Done)   = `scripts.status` filmed
- Rejected        = ideas idea_rejected / scripts rejected
Board defaults to the Ideas Pending column and auto-refetches every 30s (paused while a modal is open).

ADD A LOOM-BRIEF FILMING CARD (Timo likes suggesting content this way, 2026-06-05; he may rework the whole scheme later, so treat as TENTATIVE):
- Insert into `scripts`: `status='approved'` (Ready to Film), `idea_id`=null, title in the sibling "New X: ..." style, `length='Loom brief'`.
- `body` = array of sections `[{kicker,heading,copy,visual}]`. `copy` is injected as RAW HTML by renderScriptDetail, so embed a clickable Loom card by reusing the `.script-link.script-link-loom` markup, and the shot list as an `<ol>`. Example shipped: `s_20260605_stunt-broll-shotlist`.
- Section `<h3>` is styled by `.script-section h3` (fixed 2026-06-05; was wrongly `.section-head h3`, which never matched, so headings rendered near-black on dark).

SCRIPT-APPROVAL MODAL renders from the `scripts` row, not the idea. For a full script, `body` is a single `{type:'html_full', content, pdf_url}` entry; as of 2026-06-05 it also carries `loom_url` + `references[]` and the modal shows a Loom card + reference-video link cards + a labeled "Download the full script (PDF)" button INSTEAD of the old inline iframe preview.

CONTENT SUGGESTIONS (suggestions.html, `content_items` table) tiles use `thumbnail_url='/thumbnails/ci_<...>.jpg'` (static files under dashboard/thumbnails/, committed + deployed). To fetch covers: YouTube = `i.ytimg.com/vi/<id>/maxresdefault.jpg` (fallback hqdefault); Instagram covers via `instagram.com/p/<code>/media/?size=l` (302s to the cdninstagram jpg; the post page itself returns a login wall to curl). ALWAYS Read each fetched thumbnail and confirm it matches the tile title before committing (the /media endpoint can throttle to a random/wrong frame, and a tile's IG URL may simply be wrong, as the "Low C vs High C" tile was). Long-form tiles have a "Send to Script Approvals" button that copies refs into a new idea's notes. See [[feedback_map_named_list_and_reproduce_view]].
