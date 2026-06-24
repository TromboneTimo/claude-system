---
name: Deck Sweep Gates (Em Dash + Specificity + Multi-Slide QA)
description: 3 hard gates that must fire BEFORE declaring any multi-slide deck done. Em dash sweep, specificity check, and real-slide-by-slide visual QA.
type: feedback
originSessionId: 2443ff8e-004a-438e-8db1-84a6007e369a
---
NEVER declare a multi-slide deck done without running these 3 sweeps. All three failed simultaneously on 2026-04-13 urgency-slide rebuild — shipped decks with em dashes (rule I already know), generalized copy (when Timo had named Claude Code twice), and "visual QA" that only captured slide 1.

**Why:** Memories that live as "know the rule" without enforcement checkpoints don't fire. The failure mode is generating, declaring done, then getting yelled at. These 3 sweeps turn passive rules into active gates.

**How to apply:** Run all 3 before any "deck is ready" claim.

### Gate 1: Em Dash Post-Write Sweep
After writing ANY copy in ANY deck:
```
grep -n "&mdash;\| — " <file>
```
Check EVERY hit. Rule out only: HTML comments (`<!--`), `<title>`, `alt=`, name attribution lines (e.g., "— Sarah K., Sales Director"). Everything else is a violation. Also sweep decks I'm editing but didn't originate — em dashes from previous sessions are still em dashes.

### Gate 2: Specificity Check on "Warning" or "Urgency" Slides
When Timo says "warn people about AI" — NEVER write abstract "tools your agency hasn't heard of." Name the specific tool he named. If he said Claude Code, the slide says Claude Code. Generic = dead slide. Decision rule: if I generalized a proper noun Timo used in the prompt, that's fabrication-lite (losing the specificity that makes it true).

### Gate 3: Multi-Slide Visual QA Requires Scroll Manipulation
Default headless Chrome capture shows ONLY slide 1. Decks using `.active` class toggles, scroll-snap, or `height:100vh` + scroll positioning will NOT show slide 2+ in a vanilla screenshot. Required technique:
- For `.active` class systems: copy HTML to tmp, sed-swap which section has `.active`, screenshot
- For scroll-snap systems: copy HTML, sed-replace `scroll-snap-type: y mandatory` → `none` AND `height: 100vh` → `height: auto; min-height: 1080px`, then tall-viewport capture + sips crop
- Keep viewports ≤5000px tall; 20000px hangs headless Chrome

If I can't actually see slide N, I haven't QA'd slide N. Claiming otherwise is the failure mode.
