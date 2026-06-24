---
name: hook-library-client-access
description: Hook Library is client-visible READ-ONLY on all 4 client dashboards as of 2026-06-10; edit/delete/send stay admin-only (UI + RLS)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8e5cf3e7-8360-47bb-b1d5-3a9af7c74e1f
---

As of 2026-06-10 (per Timo: "make sure all clients have access to the Hook Library; Harrison didn't"), the Hook Library (hooks.html) is visible to restricted client logins on ALL FOUR client dashboards:

| Client | Vercel project | Supabase |
|---|---|---|
| Harrison Ball | precision-brass-dashboard | iwlernqpwdsjarygoeog (own project) |
| Victor Alegria | victor-alegria-music | agbldmgbxzrrxznwbxar (shared) |
| Tzu Chin | tzu-chin | agbldmgbxzrrxznwbxar (shared) |
| Sohee Kwon | sohee-kwon | agbldmgbxzrrxznwbxar (shared) |

What changed (4 layers, all must agree):
1. **RLS**: added `"hooks authenticated read"` SELECT policy on `public.hooks` in BOTH Supabase projects. `"hooks admin all"` (is_content_admin()) still gates writes. Verified live: restricted users read 325 rows; UPDATE/DELETE affect 0 rows.
2. **Page guard**: hooks.html `boot()` no longer blocks non-admins; new `isAdmin()` helper.
3. **UI**: Edit / Delete / Send-to-Suggestions buttons render only for admin. Clients get view + localStorage favorites + See Original.
4. **Nav + allowlist**: 'hooks.html' added to LOCKED_ROLE.allow_pages in all 4 config.js; sidebar section renamed "Timo Tools" → "Library" and revealed for all signed-in roles (PB: injectContentHubNav in auth.js; V/T/S: applyNavFilter + static display:none).

Gotcha for future page un-gating: access is gated in FOUR places (RLS, page boot guard, allow_pages, nav reveal). Changing only the UI gives a blank/bounced page. Check the DATABASE first.

New-client cloning: [[clone-dashboard]] skill clones from Precision-Brass, which now carries the client-visible pattern forward automatically.
