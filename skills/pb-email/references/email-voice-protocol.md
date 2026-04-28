# Email voice protocol (load before any draft)

Every drafting agent in `pb-email/agents/` MUST load these files before composing a single sentence. Order matters.

## Load order (verbatim, every run)

1. `voc/personas/harrison-email-voice.md` (302 lines, the canonical catalog)
2. `output/email-PP01-dental-trigger-FINAL.txt`
3. `output/email-PP03-failed-lessons-FINAL.txt`
4. `output/email-PP05-isolation-FINAL.txt`
5. `voc/raw/email-sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md`. Emails 1 through 7 ONLY.

## Hard exclusion

NEVER load emails 8 through 12 of the webinar sequence. They are signed by Paul The Trombonist and target music educators. Per voice catalog Section 10, they are template leakage and they pollute Harrison's voice if mixed in.

## Voice fingerprint enforcement

Every draft must demonstrate ALL of:

### 1. Opening (Section 1 of catalog)

Pick one of these 4 patterns:
- Direct address with context restated: "Hey %FIRSTNAME%, Congrats! You..."
- Narrator self-introduction: "Hey %FIRSTNAME%, Harrisson Here."
- Exclamation with curiosity tease: "Hey, %FIRSTNAME%! Feeling like...?"
- Soft self-talk with feigned confusion: "Hey %FIRSTNAME%, Just, I'm just a little confused..."

NEVER open with corporate or marketer voice. Always first-name. Often a hanging ellipsis.

### 2. Recurring tagline (Section 3 of catalog)

This line MUST appear verbatim in every draft, near the close:

> We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system.

No paraphrase. No reorder. No "improve". Verbatim.

### 3. Sign-off (Section 2 of catalog)

Pick from observed variants:
- "Looking forward to meeting you, Harrisson Ball, CEO, Precision Brass, Featured in Forbes" (formal)
- "Talk soon, Harrisson Ball" (mid-sequence)
- "Have a beautiful day! Harrisson Ball" (warm)
- "%FIRSTNAME%, wishing you massive success! Harrisson Ball" (warm closer)
- "Your biggest fan, Harrisson Ball, Precision Brass" (high warmth)

Always named. The "Featured in Forbes" credential attaches to formal emails only.

### 4. P.S. (Section 8 of catalog)

EVERY draft includes a P.S. matching one of 5 types:
- scarcity ("Spots are limited. If the calendar is full, just hit reply...")
- timing ("If the calendar is full please check back again tomorrow.")
- urgency ("If you are interested, you must choose a time today, as the calendar is coming offline soon.")
- social-pressure ("There are only a few spots left for this enrollment season, and half are already gone.")
- risk-reversal ("Remember, there's zero cost and zero risk. Worst case? You spend 15 minutes...")

Tag the P.S. type in the draft metadata. The P.S. is never fluff. It always repeats the close with a new angle.

### 5. CTA phrasing (Section 5 of catalog)

CTA always names the asset (training, strategy session, discovery call) plus an adjective (free, complimentary, no-cost). Never bare "click here". Examples:

- "Click here to watch the training and book your complimentary strategy session"
- "Click here to apply for your complimentary strategy session"
- "Click here to book a no-cost strategy session"
- "Click here to apply today!"
- "Apply for a Strategy Session Here"
- "Click here to book your free 15-minute discovery call"

### 6. Vocabulary fingerprint (Section 6 of catalog)

Use trumpet-world terms. The audience expects them:
- Vertical Alignment System / Vertical Alignment Method
- Embouchure (correct spelling)
- Upstream / downstream physiology
- Range, sound, endurance, accuracy
- Recovery time
- Aperture, pivot, register, slots
- Conking out (informal)
- Arban's, Schlossberg, Chicowitz, Charlie Porter (name-drops for credibility)

NEVER use:
- "Mastermind" (template leakage from Email 3, voice catalog Section 10)
- "Music educators" (Paul-template leakage)
- "Profitable, flexible online teaching business" (Paul-template leakage)
- Generic SaaS or marketer language

### 7. Tone calibration (Section 9 of catalog)

- Funny vs Serious: serious-leaning, occasional levity. Never jokey.
- Formal vs Casual: strongly casual. Contractions everywhere. "Y'all" is fine.
- Respectful vs Irreverent: mostly respectful. Drops the gloves mid-sequence ("If that stings a little, good").
- Enthusiastic vs Matter-of-fact: enthusiastic. Multiple exclamation points OK. "Massive success." "I love." High affect.

If you cannot find real energy in the topic, do not fake it. Harrison's reader filter catches fake hype.

### 8. Student name proofs (Section 4f of catalog)

Every draft that cites a student MUST use a real name from `voc/raw/testimonials/`. Concrete, specific, timeframed:

- Mike: high G to Double Bb in 1 day
- Joinville: 2 months in, hit E above high C
- Enrique: clean consistent high G, repeatedly

NEVER invent a name. NEVER use a vague "one of my students" without naming.

### 9. Defense framing (Section 4b of catalog)

If the draft addresses a prospect who has been through failed methods, include the defense reframe:

> You're not lazy. You're not undisciplined. And you're definitely not "bad at trumpet." You've just been taught a system that was never designed to work long-term.

This is the bridge from shame to solution.

### 10. "It is good for business" frame (Section 4c of catalog)

If addressing skepticism around a free offer, use Harrison's signature explanation:

> Now, you might be wondering why we'd offer this for free. The answer is simple: it's good for business.

Do not replace with guru-style "I just want to help you" language.

### 11. Disqualifier (Section 7e of catalog)

If the draft is a long pitch email, include the 40-minutes-a-day threshold:

> If you don't have 40 minutes a day to play, this won't work.
> If you're looking for shortcuts or magic exercises, this isn't it.
> And if you're happy staying where you are, that's totally fine.

40 minutes is the only quantified threshold allowed.

## Pre-return self-check

Before any drafting agent returns its candidate, it must self-check ALL of:

- [ ] Opening matches one of 4 patterns from Section 1
- [ ] Recurring tagline present, verbatim, near close
- [ ] Named sign-off from Section 2
- [ ] P.S. present, type-tagged, matching declared type
- [ ] CTA from Section 5 templates (not bare "click here")
- [ ] Real student name (if cited) traces to `voc/raw/testimonials/`
- [ ] No "mastermind", no "music educators", no "Paul The Trombonist"
- [ ] No fabricated "Featured in Forbes" or "9,500 trumpet players have watched this training" without source
- [ ] Trumpet-specific vocabulary (range, embouchure, endurance, aperture, etc.)
- [ ] Body length 250 to 800 words. Outside this range, justify in rationale.

If any check fails, repair the draft before returning. The auditor (agent 7) will reject candidates that fail any check.
