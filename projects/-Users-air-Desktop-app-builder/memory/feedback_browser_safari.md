---
name: feedback_browser_safari
description: ALWAYS use Safari for ALL web tasks — browsing, previews, testing, screenshots. NEVER default to Chrome.
type: feedback
---

ALWAYS use Safari for ALL web-related tasks. NEVER use Chrome or the Chrome browser agent unless the user explicitly asks for Chrome.

This applies to: web previews, opening URLs, web testing, screenshots, reading web pages — everything.

**Why:** User has corrected this multiple times and is extremely frustrated about it. This is a hard rule, not a preference.

**How to apply:** Use `open -a Safari <url>` for opening pages. For automation tasks (clicking, typing, form filling), only use the Chrome browser agent as an absolute last resort and ASK FIRST.
