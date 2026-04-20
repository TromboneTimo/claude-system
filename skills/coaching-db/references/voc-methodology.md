# VOC Methodology: Mine the Quotes, Never Paraphrase

The copywriting tradition behind this skill. Three operators, one principle.

## The principle

Copy that converts uses the customer's exact words. Summaries of customer insights do not. The phrase "I feel like a fraud sitting first chair at 62" converts. "Prospects experience impostor syndrome" does not.

## The practitioners

### Joanna Wiebe / Copyhackers. Message mining framework.

Mine every customer interview, review, and support ticket for:
- **Pain language** (what hurts, in their words)
- **Desire language** (what they want, in their words)
- **Objection language** (what stops them from buying, in their words)
- **Outcome language** (what changed, in their words)

Each category maps to a different funnel asset. Pain powers TOFU hooks. Desire powers MOFU emails. Objection powers MOFU/BOFU ads. Outcome powers BOFU proof copy.

### Jen Havice. Finding The Right Message.

Interview 10-20 customers. Tag every quote by the job-to-be-done framework:
- Struggle moment (what triggered them)
- Before state (who they were)
- Consideration (what they evaluated)
- Purchase (why they said yes)
- Experience (what changed)
- Identity (who they became)

Havice's core insight: the BEFORE state is where TOFU copy lives. The IDENTITY state is where BOFU copy lives. Never write from founder language.

### Joel Klettke. Case Study Buddy.

Raw interview files are immutable. Store them untouched. Extract quotes into a separate tagged sheet. Never rewrite the source. When a quote is disputed, re-check the source.

Klettke's ops pattern:
- Raw file. Never edited.
- Extraction sheet. One row per quote with tags.
- Output copy. References the extraction sheet.

This skill mirrors that architecture: `raw/` (Klettke's immutable source), `quotes/` (extraction sheet as JSONL), `personas/voice-bank.md` (organized reference for writers).

## Why hybrid (raw + quotes + voice bank) beats each alternative

| Approach | Problem |
|---|---|
| Summaries only (what `prospect-psychology.md` used to be) | Kills the exact phrasings that make copy hit. Writing ABOUT customers, not LIKE them. |
| Raw only | Context-window blowout. Agent dumps all raw into prompt, pulls whichever 4K tokens it grabbed, not the best quote. Hallucinations spike. |
| Hybrid (raw + tagged quote bank + thin overlay) | Raw is untouched ground truth. Quote bank is the retrieval index. Voice bank is the fast-loading overlay for priming. Each layer does one job well. |

## Extraction heuristics

A high-impact quote is one that:

1. Uses vivid emotional language. Frustration, relief, transformation, identity.
2. Names a specific pain point with precision, not a category.
3. Describes before/after transformation in the speaker's own words.
4. Would work verbatim as ad copy, hook, or email subject line.
5. Reveals an unexpected angle or objection.

A low-value quote is one that:

1. States a generic sentiment ("I love the program").
2. Paraphrases what a coach said ("Harrison taught me fundamentals").
3. Describes the product, not the outcome.
4. Contains transcript noise (ums, stutters, restart phrases) without semantic content.

When in doubt between two quotes, pick the one with more specific language.

## Applied rule set

- Every extraction run should produce 8-15 quotes per hour of raw transcript.
- If you cannot find the exact phrase in the transcript, you cannot extract it. Full stop.
- Minor punctuation and capitalization cleanup is allowed. Word changes are not.
- If a transcript is poor quality (auto-captions with errors), mark every extracted quote `confidence: medium`. Do not invent clean wording.
