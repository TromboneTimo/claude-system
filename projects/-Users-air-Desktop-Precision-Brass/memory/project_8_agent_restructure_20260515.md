---
name: project-8-agent-restructure-20260515
description: "pb-script and pb-email restructured 2026-05-15 from 6-agent / 7-agent to 8-agent specialist rosters. New roster + database scaffolding (Instagram, HYROS el-tag attribution) + remaining gaps."
metadata: 
  node_type: memory
  type: project
  originSessionId: 467afc37-9455-4e76-8762-b666eca3bdcb
---

# 8-Agent Restructure 2026-05-15

**Why:** Timo wanted more specialists, not fewer. The old roster (6 agents in pb-script, 7 in pb-email) didn't have dedicated personalities for channel-performance analysis, masterclass mining, testimonial rotation, sales-call rotation, or random wildcard exploration. He explicitly asked for 8+ specialists with rotation-aware anti-recycling.

**How to apply:** This restructure changes what `/pb-script` and `/pb-email` do on every run. Both now spawn 8 parallel specialists + 1 sequential auditor.

## The 8 specialists (both skills)

| # | Personality | What it owns |
|---|---|---|
| 1 | Channel Performance Analyst | `youtube-database/`, `voc/meta-ads/`, `instagram-database/` (once populated). HYROS click attribution per `hyros_el_tags`. Cross-channel pattern detection. |
| 2 | Masterclass Specialist | Deep read of `voc/masterclass/raw/transcript.md` + voice bank + quotes JSONL. Lifts moments into content. |
| 3 | Testimonial Rotator | 2-3 random testimonials from 11-file pool, anti-recycling via `voices_used_log.jsonl`. |
| 4 | Sales Call Random-Rotation | 6-8 random sales calls from 28-file pool, anti-recycling. |
| 5 | Random Raw Wildcard | 1 random source from wildcard pool (research, converter, email-seq, yt-comments, vtt), anti-recycling. |
| 6 | Hidden Pain Hunter (pb-script) / Objection Dissolver (pb-email) | HP1-HP8 framework / OBJ1-OBJ8 framework. |
| 7 | Objection Dissolver (pb-script) / P.S. Trigger Specialist (pb-email) | OBJ1-OBJ8 / one of 5 P.S. types. |
| 8 | Conversion Trigger Detector (pb-script) / Best-Practices Auditor (pb-email) | T1-T8 / `~/.claude/research/perplexity/raw/` filtered to Email Marketing. |
| 9 | Voice + Diversity Auditor (sequential) | Reviews ~12-15 candidate pool, picks final 5 with anchor diversity enforcement. |

## Anti-recycling fields tracked

Both `voc/voices_used_log.jsonl` (pb-script) and `voc/email_voices_used_log.jsonl` (pb-email) now log per run:
- `testimonial_files` (which 2-3 testimonial files Agent 3 used)
- `salescall_files` (which 6-8 sales call files Agent 4 used)
- `wildcard_source` (which 1 wildcard source Agent 5 used)
- `primary_voices`, `secondary_voices`
- `lenses` (OBJ-X, HP-Y, T-Z)
- `channel_perf_anchored_idea` (Agent 1's pick)

## HYROS click attribution wiring

`youtube-database/index.json` schema v2 now includes `hyros_el_tags` per video. Each long-form video has 1-2 attribution tags embedded in masterclass CTA URLs via `?el=<tag>`. Backfilled from descriptions for the 3 published videos 2026-05-15:

- O4a-q93ENAg ("How to Form THE Easiest High Note"): `timostopbuyingmp`, `youtubetrumeptembouchure`
- sOMst4eGP2A ("Stop Buying Trumpet Mouthpieces"): `timostopbuyingmp`
- c_Wu86MFglo ("Trumpet Embouchure"): `theultimatetrumpetembouchureYT`

HYROS API access: `process.env.HYROS_API_KEY` (Vercel encrypted, also at `~/.claude/credentials/MASTER.md` HYROS section). Endpoint `https://api.hyros.com/v1/api/v1.0`. The existing `api/hyros.js` and `api/hyros-diag.js` Vercel functions have the query logic. Channel Performance Analyst can dispatch HYROS queries directly or call the deployed `/api/hyros` endpoint.

## Instagram database scaffolding

`instagram-database/` folder created 2026-05-15. Empty scaffold (README + index.json). Schema mirrors `youtube-database/`. Meta Graph API integration pending. A future `ig-vault` skill will ingest posts.

## Files changed in the restructure

- `~/.claude/skills/pb-script/SKILL.md` (description, Step 1, Step 2 fully replaced, Step 3 auditor updated, reference files cleaned)
- `~/.claude/skills/pb-email/SKILL.md` (description, Step 3 pickers, Step 4 spawn, Step 5 auditor, agent table)
- `~/.claude/skills/pb-script/references/raw-deep-dive-rotation.md` (masterclass removed from rotation; entire file deprecated)
- `Precision-Brass/youtube-database/index.json` (schema v2 with hyros_el_tags)
- `Precision-Brass/youtube-database/*/metadata.json` (hyros_el_tags + masterclass_cta_urls per video)
- `Precision-Brass/instagram-database/` (new scaffold)

## Known gaps still open

1. **HYROS click-per-video queries.** Schema is in place but the Channel Performance Analyst's prompt assumes it can hit the HYROS API. Need to test the actual query path on first run. May need a helper script.
2. **Instagram ingestion.** Scaffold exists, no posts yet. Timo will provide Meta Graph API token, then we build `ig-vault`.
3. **FB ad performance data.** All 3 ads in `voc/meta-ads/` have null performance fields. Channel Performance Analyst will note this and continue.
4. **`pb-script-write` and `pb-email-write` not updated.** Those are Phase 2 skills (single-idea expansion). They don't spawn the 8-agent roster, so they don't need this restructure. Their reference to `voc/masterclass/raw/` is already in place.
