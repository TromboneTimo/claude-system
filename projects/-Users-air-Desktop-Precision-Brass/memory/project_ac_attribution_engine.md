---
name: project_ac_attribution_engine
description: "AC entry-funnel attribution engine that recovers the source of HYROS-unattributed (\"OTHER\") sales from ActiveCampaign. Built 2026-05-25, NOT yet deployed."
metadata: 
  node_type: memory
  type: project
  originSessionId: d486e03a-95bd-4154-9c56-98535a70d59e
---

**STATUS 2026-05-25: LIVE + VERIFIED.** Layer 3 wired into api/hyros.js (enriches recent_sales whose platform is other/automatic via attributeUnsourcedSale, cached, bounded to 25 rows) + channel-attribution.html renders a green "Revived Lead"/"Email Lead" pill (recoveredPill) with funnel tooltip. Deployed to prod, verified live: the 6 OTHER sales now render Revived/Email (steve/cody=Email, bandcdr/x-stray/cybergrunt=Revived). VOC restructure landed+pushed+deployed. ALSO shipped same day: pagination HARD_CAP 5000->20000 (365d now returns 6,301 clicks not capped; was undercounting ~21% on 12M/All) + ts='an' Audience Network -> meta-ads. ACTIVECAMPAIGN_API_KEY confirmed present in Vercel env (enrichment works in lambda). REMAINING (human-only): Harrisson's funnel->channel map (channel shows funnel name only until then; fill FUNNEL_CHANNEL in ac-attribution.js); `vercel git connect` BLOCKED on Timo adding a GitHub login connection in Vercel account settings; Layer 2 UTM-at-opt-in setup (dashboard/setup/utm-capture-setup.md).

**DECISION 2026-05-25 (Timo): do NOT hard-code the funnel->channel map.** Timo's answer: webinars come from a MIX of Meta ads + YouTube (live webinar = Meta ads), no clean per-funnel single channel. Stamping one channel per historical sale would be a guess = the exact misattribution we just fixed. So `FUNNEL_CHANNEL` stays null; the final labels are `Revived Lead` / `Email Lead` (owned-audience), which are accurate and decision-useful. Exact per-sale channel is only obtainable going forward via the Layer 2 UTM capture (optional, not set up). Treat this question as CLOSED; do not re-ask Harrisson or guess channels. Also DONE 2026-05-25: Vercel git auto-deploy connected (pushes to main now auto-publish; the recurrence root cause is structurally closed).

Built 2026-05-25 to answer "where do the OTHER sales come from." Proven first: every HYROS-unsourced sale is a known AC contact (0 truly unknown); HYROS never captured their original click (opt-ins 8-10 months old, untagged/cross-device/pre-tracking). The HYROS pixel IS on the reg page (`hyros.com/v1/lst/universal-script`), so no HYROS link is needed on signup. AC is the source of truth. See [[project_youtube_attribution_classifier_fix]].

**Files built (NEW, no collision with the in-flight VOC restructure; NOT committed/deployed yet):**
- `dashboard/lib/ac-attribution.js`: engine. `classifyAcContact()` (pure, unit-tested) plus `fetchAcContext()` plus `attributeUnsourcedSale()`. Reads a contact's earliest ENTRY-funnel automation, returns {label, funnel, channel, days_old}. Label = `Revived Lead` (>30d before sale) / `Email Lead` (<=30d) / `Unknown` (not in AC).
- `scripts/recover-lost-leads.mjs`: Layer 1 runner. `HYROS_API_KEY=.. AC_KEY=.. node scripts/recover-lost-leads.mjs [days]`. Validated: 8/8 lost leads (90d) recovered to AC contacts; labels correct (4 Revived/4 Email).
- `dashboard/setup/utm-capture-setup.md`: Layer 2. Capture utm_source at opt-in into AC first-touch custom fields (NO HYROS, no signup breakage). Makes channel exact for FUTURE leads.

**The 5 ENTRY funnels (AC automation id) needing a channel from Harrisson (FUNNEL_CHANNEL map is currently all null = "pending-funnel-map"):** 6 Echoes of Excellence, 8 Precision Brass Webinar, 15 Mind Over Mastery, 16 Live Webinar Automation, 23 Dynamic Repetition. (Downstream/non-entry, excluded: 9/11 booked-call, 14/22 daily email, 17-20 workshop purchase.) AC base = https://hballmusic.api-us1.com ; ACTIVECAMPAIGN_API_KEY in MASTER + Vercel env.

**Layer 3 (live dashboard) = WIRE AFTER RESTRUCTURE:** import `attributeUnsourcedSale` into api/hyros.js inferPlatform 'other' path (cached) plus add badge color in channel-attribution.html. Both files are mid-restructure; do not edit until it lands.

**Ship sequence (all blocked on the VOC restructure commit + main divergence):** (1) Harrisson fills funnel->channel; (2) commit restructure + reconcile local b52aac0 vs origin be7eb49 divergence; (3) wire Layer 3 + Revived/Email relabel + pagination-cap fix + an->meta-ads, commit by explicit pathspec; (4) `vercel git connect`; (5) deploy, bust cache, verify live via Playwright; (6) Harrisson/Timo do the Layer 2 UTM form setup; (7) confirm the daily-scrape GitHub Action script points to new voc/ paths or it fights the restructure nightly.

**Edge case:** some AC contacts entered via a LIST not an automation (e.g. trumpetwdw), so "no entry funnel found"; still gets Revived/Email label. Could add list-based entry fallback later.
