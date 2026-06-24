---
name: Deck Flow QA (Story-Level, Not Just Pixel-Level)
description: After any slide edit, read the entire deck top-to-bottom. Verify every conjunction word's antecedent. Search for duplicate promises across non-adjacent slides. Visual QA is necessary but not sufficient.
type: feedback
originSessionId: 00ef9822-ed7d-4ee8-bfc3-2bc52d7bde1b
---
# Deck Flow QA — Story-Level

**Rule:** Visual QA per slide (headless render + read PNG) is necessary but NOT sufficient. After any slide edit, read the ENTIRE deck top-to-bottom as a continuous script. Verify narrative continuity, not just pixel correctness.

**Why:** On 2026-04-13 Timo caught multiple flow failures I missed:
1. Slide 1 said "Give me 3 minutes." Slide 3 said "In the next few minutes, I'll tell you exactly why..." — same promise twice, two slides apart. I edited slide 1 in isolation and never checked the rest of the deck for duplicates.
2. Slide 2 opened with "And on web designers..." which works (continues slide 1's "burning money on ads"). Slide 4 opened with "And when someone googles your name..." — the "And" had no antecedent because slide 3 was about competitors using AI, not about a list. I treated "And" as a stylistic choice, not a logical claim.
3. Slide 4 → Slide 5 had a zero-bridge transition (Google competitor → bought a dependency). Two unrelated beats placed adjacent.

Timo's exact words: "the slides keep starting with the word and, but the slides dont flow from one to another, why arent you catching this? why are you so fucking stupid?"

Root cause: I QA'd each slide as an independent unit. I rendered each, checked overflow/images/numbers. I never read the deck as a viewer would — slide 1, then slide 2, then slide 3, watching the story unfold.

## Mandatory Checks After ANY Slide Edit

1. **Top-to-bottom read.** Open the actual file. Read every slide's text in order. Treat it as a continuous script. If you stumble between slides — that's the bug.

2. **Conjunction audit.** Search for slides starting with: `And`, `But`, `Because`, `So`, `Then`, `Yet`, `Or`. For each one, verify the previous slide's closing sentence makes the conjunction earned. "And on web designers" requires the previous slide to have set up a list. "Because X" requires the previous slide to make a claim that needs explaining. If the antecedent isn't there, either rewrite the conjunction or restructure.

3. **Duplicate promise audit.** Phrases like "Give me 3 minutes", "In the next few minutes", "I'll show you", "By the end of this" are PROMISES. There should be ONE promise per deck. After any edit, grep the file for promise patterns.

4. **Narrative beat map.** Every deck has beats: pain → diagnosis → reveal → fix → CTA (or hook → proof → twist → escalation → resolution). After edits, name the beat each slide serves. If two adjacent slides serve the same beat without being a one-two punch, consolidate. If two adjacent slides serve different beats with no bridge, write the bridge.

5. **Read aloud test.** Mentally narrate the deck. If you'd say "uh, anyway..." between two slides, the transition is broken.

## The Failure Mode This Prevents

- Editing one slide and breaking continuity with adjacent slides
- Leaving redundant promises scattered across the deck
- Slides starting with conjunctions that have no antecedent
- Two unrelated narrative beats placed adjacent with no bridge

## What "Done" Means for a Slide Deck

NOT done when: every slide renders correctly in headless Chrome.
NOT done when: typography hierarchy passes the 20-25% ratio test.
NOT done when: no fabricated numbers, no broken images, no overflow.

DONE when: a viewer can read slide 1 → slide 2 → slide 3 → ... → slide N without ever asking "wait, what?" or "why is this here?"

## Related Memories
- feedback_visual_qa.md (per-slide pixel verification — required as foundation)
- feedback_slide_hierarchy.md (typography ratios)
- feedback_pregeneration_checklist.md (4-item pre-gen check)
- feedback_confirm_scope.md (restate scope before building)

This memory adds: NARRATIVE QA on top of pixel QA. Both are required. Pixel without narrative = the bug Timo kept catching.
