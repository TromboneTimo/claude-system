---
name: Enumerate all failure axes before shipping a visual fix, not just the one you saw
description: When the user reports a visual issue, list every plausible contributing factor (source asset, data file, CSS, component logic, container sizing, animation state, both languages) and verify each before declaring the fix complete.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
When a user reports "this looks wrong," do not ship the first fix that addresses only the aspect you noticed. Enumerate the full set of possible causes and verify each.

**Why:** On Samurai Brass (2026-04-22), user asked to remove white from album covers. I shipped three iterations: (1) threshold 240 missed grey gradient; (2) added per-album bg padding but still left CD jewel-case edges; (3) finally added inward inset to strip case edges. Each iteration exposed one more axis I hadn't checked. A single up-front enumeration (source asset has pure white? case edges? padding color? container aspect? animation timing? JA toggle?) would have caught all of them in one pass.

**How to apply:**
- Before writing a fix for a reported visual issue, list the axes:
  1. Source asset (is the input image/data itself dirty?)
  2. Data/config (per-item colors, sizes, variants in a data file?)
  3. CSS container (aspect ratio, padding, background matching?)
  4. Component logic (hardcoded strings, missing lang branches, state transitions?)
  5. Animation/transition (initial state, active state, timing, easing?)
  6. Downstream language modes or responsive breakpoints
- For each axis, ask: "if this were the only bug, would it reproduce the user's screenshot?" If yes, verify before shipping.
- After shipping the fix, do a full visual pass (both langs, multiple items in the list, hover/active states) before reporting done.
- Iterating 3+ times on the same complaint is a signal that the first enumeration was incomplete. Stop and re-enumerate, don't guess again.
