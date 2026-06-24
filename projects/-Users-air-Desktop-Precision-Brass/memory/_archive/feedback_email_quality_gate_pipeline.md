---
name: feedback_email_quality_gate_pipeline
description: "THE enforced pipeline for every Precision Brass email. My self-judgment is removed from the loop: mechanical char-gate BLOCKS walls at send time, an independent agent renders + judges before declaring done, and I read the screenshot myself. Built 2026-06-04 after I shipped walls 3x in one session."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e78e3def-a8e6-435a-868b-29e6509590cd
---

2026-06-04: I shipped a wall of text, over-corrected to one-sentence-per-line, over-corrected again into 4-5 sentence blocks (walls again), THREE times in one session, each time declaring it fixed off my own read. Timo: "you just keep missing it... there has to be a solution that makes you do this right without me ever having to ask again." The root cause was NOT the rule, it was that I self-certified on my own judgment, which is unreliable on rendered density.

**THE FIX = take my judgment out of the loop. Three independent gates, all must pass before any email send or "done":**

1. **Mechanical char-gate (BLOCKS the send).** `scripts/email-rhythm-check.py` flags any `<p>` over ~170 chars (the visual-height wall signal; sentence count alone never fails, short punches are fine). Wired as a PreToolUse hook `~/.claude/hooks/email-send-rhythm-gate.sh` on `send_draft_through_campaign`/`duplicate_campaign`: if the html_body fails, the send is BLOCKED (exit 2). I physically cannot send a wall.

2. **Auto-fired repetition gate.** `scripts/email-angle-ledger.py` + UserPromptSubmit hook `~/.claude/hooks/email-angle-gate.sh` inject the live saturation report into context on any email-intent prompt, so I see overused tropes before drafting (see [[feedback_email_batch_trope_diversity]]).

3. **Independent visual review (no self-certification).** Spawn a FRESH agent that renders each email to a screenshot at phone width, READS the pixels, and returns WALL/LIST/GOOD-RHYTHM + re-verifies every student quote against source + checks tropes. I do NOT declare done on my own read. I ALSO read the screenshot myself (never outsource visual QA, per global VISUAL GATE), but the independent agent is the tiebreaker because my own read is the thing that kept failing.

**THE PARAGRAPH RULE (precise, char-gated, no more oscillation):** Dimitri rhythm = mostly 1-2 sentences per paragraph, max ~170 chars (~2 phone lines), VARIED, with deliberate one-line punches ("That's backwards." / "A major third. In an afternoon."). BANNED both ways: 6-8 sentence walls AND every-sentence-on-its-own-line lists. The char count is the wall signal, not raw sentence count.

**OPERATING SEQUENCE for any email work going forward:**
draft -> run `email-rhythm-check.py` until PASS -> run `email-angle-ledger.py`, confirm no HEAVY trope reused -> spawn independent review agent (render + judge + verify quotes) -> read the screenshot myself -> only then send/schedule. The send hook is the backstop if I skip step 1.

Pairs with [[feedback_email_short_paragraphs]], [[feedback_email_batch_trope_diversity]], [[feedback_email_friend_to_friend_depth]], [[feedback_verify_with_eyes_not_curl]].
