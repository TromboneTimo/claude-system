---
name: project-meta-ads-hyros-revenue-pipeline
description: "Meta ads + HYROS revenue pipeline: Supabase edge functions hyros-revenue + meta-ads-sync. HYROS sale schema, the ad-account access split, and the meta_ads column gotchas. Built 2026-05-25."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9627bbfc-ecec-4b40-9187-f019508c4cee
---

# Meta Ads + HYROS revenue pipeline (built 2026-05-25)

Two Supabase Edge Functions in `supabase/functions/` (project's FIRST edge functions; CLI installed via brew). Deploy: `supabase functions deploy <name>`; secrets via `supabase secrets set`.

## hyros-revenue (dashboard-facing, verify_jwt)
Returns per-ad NET CASH COLLECTED for paid Meta/FB ads from HYROS `/sales`.
**Revenue truth (Timo-confirmed):** per ad = Σ (`usdPrice.price` minus `usdPrice.refunded`). 2 sales = 2 summed records. A 1/3-upfront shows the real $2,500 collected, NOT the contract. Refunds subtracted.
Verified live: **$289,585 net across 22 paid ads (365d).** Top ad "July 15 2025 // USA // 30+" = $63,500.

### HYROS sale record schema (the important fields)
- `firstSource.adSource.adSourceId` = **the Meta ad_id** (120-format) = joins `meta_ads.ad_id` exactly.
- `firstSource.adSource.adAccountId` + `.platform` (FACEBOOK/INSTAGRAM) = paid-ad signal.
- `firstSource.name` = the ad NAME.
- `usdPrice.price` = ACTUAL cash collected on that Stripe transaction (installments are separate records). `usdPrice.refunded` = refunded amount. `product.name` = the plan sticker (e.g. "Stripe 9200"), NOT the collected amount.
- `provider.integration.name` = "Stripe Account #1", label it "Stripe". `orderId` = Stripe charge id (ch_/py_).
- Internal/test buyers excluded (harrissonball@precisionbrass.info, hballmusic@yahoo.com, trombonetimollc@gmail.com), mirrors api/hyros.js.

## meta-ads-sync (cron, x-perf-secret)
Pulls Meta Marketing API `level=ad` insights, upserts `meta_ads` + appends `meta_ads_daily`. Superset of the old CSV ingest (adds video metrics). Parameterized over `META_AD_ACCOUNTS`.

### HARD BLOCKER: ad-account access split (verified 2026-05-25)
- The Meta token (user token, **expires 2026-07-16**) reaches `act_2443232582800725` "Precision Brass 1" = the 598-suffix ads (new "Timo"/no-cost lead ads, ~no revenue yet).
- The **$289K revenue ads (430-suffix)** live in account **`8388204844642603`**, which the token has **NO ads_read on** (`(#200)` error). Timo's manual CSV export covers that account today.
- To auto-sync the revenue account: its Business Manager owner must grant ads_read to the token's app/system user. A **System User token** (non-expiring) also kills the July-16 expiry. Timo's call 2026-05-25: build now on the user token + remind before expiry.

### meta_ads schema gotchas (query-destination-schema-first paid off)
- NO `hook_rate` / `hold_p25` / `source` columns. Dashboard computes hook = `video_plays`/impressions, hold = `video_p25`/`video_plays` at render time. Store RAW counts: video_plays, video_3s_views, video_p25/p50/p75/p100, video_thruplays, video_avg_sec.
- Real holds are ~1-2% (p25/plays); any "20%" in old screenshots is stale cache.
- `meta_results` (Meta's "Results") is objective-dependent. The sync picks via `META_RESULT_ACTION_TYPES` (default fb_pixel_lead, lead_grouped, lead, landing_page_view). For the 598 ads it resolved to landing_page_view. **CONFIRM against Ads Manager per account (classifier gate); not yet confirmed.**
- Partial upsert (PostgREST merge-duplicates) only updates payload keys, so hyros_* columns + raw_row are preserved.

## Column bug (the original complaint) = NOT a real bug
meta_ads data is correctly typed and the render maps headers to values correctly (proven: row1 CPM $26.58 times 10,215 impr /1000 = $271 spend). Frequencies of 7-20 are real warm-audience over-serving. `/meta-ads` returns no-store. The misaligned screenshot is a stale Safari tab from before the 2026-05-17 table-layout:fixed fix. See [[feedback_html_no_store_for_safari_cache]].

## IF META ADS STOP READING / pixel or insights fail (CHECK THIS FIRST)
The Meta token **expires 2026-07-16**. Symptom when expired: `meta-ads-sync` returns `(#190)` or `(#102)` OAuth errors, ad spend/impressions/freq/cpm stop updating, and the dashboard's Meta columns go stale or empty. FIX: re-extend the token at https://developers.facebook.com/tools/debug/accesstoken, then save the new value to `~/.claude/credentials/MASTER.md` ("Precision Brass / Meta Graph API"), `project_credentials.md`, and the Supabase secret `META_USER_TOKEN` (`supabase secrets set META_USER_TOKEN=...`). A reminder routine is scheduled for ~2026-07-09. Permanent fix = a non-expiring System User token (needs the access grant on acct 8388204844642603 anyway).

## 2026-05-25 update: API is now the source (for the reachable account)
- meta-ads-sync RAN to prod: `meta_ads` for account act_2443232582800725 (598-suffix ads) is now API-sourced, NOT CSV. Auto-refreshes hourly via pg_cron job `meta-ads-sync-hourly` (`7 * * * *`, pg_net -> edge fn with x-perf-secret).
- **Correct "Results"/leads action type = `offsite_conversion.custom.1628048068427083`** (Harrison's custom pixel conversion). Ground-truthed against CSV (matched 1/4/4/2/9 exactly). `landing_page_view` was 10-1000x WRONG. Set as DEFAULT_RESULT_ACTIONS[0] + can override via META_RESULT_ACTION_TYPES secret.
- **CSV DELETED 2026-05-25 per Timo's explicit override** (api/meta-ads-ingest.js removed, upload UI gone, Vercel daily-pull cron emptied, endpoint now 404). Meta data is now API-only.
- CONSEQUENCE Timo accepted: account 8388204844642603 (the 430-suffix ads holding most of the $289K) is unreadable by the token (verified 3 ways: account insights #200, direct ad-id "does not exist", direct insights error). With CSV gone, those ads have NO metrics updater. Their existing meta_ads rows are frozen (stale spend); HYROS revenue still shows live. They only become live again after an ads_read grant on that account (likely owned by a different Business Manager that hasn't shared it with Timo's user/token).

## Status / next
- Both functions written + typechecked + dry-run verified. NOT deployed.
- Next: deploy + set secrets (HYROS_API_KEY, META_USER_TOKEN, EMAIL_PERF_SECRET, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY), then Step 4 = wire dashboard to render the per-sale Stripe breakdown + net-collected revenue.
