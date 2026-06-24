---
name: Use APIs and tools proactively - don't ask the user
description: When you have API keys or CLI tools available, USE THEM instead of asking the user to look things up
type: feedback
---

Stop asking the user to provide information you can look up yourself. If you have an API key, credentials, or CLI access to a service — USE IT.

**Why:** User got frustrated when asked for a Fireflies meeting ID despite having the Fireflies API key available. One simple GraphQL query (`transcripts { id title }`) returned the answer instantly. The user shouldn't have to hold your hand when you already have the tools.

**How to apply:**
- Before asking the user for any piece of data, check if you already have API access, credentials, or CLI tools that can retrieve it
- Fireflies API key: `d9622a37-e54a-4ff3-be21-82f027942cbd` — use it to query meetings, transcripts, attendees directly
- Google Sheets API — accessible via n8n workflows or credentials on the instance
- Always try to fetch/find information yourself FIRST, only ask the user as a last resort
- This applies broadly: don't claim you "can't" do something without actually trying the tools you have available
