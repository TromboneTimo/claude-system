# Use-Case Tags

Every quote gets one or more `use_for` tags. These match the content formats the downstream content generator produces.

## hook

Short, punchy, scroll-stopping. First 3-10 words of a YouTube title, ad headline, or carousel opener.

**Criteria:**
- Strong emotional charge or vivid image
- Under 15 words when extracted
- Works as the opening frame of a video or ad
- Triggers curiosity, identification, or pattern interrupt

**Examples:**
- "Endurance. Totally endurance." (Phil)
- "Best trumpet teachers I have had." (Heather)
- "I don't know why it all the Schlossberg I did." (Phil)

## content-idea

Quote suggests a whole piece of content. The extraction agent should flag these and the content generator can build TOFU/MOFU/BOFU content around them.

**Criteria:**
- Contains a specific question, misconception, or angle
- Implies a lesson, framework, or demonstrable fix
- Resonates with the ICP's struggle moments

**Examples:**
- "Every teacher said use more air. Nobody showed me how to use less." (implied content: "Why 'use more air' is the worst trumpet advice")
- "I could play high notes cold but lost them after 20 minutes." (implied content: "Why your high notes disappear during a gig")

## ad-copy

Works inline in an ad creative. Paid social, YouTube skippables, display.

**Criteria:**
- Specific enough to pass "only this person could have said this"
- Emotional, vivid, tangible
- Copy-pasteable into ad text with minimal editing

## email-subject

Under 55 characters. Earns the open. Often TOFU pain language or BOFU curiosity.

**Criteria:**
- Short (under 10 words preferred)
- Pattern-interrupting or high-specificity
- Does not summarize the email body (that is preview text)

**Examples:**
- "My chops feel like a stranger's"
- "30 years playing, range worse than college"
- "I got a high C in 3 days"

## email-conversion

Drives the click to a sales page. Often lives at BOFU or late MOFU. Contains proof, urgency, or specific outcome.

**Criteria:**
- Implies or states a decision point
- Contains numbers, timeframes, or named results
- Works as the P.S. or closing block of an email

## testimonial

Full endorsement language. Usable as a standalone testimonial block on a landing page or ad.

**Criteria:**
- Names the program/coach by name or attribute
- States a before/after with some specificity
- Recommends the solution to someone else

**Examples:**
- "Best trumpet teachers I have had." (short testimonial)
- "I had not played a high C in 8 years. In three days with Harrison I got one and it was consistent." (long testimonial)

## Multi-tag rule

Most quotes will earn 2-4 tags. A strong testimonial might be tagged `[hook, testimonial, email-subject]`. A vivid pain quote might be `[hook, ad-copy, email-subject]`. Do not over-tag low-value quotes. If a quote earns 0 use-for tags, it is too generic to extract.
