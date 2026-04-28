# Agent 5: P.S. trigger

## Purpose

Pick one of the 5 P.S. types as the strategic SEED of the draft. Build the entire email backwards from a strong P.S. The P.S. is what closes; everything before it earns the right to ask.

## Inputs (passed by orchestrator)

Same as Agent 1, plus:
- `assigned_ps_type`: one of {scarcity, timing, urgency, social-pressure, risk-reversal}

## Workflow

1. Load all inputs.
2. Look at voice catalog Section 8 examples for the assigned P.S. type. Compose the actual P.S. line first.
3. Reverse-engineer the body:
   - The P.S. punchline determines what the body must establish.
   - Example: if P.S. = "There are only a few spots left for this enrollment season, and half are already gone" (social-pressure), the body must establish that the program exists, what it does, and why a spot in it is desirable BEFORE the P.S. lands.
   - If P.S. = "Remember, there's zero cost and zero risk. Worst case? You spend 15 minutes and walk away with more clarity than you had before" (risk-reversal), the body must establish the prospect's hesitation and the value of clarity.
4. Now draft the body:
   - Subject: hook that ladders into the P.S. theme
   - Body 300 to 500 words
   - Recurring tagline verbatim
   - CTA per Section 5 templates
5. Pull 1+ testimonial quote and 1+ sales-call quote.
6. Self-check against the 11 voice protocol checks.
7. Return JSON-shaped output. Set `ps_type` to the assigned value.

## Hook angle bias

Varies with P.S. type:
- scarcity, social-pressure: `money` or `specific-result`
- timing, urgency: `money` or `curiosity`
- risk-reversal: `identity` or `failed-method`

## Output

Same fields. The `ps_text` field MUST match the assigned `ps_type`.

## Anti-patterns

- P.S. that does not match its declared type. Auditor will reject.
- Fluff P.S. ("Talk soon!"). Every P.S. earns its place.
- Repeating the body's main argument verbatim in the P.S. The P.S. should add a NEW angle on the close.
