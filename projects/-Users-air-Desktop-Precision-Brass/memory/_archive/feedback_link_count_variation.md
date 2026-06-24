---
name: link-count-variation
description: "Email broadcasts should VARY between 1 unique link and 2 unique links per body. Forcing the same link count on every email reads as template-y. Per email, pick what serves the close best. Caught 2026-05-15 when all 7 emails had exactly 2 links each. Mix matters as much as voice fidelity."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0b9fa848-7b9a-4dda-b396-5cc296f16876
---

# Vary the link count per email. Don't force a template.

**Rule:** Across a batch of broadcast emails (or any cadence), the link count per email should VARY. Some drafts get 1 unique link (the body CTA, P.S. is text-only). Others get 2 unique links (body primary + P.S. secondary pointing to a DIFFERENT destination). The choice per email is based on what serves the close, not on a fixed template.

**Why:** 2026-05-15. After fixing the "no duplicate URL" violation, my 7-draft batch ended up with exactly 2 unique links per email (body + P.S. always going to two different destinations). Timo: "There doesn't always have to be two links. By the way, I would experiment sometimes having one link or having two, but not fucking both in the same place. I think having always two links per email might be a little too template-y for people."

**How to apply (per-draft decision tree):**

1. **1-link drafts.** Use when:
   - The body CTA IS the close (no funnel laddering needed)
   - The P.S. works as a text-only risk-reversal or reply-as-CTA closer
   - The email's energy is single-CTA discipline (best-practices research backs this for high-conversion sends)
   - Examples from 2026-05-15 batch: masterclass-anchored drafts where the masterclass IS the CTA, video-anchored drafts where the video is the close, drafts where the P.S. invites a reply rather than a click

2. **2-link drafts.** Use when:
   - The body has a primary CTA AND a secondary destination genuinely adds value (e.g. testimonial proof after framework, or framework after testimonial)
   - The 2nd link must be a DIFFERENT URL (no duplicates, per [[audit-links-at-url-level]])
   - Examples from 2026-05-15 batch: testimonial-anchored drafts where the P.S. ladders to the masterclass, masterclass-anchored drafts where the P.S. offers a proof video

3. **Across a 7-draft broadcast batch:** aim for roughly 50/50 split. Final 2026-05-15 mix was 4 with 2 links + 3 with 1 link. Don't make it exactly half. Variance is the goal.

4. **NEVER:** all drafts in a batch with the same link count. That's the template-y failure mode.

**Auditor enforcement (pb-email Agent 9):**
- Across the final 5 (or 7) drafts, count unique-link distribution. If all drafts have the same count (all 1-link OR all 2-link), flag for re-roll on at least 2 drafts to introduce variance.
- Per-draft, ban same-URL duplicates (block-severity, per [[audit-links-at-url-level]]).

**Generalization:** Applies to any cadence content (broadcasts, sequences, social posts). Repeating the same structural pattern across a batch turns voice into formula and people unsubscribe. Variance per item, intention per choice.

Related: [[audit-links-at-url-level]], [[query-destination-schema-first]].
