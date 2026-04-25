---
name: yt-vault
description: Ingest a YouTube video into the Precision Brass video database. Pulls metadata, transcript (auto-captions), top 200 comments + replies, and writes a structured analysis citing prospect-psychology.md and voc/personas/ files. Tracks status (winner / flop / unrated), sales attribution, and sales history over time. Use this skill any time Timo (or Harrison) says "store this video", "store this youtube", "add to yt vault", "add to youtube database", "save this video to the database", "ingest this youtube", or pastes a YouTube URL with the words winner, flop, or sales attached. Also trigger when the user says "this video made N sales" with a YouTube URL, "study why this video worked / flopped", or "add to the youtube db". This is the canonical way new videos get into the analysis loop, so always use it instead of trying to handcraft the folder structure.
---

# yt-vault

Ingest a YouTube video into `Precision-Brass/youtube-database/` so future content scripts can study what worked (winners) and what didn't (flops). Outputs raw transcript, structured comments, metadata, and an analysis grounded in the project's voice-of-customer files.

## When to trigger

Use this skill on any of these:

- "store this video <URL>"
- "store this youtube <URL>"
- "add to yt vault" / "add to youtube database" / "add to the youtube db"
- "ingest this youtube"
- "save this video to the database"
- A YouTube URL pasted alongside the words `winner`, `flop`, `sales=N`, `made N sales`
- "study why this video worked / flopped"

If status (winner/flop) or sales count is missing, ASK before proceeding. Don't guess.

## What the user must give you

Required:
- **YouTube URL**

Strongly preferred (ask if missing):
- **Status:** `winner` | `flop` | `unrated`
- **Sales attributed:** integer (use `0` if a flop or unknown, and note it in the analysis)

Optional:
- **Slug:** 2-4 word lowercase hyphenated descriptor (e.g. `embouchure-truth`). If omitted, the script auto-derives one from the title.
- **Note:** any context about WHY Timo is storing this one ("retest after 30 days", "Harrison wants to dissect")

## What this skill produces

Folder at `Precision-Brass/youtube-database/<YYYY-MM>_<slug>_<videoID>/` with:

| File | Purpose |
|---|---|
| `metadata.json` | Flat schema. URL, title, channel, views, likes, comments, status, sales_converted, sales_history, last_updated |
| `transcript.md` | Deduped + timestamped auto-caption transcript (medium confidence) |
| `comments.json` | Top 200 comments + replies, structured (author, likes, replies, pin/uploader flags) |
| `comments-top.md` | Top 50 by likes, human-readable, with Harrison's replies inline |
| `analysis.md` | The whole point. 12-move structural breakdown citing `context/prospect-psychology.md` + `voc/personas/`. See `references/analysis-template.md` |

Also updates `Precision-Brass/youtube-database/index.json` (master list).

## Workflow

### Step 1. Confirm inputs

If the user did not give status + sales, ask for them in one short message. Don't proceed without both. Example:

> Got the URL. Two things before I store it:
> 1. winner / flop / unrated?
> 2. how many sales did this video drive (use 0 if flop or unknown)?

### Step 2. Pull raw data via yt-dlp

`yt-dlp` is installed at `/Users/air/Library/Python/3.10/bin/yt-dlp` (or just on PATH). Run:

```bash
mkdir -p /tmp/yt-vault-staging
cd /tmp/yt-vault-staging
yt-dlp --skip-download \
  --write-info-json \
  --write-auto-subs --sub-lang en --convert-subs srt \
  --write-comments \
  --extractor-args "youtube:max_comments=200,200,all,all" \
  -o "%(id)s" \
  "<URL>"
```

This writes `<videoID>.info.json` and `<videoID>.en.srt` into the staging dir.

Note: yt-dlp prints a verbose progress log. That's normal. Look for `Extracted N comments` to confirm comments came through.

### Step 3. Run the processor

```bash
python3 /Users/air/.claude/skills/yt-vault/scripts/process_video.py \
  --info-json /tmp/yt-vault-staging/<videoID>.info.json \
  --srt /tmp/yt-vault-staging/<videoID>.en.srt \
  --status winner \
  --sales 3 \
  --slug embouchure-truth \
  --out-root /Users/air/Desktop/Precision-Brass/youtube-database
```

Required flags: `--info-json`, `--status`, `--sales`, `--out-root`. `--srt` is optional (skip transcript if not present). `--slug` is optional (auto-derived from title).

If the video is already in the vault, the processor updates `metadata.json` in place (preserving `sales_history`, appending a new snapshot) and updates the `index.json` row.

### Step 4. Write `analysis.md`

The processor does NOT write `analysis.md`. You do. This is where the value is, and it requires reading the transcript and citing the right voice-of-customer files.

Read `/Users/air/.claude/skills/yt-vault/references/analysis-template.md` for the full structure. In short:

1. Header block (status, sales, views, likes, comments, source files cited)
2. TL;DR. 3-5 numbered reasons it worked or flopped, each tied to a structural move + a psych principle
3. Audience match. Did the ICP show up in comments? Cite specific commenters
4. Structural moves. For winners, score against the 12 canonical moves (in `references/converting-video-embouchure-transcript.md`). For flops, score which moves are MISSING or BROKEN
5. Comments map. 2-column table: commenter pain language vs won-deals pain language from `voc/personas/won-deals-voice-bank.md`
6. Reproducible pattern checklist. Markdown checkboxes the next script should hit
7. What we don't know yet (retention curve, attribution mechanism, channel baseline)
8. How to use this analysis for the next script

Sources you must cite from:
- `Precision-Brass/context/prospect-psychology.md`
- `Precision-Brass/voc/personas/comments-voice-bank.md`
- `Precision-Brass/voc/personas/won-deals-voice-bank.md`
- `Precision-Brass/voc/personas/lost-deals-voice-bank.md` (especially for flops)
- `Precision-Brass/voc/personas/objection-library.md` (for credibility / price / time objections)
- `Precision-Brass/references/converting-video-embouchure-transcript.md` (the proven-converter 12-move template)

### Step 5. Confirm with Timo

Tell Timo:
- The folder path
- View / like / comment counts
- Comment count actually scraped (sometimes capped)
- That the analysis.md is written and ready for review
- Any caveats (e.g. transcript is auto-caption medium confidence, sales is placeholder until DB hookup)

## Updating an existing video (re-store)

When Timo says "update sales for <URL>" or "re-store this video, it's now N sales":

1. Re-run yt-dlp (so view/like/comment counts are fresh)
2. Re-run the processor with the new `--sales N`
3. The processor preserves `sales_history` and appends today's snapshot
4. Re-read transcript briefly. If no major content changes, you don't need to rewrite `analysis.md`. If retention pattern changed (e.g. the video went viral), update the analysis with the new conclusions.

## Error handling

- **"command not found: yt-dlp"** → check `which yt-dlp`. The Mac install is at `/Users/air/Library/Python/3.10/bin/yt-dlp`. Add to PATH or use the absolute path.
- **"Extracted 0 comments"** → comments are off on this video, or the channel disabled them. Set `comment_count: 0` in metadata, note in analysis.md, proceed.
- **"No subtitles for en"** → the video has no auto-captions yet (very new uploads). Skip `--srt` argument, transcript.md gets a placeholder. Re-run in 24-48 hours.
- **Channel handle / video private** → yt-dlp errors with `Private video`. Tell Timo, ask whether to skip or get the URL fixed.
- **Em dash hook blocks Write** → the project hook `~/.claude/hooks/block-em-dashes.sh` blocks any Write that contains an em dash. If you see "BLOCKED: Em dash detected", rewrite the content with periods, commas, or colons. This applies to analysis.md.

## Style and tone (Timo's preferences)

- Direct. No fluff. No padding adjectives.
- Cite specifics or flag as unknown. Never write "the hook is strong" without naming the timestamp + transcript line + psych principle.
- Verbatim customer quotes go in `> "..."` blockquote format. Never paraphrase.
- For winners: prove WHY by quoting commenters who match won-deals pain language.
- For flops: name which canonical moves are missing. Don't be polite about it.

## Why this skill exists

The vault is the substrate that lets every future video script get smarter. Each entry feeds the script-creation loop in `CLAUDE.md` (Phase 1, Topic Selection). When Harrison says "I want to make a video about endurance," Claude opens `youtube-database/index.json`, finds the existing endurance videos, reads their analyses, and proposes a script that replicates winner moves while avoiding flop traps.

If the vault is sloppy, every future script is sloppy. So the analysis.md quality bar is high. See `references/analysis-template.md` for the standard.
