---
name: Proposal PDF Dual-Save Rule
description: Every proposal PDF gets saved to TWO locations. Never just one. Backfill if missed.
type: feedback
originSessionId: 3860a3a8-590f-4199-8724-16d7b6a081e5
---
Every proposal PDF Timo asks for must be saved to BOTH locations:

1. `~/Downloads/{client-slug}-proposal-{YYYY-MM-DD}.pdf`. For Timo's daily-driver access (DocuSign upload, email attachment, etc.)
2. `/Users/air/Desktop/Timo LLC/creator-conservatory/output/proposals/{client-slug}/{client-slug}-proposal-{YYYY-MM-DD}.pdf`. The project's proposal database, alongside the HTML and MD source files.

Never one without the other. The Downloads copy is for active use. The project-folder copy is the canonical archive that lives next to the HTML/MD source so the proposal is self-contained.

**Why:** Timo flagged 2026-04-27 that I was rendering Robinson's PDF only to ~/Downloads, which means the proposal database in the project folder was incomplete (only HTML + MD, no PDF). Harrisson had the same gap. He wants every proposal stored in the database where Harrisson's lives, not just dropped in Downloads.

**How to apply:** After every Chrome `--print-to-pdf` render, run a `cp` to copy the PDF from Downloads into the project's `output/proposals/{client-slug}/` folder. Do this on the SAME turn as the render. Never declare a proposal "done" until both copies exist. Verify with `ls` on both paths.

**Backfill rule:** If a past proposal PDF is in Downloads but missing from the project folder, copy it over the next time you touch that client's proposal. Keep the database complete.
