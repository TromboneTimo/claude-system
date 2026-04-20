# Quote Entry Template

Canonical example of one line in `voc/quotes/all-quotes.jsonl`. Every quote entry must match this schema.

```json
{
  "quote": "I've been playing 30 years and my range is worse than it was in college.",
  "speaker_type": "prospect",
  "speaker_name": "Jim",
  "source_file": "raw/sales-calls/2026-03-15_salescall_jim_call-14.md",
  "source_timestamp": "00:14:22",
  "pain_point": ["range", "age-regression", "comeback"],
  "emotional_trigger": ["frustration", "identity-loss"],
  "funnel_stage": "TOFU",
  "use_for": ["hook", "ad-copy", "email-subject"],
  "mining_angle": "age-regression",
  "confidence": "medium",
  "notes": ""
}
```

## Field rules

| Field | Required | Values |
|---|---|---|
| `quote` | yes | Exact verbatim text from source. Light punctuation cleanup allowed. |
| `speaker_type` | yes | `prospect` \| `customer` \| `commenter` |
| `speaker_name` | yes | First name string or `"unknown"`. No guessing. |
| `source_file` | yes | Path relative to `voc/`. E.g. `raw/sales-calls/2026-03-15_salescall_jim_call-14.md`. |
| `source_timestamp` | yes | `HH:MM:SS` format. |
| `pain_point` | yes | Array. Pick from approved list or add new tag. |
| `emotional_trigger` | yes | Array. Pick from approved list or add new tag. |
| `funnel_stage` | yes | `TOFU` \| `MOFU` \| `BOFU` |
| `use_for` | yes | Array. Subset of `[hook, content-idea, ad-copy, email-subject, email-conversion, testimonial]`. |
| `mining_angle` | yes | Short kebab-case slug describing the lens under which the quote was pulled. |
| `confidence` | yes | `high` \| `medium` \| `low`. Never `high` for auto-captioned sources. |
| `notes` | no | Free text. Flag unusual names, suspected errors, or context a consumer should know. |

## Approved tag vocabularies

**pain_point** (extend as needed):
range, endurance, mouthpiece, embouchure, consistency, age-regression, comeback, practice-habits, accountability, fundamentals, tone, articulation, breathing, identity-loss, plateau, confidence

**emotional_trigger**:
frustration, identity-loss, invisibility, relief, validation, pride, embarrassment, curiosity, hope, desperation, surprise, shame, anger, grief

**use_for**:
hook, content-idea, ad-copy, email-subject, email-conversion, testimonial
