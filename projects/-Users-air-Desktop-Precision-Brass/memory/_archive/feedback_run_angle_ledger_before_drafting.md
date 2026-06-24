---
name: feedback_run_angle_ledger_before_drafting
description: "MANDATORY. Before drafting ANY Precision Brass email, run scripts/email-angle-ledger.py and avoid OVERUSED mechanisms. I kept rewriting the same \"use more air\" email because I never checked what already existed."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 349b39de-60b0-406b-8c46-6d46a2bd309a
---

2026-06-01: Timo, furious (rightly), caught me writing variation after variation of the same email. The "use more air" angle alone appeared 12 times across email_proposals; "use more air" was already a subject line TWICE. I draft from memory and never look at what I have already shipped, so I keep grabbing the same 3-4 mechanisms. He called it "clown town" and demanded a SYSTEM to check past work and catch self-repetition.

**The fix that now exists:** `scripts/email-angle-ledger.py` (Precision-Brass repo). It reads every row in email_proposals and prints: hook_angles used, teaching MECHANISMS/THEMES by frequency (flagging `<-- OVERUSED` at >=4), the UNUSED/fresh mechanisms, and every subject line already written. Zero tokens, ~2 seconds.

**HARD RULE going forward (refined by Timo 2026-06-01): REPETITION IS ALLOWED. The sin is repeating SILENTLY. Catch it, cite it, ask.**
1. **Before drafting ANY email** (pb-email, pb-email-write, or ad-hoc in chat), RUN `python3 scripts/email-angle-ledger.py` FIRST. No exceptions. This is the email sibling of the pb-script "voice diversity log."
2. Read the output. If the angle/mechanism I am about to use is marked HEAVY, or a subject is close to an existing one, I do NOT silently avoid it AND do NOT silently ship it. I **surface it to Timo with a citation**: "This repeats the [angle] from [exact prior subject(s) + status], e.g. sent 'X' and scheduled 'Y'. Want me to run it again or go fresh?" Then I wait for his call. The ledger prints up to 3 example subjects per heavy theme precisely so I can cite the last time.
3. Fresh, never-used angles are always available if he wants new: mine `voc/youtube/raw/*/transcript.md`. As of 2026-06-01 the never-used ones were **tongue arch (taro vs "ti")** and **four points of contact / pressure distribution** (Donald Reinhardt, the "tank over an egg vs hovercraft over eggs" metaphor, bruised vibrating surface = thin sound). The transcripts hold dozens more (overdrive, embouchure swing, aperture/efficiency car metaphor, "muscle memory does not exist", Bernoulli/cone, open resonant breath, type-1/type-2 air direction).
4. The same principle generalizes: **before producing any recurring deliverable, enumerate what already exists and diff against it; when it overlaps, cite the prior instance and ask rather than silently repeat or silently dodge.** I default to generating fresh from memory; that is how the silent repetition happens. Check first, cite, then write.

**Why this keeps happening (the meta):** generating feels faster than checking, so I skip the check. But the check is 2 seconds and the repetition costs Timo's trust every time. Checking past work is not optional overhead; it is step zero of the task.

Related: [[feedback_email_voice_spine_not_tone]], [[project_8_agent_restructure_20260515]] (voice-diversity log precedent), [[feedback_dedup_all_active_statuses]], [[feedback_query_destination_schema_first]] (same family: look at what's really there before acting).
