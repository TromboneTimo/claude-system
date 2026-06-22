# Phase 2: Provision the client's own Supabase project

Each client gets a fully separate project. Never reuse PB's or another client's.

## Create the project
```bash
export SUPABASE_ACCESS_TOKEN=sbp_xxx   # from MASTER.md
DBPW=$(LC_ALL=C tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 32)   # alnum only, no shell-special chars
echo "$DBPW" > /tmp/<slug>_db_pw.txt
supabase projects create "<Client Name>" \
  --org-id teulawuyhnxrwnuaffqo \
  --db-password "$DBPW" \
  --region ap-southeast-2
```
Capture the **reference id** (the `agbld...`-style ref) from the output. The project URL is
`https://<ref>.supabase.co`.

Free tier allows a limited number of active projects per org. If create fails with a limit
error, surface it to Timo (he may need to upgrade or remove an old project); do not silently
work around it.

## Wait for the database, then fetch keys
The DB takes ~30-60s to provision. Probe it:
```bash
python scripts/supa.py sql --ref <ref> --query "select version();"
```
Once it returns, grab the API keys:
```bash
python scripts/supa.py api-keys --ref <ref>
```
You need:
- **anon / publishable** (`sb_publishable_...`): goes in browser `lib/config.js`. Prefer the
  `sb_publishable_` value, matching PB's config format.
- **service_role** (JWT `eyJ...`): server/Vercel + Admin API ONLY. Never in the browser.

Record ref, URL, db password, anon key, service_role key in the working JSON for later phases
and for MASTER.md (phase 9).
