---
name: Show Full Proposal In Chat Before Render
description: After writing a proposal MD draft, paste the FULL contract content into chat for Timo to read top-to-bottom. Do not describe it, do not summarize, do not link to the file. Render gate fires only after Timo reads and approves the in-chat version.
type: feedback
originSessionId: fd3dfc9f-1ccb-45e7-a4ff-3b98709a9069
---
After writing a proposal MD draft, paste the FULL contract content into chat for Timo to read top-to-bottom. Do NOT describe it ("here's a summary of what changed"), do NOT just link to the file path, do NOT ask "want me to render now?" without showing the content first.

**Why:** Timo cannot iterate on a proposal he has not read. Asking "want me to render?" while gating the content behind a file path and a summary forces him to either (a) open the file himself, breaking flow, or (b) approve render blind, which is what previously happened with the Otto personal-site contract (the hallucinated "Two rounds per page / ¥6,000 per hour" revisions clause shipped because it was never visible in chat). Showing the full content in chat is the only review surface that catches hallucinations before they become signed contracts. 2026-05-09 incident: I described the Music System Japan draft in bullet-point summary and asked if Timo wanted to render. He had to ask me to paste it.

**How to apply:**
- After every proposal MD write or significant edit, paste the full content into chat as a markdown code block (or rendered markdown if the harness shows it cleanly).
- Pre-render trigger words ("approve / render / ship / send / final") are only valid AFTER the full content has been visible in chat at least once.
- For long proposals, paste in one message even if it scrolls. Splitting fragments review.
- This stacks with `feedback_proposal_render_gate.md` (MD-only iteration). Show in chat → take corrections via Edit → show again on meaningful changes → render only on explicit approval.
- Generalizes to any signed deliverable: contracts, statements of work, anything Timo will send to a client. NOT required for internal docs / scratch files.
