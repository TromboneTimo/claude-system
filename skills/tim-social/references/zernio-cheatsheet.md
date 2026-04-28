# Zernio API Cheatsheet (for tim-social skill family)

## Env loading (CRITICAL)
Bash subshells do NOT persist `source ~/.zshrc`. Read the key inline every call:
```bash
KEY=$(grep -oE 'sk_[a-f0-9]{64}' ~/.zshrc | head -1)
curl -4 -sS -A "Mozilla/5.0" -H "Authorization: Bearer $KEY" "https://zernio.com/api/v1/profiles"
```
Always pass `-4` (force IPv4) and a browser User-Agent. Without these, you get TLS connection resets.

## Base
- URL: `https://zernio.com/api/v1`
- Auth: `Authorization: Bearer sk_...`
- Rate limit: 60/min Starter, 600/min Pro
- Health probe: `GET https://zernio.com/api/health` (no auth)

## Tim Maines IDs (as of 2026-04-28, all 5 platforms + bonus X connected)
- Tim Maines profile: `69f00d0379b453e8d8d2fa19`
- Robinsons Remedies profile: `69f01cff6f0f75d7457d9367`

| Platform | Account ID | Username | Notes |
|---|---|---|---|
| Facebook | `69f015ba985e734bf3c6cf02` | Tim Maines | FB Page (Tim Maines selected, also has admin on TromboneTimo + Robinson's Remedies). Token expires 2026-06-17. |
| LinkedIn | `69f01f19985e734bf3c7128a` | Tim Maines | Personal profile. |
| YouTube | `69f01f2f985e734bf3c712ff` | timmaines | Channel. |
| Instagram | `69f02da5985e734bf3c77032` | timo.maines | Business or Creator account (verify via Zernio dashboard). |
| TikTok | `69f034b8985e734bf3c79582` | timo.maines | Personal account. |
| Twitter/X | `69f02d7f985e734bf3c76f9e` | TromboneTim0 | Bonus, not in original spec. No skill yet. |

## Refresh after OAuth
After connecting/disconnecting any account on zernio.com:
```bash
python3 ~/.claude/skills/tim-social/scripts/zernio_refresh.py
```
Writes `tim-maines/config/zernio-{profiles,accounts}.json`.

## Posting (per `/v1/posts`)
- Immediate: include `publishNow: true`
- Scheduled: include `scheduledFor: "2026-05-01T15:00:00Z"`
- Draft: omit BOTH (Zernio internal draft, NOT platform-native)
- Per-platform fields under `platforms.{linkedin|facebook|instagram|tiktok|youtube|...}`
- Always include `accountId` per platform
- Refer to `zernio-openapi.yaml` for the full schema (search for `Post` request body)

## Critical caveats
- Facebook: Pages only. Personal profiles cannot post via API. Selected Page chosen via Zernio dashboard.
- Instagram: Business or Creator accounts only. Reels (9:16) need video shorter than 90 seconds.
- TikTok: Requires consent flags + privacy settings on every post.
- YouTube: Schedule = upload as private, public at scheduled time.
- Analytics add-on: NOT enabled on this account. Until enabled, /tim-social analyze pulls metrics directly from Facebook Page Insights via the connected token (we'll wire that in Phase 6).
