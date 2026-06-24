---
name: feedback_diagnose_with_control_and_surface_failures
description: "Don't announce a root cause until you've checked it against a known-good control; run the definitive end-to-end test BEFORE theorizing; label hypothesis vs proven; and make failures visible where the user actually looks."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 25cd0445-216c-44ea-993d-1bfdbf782ae2
---

From the 2026-06-01 "emails stopped sending" session. Timo: "It seems like you're still unclear what was causing the issue, and you're just guessing. Can you be more thorough?" then "There has to be some way for you to test this works" then "if there's an error it needs to show."

What I did wrong, specifically:
1. I declared a root cause before verifying it against a control. I wrote "Found the smoking gun: sourcesize=0" on the stopped campaigns, then had to RETRACT it because the campaign that sent FINE also had sourcesize=0. A field that is identical in the broken AND working case is not a cause. I also confidently floated "account-level sending block," "bulk schedule-all path is buggy," and "frequency-cap collision" across successive turns; each was killed by evidence I could have pulled first.
2. I theorized for multiple rounds when a definitive end-to-end test existed the whole time (send through the real pipeline to the safe test list). Timo had to TELL me to test. The single scheduled-send test settled in 3 minutes what 4 turns of speculation could not.
3. I narrated guesses in the language of conclusions ("smoking gun", "this is X"), which is exactly what read as "you're guessing."
4. I built the safety net (Slack watchdog) but left the failure invisible on the dashboard Timo actually watches. The broadcasts table drops send_amt<=50, so a 0-recipient stop just vanished. He had to ask "why didn't it register as not sent in the dashboard."

**Why it matters:** announcing unverified causes erodes trust, wastes the user's time, and risks "fixing" the wrong thing. A correct, slower answer beats a fast wrong one (see [[feedback_ship_right_not_fast]]).

**How to apply (every diagnosis, every workspace):**
- CONTROL FIRST. A difference between the broken case and the spec is not a cause until it is confirmed PRESENT in the broken case AND ABSENT in a known-good control. Pull the working instance and compare the same field before you name a cause. (Same discipline as [[feedback_classifier_verification_must_use_ground_truth]]: internal consistency is not proof.)
- TEST BEFORE THEORIZE. If a cheap, definitive end-to-end test exists (send to a safe test target, run the real code path, curl the real endpoint), RUN IT before stacking hypotheses. Reach for the decisive test on move 2, not move 8 (see [[feedback_diagnose_dont_guess]], [[feedback_root_cause_before_patch]]).
- LABEL CONFIDENCE. Say "proven" vs "hypothesis" explicitly. Never use "smoking gun / the cause is / this is why" for anything unverified. Lead with what is verified and what is ruled out, with the evidence for each.
- NAME THE KNOWABILITY BOUNDARY. If the real reason lives somewhere you can't see (a UI the API doesn't expose, a vendor's internal state), say so plainly instead of inventing a plausible cause to fill the gap. ASK, don't invent.
- MAKE FAILURES LOUD AND VISIBLE. Any automated pipeline that can fail must (a) detect absence-of-success, not just log success, and (b) surface the failure WHERE THE USER LOOKS, not only in a side channel. A silent `continue` past a failure, or a list filter that hides the 0-count error row, is a latent multi-day outage. Alert + render the error state in the primary UI.
