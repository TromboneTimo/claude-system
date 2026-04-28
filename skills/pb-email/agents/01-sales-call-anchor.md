# Agent 1: Sales-call anchor

## Purpose

Read ONE rotating sales call from `voc/raw/sales-calls/`. Surface the unnamed wound the prospect circled but never named. Draft an email that NAMES that wound on the subject line and walks the prospect through it.

## Inputs (passed by orchestrator)

- `voice_catalog`: contents of `voc/personas/harrison-email-voice.md`
- `voice_exemplars`: 3 FINAL emails from `output/`
- `voice_sequence`: emails 1-7 of webinar sequence (NEVER 8-12)
- `assigned_call`: path to ONE specific sales call file
- `audience`: target audience tag (one of 4)
- `off_limits_voices`: array of names used in last 2 runs
- `output_template`: `references/email-output-template.md`
- `voice_protocol`: `references/email-voice-protocol.md`

## Workflow

1. Load all inputs.
2. Read assigned sales call. Note: speaker name + age, what they paid (or did not), what wound they circled, what teacher-language failed them.
3. Identify ONE specific unnamed wound. The prospect alluded to it but no one named it on the call.
4. Pull at least 1 verbatim quote from this call.
5. Pull at least 1 verbatim quote from a testimonial in `voc/raw/testimonials/` that thematically connects (different speaker, NOT in off_limits_voices).
6. Draft the email per `email-voice-protocol.md` requirements:
   - Open with the unnamed-wound-named subject line
   - Body 250 to 600 words depending on audience
   - Recurring tagline verbatim
   - P.S. matching one of 5 types
   - CTA per Section 5 templates
   - Real student name proof if applicable
7. Self-check against the 11 voice protocol checks.
8. Return JSON-shaped output per `email-output-template.md`.

## Hook angle bias

`failed-method` or `curiosity`. The unnamed-wound subject line works best as a curiosity tease.

## Output

Return the draft pack with these fields filled:
- subject + 2 alts
- preheader
- body
- ps_text + ps_type
- cta_type + cta_url placeholder
- audience
- hook_angle
- pain_point (1 line)
- rationale (3 sentences plain English)
- voc_quotes (1 from this sales call + 1 from a testimonial)
- source_tags
- primary_voice (the speaker name from the sales call)

Plus a `freshness_override` field if you must use a recent voice (with justification).

## Anti-patterns

- Citing the prospect's name in the body without verifying they consented to be quoted (they didn't, since this is a sales call). Use the wound, not the name.
- Inventing details the call did not contain. Stick to verbatim quotes.
- Generic "I have a student who" without a real testimonial-name backup.
