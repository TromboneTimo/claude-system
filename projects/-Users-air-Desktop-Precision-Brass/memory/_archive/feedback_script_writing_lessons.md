---
name: Script writing failure modes from 2026-04-25 mouthpieces script iteration
description: Specific patterns Timo flagged repeatedly when writing Phase 2 scripts. Read before generating any new script.
type: feedback
originSessionId: 96d24bc4-360e-4d3e-b566-fcab2c713a01
---
When writing Phase 2 scripts for Harrison (the script-writing companion to /pb-script), follow these rules. They were learned the hard way during the "Stop Buying Mouthpieces" iteration.

## What NOT to do

1. **Don't write paragraphs of explanation.** Bullet director's notes only. Timo said "too much text", "be efficient", "lower text by half" multiple times.
2. **Don't summarize his locked phrasing.** Preserve verbatim. He had to repaste his own draft when I edited.
3. **Don't drop visual specs.** "Harrison sitting in front of all his mouthpieces" was specific and mandatory. Preserve all visual detail.
4. **Don't stack mistakes/tests as separate beats after trap topics.** Weave them inside the same beat. He flagged this twice.
5. **Don't fabricate stats or social proof.** Knowledge gaps OK, made-up "every single one of them stopped buying" claims NOT.
6. **Don't put meta-instructions inside the deliverable.** No "Send to Timo for review" footer in the page Harrison reads while filming.
7. **Don't write in clinical third-person register.** Harrison talks second-person, conversational ("Now,", "right?", repetitions, mid-sentence metaphors).
8. **Don't fragment every sentence into its own shot.** Beats can hold many sentences that flow together.
9. **Don't regress.** Once a fix lands, it stays. He repeatedly said "we fixed this before."
10. **Don't manhandle Harrison.** Locked lines for critical moments, riff topics for the rest. Trust him to improvise.
11. **Don't let PDF paragraphs split across pages.** CSS: `break-inside: avoid` on script paragraphs.
12. **Don't design over readability.** No yellow speech bubbles, no italic body, no chat-bubble metaphor. Script readability is sacred.

## What TO do

1. **7-beat interleaved structure.** Cold Open -> Demo -> Apparatus Reveal -> Mistake 1 (trap+mistake+test) -> Mistake 2 (same) -> Mistake 3 (same) -> Funnel.
2. **Each beat = one cycle.** Trap topic + named mistake + test demo all in one color-coded beat.
3. **Cold open visual gag.** Curiosity in 0-5s before any dialogue (e.g., Mission Impossible mouthpiece swap).
4. **Voice fingerprint:** "Now,", "right?", second person, repeats key terms 3-5x, names wrong way before right way, metaphors mid-sentence.
5. **Funnel pattern:** callback to tests + NEW knowledge gap question + "Hint: it's not what you think" + point to embouchure video card.
6. **Locked lines for hook, apparatus reveal, mistake callouts, funnel CTA.** Riff topics for everything else.
7. **Save deliverables to BOTH** project output AND `~/Downloads/` (per `feedback_pdfs_to_downloads.md`).
8. **PDF aesthetic:** warm off-white #FAF7F2 bg, near-black 22px Inter, 7-color vibrant accent palette per beat, no boxes around script, generous whitespace, max-width 760px single column.

## Reference files (read when generating a new script)

- `~/.claude/skills/pb-script/references/example-mouthpieces-script.md` (the proven structural template)
- `~/.claude/skills/pb-script/references/script-writing-protocol.md` (full ruleset)
- `/Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md` (voice source)

## Why this matters

The 2026-04-25 session went through 12+ iterations on a single script because I kept regressing on these patterns. Future script work should hit the bar in 1-2 iterations, not 12.

## CRITICAL: applies even outside the pb-script-write skill

These rules apply to ANY script-related work in this project, not just inside the `pb-script-write` skill. If Timo pastes a draft with locked phrasing in a free-form conversation, I must preserve it character-for-character. Regression on this happened immediately after the rules were written. Verify before drafting: "did Timo write the cold open already? If yes, preserve it verbatim, no improvising."
