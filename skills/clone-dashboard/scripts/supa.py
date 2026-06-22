#!/usr/bin/env python3
"""
supa.py - Supabase helper for the clone-dashboard skill.

Wraps the exact mechanics validated during the Precision Brass -> Victor Alegria
clone, so the skill never re-derives them or trips the bash single-quote / SQL
escaping traps. Every payload is built with json.dumps; nothing is interpolated
into a shell.

Auth: pass tokens explicitly, or set env vars:
  SUPABASE_ACCESS_TOKEN   personal access token (sbp_...) for the Management API
                          (DDL/DML, project create). Lives in MASTER.md.

Subcommands:
  sql        Run SQL against a project (Management API). --file or --query. Prints JSON.
  api-keys   Print a project's anon / service_role / publishable keys.
  create-user  Create an auth user (Admin API). --email --password [--service-key].
  copy-hash  Copy auth.users.encrypted_password for an email from a SOURCE project
             into a DEST project, then verify md5(hash) matches. Plaintext never seen.

Examples:
  python supa.py sql --ref agbld... --file setup/schema.sql
  python supa.py sql --ref agbld... --query "select tablename from pg_tables where schemaname='public';"
  python supa.py api-keys --ref agbld...
  python supa.py create-user --ref agbld... --service-key eyJ... --email a@b.com --password pw
  python supa.py copy-hash --src-ref iwler... --dst-ref agbld... --email timothyjay.maines@gmail.com
"""
import argparse, json, os, sys, urllib.request, urllib.error

MGMT = "https://api.supabase.com/v1"


def _req(url, token, method="GET", body=None, extra_headers=None):
    data = None
    # Supabase sits behind Cloudflare, which blocks urllib's default UA (error 1010).
    # A curl-style UA passes, matching the curl calls this script replaces.
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json",
               "User-Agent": "curl/8.4.0"}
    if extra_headers:
        headers.update(extra_headers)
    if body is not None:
        data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw.strip() else []
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"HTTP {e.code}: {e.read().decode()}\n")
        sys.exit(1)


def mgmt_token(args):
    tok = getattr(args, "token", None) or os.environ.get("SUPABASE_ACCESS_TOKEN")
    if not tok:
        sys.stderr.write("No management token. Pass --token or set SUPABASE_ACCESS_TOKEN "
                         "(the sbp_ personal access token from MASTER.md).\n")
        sys.exit(1)
    return tok


def run_sql(ref, token, query):
    """POST a SQL string to the Management API query endpoint. Returns parsed JSON."""
    out = _req(f"{MGMT}/projects/{ref}/database/query", token, "POST", {"query": query})
    if isinstance(out, dict) and out.get("message"):
        sys.stderr.write("SQL error: " + out["message"] + "\n")
        sys.exit(1)
    return out


def cmd_sql(args):
    token = mgmt_token(args)
    if args.file:
        query = open(args.file).read()
    elif args.query:
        query = args.query
    else:
        query = sys.stdin.read()
    print(json.dumps(run_sql(args.ref, token, query), indent=2))


def cmd_api_keys(args):
    token = mgmt_token(args)
    keys = _req(f"{MGMT}/projects/{args.ref}/api-keys", token)
    # Normalize to a simple name->value map plus the publishable/secret if present.
    out = {}
    for k in keys:
        out.setdefault(k.get("name"), k.get("api_key") or k.get("key") or k.get("api_key_value"))
    print(json.dumps(out, indent=2))


def cmd_create_user(args):
    sk = args.service_key
    if not sk:
        sys.stderr.write("create-user needs --service-key (the dest project's service_role JWT).\n")
        sys.exit(1)
    url = f"https://{args.ref}.supabase.co/auth/v1/admin/users"
    body = {"email": args.email, "password": args.password, "email_confirm": True}
    headers = {"apikey": sk, "Authorization": f"Bearer {sk}", "Content-Type": "application/json",
               "User-Agent": "curl/8.4.0"}
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method="POST", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        # Surface "already registered" without aborting the whole run.
        msg = e.read().decode()
        sys.stderr.write(f"create-user HTTP {e.code}: {msg}\n")
        print(json.dumps({"error": msg, "email": args.email}))
        return
    print(json.dumps({"email": d.get("email"), "id": d.get("id"),
                      "confirmed": bool(d.get("email_confirmed_at"))}, indent=2))


def cmd_copy_hash(args):
    """Copy encrypted_password for one email from src project's auth.users to dest's,
    then verify md5 of the stored hash matches across both. Never reads plaintext."""
    src_tok = args.src_token or os.environ.get("SUPABASE_ACCESS_TOKEN")
    dst_tok = args.dst_token or os.environ.get("SUPABASE_ACCESS_TOKEN")
    email = args.email.replace("'", "''")
    rows = run_sql(args.src_ref, src_tok,
                   f"select encrypted_password from auth.users where lower(email)=lower('{email}');")
    if not rows or not rows[0].get("encrypted_password"):
        sys.stderr.write(f"No password hash for {args.email} in source project.\n")
        sys.exit(1)
    pw = rows[0]["encrypted_password"].replace("'", "''")
    run_sql(args.dst_ref, dst_tok,
            f"update auth.users set encrypted_password='{pw}', updated_at=now() "
            f"where lower(email)=lower('{email}');")
    # Verify
    q = f"select md5(encrypted_password) h from auth.users where lower(email)=lower('{email}');"
    s = run_sql(args.src_ref, src_tok, q)
    d = run_sql(args.dst_ref, dst_tok, q)
    sh = s[0]["h"] if s else None
    dh = d[0]["h"] if d else None
    ok = sh is not None and sh == dh
    print(json.dumps({"email": args.email, "src_md5": sh, "dst_md5": dh, "match": ok}, indent=2))
    if not ok:
        sys.exit(1)


def main():
    p = argparse.ArgumentParser(description="Supabase helper for clone-dashboard")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sql"); s.add_argument("--ref", required=True)
    s.add_argument("--token"); s.add_argument("--file"); s.add_argument("--query")
    s.set_defaults(func=cmd_sql)

    s = sub.add_parser("api-keys"); s.add_argument("--ref", required=True)
    s.add_argument("--token"); s.set_defaults(func=cmd_api_keys)

    s = sub.add_parser("create-user"); s.add_argument("--ref", required=True)
    s.add_argument("--service-key"); s.add_argument("--email", required=True)
    s.add_argument("--password", required=True); s.set_defaults(func=cmd_create_user)

    s = sub.add_parser("copy-hash")
    s.add_argument("--src-ref", required=True); s.add_argument("--dst-ref", required=True)
    s.add_argument("--src-token"); s.add_argument("--dst-token")
    s.add_argument("--email", required=True); s.set_defaults(func=cmd_copy_hash)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
