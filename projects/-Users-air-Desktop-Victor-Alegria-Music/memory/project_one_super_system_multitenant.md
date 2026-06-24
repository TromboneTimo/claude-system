---
name: project-one-super-system-multitenant
description: "Timo wants ONE multi-tenant app for all coaching clients, NOT separate per-client deployments. Overrides the clone-dashboard skill's isolated-deploy approach."
metadata: 
  node_type: memory
  type: project
  originSessionId: bd198810-c952-4679-a271-32a9874fb430
---

Timo's coaching dashboards must be ONE super system, not one Vercel/Supabase project per client.

The `victor-alegria-music` app (Supabase ref `agbldmgbxzrrxznwbxar`) IS that system. Multi-tenancy lives in the `content_hub` schema ([dashboard/setup/migrations/2026-06-04_content_hub.sql](dashboard/setup/migrations/2026-06-04_content_hub.sql)):
- `content_clients`: one row per client; `id` = that client's Supabase auth uid.
- `content_items`: board rows, `client_id` FK, RLS "client read own" / "admin all".
- `is_content_admin()` predicate + `content_admins` email allowlist.
- Admin client switcher in `dashboard/suggestions.html`: Timo picks a client, sees exactly that client's board. This is how he "fleshes out each client as he sees fit."

As of 2026-06-05 all three tenants exist: Victor Alegria, Sohee Kwon, Tzu Chin.

**Why:** On 2026-06-05 Timo said "I ideally just have one super system that hosts all my clients in one place." A prior session had built separate `sohee-kwon` and `tzu-chin` Vercel projects (Desktop folders) pointing at the SAME Supabase, i.e. redundant duplicate frontends, the wrong direction.

**How to apply:** To onboard a new coaching client, do NOT run [[project-clone-status]]'s clone-dashboard isolated-deploy path. Instead: create their Supabase auth user, insert a `content_clients` row with `id` = their uid, and they appear in the switcher. The `clone-dashboard` skill (isolated per-client Supabase+Vercel) is WRONG for Timo's coaching clients. Push skills (va-ideas-push, va-script-write) must tag inserted rows with the target client's `client_id`/owner uid or the client won't see them.
