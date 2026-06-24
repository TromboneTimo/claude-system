---
name: Subagent Output Is Advisory, Not Authoritative
description: When a subagent returns recommendations, treat the diagnosis as authoritative but treat the prescription as a draft. Filter every recommendation through your own judgment before executing, especially when Timo says "do everything."
type: feedback
originSessionId: bb11f5ff-044e-47bd-9a9d-ecc9b0a26bf5
---
When you spawn a subagent for analysis (audit, research, diagnosis, recommendations), the returned report has two parts: what's WRONG and what to DO about it. The first part is usually right. The second part is often partially wrong and needs filtering.

**Why:** 2026-04-22 contract audit. The subagent correctly diagnosed that Harrisson got confused by the per-component pricing math during a call. Its prescription was to "collapse the $1,500 coaching credit line" into the notes column. I executed the prescription verbatim. Timo caught it: collapsing a client-favorable deduction into notes hides a benefit the buyer should see prominently and weakens the seller's negotiating position. The right fix was different (clearer labeling, not deletion of the line). The agent's diagnosis was right; its prescription was wrong; I shipped the prescription anyway.

Same pattern as the 2026-04-20 proposal-writer initial build, where I executed the audit agent's structural recommendations (Artifact 11-section pattern) without filtering for what Timo actually needed (Harrisson 6-section signable contract). And the 2026-04-21 fabricated-tagline incident, where the audit agent's recommendation drove a contract addition I should have asked about first.

**How to apply:**

1. **When a subagent returns a report**, separate it into "diagnosis" (what is true about the current state) and "prescription" (what to change). Trust the diagnosis. QC the prescription.

2. **Before executing any prescription**, ask three questions:
   - Does this actually serve the user's goal, or just the agent's framing of the problem?
   - Who benefits from this change? If the user is the seller and the change hides terms favorable to the buyer, that weakens the user's negotiating position. Reverse it.
   - Is the agent solving the right problem? It might have correctly identified a confusion or gap but proposed the wrong fix. Often the right fix is "make it clearer," not "remove it."

3. **When Timo says "do everything" or "apply all of these,"** that is permission to act, NOT a waiver of your filter. You still owe him a critical pass on each item before shipping. Bulk-approval shortens the review cycle, it does not eliminate it.

4. **If you decide to override or modify a subagent's prescription**, say so in your response so Timo knows you applied judgment instead of just executing. Example: "Agent recommended X. I applied a softer version because X would hide a benefit Harrisson should see."

5. **The bigger frame**: subagents are like junior staff. Their fact-finding is faster than yours and often more thorough. Their judgment calls are not yet calibrated to the user's goals. Treat them as research-and-draft, not as decisions-shipped.

**Crosswalk to existing memory:**
- Builds on `feedback_match_reference_exactly.md` (don't import generic patterns when user-specific patterns are needed).
- Builds on `feedback_proposal_default_pattern.md` (visible client-favorable terms stay visible).
- Reinforces the audit-state-before-prescribing rule in `~/.claude/knowledge/audit-state-before-prescribing.md`.
