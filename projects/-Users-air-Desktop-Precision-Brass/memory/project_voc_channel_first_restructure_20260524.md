---
name: project-voc-channel-first-restructure-20260524
description: "2026-05-24: voc/ corpus moved from raw/<source> flat layout to channel-first (each channel owns raw/ + extracts/). Path map of record is voc/config.yaml source_paths. Full layout in voc/STRUCTURE.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9627bbfc-ecec-4b40-9187-f019508c4cee
---

# voc/ restructured to channel-first (2026-05-24)

**Why:** Timo wanted the corpus organized by channel (raw lives inside each source), Facebook split organic vs paid, masterclass first-class, no shorts. Single source of truth for where each data type lives.

**How to apply:** The authoritative path map is `voc/config.yaml` → `source_paths`. Human-readable map + judgment calls are in `voc/STRUCTURE.md`. New channels: `youtube/` (long-form only), `facebook-organic/`, `meta-ads/` (paid, was `facebook-ads-database/` at repo root), `sales-calls/`, `lessons/`, `masterclass/`, `testimonials/`, `emails/`, `synthesis/` (cross-channel rollups: all-quotes, voice-bank, comments-voice-bank, objection-library, social-comments/, deep-psychological-dive).

## Key moves (old -> new)
- voc/raw/youtube-long/<vid> -> youtube/raw/<vid> (transcript/comments/metadata) + youtube/extracts/<vid> (analysis/comments-top); index.json -> youtube/index.json; perf -> youtube/performance/
- facebook-ads-database/ -> voc/meta-ads/ (raw/<ad> + extracts/<ad>/analysis.md)
- voc/raw/{sales-calls,lessons,masterclass,testimonials} -> voc/<name>/raw; their voice banks + quotes -> voc/<name>/extracts
- voc/personas/* + voc/quotes/* -> split into each channel's extracts/ or into synthesis/
- voc/raw/winning-emails -> emails/raw/winning-emails; NEW emails/raw/losing-emails (empty, see [[project-winning-emails-corpus]])

## Parked, NOT deleted (voc/_archive/ or left in place)
- youtube-shorts + its perf -> voc/_archive/ (long-form-only rule; shorts deprecated in daily scrape)
- converting-video-embouchure (dup of O4a) + video-transcripts -> voc/_archive/
- Instagram PARKED: voc/raw/instagram-videos, voc/raw/instagram-dms, voc/raw/instagram-videos-performance left in place. No instagram/ channel built. IG comments stay combined with FB in synthesis/social-comments/.

## Code repointed (verify if touching)
- voc/config.yaml source_paths (rewritten)
- dashboard/scripts/daily_pb_scrape.py: LONG_BASE=voc/youtube, LONG_ROOT=voc/youtube/raw, PERF_LONG=youtube/performance, PERF_EMAIL=emails/performance, SHORTS->_archive
- yt-vault process_video.py: writes raw to out-root, comments-top.md + analysis.md to ../extracts, index.json to ../ (channel level)
- fb-vault process_ad.py: writes raw/<ad>, analysis.md to extracts/<ad>
- pb-script, pb-email agents/references; api/hyros.js + dashboard/lib/hyros-source-map.js comments; channel-attribution.html tooltips

## CAVEAT: generic coaching-db NOT changed
`/coaching-db` is cross-workspace and still writes its generic convention (voc/raw/<source>, voc/quotes, voc/personas). PB now diverges. Ingesting new PB sources via coaching-db needs explicit --output-dir overrides to the channel-first paths. PB-specific skills already read the new layout.
