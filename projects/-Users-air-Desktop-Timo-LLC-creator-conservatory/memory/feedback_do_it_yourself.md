---
name: Do It Yourself, Don't Delegate to User
description: Never tell Timo to do setup steps that Claude can do programmatically - install tools, create resources, configure services
type: feedback
originSessionId: fa5b0780-ff1a-4302-b31e-60891e1f1991
---
Do it yourself. Don't tell Timo to do things you can do.

**Why:** Got called out multiple times for saying "go do X in the Google Cloud Console" or "share this sheet with this email" when I could have scripted it. Timo expects me to be an operational partner, not a tutorial.

**How to apply:**
- If a CLI tool isn't installed, install it
- If an API can create a resource, use the API instead of telling the user to click through a UI
- If the user needs to do ONE thing (like authorize in a browser), that's fine - but batch everything else
- Google Workspace accounts block Apps Script web apps for external access - use service accounts instead
- Never use browser-agent (Timo explicitly said never)
