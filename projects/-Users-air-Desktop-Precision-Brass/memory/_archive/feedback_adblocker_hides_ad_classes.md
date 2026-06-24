---
name: feedback-adblocker-hides-ad-classes
description: Dashboard content blank in normal browser but fine in incognito = an ad blocker cosmetically hiding elements whose CSS class starts with ad-/ads/banner/sponsor/promo. Never name UI with those.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6a16b3f6-b8fd-429a-acff-d79a73c1345e
---

**Symptom:** a dashboard section renders for me (Chromium/Playwright) and in the user's INCOGNITO window, but is BLANK in their normal browser profile (tabs/header show, the content grid is empty, no console error).

**Cause:** an ad blocker extension (uBlock, AdBlock, etc.). Incognito disables extensions by default, which is the tell. Ad blockers apply EasyList-style COSMETIC filters that inject `display:none !important` on any element whose class matches `ad-`, `ads`, `banner`, `sponsor`, `promo`, `doubleclick`, or attribute `[data-ad]`. The Precision Brass meta-ads cards were class `ad-card` / `ad-card-grid` / `ad-thumb` / `table.ads` / `ad-cell` -> all silently hidden. (2026-05-28)

**Proven, not guessed:** reproduce by injecting `[class^="ad-"]{display:none !important}` on the live page -> the cards vanish while tabs stay = the exact symptom. After renaming, inject an aggressive `ad-/ads/banner/sponsor/promo/[data-ad]` filter and confirm cards STAY visible.

**Fix:** rename every ad-keyword CSS class/attr to a NEUTRAL name with no `ad`/`ads` substring. meta-ads now uses `creative-card`, `creative-grid`, `creative-thumb`, `creative-cell/flex/text`, `table.creatives`, `data-cid`. Inner `ac-*` classes were already safe (no `ad` substring). Data fields (`meta_ads`, `ad_id`, `ad_set_id`) are NOT classes, leave them.

**How to apply / prevent:**
1. Never name viewer-facing UI with `ad`, `ads`, `advert`, `banner`, `sponsor`, `promo`, `doubleclick` in a class/id. For an ads dashboard use `creative-*`, `campaign-*`, `unit-*`, or a `pb-` prefix.
2. "Works in incognito, blank in normal browser" -> suspect ad blocker FIRST. Ties to global failure pattern #3 (verify in the real browser + its extensions, not Chromium/curl).
3. Related: [[feedback_html_no_store_for_safari_cache]] (other "stale/blank after deploy" cause), [[feedback_concurrent_repo_use_worktree]].
