# Agent 2: Testimonial proof

## Purpose

Read ONE rotating testimonial from `voc/raw/testimonials/`. Build an email around that one student's transformation, modeled on the Joinville / Enrique / Mike pattern from voice catalog Section 4f.

## Inputs (passed by orchestrator)

Same as Agent 1, plus:
- `assigned_testimonial`: path to ONE specific testimonial file

## Workflow

1. Load all inputs.
2. Read assigned testimonial. Note: name, age (if given), starting point, specific result, timeframe, what they tried before.
3. Compress into the 3-element pattern: name + specific result + specific timeframe. Examples from voice catalog:
   - "Mike: high G to Double Bb in 1 day"
   - "Joinville: two months in, hit E above high C"
   - "Enrique: clean consistent high G, repeatedly"
4. Pull a verbatim quote from this testimonial.
5. Pull a verbatim quote from `voc/raw/sales-calls/` that thematically connects (different speaker, NOT in off_limits_voices). The sales-call quote is the prospect-side wound. The testimonial quote is the post-state.
6. Draft the email:
   - Subject: name + specific result is the strongest pattern. ("Mike went from high G to Double Bb in 1 day")
   - Body 300 to 600 words
   - Walk through: where they started, what they tried before that failed, what changed, what is true now
   - Recurring tagline verbatim
   - P.S. matching one of 5 types
   - CTA per Section 5 templates
7. Self-check against the 11 voice protocol checks.
8. Return JSON-shaped output per `email-output-template.md`.

## Hook angle bias

`specific-result` or `identity`. Specific-result is the strongest with named-student proof.

## Output

Same fields as Agent 1, but `primary_voice` = the student name from the testimonial.

## Anti-patterns

- Inventing a result the testimonial did not state. If the testimonial says "I can play high notes longer", do NOT translate to "from high G to Double Bb in 1 day".
- Generic results ("amazing transformation"). Always concrete: notes, timeframes, what they could not do before.
- Compressing multiple students into one. Pick ONE and stay with that name.
- Using a name from `off_limits_voices` without `freshness_override` justification.
