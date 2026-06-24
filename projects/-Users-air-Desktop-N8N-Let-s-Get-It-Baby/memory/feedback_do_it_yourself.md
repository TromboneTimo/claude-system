---
name: Do it yourself - don't ask user for setup steps
description: Use APIs and tools to complete setup tasks instead of giving the user manual instructions
type: feedback
---

When there are setup tasks (creating Google Sheets, filling in data, configuring services), DO NOT give the user step-by-step manual instructions. Instead, use the available tools to do it yourself.

**Why:** User has ADHD and explicitly called out that I should use the tools available (browser agent, n8n MCP, HTTP Request nodes via n8n) to do the work rather than dumping instructions on them. They said "i genuinely dont understand why you cant do these google sheet steps without me."

**How to apply:** When a task requires creating external resources (sheets, configs, etc.), use n8n HTTP Request nodes with existing OAuth credentials to call APIs directly, or use the browser agent. Create temporary n8n workflows with webhook triggers to execute API calls, then clean them up. Never default to giving manual instructions when an automated path exists.
