# Phase 4: Auth accounts

Two kinds of account: the CLIENT (restricted, their own password) and the ADMINS (Timo, whose
password is copied from PB so his login is identical everywhere).

## 4a. Create the client account (restricted role)
```bash
python scripts/supa.py create-user --ref <new_ref> --service-key <new_service_role_jwt> \
  --email <client_email> --password <client_password>
```
Record the returned `id` (the client's auth uid). You need it for the `content_clients` seed in
phase 3d, because RLS keys client rows to `auth.uid()`.

## 4b. Create + hash-copy each admin (Law 1: never ask for the password)
Timo's real password lives only as a bcrypt hash in PB. Copy the hash; never read plaintext.
For each admin email:
```bash
# 1. create the account with a throwaway password (it gets overwritten next)
python scripts/supa.py create-user --ref <new_ref> --service-key <new_service_role_jwt> \
  --email <admin_email> --password "TEMP_$(LC_ALL=C tr -dc A-Za-z0-9 </dev/urandom | head -c 16)"

# 2. copy PB's bcrypt hash into the new project + verify md5 matches across both DBs
export SUPABASE_ACCESS_TOKEN=sbp_xxx   # from MASTER.md
python scripts/supa.py copy-hash \
  --src-ref iwlernqpwdsjarygoeog --dst-ref <new_ref> --email <admin_email>
```
`copy-hash` prints `{"match": true}` when the stored hashes are byte-identical. If it prints
`match: false` or exits non-zero, the admin password did NOT transfer; investigate before phase 7.
If an admin email has no account in PB yet, there is no hash to copy. Tell Timo and either set a
known password or skip that admin.

## Why this works
Supabase verifies a login by bcrypt-checking the submitted password against the stored
`encrypted_password`. Identical stored hash + same typed password = successful login. So copying
the hash makes Timo's existing PB password work on the new dashboard without anyone knowing it in
the clear.
