# The Beat-Cloning Method (pb-email drafting law)

Built 2026-05-31 from a full teardown of 275 real emails (Dimitri Fantini, Ed Lawrence / Film Booth, Max / Inbox Newsletter) stored at `voc/emails/swipe-file/`, cross-checked against Harrison's OWN send performance and his own content. This is HOW every pb-email draft gets written. It is not optional flavor; it is the drafting law.

## THE LAW

Every draft does three things or it is not a send, it is a reject:

1. **Clone a real swipe-file template skeleton.** Pick one actual stored email, extract its beat map, write Harrison onto the identical beats (subject pattern, beat order, rhythm, CTA shape, P.S. shape). Do not freelance a structure. Mimic a proven one.
2. **Fill every slot from Harrison's OWN material.** The hook, story, analogy, and teaching come from his masterclass transcript or one of his YouTube transcripts, quoted or tightly paraphrased in his words. Never invent a story. He has the content; use it.
3. **Carry one verified proof point.** A specific number or a named, real, sourced student result from `voc/testimonials/raw/` or a sales call. No proof = not a send. (Harrison's own #1 email ever, "I could almost cry," is pure proof. His own data demands this.)

## WHY (evidence, do not re-litigate)

- Harrison's OWN top-clicked sends prove the archetypes: #2 "Use more air and other useless advice" (myth-bust), #3 "What another year of this costs you" (delay-cost), #5 "I'm not 24 anymore" (age), #7 "the I'm too old lie" (age-lie). Only 1 of his top 8 is a student story.
- Swipe data: of Dimitri's 143 emails, 15 open on a named student. Student-story is ~10%, not the default.
- Research [cached]: every email needs an objective; one idea, one CTA; cadence is not the revenue lever, content is; soft-sell daily, hard-sell on launch only; 68% mobile so single-column and scannable.

## THE SOURCE VAULT (USE EVERYTHING, in priority order)

Mining agents MUST pull from these, not just sales calls and testimonials:

1. **Swipe templates (skeleton source):** `voc/emails/swipe-file/raw/<creator>/` + the teardown in `voc/emails/swipe-file/analysis/<creator>.md` + the playbook `voc/emails/swipe-file/STRATEGY.md`.
2. **Harrison's masterclass (primary story source):** `voc/masterclass/raw/transcript.md` + `voc/masterclass/extracts/masterclass-voice-bank.md` + `masterclass-quotes.jsonl`. His verbatim teaching: energy not air, upstream/downstream, gravity breath, embouchure swing, dynamic repetition, Vertical Alignment, James Morrison, "secret to high notes."
3. **Harrison's YouTube transcripts (primary story source):** `voc/youtube/raw/<vid>/transcript.md` + `voc/youtube/extracts/<vid>/`. Current videos: embouchure-truth (the $36K converter), mouthpiece-pressure, 60-vs-550, stop-buying-trumpet, relaxation-routine. Route emails to the matching video (Rung 1).
4. **Testimonials (proof source):** `voc/testimonials/raw/` (11 real students with public videos). Verbatim quotes + real names ONLY.
5. **Sales calls + lessons (wound + proof source):** `voc/sales-calls/raw/`, `voc/lessons/raw/`.
6. **His own winners (pattern + subject source):** `voc/emails/raw/winning-emails/` + `voc/emails/performance/ranking.json` (mimic his proven subject patterns and lengths).
7. **Social comments (live objection source):** `voc/synthesis/social-comments/`.

## THE 7 ARCHETYPES (and which swipe template each clones)

| Archetype | Clone this stored template | Harrison story source |
|---|---|---|
| Myth-bust rant | Dimitri "this is why you're not improving" | masterclass: "use more air is wrong / energy not air" |
| Named-student story (cap ~1 in 8) | Dimitri "he practiced more than you" | a real testimonial student |
| Delay-as-cost | Dimitri P.S. pattern / his own #3 winner | masterclass: "would it be worth it" + cost framing |
| "It's not talent" | Ed "What every Hollywood Bowl player has in common" | masterclass: upstream/downstream, Morrison |
| Curiosity / withheld secret | Dimitri "The metronome is lying to you" | masterclass: "do you think there's a secret to high notes? There is" |
| Personal confession | Ed "That guy was me in 2019" | Harrison's own discovery of Vertical Alignment |
| Result-number / video tease | Ed "Copy This Video, $240k in 90 days" | a YouTube video + its result, routes Rung 1 |

## THE BEAT-CLONING PROCEDURE

1. Open the chosen stored template. Write out its beat map (e.g. Dimitri "he practiced more than you" = 10 beats: name+stuck+timeframe, effort-list+"nobody could say he wasn't trying," it-failed+the-dagger+"for decades," fast-diagnosis+cause, kill-the-false-fix, result+specific-number+"no secret," name-the-offer, what-the-offer-is, proof-person+cheeky-ask, scarcity+CTA).
2. For each beat, write Harrison's line: swap drums/YouTube for trumpet, keep the move and the rhythm. Short fragments where the template has fragments. The dagger stays a dagger.
3. Inject the verified proof point at the result beat (real number/name/quote, else placeholder marked `[REAL STUDENT ...]` for the testimonial pull).
4. Anoint and repeat ONE branded mechanism (Vertical Alignment, or one named secret). Do not invent a new framework name per email.
5. One idea, one CTA, one rung. P.S. sells again (delay-as-cost or fresh proof).

## RANDOMIZATION (rotate 5 dimensions, log every run)

No two consecutive drafts share a shape. Rotate and log to `voc/email_voices_used_log.jsonl` (extend each record with these keys):
- `archetype` (the 7 above; student-story capped ~1 in 8)
- `clone_template` (which stored swipe email's skeleton)
- `story_source` (which masterclass section or YouTube video)
- `cta_rung` (youtube / masterclass / strategy-session, one per email)
- `length_band` (daily 120-220w / launch 600-900w)
- `subject_pattern` (myth / age / cost / not-talent / quote / secret)

Auditor rejects a batch that repeats the prior run's archetype+clone_template+story_source combo.

## LENGTH POLICY (governed by job)

- **Daily teaching send: 120 to 220 words.** Dimitri's median is 134. Tight, one idea, mobile-first.
- **Launch / masterclass-replay / urgency send: 600 to 900 words.** Long only here; Harrison's own long winners were all launch emails.
- Reject a 600-word teaching email and a 120-word launch email. Match length to job.

## HARD GUARDRAILS (unchanged, still enforced)

Real student names only (trace to `voc/testimonials/raw/`). No fabricated authority. Subjects speak to the reader, never name a third-party student. Tagline verbatim. CTAs are hyperlinked anchors, not raw URLs. P.S. inside the body. Body link and P.S. link must not share a destination URL. Ship right, never ship fast.
