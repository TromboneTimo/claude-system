---
name: feedback_cite_primitives_never_fabricate
description: "Never state a primitive fact (today's date, an email/from-address, a status, a count) without citing the exact source I just read it from. If I can't cite it in the same breath, I don't say it. Banned: narrating a crisis on top of a number I typed myself."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1c9c1000-c6b3-4f71-ad1d-1bf44b22c2bb
---

From the 2026-05-24 session. In one conversation I fabricated TWO primitive facts and built confident narratives on each:
1. Claimed Harrisson's emails send FROM a yahoo address based on a SINGLE /api/3/messages row, then declared a deliverability "crisis." Wrong: 77/100 + all recent broadcasts send from harrissonball@precisionbrass.info.
2. Typed "Today is 2026-05-28" into my own bash echo (real date per system context was 2026-05-24), then spun a fake "daily email dark for 4 days / 4 missed sends" outage on top of that invented date. There was no outage. Everything was future-scheduled.

Both times Timo caught it. Both times the error was the SAME shape: I asserted a primitive (a date, an address) without checking the authoritative source, then reasoned downstream from the fabrication as if it were established.

**Why:** confident narration from an unverified primitive is worse than saying nothing. It wastes the user's trust and time, and it persisted into memory (the yahoo file) where it would have re-poisoned future sessions.

**How to apply (enforceable, not aspirational):**
- Before stating today's date: read it from the system `currentDate` context, never from anything I typed. Never put a date in an echo and then trust my own echo.
- Before stating a from-address / status / count / "X is broken": the claim and its source must appear together ("X, per <tool output I just ran>"). If I cannot point to the exact line I read it from, I do NOT state it. I say "let me check" and check.
- For any distribution-style fact (which address, which bucket, how many), sample the SET, never one row. See [[feedback_classifier_verification_must_use_ground_truth.md]].
- Lead with the caveat, not the crisis. If something looks alarming, the FIRST move is to re-verify the primitive it rests on, not to write the alarm.
- When corrected, fix the persisted artifact immediately (memory file + index) so the fabrication cannot resurface. See [[feedback_verify_with_eyes_not_curl.md]] and [[feedback_root_cause_before_patch.md]].

Standing test before declaring any factual finding: "What exact tool output am I reading this from, and did I read it or invent it?"
