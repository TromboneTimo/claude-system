---
name: meta-thumbnails-endpoint-and-csp
description: How Meta ad creative thumbnails are fetched + the CSP img-src + Hobby 12-function cap gotchas. Read before adding any new api/*.js or showing fbcdn images.
metadata: 
  node_type: memory
  type: project
  originSessionId: 46c2fc3a-b92f-4a7f-9793-e034cddea1db
---

2026-05-27: channel-attribution.html "Best Performing Ads" (Meta Ads tab, Top Content view) was redesigned into TWO boards. Top Performers (ads with a HYROS sale, sortable) and Warnings (active 0-sale ads ranked by spend, with DISCONTINUE/WATCH/PROVING verdict via $500 kill line + red/yellow alert triangles). Logic ported from meta-ads.html (adVerdict, rowAlerts). Each row shows the ad CREATIVE THUMBNAIL instead of just the name.

Three gotchas that cost real time:

1. **No thumbnail column in `meta_ads`** (CSV-sourced). Thumbnails come live from Meta Graph `/{ad_id}?fields=creative{thumbnail_url}`. The URL is a signed fbcdn link, never persisted.

2. **Hobby plan caps at 12 serverless functions.** `api/` already has 12. Adding `api/meta-thumbnails.js` failed the deploy ("No more than 12 Serverless Functions"). FIX: folded it into `api/ac.js` as `action=meta-thumbnails` (POST {ids:[...]} or ?ids=, batches Graph at concurrency 12, returns {ad_id:url}). Uses `process.env.META_USER_TOKEN`. NEVER add a new api/*.js file. Extend an existing one with a new action instead.

3. **CSP `img-src` blocked fbcdn.** vercel.json CSP only allowed ytimg.com, so creative thumbnails 200'd via curl but failed silently in-browser. Added `https://*.fbcdn.net https://*.xx.fbcdn.net` to img-src. Any new external image host needs adding to that CSP line.

Coverage reality: thumbnails (and real Cost) only resolve for ads in the **token-accessible** ad account (act_2443232582800725). The high-revenue $0-cost evergreen winners live in account 8388204844642603 which the token CANNOT read, so they fall back to the blue Meta chip and $0 cost. Same root limit as [[project-meta-ads-hyros-revenue-pipeline]]. Warnings board = all spend-ads in the accessible account, so 100% thumbnail coverage; Top board = sparse (only spend-ads).

Sort selection persists in localStorage `pb_content_sort`. YouTube/All tabs stay HYROS-only (Content/Clicks/Sales/Calls/Revenue, no cost cols, no warnings, organic).
