---
name: Test Locally Before Deploying
description: Always test serverless functions and API integrations locally before deploying to production - avoids wasted deploy cycles
type: feedback
originSessionId: fa5b0780-ff1a-4302-b31e-60891e1f1991
---
Test locally before deploying. Always.

**Why:** Spent 4+ failed Vercel deploys debugging a serverless function that crashed on production. When finally tested locally, found and fixed the bug (wrong JWT constructor signature) in one shot. Every deploy cycle was wasted time.

**How to apply:**
- For Vercel serverless functions: write a local test script, run it with real env vars, confirm it works, THEN deploy
- For API integrations (Google Sheets, etc.): test the auth and API calls locally with the actual credentials before wiring into production
- For env vars with special characters (private keys): base64 encode them. Don't try to escape newlines manually.
- `google.auth.JWT` in googleapis v171+: use object form `{ email, key, scopes }`, NOT positional args `(email, null, key, scopes)`
