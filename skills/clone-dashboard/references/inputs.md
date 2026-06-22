# Phase 1: Gather inputs + page selection

## Read credentials first (Law 1)
Pull the Supabase personal access token from MASTER.md. Do NOT ask Timo for it.
```bash
grep -E "SUPABASE_PERSONAL_ACCESS_TOKEN" ~/.claude/credentials/MASTER.md
```
Export it for every Supabase command this run:
```bash
export SUPABASE_ACCESS_TOKEN=sbp_xxx   # the value you just read
```
You will also need PB's service-role key (for reading PB data if ever needed) and PB's
ref `iwlernqpwdsjarygoeog`, both in MASTER.md.

## Prompt Timo for the few things only he knows
Ask these as a quick batch (one message, or AskUserQuestion):
- **Client name** (display), e.g. "Jane Doe Cello". Derive a slug: lowercase, spaces->`-`,
  strip anything not `[a-z0-9._-]`, no `---`. e.g. `jane-doe-cello`. Vercel project names
  must be lowercase and cannot contain spaces (this bit us: a folder with spaces fails).
- **Niche / segment** (one line, used in page copy + memory).
- **Client login email** + **client login password** (the account THEY use; restricted role).
- **Admin emails** (default: timothyjay.maines@gmail.com + trombonetimollc@gmail.com).

## Present PB's page inventory as a multi-select
List the actual pages so the set is current, not hardcoded:
```bash
ls /Users/air/Desktop/Precision-Brass/dashboard/*.html | xargs -n1 basename
```
Typical inventory and what each is:
- `scripts.html` (Script Approvals, the core workflow) and `login.html` / `index.html` are ALWAYS included.
- `suggestions.html` (Content Suggestions, client-facing)
- `hooks.html` (Hook Library, ADMIN-ONLY / Timo Tools)
- `ideas.html`, `emails.html`, `scheduled.html`, `email-analytics.html`,
  `channel-attribution.html`, `meta-ads.html`, `book-meeting.html`, `broadcast.html`,
  `standalone.html`, `facebook.html`, `instagram.html`, `youtube.html`, `revenue.html`,
  `changes.html`

Use AskUserQuestion (multiSelect) so Timo ticks what THIS client gets. Note for him which
are admin-only vs client-facing, and that paid-ads pages (meta-ads, etc.) only make sense if
the client runs paid ads. Record the selected set; it drives phases 3, 5, and 8.

## Carry forward
Write a small JSON to the new client's working dir capturing: client_name, slug, niche,
client_email, client_password, admin_emails[], selected_pages[]. Every later phase reads it.
