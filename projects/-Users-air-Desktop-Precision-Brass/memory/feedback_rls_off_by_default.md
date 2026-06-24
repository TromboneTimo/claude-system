---
name: feedback-rls-off-by-default
description: "Why the Supabase RLS leaks existed (4 PB + 5 VA public tables open) and the lessons. RLS is opt-in/off-by-default per table; app-layer auth masked the DB hole; clones inherit the gap. Verify as the logged-out attacker, not the happy path."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7eb5b045-0178-473d-b6ad-eee5348d22dd
---

On 2026-06-23 Supabase's scanner flagged `rls_disabled_in_public` on Precision Brass (4 tables: daily_run_log, email_perf_snapshots, email_perf_trends, meta_ads_trends) and Victor Alegria (those + email_ideas). ~19 of 23 PB tables already had RLS on; only the LATER-added ones were open.

**Why they existed (root cause):**
1. **RLS is off-by-default and opt-in PER TABLE in Postgres/Supabase.** The original `dashboard/setup/schema.sql` hardened the first batch with RLS+policies. Every table added afterward as features grew (email-analytics snapshots/trends, meta-ads trends, daily scrape logging, email_ideas) was created ad hoc and born OPEN, because nothing re-applied the RLS step.
2. **Defense was at the wrong layer.** Auth was enforced in the APP (login gate + JWT on every request), NOT at the DB. The app working perfectly MASKED the hole: the publicly-shipped anon key could hit PostgREST directly and bypass the login entirely.
3. **No gate caught it.** This project has a gate for everything (deploy, em-dash, classifier) but none for "every new table must have RLS." My own CLAUDE.md even says "Same bug 3x = check the DATABASE (RLS, policies)" yet nothing enforced it on creation.
4. **Clones inherit the gap.** VA is a clone of PB and had one MORE open table, confirming the leak propagates through clone-dashboard.

**Why:** app-first build, security-as-afterthought, incremental table creation outside an enforced hardened path. Postgres defaults to RLS-off, so every forgotten table = world-readable/writable.

**DEEPER root cause (found 2026-06-23 on the audit):** every public table grants the `anon` role FULL privileges (SELECT/INSERT/UPDATE/DELETE/TRUNCATE) by Supabase default. RLS was the ONLY thing gating anon. So a single forgotten RLS toggle = anon can read AND destroy a table. The durable fix is defense-in-depth: `revoke all on all tables in schema public from anon` + `alter default privileges ... revoke all on tables from anon`. Then anon (the public key, no login) has zero table access and a future un-RLS'd table is non-catastrophic. Model = DEFAULT-DENY: RLS on all + anon revoked + authenticated OPT-IN per data table (explicit policy). New table born locked (dashboard can't read until a policy is added = safe, visible failure), never world-open.

**MY OWN MISTAKE this session (the thing to actually learn):** my first fix blanket-applied `create policy ... for all to authenticated using(true)` to EVERY table. That was too broad and introduced two regressions: (1) it put an authenticated policy on `api_cache` + `pb_webhook_config` (backend/secret tables that must be service-role-only), and (2) it OVERRODE the `auth.uid()`-keyed per-tenant policies on `content_*`, which in a multi-client clone = cross-tenant leak. Lesson: a blanket policy is NOT safe when tables have intentional finer-grained or stricter policies. Audit existing policies + grants per table BEFORE applying a uniform one. This also recurred from 2026-05-13 (pb_webhook_config flagged by the SAME detector, fixed for that one table only) = fix the CLASS, not the instance.

**Enforcement now in place:** `dashboard/setup/schema.sql` ends with a default-deny block (RLS-on-all + revoke anon) that runs every apply; `scripts/enable-rls.sql` = full reusable model; `scripts/check-rls.mjs` = read-only drift detector (flags RLS-off or anon-granted tables, exit 1); clone-dashboard SKILL.md step 3b makes RLS lockdown mandatory for every new client.

**How to apply:**
- **Verify as the attacker, not the happy path.** Testing the authenticated dashboard (which worked) would have HIDDEN this. I only saw it by reading a previously-exposed table with the logged-out anon key (0 rows after fix = closed). Always test the adversarial/negative case.
- **A "nothing found / it works" result is often a query bug, not ground truth.** Same meta-mistake as the Anthony search this session (queried `lead.email` when the leads feed uses top-level `email`, so I wrongly concluded "no records"). Check HOW you looked before trusting a negative.
- **Enforce, don't document** ([[canon_working_process]] enforcement-first): the durable fix is RLS in the schema/clone TEMPLATE (every table born locked) + a periodic diagnostic (`scripts/enable-rls.sql` step 1) to catch drift. Not "remember to enable RLS."
- Safe fix pattern: enable RLS on all public tables + `create policy ... for all to authenticated using(true) with check(true)`. Server uses service-role (bypasses RLS); dashboard reads post-login (authenticated); anon locked out. Reusable SQL: `Precision-Brass/scripts/enable-rls.sql`.
