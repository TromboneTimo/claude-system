---
name: Never close or restart Chrome without asking
description: Do not use Chrome browser agent for tasks that can be done other ways - never close Chrome without permission
type: feedback
---

NEVER close, quit, or restart Google Chrome without explicitly asking the user first. The browser agent's `launch --own-profile` kills the user's running Chrome, which is extremely disruptive.

**Why:** User was furious that Chrome was closed without warning. They had tabs open and didn't want their browser disrupted.

**How to apply:**
1. Never use the Chrome browser agent when other approaches exist (curl, n8n HTTP Request nodes, downloading files, etc.)
2. If Chrome browser is truly the only option, ASK the user before launching it
3. For checking Google Sheets: use n8n HTTP Request nodes with Google Sheets OAuth credential, or download the sheet via API, or check execution data
