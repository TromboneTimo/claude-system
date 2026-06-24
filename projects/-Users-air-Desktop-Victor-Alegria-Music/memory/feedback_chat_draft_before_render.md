---
name: Chat draft BEFORE rendering files (pb-script-write + any deliverable-producing skill)
description: For any skill that generates a rich file deliverable (HTML, PDF, image, deck), show Timo the full draft as plain markdown in chat FIRST. No Write/Chrome/filesystem touches until he approves. Two checkpoints, not one.
type: feedback
originSessionId: e195fea4-1b67-4561-b9a9-90e76c566a16
---
For pb-script-write, pb-email, pb-email-push, pb-ideas-push, marketing-blog, marketing-present, marketing-creative, blog-write, blog-rewrite, frontend-slides, render-animation, and any other skill that produces a heavy file deliverable: the order is **chat draft FIRST, file render SECOND, upload THIRD.** Two distinct approval checkpoints. Never compress them into one.

## The rule

1. Draft the full content in chat as plain markdown. Beats / sections / slides / email body / brief sections all visible inline.
2. Wait for explicit approval ("render", "ship it", "looks good", "go", or equivalent).
3. THEN call Write / Chrome / Edit / image generators / Supabase Storage.
4. Show file paths + a visual QA screenshot.
5. Wait for second explicit approval ("go", "upload", "publish", or equivalent).
6. THEN push to dashboard / send / publish / commit.

**Why:** Iteration on plain text is cheap. Iteration on rendered HTML / PDF / image / deck is wasteful and slow. Timo flagged on 2026-05-06: "instead of making a PDF every single time, I need you to show the text to me in this chat box here. I don't know why you're not already doing that." Before this rule, the loop was: draft a PDF -> get yelled at -> fix -> re-render -> get yelled at again -> re-render. Total time burned: minutes per iteration when it should have been seconds.

## How to apply

- Match the chat draft to the file structure exactly. If the file will have 7 beats with bullets and EXAMPLES boxes, the chat draft has 7 sections with bullets and EXAMPLES boxes. No summary tier. The chat draft IS the spec.
- For locked-line moments (hooks, funnel CTAs, mistake callouts, email subject lines, slide titles): present them verbatim in the chat draft. Timo edits the verbatim there, not in the file.
- For visual specs (action notes, image positions, slide layouts): write them as text in the chat draft so Timo can correct them before render.
- The render checkpoint and the upload checkpoint are separate. Never roll them into one.
- If a skill currently calls Write/Chrome/Supabase before the first approval, that skill needs updating. Update it the same session Timo flags it.

## Skills already updated under this rule

- pb-script-write (SKILL.md, 2026-05-06)
- (extend this list as other skills get aligned)

## Edge cases

- For trivial one-shot files (a single bash script, a single config edit Timo explicitly asked for), the chat draft can be the diff or a quoted snippet. The rule still applies in spirit: show the change in chat before writing it.
- For background research / data fetches that aren't deliverables, no chat checkpoint needed. The rule is about deliverables, not exploration.
