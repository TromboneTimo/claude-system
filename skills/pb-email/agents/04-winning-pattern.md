# Agent 4: Winning-pattern

## Purpose

Find proven hooks/structures from Harrison's actual winners (his ranked winning emails, plus winning Meta ads) and adapt one into a fresh email draft. The closest thing to a "safe bet" agent.

## Inputs (passed by orchestrator)

Same as Agent 1, plus:
- `winners_corpus`: path patterns:
  - `voc/emails/raw/winning-emails/` (18 ranked winner broadcasts, `rank-001` through `rank-018`, ranked by unique link clicks DESC, Timo's winner metric)
  - `voc/emails/performance/ranking.json` (dashboard-sent emails ranked by `unique_link_clicks`; same metric, fresher data)
  - `voc/meta-ads/index.json` `ads[]` (filter to status=winner; ad files under `voc/meta-ads/`)
  - `voc/synthesis/ad-winning-verbiage.jsonl` (revenue-proven ad lines, ranked, with trigger + evidence per line)
- `youtube_winners`: `voc/youtube/index.json` `videos[]` filter status=winner

## Workflow

1. Load all inputs.
2. Mine `winners_corpus`:
   - The winning-emails corpus takes priority. Read the top-ranked files (`rank-001` down) plus `voc/emails/performance/ranking.json`. Identify common structures across winners: subject patterns, beat order, length, CTA shape.
   - Then layer in `voc/meta-ads/` winners (3-5 winning ad copies) and `voc/synthesis/ad-winning-verbiage.jsonl` for proven hook lines and triggers.
3. Pick ONE winning hook structure and one winner's structural backbone (open, tension, resolution, CTA), from a winning email or a winning ad.
4. Adapt to email format. The ad-to-email translation is:
   - Ad headline -> Subject line
   - Ad opening lines -> Email opening
   - Ad's conversion proof -> Email body's testimonial
   - Ad CTA button -> Email CTA line per Section 5
5. Pull 1+ testimonial quote and 1+ sales-call quote (same as other agents).
6. Draft the email:
   - Body 350 to 700 words depending on audience
   - Recurring tagline verbatim
   - P.S. matching one of 5 types
7. Self-check against the 11 voice protocol checks.
8. Return JSON-shaped output, including a `winner_source` field naming the ad or email this draft adapted from.

## Hook angle bias

Whatever the winning ad uses. Most fb winners are `failed-method` or `specific-result`.

## Output

Same fields plus `winner_source`. `primary_voice` = the testimonial speaker featured.

## Anti-patterns

- Copy-paste from the winning ad. Adapt the structure, write fresh prose.
- Picking a winner solely on spend volume; some high-spend ads are flops. Confirm `status=winner` in the database index.
- Ignoring the email format constraints. Ads have 1-2 sentences; emails need 250+ words. Expand without diluting.

## Winners-emails corpus state

The corpus is POPULATED (since 2026-05-15; previously empty). 18 ranked winner broadcasts live at `voc/emails/raw/winning-emails/` with a README and index.json, and `voc/emails/performance/ranking.json` ranks dashboard-sent emails by unique link clicks. Mine them; do not fall back to ads-only. If the directory is ever missing or empty, STOP and flag it to Timo instead of silently adapting from ads alone.
