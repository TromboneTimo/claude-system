---
name: Never use browser agent for transcripts
description: Never launch browser agent to get video transcripts. Use WebFetch, transcript APIs, or ask user to provide them.
type: feedback
---

Never use the browser-agent skill to fetch video transcripts. It relaunches Chrome, disrupts the user's workflow, and is the wrong tool for the job.

**Why:** User explicitly blocked this. Browser agent kills their running Chrome session.

**How to apply:** For transcripts, use WebFetch on transcript service URLs, ask the user to export/provide them, or use YouTube transcript APIs via WebFetch. If those fail, tell the user what you need and let THEM get it. Don't take over their browser.
