---
name: Negative Rules > Positive Rules (Learn What NOT To Do)
description: When learning from corrections, prefer phrasing the lesson as "NEVER do X" over "always do Y". Negative rules are easier to enforce because there's only one anti-pattern to spot.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
When saving feedback memories, prefer NEGATIVE rules ("NEVER do X" / "STOP defaulting to Y") over POSITIVE rules ("always do X" / "remember to do Y").

**Why negative rules are more efficient:**
- Negative rules block one specific failure pattern. Easier to check.
- Positive rules compete for attention against every other positive rule. The 30+ entries in MEMORY.md prove this — they all want to fire, none reliably do.
- Negative rules state the failure mode as the trigger. Positive rules state the desired behavior as the trigger, which is harder to recognize because the desired behavior is what I should be doing anyway.
- Failure modes are concrete and observable. Best practices are abstract and contextual.

**The shift in framing:**
- ❌ "Always include real brand logos in case study slides" (positive — competes for attention)
- ✅ "NEVER use a fake browser tab labeled with a company name. If the slide cites a real brand, the slide must show the real brand mark." (negative — clear anti-pattern)

- ❌ "Always check the file type after curling an image" (positive)
- ✅ "NEVER pass a sub-3KB file with a `.png` extension to the Read tool. It is an HTML error page. The Read API will crash." (negative — clear anti-pattern)

- ❌ "Always list existing slide elements before rewriting" (positive)
- ✅ "NEVER rebuild a slide from scratch in response to an ADD request. ADD does not mean REPLACE." (negative)

- ❌ "Always generate real visuals when showing a specific change" (positive)
- ✅ "NEVER use generic icon placeholders (play-button rectangles, silhouette boxes) when the slide cites a specific real-world visual AND a working image generator is available." (negative)

**Why:** 2026-04-13 Timo: "perhaps you can learn what NOT to do more than learn what TO DO so we can be more efficient." This is correct. My memory file count keeps growing because positive rules don't displace each other — they accumulate. Negative rules are exclusionary: they remove a specific behavior from my action space.

**How to apply:**
- When writing new feedback memories, lead with the NEVER/STOP phrasing.
- When updating existing memories, rewrite positive prescriptions as negative proscriptions where possible.
- The structure should be: "NEVER do X. Specifically: [the exact failure pattern]. Why: [the concrete cost]. The decision rule that prevents X: [one rule]."
- Length cap: a negative rule should fit in 3-5 sentences. If it needs more, it's probably 2 rules pretending to be 1.
- Do this retroactively too: audit existing memory files and rewrite the positive ones as negative ones. Will reduce memory bloat.

**Meta:** This memory itself follows the pattern. The rule is "NEVER write positive memories when a negative version is available."
