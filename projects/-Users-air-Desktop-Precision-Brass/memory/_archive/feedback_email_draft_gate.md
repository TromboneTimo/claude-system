---
name: email-draft-gate
description: Draft-time enforcement for emails. 4 checks + visible GATE proof line above every draft. Born 2026-06-10 when 4 existing rules got broken in one draft cycle despite being in context.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ea6cac20-d8ce-4380-b08e-5be242db8d60
---

Canonical gate: `~/.claude/knowledge/email-draft-gate.md`. Wired into pb-email (auditor rule 8) and pb-email-write (chat draft gate step 0).

**Why:** 2026-06-10 quiz-email session. Timo: "clearly you're not learning and applying your learnings... I keep having to remind you." Four rules that already existed (specific named technique, swipe-file pacing, no oscillation, batch diversity) were injected into context by the angle-ledger hook and STILL broken at draft time. Knowledge in context does not equal execution at draft time.

**How to apply:** Before pasting ANY email draft in chat: (1) READ 2-3 dimitri swipe-file emails this session, never draft from a remembered rhythm description; (2) check every question's grammar matches its answers (action question, action answers); (3) the mechanism must be a do-able named Harrison technique verbatim from a transcript, a diagnosis is soft cock; (4) synthesize corrections toward the middle, never flip extremes. Then print the 1-line `GATE:` proof block above the draft so Timo can see the gate ran. No proof line = not paste-able.

Related: [[feedback_email_batch_trope_diversity]], [[feedback_email_quality_gate_pipeline]], [[feedback_email_cite_specific_technique_and_vary_transition]]

## Detail (moved from index 2026-06-10)
Send-time gates (send-rhythm-gate hook, angle-ledger) already existed and were NOT enough: the rules broke at DRAFT time, before any send gate could fire. That is why this gate runs at draft time, before pasting any draft in chat.
