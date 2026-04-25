---
name: pb-script-write
description: Phase 2 of Harrison Ball's Precision Brass YouTube content engine. Generates a full filming-ready script for a single idea picked from the pb-script menu. Outputs a colorful, scannable HTML doc + PDF (saved to project output AND ~/Downloads/) with the proven 7-beat interleaved structure (Cold Open + Hook, Demo, Apparatus Reveal, Mistake 1 / Mistake 2 / Mistake 3 each woven trap+mistake+test, Funnel). Follows Harrison's voice fingerprint (second-person, "Now,", "right?", repetitions, mid-sentence metaphors) modeled on the $36K embouchure converter. Funnel always points to the embouchure video using the converter's "Hint:" pattern. Use this skill IMMEDIATELY after Timo picks an idea from the pb-script menu (replies with "idea N", "go with #N", "let's do that one", "do the mouthpiece one", or any selection from the menu). Also use whenever Timo says "write the script", "make the script", "draft the script", "phase 2", "/pb-script-write", "now write it", "do it", "let's go on idea X", or names a specific idea title from a recent pb-script run and asks for the script. ALWAYS load the reference files before drafting (`references/example-mouthpieces-script.md`, `references/script-writing-protocol.md`, the project memory file `feedback_script_writing_lessons.md`, and the converter transcript at `Precision-Brass/references/converting-video-embouchure-transcript.md`). Do NOT skip the references. They contain the failure modes that cost 12 iterations on the first script. The skill ships an HTML+PDF deliverable. Not text-only.
---

# pb-script-write. Phase 2: Filming-Ready Script Generator

## When to fire

- Auto: immediately after pb-script outputs the 5-idea menu and Timo replies with a selection ("idea 1", "go with #2", "let's do the mouthpiece one", etc.)
- Manual: any time Timo says "write the script", "make the script", "/pb-script-write", "phase 2", "draft the script for X"

## Hard preconditions (do not skip)

Before drafting a single line, READ all of these:

1. `references/example-mouthpieces-script.md`. Proven 7-beat structural template.
2. `references/script-writing-protocol.md`. Full ruleset. 14 failure modes. Voice fingerprint. Funnel pattern.
3. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_script_writing_lessons.md`. Project-level failure memory.
4. `/Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md`. Source-of-truth Harrison voice.

Skipping these = repeating the 12-iteration mistake from 2026-04-25.

## The 7-beat interleaved structure (default)

| Beat | Color | Title | Function |
|---|---|---|---|
| 01 | Coral #E63946 | Cold Open + Hook | Visual gag + locked hook + comeback/age callout + demo promise |
| 02 | Blue #2563EB | The Demo | Part 1 (same content, multiple cups) + Part 2 (shitty setup) |
| 03 | Green #059669 | Apparatus Reveal | Mouthpiece reframe -> BEAT -> apparatus reveal -> definition |
| 04 | Mustard #D97706 | Mistake 1: [Name] | The Trap -> The Mistake -> The Test (woven inside one beat) |
| 05 | Plum #7C3AED | Mistake 2: [Name] | Same woven structure |
| 06 | Magenta #DB2777 | Mistake 3: [Name] | Same woven structure |
| 07 | Teal #0891B2 | Funnel | Callback to tests + NEW provocation question + Hint pattern + embouchure video CTA |

**Interleaving is non-negotiable.** Each Mistake beat contains The Trap (named topic), The Mistake (named with "the first/second/third mistake"), and The Test (visual + riff) in one cycle. Never stack them as separate beats.

## Voice rules

Match Harrison's converter fingerprint. Examples in `references/example-mouthpieces-script.md`:

- Second person + "we"
- Conversational fillers: "Now,", "right?", "Look,"
- Names the wrong way before the right way
- Repeats key terms 3-5 times
- Builds metaphors mid-sentence
- Confident declaratives, no hedging
- Demos woven into the talk ("If I play [demo]")

## Funnel pattern (always)

End the video with this exact structural move (modeled on the $36K converter):

1. Callback: "if you struggled with any of those tests..."
2. NEW provocation: a question the tests don't answer (e.g., "WHERE on your face is the mouthpiece supposed to sit?")
3. Hint line: "it's not where 99% of teachers tell you"
4. CTA to embouchure video: "I broke it all down in this video right here. Make sure you watch that next."

The funnel ALWAYS points to the embouchure video (`youtube-database/2026-04_embouchure-truth_O4a-q93ENAg/`) unless explicitly told otherwise.

## Output format

Generate an HTML file with this design (full template lives in `Precision-Brass/references/example-script-mouthpieces.html`):

- Single column, max-width 760px
- Warm off-white bg #FAF7F2, near-black text #1A1A1A
- Inter sans-serif (22px body, 38px beat titles)
- Beat number in filled colored tile (64x64px, 14px radius)
- 🎥 emoji + colored ACTION pill for visual blocks
- 💬 emoji marker before script blocks
- Section labels (THE 99% LIE, etc.) in beat-color caps, no fills
- Script paragraphs flow with whitespace, no boxes
- CSS: `break-inside: avoid` on `.script` paragraphs to prevent mid-paragraph page breaks

Then convert to PDF via Chrome headless and save BOTH HTML+PDF to ALL THREE locations:

1. `/Users/air/Desktop/Precision-Brass/scripts/YYYY-MM-DD_<slug>.{html,pdf}` (CANONICAL ARCHIVE. always go here. see `project_scripts_archive.md` memory)
2. `/Users/air/Desktop/Precision-Brass/output/YYYY-MM-DD_<slug>.{html,pdf}` (working copy)
3. `~/Downloads/YYYY-MM-DD_<slug>.{html,pdf}` (fast handoff per `feedback_pdfs_to_downloads.md`)

After saving, append a row to `Precision-Brass/scripts/README.md` index table with date / slug / topic / status.

## What goes where

- **Locked lines** (italic, must be verbatim): cold open hook, apparatus reveal line, mistake callouts ("That's how you fall into the first/second/third mistake..."), funnel CTA close.
- **Riff topics** (regular weight, director's notes): trap explanations, mistake elaborations, test riffs. Harrison improvises off these.
- **Visual specs**: preserve EXACTLY as Timo writes them. If he says "Harrison sitting in front of all his mouthpieces", that detail is mandatory. Don't compress it.
- **[HARRISON FILLS]**: tag specific gear / tunes / student names that need Harrison's input. Do not invent.

## Hard rules (do NOT break)

These come from the 2026-04-25 iteration. Each was flagged repeatedly:

1. NO paragraphs of explanation. Bullet director's notes only.
2. NO summarizing Timo's locked lines. Verbatim or nothing.
3. NO dropping visual specs. Preserve them exactly.
4. NO stacking mistakes/tests as separate beats. Always interleave inside the trap beat.
5. NO fabricated stats, social proof, or behavioral claims. Open knowledge gaps, do not invent answers.
6. NO meta-instructions inside the deliverable ("send to Timo", "Harrison fills" lists go in conversation, not on the page).
7. NO third-person clinical register. Always second-person, conversational.
8. NO over-fragmenting. Beats hold many sentences that flow together. Don't make every line its own shot.
9. NO regression. Once Timo corrects something, it stays corrected.
10. NO manhandling Harrison's improv. Locked lines for critical moments, riff topics for the rest.
11. NO mid-paragraph PDF breaks. CSS must protect script blocks.
12. NO design over readability. Script is the hero. No yellow speech bubbles, no italic body, no chat-bubble metaphor.
13. NO em dashes anywhere (project hook blocks them).
14. NO inventing named mistakes from thin air. Pull from corpus or extend a pattern Timo has accepted.

## Workflow

1. Confirm the picked idea title and conversion trigger (carry over from pb-script output)
2. READ all 4 reference files (preconditions above)
3. Outline the 7 beats. Name the 3 mistakes from the corpus or extend a Timo-approved pattern.
4. Draft each beat in Harrison's voice with the locked-lines / riff-topics split
5. Generate the HTML using the proven aesthetic spec
6. Render PDF via Chrome headless, run visual QA on PNG export of each page
7. Copy HTML+PDF to BOTH project output AND ~/Downloads/
8. Report file paths to Timo. Offer to iterate on any beat.

## Reference files (in this skill)

- `references/example-mouthpieces-script.md`. The proven structural template.
- `references/script-writing-protocol.md`. Full ruleset.

These mirror copies in `Precision-Brass/references/` so the skill works even if the project files move.

## What this skill is NOT

- Not Phase 1 (research / 5-idea menu). That's pb-script.
- Not a thumbnail / title generator (titles come WITH the structure).
- Not a teleprompter mode (the doc is for prep + filming, not live-rolling text).
- Not for short-form (long-form first per project CLAUDE.md).