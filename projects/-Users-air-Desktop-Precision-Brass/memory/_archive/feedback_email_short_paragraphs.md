---
name: feedback_email_short_paragraphs
description: "Harrisson email bodies MUST use short paragraphs (1-2 short sentences each, lots of whitespace), like Dimitri. NEVER cram 6-8 sentences into one <p>. Walls of text are banned."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 349b39de-60b0-406b-8c46-6d46a2bd309a
---

2026-06-02: Timo sent screenshots comparing my Harrisson emails (dense 6-8 sentence paragraphs, walls of text) against a real Dimitri Fantini email (every paragraph 1-2 short sentences with air between them). Mine were far harder to read. He was angry I shipped walls and did not notice, when the reference emails I am supposed to be cloning are visibly airy.

**Why:** readability is part of the deliverable, not an afterthought. A wall of text kills the friend-to-friend feel and tanks the read-through even when the words are good. The swipe-file teardowns even call this out: Dimitri is "plain, short-paragraph, white-space-as-rhythm." I had the reference in hand and still crammed.

**CORRECTED 2026-06-02 with hard data.** Timo pushed back on "1-2 short sentences" as too rigid and choppy. I measured all three swipe creators' real emails. The data:
- **Ed Lawrence / Film Booth (1057 paras):** 85% are ONE sentence, 14% two, 1% three. Sentence length swings: p25=6 words, median=12, p75=18, MAX=57.
- **Max / Inbox (3922 paras):** 82% one sentence. Sentence words 6/10/15/55.
- **Dimitri (1506 paras):** 59% one sentence, 24% two, 10% three (the only one who clusters for staccato runs). Sentence words 5/10/15/52.

**The rule for EVERY email body (pb-email, pb-email-write, ad-hoc):**
1. **One THOUGHT per `<p>` block, usually one sentence.** Ed and Max are ~85% single-sentence paragraphs. Two sentences only when tightly linked. Three is rare (Dimitri-style staccato only). White space comes from one-thought-per-line.
2. **VARY sentence length deliberately. Do NOT force everything short.** That was my mistake and it reads choppy and monotone. Mix 5-6 word punches with 15-20+ word flowing lines (Ed goes up to 57 words in a single line). Median ~10-12 words. The alternation between short and long IS the rhythm.
3. **A long sentence is fine on its own line.** The thing that is banned is CRAMMING multiple sentences into one block (my 6-8 sentence walls). Never break a single sentence mid-way into its own paragraph (lowercase fragments read broken).
4. Numbered-lever lines (`<strong>1. ...</strong>`), the CTA anchor, the sign-off, the P.S., and the tagline each stay their own block.
5. Model the paragraphing AND the short/long sentence rhythm on the actual swipe emails in `voc/emails/swipe-file/raw/film-booth/` and `dimitri-fantini-drums/`, not on a blog post.

**Tooling:** `/tmp/reflow.py` pattern (or rebuild it) mechanically splits dense `<p>` blocks at sentence boundaries and re-patches email_proposals rows. It keeps structural blocks (links, em, strong, br, P.S.) intact and lint-guards tagline/link counts. Used 2026-06-02 to fix all 19 scheduled+proposal emails (paragraph counts roughly doubled). Reuse it whenever bodies come out dense.

**Self-check before declaring any email done:** look at the body as the reader will see it. If any paragraph is more than ~3 lines tall, split it. This is part of the [[feedback_ship_polish_not_skeleton]] polish gate and pairs with [[feedback_email_voice_spine_not_tone]] and [[feedback_email_friend_to_friend_depth]].

**CORRECTED AGAIN 2026-06-04 (the other extreme).** Applying "one thought per <p>" MECHANICALLY (the reflow.py split-every-sentence pass) produced the opposite failure: every sentence on its own line, which Timo called "soft" and "reads like a list," not friend-to-friend prose. BOTH extremes are banned: 6-8 sentence walls AND one-sentence-per-line lists. The real target is Dimitri's RENDERED rhythm: group a narrative/descriptive beat into 2-3 linked sentences in ONE block, and let a one-liner stand alone ONLY when it lands as a punch (the turn, the gut-shot, the reveal). The 85%-single-sentence stat is measured per sentence, NOT a license to isolate every sentence; Ed/Dimitri still read as grouped because long flowing sentences fill a line and related thoughts sit together. Do NOT mechanically reflow; group by thought-unit with editorial judgment, eyeballing against `dimitri-fantini-drums/` rendered. This walls<->list ping-pong is the oscillation failure called out in [[feedback_email_batch_trope_diversity]] (check for the prior correction on this axis before swinging again).
