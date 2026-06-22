# Phase 5: Clone + rebrand the dashboard

Goal: a new project dir containing ONLY the selected pages, pointed at the client's Supabase,
branded for the client, with admin-only pages gated correctly.

## 5a. Copy the source structure
Create the client project dir (e.g. `/Users/air/Desktop/<Client Name>/`). Copy from PB:
- `dashboard/lib/`, `dashboard/assets/`, `dashboard/setup/`, `dashboard/styles.css`,
  `dashboard/favicon.ico`, `dashboard/robots.txt`
- **Asset folders that ROW DATA points at**, not just `assets/`. Hook rows store
  `thumbnail_url` like `/thumbnails/002.jpg`, served from `dashboard/thumbnails/` (PB has ~293
  images). If you copied the `hooks` rows (3d-shared) you MUST copy `dashboard/thumbnails/` too,
  or every card shows "No thumbnail" and 404s. General rule: after copying any shared library,
  grep its rows for local paths (`grep -oE "/[a-z]+/[^\"']+\.(jpg|png|webp)"`) and copy each
  referenced directory.
- `dashboard/login.html` + `dashboard/index.html` (always)
- each SELECTED `*.html` page
- root `vercel.json` and `.env.local.template`
- `api/` only if a selected page or vercel.json cron needs it (check `from('/api/')`,
  `fetch('/api`, vercel.json `crons`/`functions`). Drop ad-only api files if no ad pages chosen.
Do NOT copy PB's voc/, references/, content corpora, `.vercel/` link, or `CLAUDE.md`.

## 5b. Point lib/config.js at the NEW Supabase (the data-bleed guard)
The cloned `config.js` still points at PB. Rewrite:
- `SUPABASE_URL` = `https://<new_ref>.supabase.co`
- `SUPABASE_ANON_KEY` = the new `sb_publishable_...` key
- `ADMIN_EMAILS` = the admin emails for this client
- `LOCKED_ROLE.allow_pages` = the CLIENT-FACING selected pages only, plus `index.html`,
  `login.html`. EXCLUDE admin-only pages (e.g. `hooks.html`) so restricted users are redirected
  away from them by `enforcePageAllowlist`.

## 5c. Rebrand
Replace Precision Brass / Harrison identity with the client's, everywhere it appears:
- sidebar brand name + tag + logo (`assets/<name>.jpg`; drop in the client's or use initials)
- `<title>` on every page and `login.html`
- the login card brand block (mark initials + name + "Intelligence dashboard")
- page intro copy that names Harrison/PB or the niche
Grep to be sure nothing leaks: `grep -rniE "harrison|precision brass|pb " <client dashboard/>`.

## 5d. Admin-only nav gating (the bounce-bug fix)
For any admin-only page (Hook Library etc.), the nav section header + link must ship hidden and
be revealed only for admins. In each page's static nav:
```html
<div class="nav-section" id="adminSection" style="display:none">Timo Tools</div>
<a href="hooks.html" class="nav-item" id="hooksNav" style="display:none">Hook Library</a>
```
Confirm `lib/auth.js` reveals them for admins (its `applyNavFilter` sets
`#adminSection`/`#hooksNav` display to '' when role is admin, deferring until DOMContentLoaded).
PB's current auth.js already has this; if the cloned copy is an older version that leaves nav
always-visible, port the admin-reveal in. Without this, a restricted user sees a link that
bounces them, which reads as broken.

## 5e. Cache-bust
Bump every `lib/config.js?v=` and `lib/auth.js?v=` query string on the pages so the new config and
auth load instead of a cached copy (Vercel + Safer caching otherwise serve stale logic). Pick a
fresh integer higher than what PB used.
