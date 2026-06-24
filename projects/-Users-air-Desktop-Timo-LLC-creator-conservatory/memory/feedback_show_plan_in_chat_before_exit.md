---
name: Show Plan In Chat Before ExitPlanMode
description: Always paste the full plan content into chat as text BEFORE calling ExitPlanMode. Pointing at the plan file path is not review. Timo says this every time.
type: feedback
originSessionId: 44a98549-51b8-4912-8651-9ce2b92f8852
---
Before calling ExitPlanMode, paste the full plan content into the chat as plain markdown text. Do NOT just say "here's the plan, ready for sign-off" with the file path. Render the plan inline so Timo can read and evaluate it without opening a separate file.

**Why:** Timo cannot see the plan file from the chat UI in plan mode. The plan box only opens after ExitPlanMode is approved. So pushing for ExitPlanMode without showing the content forces him to either (a) approve blind, or (b) explicitly ask "show me what it says." He has to repeat this correction across sessions. 2026-05-09 Ilan Morgenstern proposal: Timo rejected the first ExitPlanMode call with "show me what it says in the chat box, i say this everytime please do that first before asking me to render."

**How to apply:** After every plan write/edit, before ExitPlanMode, dump the plan file content into the chat as a markdown block. Trim verbose preamble if needed but keep the substantive sections (Context, Pattern selection, Section structure, Gaps, Verification). Then call ExitPlanMode.

**Generalization:** This is the plan-mode twin of `feedback_proposal_show_full_draft_in_chat.md`. Same principle applies to any artifact under review: if the user can't see the content from the chat surface they are working in, paste it.
