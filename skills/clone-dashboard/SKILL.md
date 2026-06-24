---
name: clone-dashboard
description: >
  Onboard a new client by cloning the Precision Brass dashboard into a brand-new,
  fully ISOLATED deployment (its own Supabase project + Vercel project + login).
  Use this WHENEVER Timo is enrolling/onboarding a client and wants them a dashboard,
  or says "clone the dashboard", "new client dashboard", "spin up a dashboard for
  <name>", "set up <client> on the dashboard", "give <client> their own dashboard /
  login", "copy the dashboard for <client>", "enroll <client>", or anything that means
  "stand up the dashboard system for a new person." Picks which Precision Brass pages
  the client gets, provisions everything, hash-copies Timo's admin password so his
  login stays identical, deploys a preview, and STOPS for approval before going to
  production. Do NOT use for editing an existing client's dashboard (that is dashboard-dev),
  for marketing/content, or for non-dashboard client setup.
---

# Clone Dashboard (client onboarding)

Stand up a complete, isolated dashboard for a new client by cloning Precision Brass.
Every client gets their OWN Supabase project, OWN Vercel project, OWN login. Nothing
is shared with PB or any other client.

## Two laws (these are why the manual version was painful; do not repeat)

1. **Check capability before asking.** Every credential you need already exists. The
   Supabase personal access token (`SUPABASE_PERSONAL_ACCESS_TOKEN=sbp_...`) and PB's
   service-role key are in `~/.claude/credentials/MASTER.md`. Admin passwords are set by
   **copying the bcrypt hash** from PB's `auth.users` into the new project (plaintext is
   never needed or seen). NEVER ask Timo for a token or a password that is derivable.
   "I can't" is the conclusion of an investigation, not a reflex.

2. **Audit the full target state up front.** The tracked `schema.sql` is INCOMPLETE.
   Pages query tables/functions that live only in PB's running database (we got burned
   by `content_admins` / `content_clients` / `content_items` / `hooks` + `is_content_admin()`).
   Before any deploy, enumerate every table/function each selected page touches and pull
   whatever is missing from PB's LIVE db. Then verify per ROLE in a real browser. A login
   that lands fine but has a nav link that bounces is NOT verified.

## Constants
- PB source dir: `/Users/air/Desktop/Precision-Brass` (root has `api/`, `vercel.json`; `dashboard/` has the pages).
- PB Supabase ref: `iwlernqpwdsjarygoeog`. Supabase org: `teulawuyhnxrwnuaffqo` (Timo LLC). Region: `ap-southeast-2`.
- Default admin emails: `timothyjay.maines@gmail.com`, `trombonetimollc@gmail.com`.
- Helper: `scripts/supa.py` (json-safe SQL, Admin API, hash-copy). Use it instead of hand-rolling curl, because it avoids the bash/SQL quoting traps that cost time in the manual run.

## Workflow

Use TodoWrite to track the phases. Run phases 1-6 automatically; **hard stop at phase 7**.

1. **Gather inputs** (quick prompts): client name, niche/segment, client login email,
   client login password, admin emails (default to the pair above). Then read PB's live
   `dashboard/` directory and present the page inventory as a multi-select, so only the
   chosen pages + their dependencies get cloned. See `references/inputs.md`.

2. **Provision Supabase**: create the client's own project, capture ref/URL/anon/service_role.
   See `references/provision-supabase.md`.

3. **Schema + full-state audit**: apply `schema.sql` + migrations, then for the SELECTED
   pages find every `from('x')` / `.rpc('y')` and backfill anything missing from PB's live db
   (DDL + RLS + function defs). Then COPY THE ROWS of shared reference libraries (e.g. `hooks`,
   the music-niche hook library) so the page is not empty on day one, but NOT per-client/PB-private
   data (content_items, ideas, scripts, email_*, meta_ads). Seed per-client rows where RLS is keyed
   to `auth.uid()`. See `references/schema-and-audit.md`.

3b. **RLS LOCKDOWN (MANDATORY, runs LAST after all DDL).** Apply `Precision-Brass/scripts/enable-rls.sql`
   to the new project, then run `node Precision-Brass/scripts/check-rls.mjs` and confirm the new ref
   shows "all RLS-on, no anon grants". This is non-negotiable: backfilled tables are created
   RLS-OFF by default and `anon` gets full grants, so skipping this ships the client world-open
   (Supabase advisor "rls_disabled_in_public"; happened on PB + VA 2026-06). Default-deny model:
   RLS on every table + anon revoked + authenticated opt-in per data table; api_cache/pb_webhook_config
   stay service-role-only; content_* keep their auth.uid() policies (never blanket them).

4. **Auth accounts**: create the client (restricted) with their password; create each admin
   email and hash-copy its password from PB so Timo's login is identical. Verify md5 match.
   See `references/auth-accounts.md`.

5. **Clone + rebrand**: copy only selected pages + `lib/` + `assets/` + `setup/` + needed `api/`;
   point `lib/config.js` at the NEW Supabase, set ADMIN_EMAILS + LOCKED_ROLE.allow_pages
   (client pages only; admin-only pages excluded); rebrand sidebar/titles/login; keep admin
   nav `display:none` + admin-reveal; bump `?v=` cache-busters. See `references/clone-and-rebrand.md`.

6. **Preview deploy**: set Vercel env vars, `vercel link --project <slug>`, deploy a PREVIEW
   (not `--prod`). See `references/deploy-and-verify.md`.

7. **STOP for approval.** Show: preview URL, Supabase ref, pages included, accounts created
   (client + admins, noting admin password = "same as Precision Brass"). Ask Timo to approve
   before the irreversible production deploy. Do not proceed without an explicit yes.

8. **Production + verify**: `vercel --prod`, then Playwright per-role checks: client sees only
   their pages, 0 console errors, bounced from admin URLs; admin sees admin tools and every
   selected page loads. Report PASS/FAIL with evidence. See `references/deploy-and-verify.md`.

9. **Record**: append the new client's Supabase + Vercel + login details to MASTER.md and
   write a project memory. See `references/record.md`.

## Style
Mirror Timo's pace: act, do not narrate every micro-step; surface findings and blockers, not
ideal-state hype. Lead with caveats. The only mandatory pause is phase 7.
