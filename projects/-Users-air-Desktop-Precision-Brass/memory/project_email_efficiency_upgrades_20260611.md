---
name: email-efficiency-upgrades-20260611
description: "2026-06-11 broadcast-efficiency build: NO YouTube links (standing order), per-email el=email-<slug> HYROS tags, quadrant script, losers ANTI-PATTERNS, replies in Step 0"
metadata: 
  node_type: memory
  type: project
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

2026-06-11 broadcast-efficiency build (Timo: "we're not linking YouTube videos into emails anymore... increase the efficiency of the daily email list").

**Standing order: NO YouTube links in broadcasts.** No videos, no channel. Every CTA -> master class. cta_type youtube-watch RETIRED. Lint rule `no-youtube-links` (warn-only per [[never-hard-block-user-send]]).

**Per-email HYROS tags: WITHDRAWN same day.** The el=email-<slug> scheme was built on the WRONG destination (registration page) and is REDUNDANT anyway: the HYROS<->AC integration auto-injects per-campaign el tags (sales already show @quick-question etc.), so per-send revenue exists natively. Master class CTA = CANONICAL_MASTERCLASS_URL registry in dashboard/lib/email-lint.js (training-room VSL, no added params). Full story: [[wrong-cta-destination-five-guards]]. The api/hyros.js email-prefix classifier rule stays (harmless, correct for auto-tags).

**New Step 0 inputs for pb-email:** `scripts/email-perf-quadrant.py` (CLONE WHOLE / CLONE SUBJECT / CLONE BODY / AVOID on cohort medians + UNSUB-HOT/BOUNCE flags, MATURING <48h excluded), `voc/emails/raw/losing-emails/ANTI-PATTERNS.md` (9 patterns from the 13 bottom sends; auditor kill-list), `get_recent_replies` MCP (reply themes -> hook angles; too-old pulls 2-5x replies).

**Research applied** (cache 5116e9a0, 23fd6ecc, bf7fd7b4): every email sells (one idea/one CTA), front-load subject's first 4-6 words (Apple Mail AI summaries), hygiene thresholds (unsub >0.5%, bounce >1%, complaints >0.3%), engagement segmentation > frequency. Full section: pb-email references/email-data-driven-patterns.md.

**Open ops decisions for Timo (NOT implemented):** AC engagement segments (engaged-30d daily / moderates reduced / 90d+ win-back-then-suppress); send-time test vs the locked 4am LA slot.
