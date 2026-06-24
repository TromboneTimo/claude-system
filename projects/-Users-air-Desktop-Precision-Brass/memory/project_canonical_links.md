---
name: project-canonical-links
description: Canonical destination URLs for Precision Brass emails and ads. Where every link in a draft should point.
metadata: 
  node_type: memory
  type: project
  originSessionId: d0c10100-009e-4416-b9c9-ee766cc9fe29
---

Canonical destination URLs for Precision Brass emails, ads, and dashboard CTAs. When in doubt, link here. Updated 2026-06-11 (webinar_ext rotated uc8hAYqe -> LRJGW50E, Timo-supplied verbatim after 5 broadcasts shipped to the registration page; the staleness warning at the bottom of this file predicted exactly this token rotation).

## Masterclass / training room

**Use this exact URL:**

```
https://www.precisionbrass.info/training-room1729899474908?webinar_ext=LRJGW50E&cf_uvid=7747dd81f6bb4119789f22c97cdc579e
```

The `webinar_ext` and `cf_uvid` params are required (they identify the training session in Harrison's webinar host). Strip them and the page breaks. Use this URL exactly. **Do NOT append `&el=` HYROS tags.**

**Why no `&el=` tags:** Per Timo 2026-05-17. Email subscribers are already in HYROS with first-touch attribution set on their original entry source (usually Facebook ads, which drove $204K / 73 sales in the last 6 months). Appending a per-email `&el=` tag risks contaminating that first-touch attribution if HYROS treats the tag as a higher-priority source. The marginal granularity (telling "dental email made $1.2K" from "regret email made $0.8K" inside the $5.7K email bucket) is not worth the risk to the FB attribution that's actually driving revenue. ActiveCampaign already tracks per-campaign clicks, so per-email click data is preserved at the AC layer without touching HYROS.

**Untagged email STILL gets full channel credit (PROVEN 2026-05-24 against live HYROS data):** untagged is not "untracked." Pulled 90d of HYROS sales directly: 14 email last-touch sales, $41.4K net, EVERY one with `trafficSource.name=activecampaign`, ZERO carrying a manual `el=` tag. `api/hyros.js` maps that to platform=email via the `EMAIL_TRAFFIC_SOURCES` set (`api/hyros.js:93`).

The mechanism (corrected understanding): `el=` is HYROS's EMAIL tracking parameter, and the HYROS<->ActiveCampaign integration AUTO-injects a per-campaign `el=` for every send. That is why the sales show source names like `@last-chance`, `@quick-question`, `@october-live-webinar-replay` already. The campaigns are effectively already tagged, automatically. So adding a manual `el=` buys NOTHING. It is redundant, not magic.

First-touch is NOT at risk (this corrects the earlier "tagging contaminates first-touch" rationale, which the data does NOT support): HYROS stores firstSource and lastSource as SEPARATE objects. In 13 of the 14 email-last-touch sales the first-touch was a Facebook ad / the YouTube embouchure video / the channel page, fully preserved, while email sat in last-touch. An email click sets last-touch only; it does not overwrite acquisition source.

NET RULE (unchanged, better-grounded): do NOT hand-tag email links. Reason = redundant (AC auto-tags per campaign), not danger. Per Harrisson: a lead who received the email already had a first touch and is tracked everywhere. The only real failure mode is the HYROS<->AC integration silently disconnecting (would drop email clicks to "direct"); hand-tagging would not protect against that either. Recency proof: 1 email last-touch sale ($6.8K) in the trailing 7d as of 2026-05-24, so the integration is live. See [[feedback-email-html-links-and-cta]].

**Why the URL changed (for EMAIL):** for email CTAs, use the `training-room` URL above. CORRECTION 2026-05-24: the claim that `precisionbrass.info/webinar-registration-pb` is a "dead link" was WRONG. Verified live with a browser user-agent: it returns 200, serves the "Precision Brass Webinar" page, redirects once to `webinar-registration-635785...` while PRESERVING the `?el=` tag, and fires the HYROS + FB + GTM pixels. It is the active YouTube-description + IG-bio destination and is converting (e.g. `el=timostopbuyingmp` drove a $6,300 sale). A `curl` without a browser UA returns 403 (bot block), which is NOT a dead page. The `training-room` URL is the preferred EMAIL CTA; `webinar-registration-pb` is the working tagged-traffic destination for YouTube/IG. Do not call it dead again.

**How to apply:** every email body anchor + cta_url that promotes the free masterclass uses the SAME base URL above. No per-email tagging. Same link for everyone.

## YouTube destinations

The embouchure converter video is the proven $36K converter and its description carries the masterclass tracking link. Any time an email needs a YouTube fallback (broken link, no specific video for the angle) point to:

```
https://www.youtube.com/watch?v=O4a-q93ENAg
```

No `&el=` tag needed on YouTube URLs. Per Timo 2026-05-17: tracking happens via the YouTube description link, not via the URL the email sent the user to. So bare YouTube URLs in email bodies are fine.

## Anti-patterns (links that are WRONG)

- `https://precisionbrass.com/training` (landing page, not masterclass)
- `https://www.precisionbrass.info/webinar-registration-pb` (BANNED IN BROADCASTS, lint-blocked 2026-06-11. It is the email CAPTURE page; the list is already captured. Still the live tagged destination for YouTube/IG bios only. 5 broadcasts shipped here 2026-05/06 before Timo caught it.)
- `https://youtu.be/PLACEHOLDER?...` (literally never replaced from a template; broken)
- Any URL with `&el=...` appended (risks HYROS first-touch contamination per the 2026-05-17 decision; AC already tracks per-campaign clicks)

RESOLVED 2026-06-11: `dashboard/lib/email-lint.js` now carries `CANONICAL_MASTERCLASS_URL` (this exact URL) as the executable registry. Lint BLOCKS webinar-registration-pb in any broadcast body (rule wrong-destination-registration-page) and BLOCKS any non-canonical training-room variant (rule masterclass-url-not-canonical); both autoFix to canonical. This memory file and that constant must change TOGETHER.

## When this file gets stale

Anytime Harrison changes the webinar host, the webinar slug, or the cf_uvid param. The next session that drafts an email should re-confirm with Timo before using a memorized URL more than 30 days old. The webinar host's tokens have rotated before.
