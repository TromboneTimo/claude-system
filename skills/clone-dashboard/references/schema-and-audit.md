# Phase 3: Schema + full-state audit (Law 2)

This is the phase that bit us. `schema.sql` does NOT contain every table the pages use.
Some live ONLY in PB's running database. You must reconcile against reality, not the file.

## 3a. Apply the tracked schema + migrations
```bash
python scripts/supa.py sql --ref <new_ref> --file /Users/air/Desktop/Precision-Brass/dashboard/setup/schema.sql
for f in /Users/air/Desktop/Precision-Brass/dashboard/setup/migrations/*.sql; do
  python scripts/supa.py sql --ref <new_ref> --file "$f"
done
```
(`[]` from each = success. A `{"message": ...}` is an error; stop and read it.)

## 3b. Enumerate what the SELECTED pages actually query
For only the pages this client gets, list every table and rpc referenced:
```bash
cd /Users/air/Desktop/Precision-Brass/dashboard
grep -rhoE "from\('[a-z_]+'\)|\.rpc\('[a-z_]+'\)" <selected pages> | sort -u
```
Compare against what now exists in the new DB:
```bash
python scripts/supa.py sql --ref <new_ref> --query "select tablename from pg_tables where schemaname='public' order by tablename;"
```
Any referenced table/function NOT present is a gap. (In the Victor run the gaps were
`content_admins`, `content_clients`, `content_items`, `hooks`, and the function
`is_content_admin()` -- the entire Content Hub. Hook Library + Content Suggestions need them.)

## 3c. Pull missing objects from PB's LIVE database
For each missing table, read its real shape from PB (ref `iwlernqpwdsjarygoeog`) and rebuild it:
```bash
# columns
python scripts/supa.py sql --ref iwlernqpwdsjarygoeog --query "select table_name, column_name, data_type, udt_name, is_nullable, column_default from information_schema.columns where table_schema='public' and table_name in ('<missing>',...) order by table_name, ordinal_position;"
# RLS policies
python scripts/supa.py sql --ref iwlernqpwdsjarygoeog --query "select tablename, policyname, cmd, roles::text, qual, with_check from pg_policies where tablename in ('<missing>',...) order by tablename;"
# any function the policies call (e.g. is_content_admin)
python scripts/supa.py sql --ref iwlernqpwdsjarygoeog --query "select pg_get_functiondef(p.oid) def from pg_proc p join pg_namespace n on n.oid=p.pronamespace where p.proname in ('is_content_admin');"
```
Hand-write a migration that recreates: the function(s) first, then `create table if not exists`
(types/defaults from the column query), `alter table ... enable row level security`, and the
policies (drop-if-exists then create, so it is re-runnable). Save it under the NEW client's
`dashboard/setup/migrations/<date>_<feature>.sql`, then apply it with `supa.py sql --file`.

A reusable copy of the Content Hub migration already exists at
`/Users/air/Desktop/Victor Alegria Music/dashboard/setup/migrations/2026-06-04_content_hub.sql`
(content_admins/clients/items/hooks + is_content_admin + RLS). If the client selected
`suggestions.html` or `hooks.html`, start from that file and re-seed for this client.

## 3d-shared. Copy SHARED reference data (rows), not just structure
Creating a table empty is wrong when the table is a shared reference LIBRARY that every client
should inherit. The clearest example is `hooks` (Hook Library): "viral hook formulas for the
music niche", 300+ curated rows Timo built once and reuses across all music clients. We shipped
Victor an empty Hook Library and Timo (rightly) called it out -- "this is not like you copied
from Precision Brass."

Decide per table:
- **Shared reference library -> COPY THE ROWS** from PB. So far: `hooks`. (If future shared
  libraries appear, same treatment.)
- **Per-client / per-user data -> STRUCTURE ONLY**, no rows: `content_items`, `ideas`, `scripts`,
  `email_*`, `harrison_suggestions`, `meta_ads*`. These are PB-private; copying them would leak
  Harrison's data into the client's dashboard.

Copy rows structure-safely with `jsonb_populate_recordset` (handles every column/type, no manual
escaping). For each shared table:
```python
# python (build payloads via json.dumps; never interpolate into bash)
rows = sql(PB_REF,  "select coalesce(json_agg(t),'[]'::json)::text j from <table> t;")[0]["j"]
sql(NEW_REF, f"insert into <table> select * from "
             f"jsonb_populate_recordset(null::public.<table>, $tag${rows}$tag$::jsonb) "
             f"on conflict (id) do nothing;")
```
Then verify the count in the new project matches PB. If the client's niche differs enough that
some library rows are irrelevant, that is Timo's call to prune later; default to copying the
whole library so the page is not empty on day one.

## 3d. Seed per-client rows where RLS is keyed to auth.uid()
Some tables gate rows by the signed-in user's id, so they need seeds tied to THIS client:
- `content_admins`: insert each admin email (so `is_content_admin()` returns true for Timo).
- `content_clients`: insert one row whose `id` EQUALS the client's auth user uid (you get that
  uid in phase 4 when you create the client account). `display_name` = client name.
  RLS `content_clients read own` is `id = auth.uid()`, so a mismatched id means the client sees
  nothing. Do this seed AFTER phase 4 once you have the uid, or revisit here.
Use `on conflict do nothing` so re-runs are safe.

Build every SQL payload via `supa.py` (json.dumps), never by interpolating quotes into bash.
