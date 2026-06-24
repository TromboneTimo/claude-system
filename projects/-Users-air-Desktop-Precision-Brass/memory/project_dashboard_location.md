---
name: Precision Brass Dashboard Location
description: Harrison's Precision Brass dashboard lives in the workspace, not Downloads. Open index.html in Safari.
type: project
originSessionId: 601d67f3-d629-457e-9d0b-56cae7e6513a
---
Precision Brass dashboard location: `/Users/air/Desktop/Precision-Brass/dashboard/`

- Main entry: `dashboard/index.html` (redirects to login)
- Harrison's command center: `dashboard/scripts.html` (idea + script approvals)
- Email proposal queue: `dashboard/emails.html` [added 2026-04-28]
- Email performance analytics: `dashboard/email-analytics.html` [renamed from email.html on 2026-04-28; /email path redirects via vercel.json]
- Other tabs: `revenue.html`, `facebook.html`, `instagram.html`, `youtube.html`, `ideas.html`
- Standalone single-file version: `dashboard/standalone.html`
- Supporting: `styles.css`, `scripts/`, `data/`, `setup/`, `lib/{config,auth,db}.js`

**Why:** Timo moved it out of Downloads on 2026-04-21 after getting annoyed chasing the file. Canonical location is the workspace.

**How to apply:** When asked to "open Harrison dashboard" or "open Precision Brass dashboard," run `open -a Safari /Users/air/Desktop/Precision-Brass/dashboard/index.html`. Do NOT look in Downloads.
