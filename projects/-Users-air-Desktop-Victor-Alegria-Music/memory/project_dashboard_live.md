---
name: project-dashboard-live
description: "Victor's dashboard is deployed to Vercel with its own Supabase project + working PB-style login."
metadata: 
  node_type: memory
  type: project
  originSessionId: e670584f-0b7e-4881-9e25-25b39353b8ae
---

Victor Alegria Music dashboard is LIVE in production (deployed 2026-06-04).

- **URL:** https://victor-alegria-music.vercel.app (login at /login)
- **Vercel project:** victor-alegria-music (org trombonetimo-9261s-projects). Deploys from project root; outputDirectory=dashboard. Public (no Vercel SSO wall).
- **Supabase project:** Victor's OWN, ref `agbldmgbxzrrxznwbxar`, org Timo LLC, Sydney. NOT Precision Brass. URL + anon publishable key live in dashboard/lib/config.js; service_role is a Vercel env var. Schema (setup/schema.sql + migrations) applied, 17 tables, RLS authenticated-only.
- **Auth = PB-style Supabase signInWithPassword.** Accounts (creds in ~/.claude/credentials/MASTER.md):
  - victoralvarezalegria@gmail.com (restricted role) -> Victor Workflow pages only (scripts.html, suggestions.html). Bounced from hooks.html.
  - timothyjay.maines@gmail.com (admin, in ADMIN_EMAILS) -> full access incl. Timo Tools / Hook Library.
- **Nav (all 3 pages):** Victor Workflow = Script Approvals + Content Suggestions. Timo Tools = Hook Library. Timo Tools ships `display:none` in static HTML and auth.js `applyNavFilter` reveals it for admins only. Restricted users never see the link (prevented the bounce bug 2026-06-04). hooks.html also excluded from LOCKED_ROLE.allow_pages, so direct-URL is redirected too.
- **ADMIN_EMAILS** mirrors PB exactly: timothyjay.maines@gmail.com + trombonetimollc@gmail.com.
- **Content Hub backend** (mirrored from PB live 2026-06-04, migration setup/migrations/2026-06-04_content_hub.sql): tables content_admins, content_clients, content_items, hooks + `is_content_admin()` SECURITY DEFINER fn. RLS keyed to auth.uid(): each client's content_clients.id IS their auth uid. Seeded: content_admins = both Timo emails; content_clients = Victor's row id = his auth uid e352dcca-e583-45c4-b2d6-cb4370ffaa44.
- Verified end-to-end via Playwright on prod: Victor login -> only Victor Workflow nav, 0 errors, bounced from /hooks. Admin login -> Timo Tools revealed, Hook Library + Content Suggestions both load empty-state (no "could not load" error). 0 console errors either role.

**Why:** earlier config.js pointed at Precision Brass's Supabase (data-bleed risk); this corrected it to Victor's own backend before going live.
**How to apply:** API data features (ideas/scripts/email) still need Victor's ActiveCampaign keys + remaining env vars in Vercel (env template at .env.local.template was blank for AC). See [[project-clone-status]].
