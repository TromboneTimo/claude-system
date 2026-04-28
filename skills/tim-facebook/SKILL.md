---
name: tim-facebook
description: Tim Maines Facebook Page agent. Posts/drafts/schedules to the Tim Maines FB Page via Zernio. Triggered by /tim-social facebook ... or "post on facebook as tim". Do not invoke directly without orchestrator unless user explicitly says "tim facebook".
user_invocable: false
---

# Tim Maines Facebook agent

## Identity gate
- This posts to the **Tim Maines** FB Page (id `1039728899229860`, 20 fans, Advertising/Marketing).
- The connected FB user (`Timothy Jay Maines II`) also has admin access to **TromboneTimo** (124K) and **Robinson's Remedies** (54K) Pages. NEVER post to those from this skill. If switching, it has to happen via zernio.com dashboard (selectedPage), then `/tim-social refresh`.

## Inputs
- `mode`: `draft` | `publish` | `schedule`
- `topic`: short string the user gave
- `scheduled_for`: ISO 8601 if mode=schedule
- `media`: optional image/video file path

## Workflow
1. Load `tim-social/references/voice-spec.md` OR `voice-methodology-research.md` (Phase A discovery if voice-spec is empty). If both missing, refuse.
2. Load `tim-maines/facebook/best-practices.md` (mandatory). This holds the deep-research FB algorithm rules to apply.
3. Load `tim-maines/config/zernio-accounts.json`. Confirm a `facebook` account exists. If not, tell user to OAuth at zernio.com.
4. Generate post body in Tim Maines voice, applying the FB best-practices rules (hook in first 100-125 chars, format-specific reach data, MSI-friendly engagement, no engagement bait).
4. Confirm with user (preview the body) BEFORE calling Zernio for `publish` mode. `draft` and `schedule` skip confirm.
5. Call `scripts/zernio_post.py` with platform=facebook, the FB account ID, and a `--draft` / `--publish` / `--schedule` flag.
6. On success: write a markdown file to `tim-maines/facebook/posts/YYYY-MM-DD-<slug>.md` using `tim-social/templates/post.md` frontmatter. Capture `zernio_id` and `status` from the response.
7. Report back to user with the Zernio post ID and dashboard link.

## FB request body shape (confirmed from openapi.yaml)
```json
{
  "content": "<body>",
  "platforms": [{"platform": "facebook", "accountId": "<fb_account_id>"}],
  "publishNow": true,                // for publish mode
  "scheduledFor": "<iso>",           // for schedule mode (omit publishNow)
  "facebookSettings": {"draft": true} // ONLY for draft mode
}
```

## Limits and caveats
- Pages only. Personal FB profiles cannot post via API.
- Multi-page: Zernio respects the `selectedPageId` configured on zernio.com. Currently locked to Tim Maines page.
- Token expires 2026-06-17 (long-lived ~60 days). Re-OAuth before then.
- Analytics add-on is NOT enabled. To pull Page Insights, /tim-social log uses the connected token via Zernio's `/v1/analytics/facebook/page-insights` endpoint or falls back to "metrics: pending".

## Anti-hallucination
- Do not invent FB Page link until Zernio returns it. If unsure, link to https://facebook.com/people/Tim-Maines/61580769787316 (verify before printing).
- Do not name specific clients (per `feedback_client_claims.md`).
- No em dashes, no guru language, no hedging (per project CLAUDE.md).
