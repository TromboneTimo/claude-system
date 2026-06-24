---
name: feedback_email_batch_trope_diversity
description: "Across a BATCH of Harrisson emails, vary the opener, reframe, myth, and proof student. ~5 reflex tropes (use-more-air, it-was-never-you, nobody-ever-told-you, for-years, the-wall) must each appear at most once per batch. Verify against the live queue BEFORE drafting, not after Timo catches it. Also: stop oscillating between extremes when corrected."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e78e3def-a8e6-435a-868b-29e6509590cd
---

2026-06-04: Timo asked if my "fresh" email rewrite "sounds exactly like other emails we've drafted." I checked all 16 scheduled bodies (June 5-20) and he was right. The whole queue leans on the same handful of moves, so every email reads same-y even when individually fine.

**The reflex tropes I rotate (cap each at ONCE per batch):**
- "use more air" myth-bust (was in 3 of 16 + my new draft)
- "it was never you / the problem was never you" reframe (5 of 16)
- "Here is something nobody in your section/world ever told you" opener (4 of 16)
- "for years..." (6+ of 16)
- "the wall you keep hitting" (4 of 16)
- "Quick rant." opener (3 of 16, two were near-identical mouthpiece-drawer rants back to back)

**Why this happens (root cause):** the three "bar-setting" reference drafts in [[feedback_email_friend_to_friend_depth]] are ALL confession + myth-bust + teach. Cloning them faithfully mass-produces sameness. The friend-to-friend depth rule made each email good in isolation but never enforced variety ACROSS a set. Diversity has to be a batch-level gate, not a per-email one.

**The winners we UNDER-use (rotate these shapes in):** the proven winning-emails corpus (`voc/emails/raw/winning-emails/`) does NOT use the myth/Rachel/"never you" machinery at all. It wins with: concrete one-day result micro-stories ("Mike added 3 notes in one day", "my sound got 20% bigger"), a specific named drill taught start-to-finish ("the routine that built my range"), real backstage stories with a turn (Dimitri's "the grip that changed everything"), and genuine usable nuggets lists (Ed Lawrence's 100 nuggets). Pull from these, not just the confession formula.

**Rotate the proof student.** We have Brad, Mike, Kay, Heather, Yens, Rachel (masterclass transcript + testimonials). I default to Rachel. Spread them; never reuse the same student twice in one batch.

**How to apply (MECHANICAL pre-draft check, run BEFORE writing, not after):**
1. Pull the live scheduled queue bodies: `email_proposals?status=eq.scheduled&select=subject,body,hook_angle,pain_point`. Grep openers, reframes, myths, and proof students already in flight.
2. Pick an opener archetype + proof student + myth (if any) NOT already used in the batch.
3. After drafting, grep the new body against the trope list above. Any trope already at its cap in the queue = rewrite.
4. Aim for distinct ENTRY MODE per email: result-story / named-drill / backstage-story / nuggets-list / myth-bust / confession / direct-challenge. No two adjacent emails share an entry mode.

**META lesson (applies beyond email): STOP OSCILLATING.** When Timo corrects something, BEFORE swinging, grep memory for the prior correction on the SAME axis and synthesize toward the middle. This session I swung walls -> one-sentence-per-line -> caught again, because I never checked I'd corrected the paragraph axis 48h earlier ([[feedback_email_short_paragraphs]]). Over-correcting to the opposite extreme is its own failure mode. See also [[feedback_diagnose_with_control_and_surface_failures]] (find the real cause), [[feedback_ship_polish_not_skeleton]].

Pairs with [[feedback_email_friend_to_friend_depth]], [[project_email_swipe_file_and_beat_cloning]], [[project_winning_emails_corpus]], [[feedback_email_short_paragraphs]].
