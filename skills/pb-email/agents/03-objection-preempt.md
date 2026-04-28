# Agent 3: Objection preempt

## Purpose

Pick the least-recently-used objection lens (OBJ1 to OBJ8 from `~/.claude/skills/pb-script/references/objection-lenses.md`). Draft an email that names the objection, dismantles it, and bridges to the offer before the prospect has the chance to silently raise it.

## Inputs (passed by orchestrator)

Same as Agent 1, plus:
- `assigned_objection`: one OBJ-N label (e.g. OBJ3) and the objection text
- `objection_lenses_file`: path to pb-script's objection-lenses.md

## Workflow

1. Load all inputs and read the assigned OBJ entry from the objection lenses file.
2. Identify how Harrison historically dismantles this objection. Pull from sales calls in `voc/raw/sales-calls/` where this objection came up and Harrison answered it.
3. Pull at least 1 verbatim sales-call quote where the prospect voiced this objection.
4. Pull at least 1 verbatim testimonial quote from a student who had this same objection going in but converted anyway.
5. Draft the email:
   - Subject: state or hint the objection ("If you've tried 3 different teachers and nothing worked", "What about the 'just use more air' people")
   - Body 350 to 600 words
   - Structure: name objection > why prospect is right to feel it > what is actually true > evidence
   - Use the "you're not lazy, you're not undisciplined" defense reframe (voice catalog Section 4b) if appropriate
   - Recurring tagline verbatim
   - P.S. matching one of 5 types (risk-reversal works well here)
   - CTA per Section 5 templates
6. Self-check against the 11 voice protocol checks.
7. Return JSON-shaped output per `email-output-template.md`.

## Hook angle bias

`failed-method`. Objection emails almost always frame around the failed approach.

## Output

Same fields. `primary_voice` = the sales-call speaker who voiced this objection most clearly.

## Anti-patterns

- Dismissing the objection. ("That's not actually true" without reframing.)
- Skipping the validation step. Every objection email starts with "you're right to feel that way".
- Selling instead of dissolving. The CTA is at the end, not the middle.
