# Agent 4: Winning-pattern

## Purpose

Find proven hooks/structures from Harrison's actual winners (Facebook ads, eventually winning emails) and adapt one into a fresh email draft. The closest thing to a "safe bet" agent.

## Inputs (passed by orchestrator)

Same as Agent 1, plus:
- `winners_corpus`: path patterns:
  - `voc/raw/winning-emails/` (currently empty as of 2026-04-21)
  - `facebook-ads-database/*/` (filter to status=winner)
- `youtube_winners`: path pattern `youtube-database/*/index.json` filter status=winner

## Workflow

1. Load all inputs.
2. Scan `winners_corpus`:
   - If `voc/raw/winning-emails/` has any files, those take priority. Read all. Identify common structures across winners.
   - If empty (current state), fall back to `facebook-ads-database/*/` winners. Read 3-5 winning ad copies. Identify hook patterns.
3. Pick ONE winning hook structure and one winning ad's structural backbone (open, tension, resolution, CTA).
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

## Empty winners-emails fallback

If `voc/raw/winning-emails/` is empty, log a note in the rationale: "Adapted from FB ad winner '{ad name}'. Winner-emails corpus is empty; ingest performance-tagged emails to grow this corpus." This surfaces the corpus gap to Timo.
