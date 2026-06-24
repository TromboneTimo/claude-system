---
name: reference-content-suggestions-upload
description: How to upload IG/TikTok content suggestion tiles to a client coaching dashboard (Content Suggestions page)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 177f13fd-0180-4b83-9a8c-b681ee01cb63
---

Repeatable workflow when Timo says "upload these to the content suggestions of <client>" with a list of IG/TikTok URLs.

**Backend:** ONE shared music-coaching Supabase, ref `agbldmgbxzrrxznwbxar` (https://agbldmgbxzrrxznwbxar.supabase.co). Victor Alegria, Sohee Kwon, Tzu Chin are RLS-isolated tenants in it. Service-role key in `~/.claude/credentials/MASTER.md` (Victor Alegria Music section). Each client has its own Vercel project + dashboard repo on Desktop (`/Users/air/Desktop/<client>/dashboard/`), deployed via `vercel deploy --prod --yes` (NOT git, these dirs are not git repos).

**Tables:** `content_clients` (id = client's Supabase auth uid; query it to get the client_id) and `content_items`. Content tiles = `type='suggestion'`, `status='todo'`, `format` in short|carousel|long, `platform` instagram|tiktok|youtube, `source_handle='@handle'`, `thumbnail_url='/thumbnails/<file>.jpg'` (same-origin static file), `url`=the post link. id = `ci_YYYYMMDD_<7char>`. Insert via REST service-role (bypasses the content_items guard trigger). Client IDs so far: Victor `e352dcca-e583-45c4-b2d6-cb4370ffaa44`, Sohee `1b223bf3-187f-46fd-aa1e-982cb3aae2c8`, Tzu Chin `35176aa3-fb39-426d-a639-e2c0c8f63acb`.

**Thumbnails (the hard part):** CSP `img-src 'self'` blocks remote IG/TikTok CDN, so MUST download locally to `dashboard/thumbnails/<file>.jpg`.
- IG: `curl -sL -A "facebookexternalhit/1.1" <posturl>` then grep `og:image`, unescape `&amp;`, curl that to `<shortcode>.jpg`. Caption + @handle from `<posturl>embed/captioned/` (`.UsernameText`, `.Caption`).
- IG format (carousel vs single video): `yt-dlp --flat-playlist --dump-single-json` gives `_type=playlist`=carousel, else single video=short. /reel/ + /reels/ are always short.
- TikTok: `https://www.tiktok.com/oembed?url=<url>` gives thumbnail_url + author_name + author_unique_id + title. Download thumb to `tt_<videoid>.jpg`.

**SHARED-BACKEND ADMIN-VIEW BUG (2026-06-07, must-know):** Because all tenants share ONE `content_clients` table, the admin board in `suggestions.html` originally did `selectClient(CLIENTS[0])` = alphabetically-first client (Sohee). So Timo (admin) opening ANY dashboard saw Sohee's board, and Sohee's `/thumbnails/*.jpg` 404 on other domains = blank tiles. FIX: each `config.js` must carry `CLIENT_ID` (that tenant's uid); admin branch does `CLIENTS.find(c=>c.id===PB_CONFIG.CLIENT_ID)`. Bump `config.js?v=` when editing config or browsers keep the cached one. The CLIENT (non-admin) view was always correct (RLS `client_id=auth.uid()`); only the admin view was wrong. Verify the ADMIN view, not just the client login: spin a PREVIEW deploy with a throwaway admin email in ADMIN_EMAILS + a temp `content_admins` row + a temp auth user, log in, screenshot, then delete all three (prod stays clean since preview carried the temp email, not prod). STILL BROKEN: Victor's dashboard (no CLIENT_ID yet, admin there still sees Sohee) and Script Approvals/`ideas`+`scripts` tables have NO client_id column so they are shared across all tenants (latent cross-tenant leak). Also tiles use eager-loading now (was `loading="lazy"`, which read as "thumbnails not loading" on first paint).

**Rules:** Title = real caption/on-screen text, NEVER invented (or use Timo's given label when he provides one). NO filler notes/tags (Timo deletes them; leave note='' tags={}). VISUAL GATE: build a labeled montage (Pillow) and READ it to confirm every thumbnail is a real on-topic frame before declaring done. After deploy, curl `<client>.vercel.app/thumbnails/<file>.jpg` and expect 200 image/jpeg. Cannot do authed in-browser render (no client passwords; Timo's admin pw is in his head only), so flag that as the one unverified step. See [[reference-conservatory-landing-page]] for the separate Conservatory/funnel properties (don't confuse). Done 2026-06-07: Sohee 13 IG tiles, Tzu Chin 6 IG + 3 TikTok.
