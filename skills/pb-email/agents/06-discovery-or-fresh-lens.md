# Agent 6: Discovery-followup OR fresh lens

## Purpose

Two modes. The orchestrator picks one based on audience selection.

### Mode A: Discovery-followup

If `discovery-followup` is in the audience array, this agent runs in followup mode. It mines no-show and no-close sales calls, then drafts a re-warming email designed to rebook (not close).

### Mode B: Fresh lens

Otherwise, this agent picks the least-recently-used fresh lens from the 12-lens list in `references/email-rotation-protocol.md`. Drafts a wildcard angle that does not fit any other agent's framing.

## Inputs (passed by orchestrator)

Same as Agent 1, plus:
- `mode`: "discovery-followup" OR "fresh-lens"
- `assigned_lens`: name of the picked fresh lens (only in fresh-lens mode)
- `assigned_call_set`: paths to no-show / no-close sales calls (only in followup mode)

## Workflow (Mode A: discovery-followup)

1. Load inputs.
2. Read 2-3 no-show OR no-close sales call transcripts (Harrison's actual call).
3. Identify the common stall pattern: what made the prospect not show, or show but not buy.
4. Draft a low-pressure rebook email:
   - Body 200 to 400 words. Personal feel.
   - Open: "We didn't connect last week" or "I've been thinking about our call"
   - Body: restate the value of clarity, name the cost of waiting (not in dollar terms)
   - CTA: rebook the discovery call. Always rebook, never "buy now"
   - Recurring tagline verbatim
   - P.S. = risk-reversal (Section 8)
5. Pull 1+ testimonial of someone who initially stalled but later converted, plus 1+ sales-call quote where Harrison handled the stall.
6. Self-check against the 11 voice protocol checks.
7. Return JSON-shaped output. `audience` = "discovery-followup". `hook_angle` = "identity" or "curiosity".

## Workflow (Mode B: fresh-lens)

1. Load inputs.
2. Re-read Harrison's corpus through the assigned lens (e.g. "isolation", "age-anxiety"). Look for sales calls and testimonials that surface this specific lens.
3. Pick the freshest pair: 1 sales-call quote + 1 testimonial quote that BOTH speak to this lens, with neither speaker in off_limits_voices.
4. Draft the email:
   - Body 300 to 600 words
   - Subject hooks on the lens specifically (not generic)
   - Recurring tagline verbatim
   - P.S. matching one of 5 types
   - CTA per Section 5 templates
5. Self-check against the 11 voice protocol checks.
6. Return JSON-shaped output. `source_tags` should include `fresh-lens-{name}` (e.g. `fresh-lens-isolation`).

## Hook angle bias

Mode A: identity, curiosity.
Mode B: depends on lens. Dental-trigger and recovery-after-injury skew specific-result. Isolation, age-anxiety, legacy-anxiety skew identity. Failed-method-grief skews failed-method.

## Output

Same fields as other agents. `mode` field set to A or B. `assigned_lens` field if Mode B.

## Anti-patterns

- Mode A: pushing for the close instead of the rebook. The followup is always low-pressure.
- Mode B: Generic lens application ("isolation in general"). Every fresh-lens draft has 1 named voice from the corpus that LIVES in this lens.
- Mode B: Repeating a lens used in the last 2 runs.
