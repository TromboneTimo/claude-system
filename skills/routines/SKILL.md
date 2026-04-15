---
name: routines
description: Create, fire, and manage Claude Code cloud routines (scheduled/API/GitHub-triggered remote agents). Use when Timo asks to set up a recurring remote agent, a webhook-triggered workflow, automate a daily/weekly task in the cloud, schedule a cron job for Claude Code, or anything involving claude.ai/code/scheduled. Triggers on "routine", "schedule a remote agent", "webhook to Claude", "daily/weekly Claude job", "cron routine", or /routines.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, ToolSearch, WebFetch, RemoteTrigger
---

# Routines: Cloud Scheduled Agents

Routines are **saved Claude Code configurations that run on Anthropic-managed cloud infrastructure**: a prompt + repo(s) + connectors, fired on a schedule, HTTP POST, or GitHub event. They keep working when Timo's laptop is closed.

Docs: https://code.claude.com/docs/en/routines
Fire API: https://platform.claude.com/docs/en/api/claude-code/routines-fire
Web UI: https://claude.ai/code/scheduled

## When to use routines vs other scheduling

| Need | Use |
|------|-----|
| Runs unattended in cloud, survives laptop off | **Routine** (this skill) |
| Runs inside the current REPL session only | `CronCreate` (in-session) |
| Runs on Timo's local machine with local file/MCP access | Desktop scheduled task |
| One-shot reminder later today | `CronCreate` with `recurring: false` |

**Hard constraint**: routines run in Anthropic cloud. They have **no access to**:
- Chrome DevTools MCP (Timo's logged-in X/Skool/etc. sessions)
- Local files outside the cloned repo
- Local `.env` variables
- Anything on Timo's local file system not in the GitHub repo

If the task needs any of those, either adapt it to use WebFetch/WebSearch + API calls (with secrets added to the cloud env), or use a local scheduler instead.

## Canonical creation body (tested, works)

Load `RemoteTrigger` first, then call `{action: "create", body: ...}` with this exact shape:

```json
{
  "name": "DESCRIPTIVE_NAME",
  "cron_expression": "MM HH * * *",
  "enabled": true,
  "job_config": {
    "ccr": {
      "environment_id": "env_01MSLjBzwZA3cAG7pqkYwLM3",
      "session_context": {
        "model": "claude-sonnet-4-6",
        "sources": [
          {"git_repository": {"url": "https://github.com/TromboneTimo/claude-system"}}
        ],
        "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch"]
      },
      "events": [
        {
          "data": {
            "uuid": "GENERATE_FRESH_LOWERCASE_V4_UUID",
            "session_id": "",
            "type": "user",
            "parent_tool_use_id": null,
            "message": {
              "role": "user",
              "content": "THE_PROMPT_HERE"
            }
          }
        }
      ]
    }
  }
}
```

### Timo's verified account values (extracted from existing routines 2026-04-14)

- **`environment_id`**: `env_01MSLjBzwZA3cAG7pqkYwLM3` (Default env, used by all 3 existing routines)
- **Default repo**: `https://github.com/TromboneTimo/claude-system` (his ~/.claude config repo; use for system-maintenance routines. Create a separate repo for business automations that shouldn't touch the config.)
- **Default model**: `claude-sonnet-4-6` (all existing routines use this)
- **Account UUID**: `43ecfec1-0230-46bc-8c4f-44c3f909818e`
- **Timezone**: JST (UTC+9). To convert local to UTC: subtract 9 hours. 9 AM JST = 0:00 UTC the same day. 7 AM JST = 22:00 UTC the previous day.
- **Available MCP connectors for routines**: Google-Calendar (`d0b207fb-272c-415e-a873-d572ae92254a`), Gmail (`1eedb707-9ef0-45fb-bc8a-725dcb6aa0e2`). Attach via `mcp_connections` in the create body when the routine needs them.

## Cron conventions

- **Cron is UTC**. Timo is in JST (UTC+9). Subtract 9 hours from JST to get UTC.
- **Minimum interval: 1 hour**. `*/30 * * * *` is rejected.
- **Avoid minute 0 and 30**: every routine on the platform lands on those. Pick an off-minute (`:07`, `:17`, `:43`, `:51`).
- **Stagger multiple daily routines** by 15+ min so they don't compete for resources.

Examples (JST to UTC):
- Daily at 8 AM JST: `17 23 * * *` (i.e. 23:17 UTC previous day)
- Daily at 7 AM JST: `43 22 * * *`
- Daily at 9 AM JST: `7 0 * * *` (midnight UTC, same day)
- Sunday 9 PM JST: `0 12 * * 0` (existing Weekly Deep Review cadence)
- Every 2 hours: `13 */2 * * *`

**Existing slots to avoid conflicting with:**
- `57 22 * * *` (Daily Morning Briefing, 7:57 AM JST)
- `0 12 * * 0` (Weekly Deep Review, 9 PM JST Sundays)
- `0 0 * * *` (Daily Brain Fix, 9 AM JST, currently DISABLED)

## Allowed tools

Pick the smallest set the routine actually needs. Common combos:

| Routine type | Tools |
|--------------|-------|
| Web research / scanning | `Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch` |
| API automation (no code) | `Bash, Read, Write, Edit, WebFetch` |
| Code review / PR work | `Bash, Read, Write, Edit, Glob, Grep` |
| Data pull + report | `Bash, Read, Write, Edit, Glob, Grep, WebFetch` |

Do **not** add MCP tools to `allowed_tools`; MCP is attached separately via `mcp_connections` in the create body. Timo has Gmail and Google-Calendar connectors available (see verified values section). Attach them only when the routine actually needs to read/send email or calendar events.

## UUID generation

Events require a fresh lowercase v4 UUID. Generate one per routine:

```bash
python3 -c "import uuid; print(uuid.uuid4())"
# or
uuidgen | tr '[:upper:]' '[:lower:]'
```

Never reuse a UUID across routines.

## Output conventions

Routines should write results to the cloned repo on a `claude/*` branch (the default allowed prefix). Standard pattern:

1. Write markdown report to `active/{routine-name}/YYYY-MM-DD-HHmm-report.md`
2. Commit to `claude/{routine-name}-YYYY-MM-DD` branch
3. Also print the report to stdout so it shows in the session transcript at claude.ai/code/scheduled/{trigger_id}

Timo can open the session URL to see output, or pull the branch if he wants the file.

## Secrets and environment variables

The Default cloud env has no custom env vars. To give a routine API access (Shopify, Resend, ClickUp, Skool, etc.):

1. Go to https://claude.ai/code/environments
2. Edit Default (or create a new env) and add `KEY=VALUE` pairs
3. Reference them in the prompt as `$KEY`. The routine's Bash sessions will see them

**Always check for secret presence in the prompt** and exit gracefully if missing:

```
REQUIRED ENV VAR: SHOPIFY_API_KEY must be set. If missing, print
"Missing SHOPIFY_API_KEY. Add at claude.ai/code/environments" and exit.
```

Never hardcode secrets in prompts. They are logged.

## Firing a routine

**Manually (right now, for testing)**:
```
RemoteTrigger({action: "run", trigger_id: "trig_01..."})
```
Returns the trigger config, not the session URL. Fire is async. The session appears at claude.ai/code/scheduled/{trigger_id}.

**Via HTTP (for webhooks)**:
```
POST https://api.anthropic.com/v1/claude_code/routines/{trigger_id}/fire
Authorization: Bearer {per-routine-token}
anthropic-version: 2023-06-01
anthropic-beta: experimental-cc-routine-2026-04-01
Content-Type: application/json

{"text": "freeform context appended to the saved prompt"}
```

The `text` field is a single string appended as a user turn. Max 65,536 chars. If sending a JSON webhook payload, stringify it; the routine can parse the string in its prompt.

**Generating the per-routine token**: Web UI only. Open the routine at https://claude.ai/code/scheduled, click pencil, then Add another trigger, then API, then Generate token. Shown once, cannot be retrieved.

## Trigger types and how to add them

| Trigger | Created via | Notes |
|---------|-------------|-------|
| Schedule | `RemoteTrigger create` (this skill) or web UI | Cron in UTC, min 1h |
| API | Web UI only (generates bearer token) | Attach to existing routine |
| GitHub event | Web UI only | Requires Claude GitHub App installed on repo |

A single routine can have multiple triggers.

## Common webhook patterns

### Pattern 1: Transcript service webhook, then recap email

```
Fireflies/Otter webhook (meeting.completed)
  POSTs {"text": "<stringified webhook JSON>"} to /fire endpoint
  Routine parses text to get meetingId
  curl transcript service GraphQL API with API_KEY for full transcript
  Claude drafts personalized recap email
  curl Resend API with RESEND_API_KEY to send
```

Secrets needed: transcript service API key, `RESEND_API_KEY`.

### Pattern 2: CRM task closed, then kickoff email

```
ClickUp/Notion webhook (taskStatusUpdated, filtered to status="Closed")
  POSTs to /fire endpoint
  Routine calls CRM API with CRM_API_TOKEN to get full task (client email, notes)
  Claude drafts kickoff email with Cal.com booking link
  Sends via Resend
```

Secrets: `CRM_API_TOKEN`, `RESEND_API_KEY`, Cal.com booking link in the prompt.

### Webhook payload to /fire translation

Most third-party webhooks (Fireflies, ClickUp, Stripe, GitHub) send their own JSON shape, but `/fire` only accepts `{"text": "..."}`. Two options:

- **Configure the sender to custom body template**: set body to `{"text": "{{stringified_event}}"}`. Works for Zapier, Make, Fireflies custom webhooks.
- **Middleware**: Cloudflare Worker / Vercel function that receives the webhook, reformats, POSTs to `/fire`. Use if you want signature verification or branching logic.

## Managing routines

```
# List all
RemoteTrigger({action: "list"})

# Get one
RemoteTrigger({action: "get", trigger_id: "trig_01..."})

# Update (partial)
RemoteTrigger({action: "update", trigger_id: "trig_01...", body: {"cron_expression": "..."}})

# Fire now
RemoteTrigger({action: "run", trigger_id: "trig_01..."})
```

**Cannot delete via API**. Direct Timo to https://claude.ai/code/scheduled to delete.

**Pausing**: set `"enabled": false` via update. Re-enable by setting back to `true`.

## Common errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `prompt: Extra inputs are not permitted` | Put `prompt` at top level | Move to `job_config.ccr.events[0].data.message.content` |
| `job_config must have "ccr" shape` | Used `session_request` or empty `job_config` | Use `job_config.ccr.{environment_id, session_context, events}` |
| `session_request.worker: Field required` | Used old `session_request` shape | Switch to `job_config.ccr` (v2 shape) |
| `invalid cron expression` | Interval < 1h, or 6-field cron | Use 5-field, >=1h |
| `proto: unknown field "type"` | Added unknown top-level field | Remove non-schema fields |
| Session fires but does nothing visible | Expected: fire is async, output is in session URL | Check claude.ai/code/scheduled/{trigger_id} |

## Full working example (tested 2026-04-14, from Nick's original)

Creates a daily routine that scans for mentions of Timo and commits a report. ADAPT THE GITHUB REPO AND ENVIRONMENT ID TO TIMO'S VALUES FIRST:

```python
# Pseudocode for the RemoteTrigger call
RemoteTrigger(action="create", body={
    "name": "Daily Mention Scan",
    "cron_expression": "51 12 * * *",  # adjust for Timo's timezone
    "enabled": True,
    "job_config": {
        "ccr": {
            "environment_id": "env_01MSLjBzwZA3cAG7pqkYwLM3",
            "session_context": {
                "model": "claude-sonnet-4-6",
                "sources": [{"git_repository": {"url": "https://github.com/TromboneTimo/claude-system"}}],
                "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch"]
            },
            "events": [{
                "data": {
                    "uuid": "d8e4a2b6-5c9f-47d1-b3a7-2e8f4c6d9b17",
                    "session_id": "",
                    "type": "user",
                    "parent_tool_use_id": None,
                    "message": {
                        "role": "user",
                        "content": "Run WebSearch queries for 'Trombone Timo' and 'Creator Conservatory' with after:{today-2} date filter across reddit, x, HN, linkedin, youtube, podcasts. Filter hard for newsworthy signal (notable mentions, press, student wins). Commit findings to claude/timo-scan-YYYY-MM-DD branch if anything interesting, else print 'No notable mentions.' and exit."
                    }
                }
            }]
        }
    }
})
```

Response includes `trigger.id` (prefix `trig_`). Store for future fire/update calls.

## Workflow checklist

When Timo asks for a new routine:

1. **Clarify the task**: what runs, when, what output, what secrets needed
2. **Check constraints**: does it need Chrome DevTools, local files, local env? If yes, redirect to local scheduler
3. **Pick schedule**: UTC, off-:00 minute, stagger against existing routines (check `RemoteTrigger list`)
4. **Pick tools**: minimum viable set (avoid adding WebFetch if not needed)
5. **Draft prompt**: self-contained, specific steps, explicit output format + save path, graceful handling of missing secrets
6. **Generate fresh UUID**
7. **Create**: `RemoteTrigger create`
8. **Test**: `RemoteTrigger run` immediately
9. **Report back**: trigger ID, schedule in local time, session URL, any secrets Timo still needs to add
10. **Add to active/todo.md if secrets are pending**

## Reference: active routines (update as they change)

Check `RemoteTrigger({action: "list"})` for the current set. Past history is on claude.ai/code/scheduled.

## Setup TODO (do before first routine creation)

Timo needs to run these once and tell Claude the values, then this skill should be updated with them inline:

1. **Get environment ID**: visit https://claude.ai/code/environments, copy the Default env ID (looks like `env_01...`), replace `env_01MSLjBzwZA3cAG7pqkYwLM3` in this file.
2. **Get default repo URL**: pick which GitHub repo routines should clone (probably the creator-conservatory repo or a dedicated automation repo), replace `TIMO_ORG/TIMO_REPO`.
3. **Confirm timezone**: tell Claude which timezone to use for cron conversion. Update examples section.
4. **Enable Claude Code on the web**: required for routines. Check at https://claude.ai/settings.
5. **Install Claude GitHub App** (only if using GitHub triggers): the trigger setup prompts for this.

After these five steps, this skill can create routines end-to-end via `/routines`.
