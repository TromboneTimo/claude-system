---
name: Google Sheets Integration Pattern
description: Proven pattern for connecting static HTML forms to Google Sheets via Vercel serverless functions with service accounts
type: feedback
originSessionId: fa5b0780-ff1a-4302-b31e-60891e1f1991
---
Use Vercel serverless function + Google service account for form-to-Sheets. Never use Google Apps Script for Workspace accounts.

**Why:** Google Apps Script web apps deployed from Workspace accounts (e.g. @trombonetimollc.com) are blocked from external access by default. Tried 3 approaches before landing on the one that works. Wasted significant time.

**How to apply:**
1. Create service account in Google Cloud Console (use gcloud CLI, not browser)
2. Enable Google Sheets API for the project
3. Share the target Google Sheet with the service account email as Editor
4. Store the full service account JSON as base64 in Vercel env var (`GOOGLE_CREDENTIALS_B64`)
5. Use `google.auth.JWT({ email, key, scopes })` - OBJECT form, not positional args
6. Call `await auth.authorize()` before making API calls
7. Always add `.vercelignore` to exclude `service-account-key.json`, `.env*`

**Security checklist for any form endpoint:**
- Restrict CORS to specific origins
- Rate limit by IP (5/hour for lead capture)
- Honeypot field (hidden, bots fill it, silently drop)
- Server-side email regex validation
- Sanitize all input (HTML escape)
- Generic error messages (never expose err.message to client)
- Security headers: X-Frame-Options DENY, X-Content-Type-Options nosniff
- Verify sensitive files return 404 after deploy
