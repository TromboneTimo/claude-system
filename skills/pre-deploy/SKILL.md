---
name: pre-deploy
description: Mandatory pre-deploy checklist. Run BEFORE every Vercel deploy. Enforces build, QA agent, API verify, and browser test. Use when about to deploy, or when user says "deploy", "ship it", "push to prod".
---

# Pre-Deploy Gate — 4-Layer Verification

**NEVER deploy without completing ALL 4 layers. No exceptions.**

## Layer 1: Build + Lint
```bash
cd [project-dir] && npm run build && npm run lint
```
Both must pass with ZERO errors. If either fails, fix before proceeding.

## Layer 2: QA Agent Review
Spawn the QA reviewer agent with a focused prompt covering:
- All files changed since last deploy
- React anti-patterns (missing keys, hook rules, missing deps)
- Auth/role leakage (admin UI visible to clients?)
- Loading states (any "Loading..." text? Must be zero)
- Build passes

QA must return **PASS** verdict. If CRITICAL issues found, fix and re-run QA.

## Layer 3: API Verify
For auth/data changes, test the actual API:
```bash
# Test login
curl -s -X POST "[SUPABASE_URL]/auth/v1/token?grant_type=password" \
  -H "apikey: [ANON_KEY]" -H "Content-Type: application/json" \
  -d '{"email":"[ADMIN_EMAIL]","password":"[ADMIN_PASSWORD]"}'

# Test data access with the token
curl -s "[SUPABASE_URL]/rest/v1/[TABLE]?select=id&limit=3" \
  -H "apikey: [ANON_KEY]" -H "Authorization: Bearer [TOKEN]"
```

## Layer 4: Browser Verify
After deploying:
```bash
open -a Safari "[DEPLOYED_URL]"
```
- Fresh visitor (incognito): must see login form instantly, no loading screen
- Admin login: must see library with cards, edit buttons work
- Client login: must see library without edit buttons

## Only after ALL 4 layers pass, tell the user it's ready.

Report results:
```
## Deploy Gate Results
- Build: PASS/FAIL
- QA: PASS/FAIL  
- API: PASS/FAIL
- Browser: PASS/FAIL (or SKIPPED with reason)
```
