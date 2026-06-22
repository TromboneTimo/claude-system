# Phase 9: Record everything

A clone produces real, billable, hard-to-rediscover infrastructure. Persist it so the next
session (or the client support request three weeks from now) does not start from zero.

## 9a. MASTER.md (`~/.claude/credentials/MASTER.md`)
Append a new section for the client. Mirror the existing Victor Alegria Music section format:
```
## <Client Name> / Dashboard

### Client login (Supabase Auth)
**Email:** <client_email>
**Password:** <client_password>
**Use:** restricted-role account the client signs in with.

### Admin accounts
**Emails:** <admin emails>
**Password:** SAME as Precision Brass (bcrypt hash copied from PB auth.users on <date>). Plaintext never stored.

### Supabase project (<Client Name>)
SUPABASE_URL=https://<new_ref>.supabase.co
SUPABASE_PROJECT_REF=<new_ref>
SUPABASE_ORG=Timo LLC (teulawuyhnxrwnuaffqo)
SUPABASE_REGION=ap-southeast-2
SUPABASE_ANON_KEY=<publishable key>          # browser, in dashboard/lib/config.js
SUPABASE_SERVICE_ROLE_KEY=<service_role jwt>  # server/Vercel ONLY
SUPABASE_DB_PASSWORD=<db password>

### Vercel
Project: <slug> (org trombonetimo-9261s-projects)
Live URL: https://<slug>.vercel.app
Pages included: <selected pages>
```
Confirm to Timo with 4-char prefixes only when echoing any secret, never the full value.

## 9b. Project memory
If the client has a workspace memory dir, write a `project_dashboard_live.md` there (model it on
Victor's: URL, Supabase ref, accounts, nav model, what is still TODO such as ActiveCampaign keys).
Add a one-line pointer in that workspace's `MEMORY.md`.

## 9c. Leftover TODOs to name out loud
The dashboard renders but data features stay empty until the client's own integrations are wired.
Tell Timo plainly what is NOT done yet, e.g.:
- ActiveCampaign / email API keys (the api functions need them; env left blank)
- any client-specific seed content
- a client avatar image if you used initials as a placeholder
Lead with these caveats rather than implying the whole system is live.
