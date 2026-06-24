---
name: project-social-comments-corpus
description: "voc/synthesis/social-comments/ holds 2,088 Facebook Page + Instagram comments (Meta Graph scrape). Mining corpus for question patterns, knowledge gaps, and positive-engagement signals. Wired into pb-script + pb-email as always-on."
metadata: 
  node_type: memory
  type: project
  originSessionId: 467afc37-9455-4e76-8762-b666eca3bdcb
---

# Social Comments VOC Corpus

**Why:** Per Timo 2026-05-17. Comments were live-only on the dashboard. He wanted them in the VOC alongside YouTube comments + organized for mining ideas, knowledge gaps, and "what content lands."

**How to apply:**

1. **Source of truth for what Harrison's social audience asks + loves.** All pb-script + pb-email mining agents now have this corpus as an always-on resource.

2. **File map** (`Precision-Brass/voc/synthesis/social-comments/`):
   - `README.md`. Orientation + refresh instructions.
   - `index.json`. Summary stats + topic distribution + Q-rates per category.
   - `all-comments.jsonl`. One comment per line. Grep-friendly.
   - `questions.md`. 65 questions grouped by topic, sorted by like_count DESC. **The "what people are asking" file.**
   - `positive.md`. 51 positive comments grouped by post (top 30 by positive-comment count). **The "what content lands" file.**
   - `by-topic/{slug}.md`. One file per topic category. Both questions + non-questions within each topic.

3. **Quotes layer.** `voc/synthesis/social-comments-quotes.jsonl` holds 1,466 extracted quotes in the same schema as the existing quote aggregator. Speaker type = `prospect` (commenters not yet customers). Tagged with platform, pain_points, use_for, mining_angle.

4. **Topic categories** (15 buckets, same as the dashboard):
   - tone / sound (114 mentions)
   - compliment / praise (51, the "what lands" signal)
   - range / high notes (26)
   - air / breathing (14, **35% Q-rate**)
   - mouthpiece (13, **30% Q-rate**)
   - practice / routine (9, **44% Q-rate**)
   - embouchure / lip (9)
   - tongue / articulation (7)
   - pressure / pain (6, **33% Q-rate**)
   - gear / equipment (6, **33% Q-rate**)
   - jaw / teeth / face (2)
   - comeback / age (1)
   - endurance / fatigue (1)

5. **High-leverage content opportunities** (Q-rate >= 25%):
   - **air / breathing**: 35%. Throat constriction, back pressure, "less air moving faster" questions.
   - **mouthpiece**: 30%. "What mouthpiece are you using?" recurs (4+ instances).
   - **practice / routine**: 44%. Slingshot method, double tongue for beginners, progressive vs go-for-it.
   - **pressure / pain**: 33%. Throat constriction connected to ascending.
   - **gear / equipment**: 33%. "Is that a copper horn?" / "applicable to French horn?"
   - **jaw / teeth / face**: 50%. "How can I hit higher notes? My instrument clamps down too much and I can't hit anything without pressing down on my teeth."

## Refresh

Two-step:
1. `cd /tmp/pb-comments && python3 build.py` (2-3 min, pulls fresh from Meta Graph API)
2. `python3 /tmp/pb-comments/ingest_to_voc.py` (1 sec, overwrites VOC corpus)

The dashboard's Comments tab on `/channel-attribution` does NOT auto-sync to this corpus. Manual refresh required when wanting fresh data in the VOC.

## Wiring

- [[pb-script SKILL.md]] always-on resource section: this corpus is read by every agent every run. Agent 1 (Channel Performance) owns the positive-engagement signal. Agent 6 (Hidden Pain Hunter) owns the question patterns.
- [[pb-email SKILL.md]] always-on masterclass-corpus block: extended to also include this corpus. Channel Performance Analyst (Agent 1) reads it for engagement signal.
- [[project-comments-intelligence-20260517]] documents the dashboard side (live fetch + UI).

## Known limits

- Coverage: 50 most recent FB posts + 50 most recent IG media that had any comments. For full archival (older than ~2-3 months on IG, longer on FB), would need date-filtered pagination.
- Heuristic question detection (ends in `?` or starts with how/what/why/etc.). Misses indirect questions, catches some rhetoricals.
- Categorization is keyword regex. Emoji-only comments (🔥, 🎺) get tagged uncategorized.
- 1,466 quotes extracted to JSONL (filtered out emoji-only + >500-char). Lower than the 2,088 total because of those filters.

## Refresh cadence

Manual for now. If patterns get useful, add a Vercel cron (every 6-12h) that runs the build + ingest. Probably worth doing when Harrison's posting cadence picks up.
