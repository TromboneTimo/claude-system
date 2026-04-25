---
name: fb-vault
description: Ingest a Facebook ad into the Precision Brass ads database. Saves the creative file (mp4/jpg), ad copy (primary text, headline, description, CTA), performance numbers (spend, impressions, CTR, CPA, ROAS, conversions), audience targeting, and writes a structured analysis citing prospect-psychology.md and voc/personas/ files. Mirrors the structure of yt-vault. Tracks status (winner / flop / unrated, set by Harrison) and sales attribution. Use this skill any time Timo says "store this ad", "store this fb ad", "add to fb vault", "add to facebook ads database", "save this ad to the database", "ingest this facebook ad", or pastes ad copy / a creative file path / a Facebook Ad Library URL with the words winner, flop, sales, ROAS, or CPA attached. Also trigger when the user says "this ad converted N sales", "this ad bombed", "study why this ad worked / flopped". Currently fully manual ingestion. Future Meta Ad Library API hookup is planned (see project_future_todos.md). Always use this skill instead of handcrafting the folder structure.
---

# fb-vault

Ingest a Facebook ad into `Precision-Brass/facebook-ads-database/` so future ad scripts can study what worked (winners) and what didn't (flops). Outputs creative file, structured ad copy, performance data, metadata, and an analysis grounded in the project's voice-of-customer files.

Mirrors `yt-vault` for consistency. Major difference: there is no automated scraper for Facebook ads (yet). Ingestion is manual until the Meta Ad Library API is wired up.

## When to trigger

Use this skill on any of these:

- "store this ad <copy/path/URL>"
- "store this fb ad" / "store this facebook ad"
- "add to fb vault" / "add to facebook ads database" / "add to the fb db"
- "ingest this facebook ad"
- "this ad converted N sales" / "this ad flopped"
- "study why this ad worked / flopped"
- Timo pastes ad copy or a creative file path alongside the words winner / flop / ROAS / CPA / sales

If status (winner/flop) is missing, ask Timo to confirm what Harrison decided. **Do not threshold a winner/flop verdict from numbers automatically.** Harrison decides; numbers are stored for reference only.

## What Timo will give you

It varies. Ingest whatever's there and flag what's missing in `metadata.json` so the analysis can address gaps. Common shapes:

**Shape A. Full rich entry:**
- Ad copy (paste or file path to a .txt/.md)
- Creative file path (.mp4 or .jpg)
- Performance numbers (spend, impressions, CTR, CPA, ROAS, conversions)
- Audience name and targeting notes
- Launch date, end date
- Status (winner/flop/unrated) and sales count
- Optional: FB Ad Library URL

**Shape B. Quick entry:**
- Just ad copy + status + sales count
- Performance numbers come later
- Creative file dropped in `/tmp/fb-staging/` or pointed at directly

**Shape C. Reference-only entry (competitor or inspiration ad):**
- FB Ad Library URL
- Timo's notes about why he's saving it
- Status = `unrated`, sales = 0, performance = empty
- Used for ideation, not for sales attribution

The skill handles all three. Don't refuse if data is partial. Run the processor with whatever's there.

## What this skill produces

Folder at `Precision-Brass/facebook-ads-database/<YYYY-MM>_<slug>_<adID>/` with:

| File | Purpose |
|---|---|
| `metadata.json` | Flat schema: ad_id, slug, status, sales_attributed, sales_history, audience, dates, ingestion_source |
| `creative/copy.md` | Primary text, headline, description, CTA, destination URL, all in markdown |
| `creative/ad.mp4` or `creative/ad.jpg` | The actual creative file, copied from wherever Timo provided it |
| `performance.json` | spend, impressions, CTR, CPA, ROAS, conversions, hook rate, hold rate (any combination) |
| `analysis.md` | The whole point. 6-move structural breakdown citing `context/prospect-psychology.md` + `voc/personas/`. See `references/analysis-template.md` |

Also updates `Precision-Brass/facebook-ads-database/index.json` (master list).

## Workflow

### Step 1. Confirm inputs

Ask Timo for missing essentials in ONE short message. Don't ask field-by-field. Example:

> Got the ad. To store it I need:
> 1. winner / flop / unrated (Harrison's call)
> 2. sales attributed (use 0 if flop or unknown)
> 3. creative file path, or paste the copy and skip the visual
>
> Anything you have on spend/CTR/ROAS/audience name helps the analysis but is optional.

### Step 2. Run the processor

Build the command from whatever Timo provided. Example for a full entry:

```bash
python3 /Users/air/.claude/skills/fb-vault/scripts/process_ad.py \
  --ad-id <meta-ad-id-or-manual-NNN> \
  --slug pain-hook-comeback \
  --status winner \
  --sales 4 \
  --launch-date 2026-04-10 \
  --primary-text "$(cat /tmp/copy.txt)" \
  --headline "Stop fighting for high notes" \
  --cta "Learn More" \
  --destination-url "https://precisionbrass.info/webinar-registration..." \
  --audience-name "Comeback Players 50+" \
  --creative-path /tmp/fb-staging/ad.mp4 \
  --creative-type video \
  --spend 412.50 \
  --impressions 18230 \
  --clicks 287 \
  --ctr 1.57 \
  --cpa 103.13 \
  --roas 2.4 \
  --conversions 4 \
  --out-root /Users/air/Desktop/Precision-Brass/facebook-ads-database
```

For minimal entries, drop the optional flags:

```bash
python3 /Users/air/.claude/skills/fb-vault/scripts/process_ad.py \
  --ad-id manual-002 \
  --slug effortless-demo \
  --status unrated \
  --sales 0 \
  --primary-text "$(cat /tmp/copy.txt)" \
  --out-root /Users/air/Desktop/Precision-Brass/facebook-ads-database
```

The processor:
- Copies the creative file into the ad's `creative/` folder
- Writes `creative/copy.md`, `metadata.json`, `performance.json`
- Updates `index.json`
- Preserves `sales_history` on re-runs of the same `ad_id`

### Step 3. Write `analysis.md`

The processor does NOT write `analysis.md`. You do. This is where the value is.

Read `/Users/air/.claude/skills/fb-vault/references/analysis-template.md` for the full structure. In short:

1. Header block (status, sales, performance numbers, audience, source files)
2. TL;DR. 3-5 numbered reasons it worked or flopped
3. Audience match. Did the targeting hit the ICP per `prospect-psychology.md` lines 6-11?
4. The 6-move ad framework: hook / promise / mechanism / proof / CTA / audience-named. For each, cite the specific copy line + a psych principle + a verbatim customer quote
5. Comments map (if comments are available)
6. Performance read. What the numbers say AND don't say
7. Reproducible pattern checklist
8. What we don't know yet (attribution windows, audience overlap, landing-page bottlenecks)
9. How to use this for the next ad

Sources to cite:
- `Precision-Brass/context/prospect-psychology.md` (the central reference)
- `Precision-Brass/voc/personas/won-deals-voice-bank.md`
- `Precision-Brass/voc/personas/lost-deals-voice-bank.md` (especially for flops)
- `Precision-Brass/voc/personas/objection-library.md`
- `Precision-Brass/voc/personas/voice-bank.md`
- `Precision-Brass/voc/personas/comments-voice-bank.md`
- `Precision-Brass/voc/personas/harrison-email-voice.md`

### Step 4. Confirm with Timo

Tell Timo:
- The folder path
- What was stored vs what was missing
- That `analysis.md` is written and ready for review
- Caveats (manual ingestion, sales is placeholder, etc.)

## Updating an existing ad (re-store)

When Timo says "update sales for ad <ID>" or "this ad now has 8 sales":

1. Re-run the processor with the new `--sales N` and the same `--ad-id`
2. The processor preserves `sales_history` and appends today's snapshot
3. If creative or copy changed (a new variation), use a new slug or new ad_id, don't overwrite

## Audience-mismatch check (do this BEFORE writing analysis)

The single most common reason an otherwise good ad flops is wrong audience. Before writing the analysis, ask yourself: did this ad target the ICP per `prospect-psychology.md`?

ICP: 40-65, US-based, comeback / community-band / church / business-owner trumpet players.

If the audience was "trumpet players 18+ worldwide" or "interested in jazz" with no age cut, that's the failure mode. Call it out in section 3 of the analysis.

## Future work [PLANNED]

### Meta Ad Library API hookup

Currently fully manual. When the Meta Ad Library API (or Marketing API for Harrison's own ads) gets wired up, this skill will gain an `--from-meta` mode that auto-pulls creative, copy, audience, and performance from the API.

**Reminder when Timo asks to wire it up:**
- He'll need a Meta App ID + secret (`developers.facebook.com` → My Apps → Create)
- For HIS ads: Marketing API access token with `ads_read` permission
- For COMPETITOR ads: Ad Library API (limited to political/social/election unless using the public web search)
- The processor already accepts `--ingestion-source api` for provenance tagging
- See `Precision-Brass/memory/project_future_todos.md` for the full TODO

This is also footnoted in `facebook-ads-database/README.md`.

## Error handling

- **No creative file provided** → ad still gets stored. `metadata.json` flags `creative_filename: null`. Note in `analysis.md` that visual analysis was skipped.
- **No performance numbers** → `performance.json` has nulls. Note in analysis section 6 that performance read is deferred until numbers come in.
- **Em dash hook blocks Write** → the project hook `~/.claude/hooks/block-em-dashes.sh` blocks any Write that contains an em dash. If you see "BLOCKED: Em dash detected", rewrite with periods, commas, or colons.
- **Folder name collision** → if Timo uses the same slug for a re-launch, append `-v2` to the slug (`pain-hook-comeback-v2`) and treat it as a new ad. Reuse only when the ad is the same and we're updating numbers.

## Style and tone (Timo's preferences)

- Direct. No fluff.
- Cite specifics or flag as unknown. Never write "the hook is strong" without naming the line + psych principle.
- Verbatim ad copy in `> "..."` blockquote format.
- For winners: prove WHY by quoting commenters or won-deals that match the ad's pain language.
- For flops: name which of the 6 moves are missing or broken. Don't be polite.
- Audience targeting is part of the analysis. A great creative on the wrong audience is a flop. A weak creative on the right audience can still convert. Always check audience match first.

## Why this skill exists

Same logic as `yt-vault`. Each ad in the vault makes the next ad smarter. When Harrison says "I want to run a new ad about endurance," Claude opens `facebook-ads-database/index.json`, finds existing endurance ads (winners + flops), reads the analyses, and proposes copy that replicates winner moves while avoiding flop traps.

The vault is the substrate. Sloppy ingestion = sloppy next ad. So the analysis quality bar is high. See `references/analysis-template.md`.
