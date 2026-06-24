---
name: Claude Routines (Claude Code feature, April 2026)
description: Routines ARE a Claude Code feature. Saved configurations (prompt + repos + connectors) that run on Anthropic cloud via schedule/API/GitHub triggers. Available in CLI via /schedule, Desktop app, or web at claude.ai/code/routines. All three surfaces write to same account.
type: reference
originSessionId: 2026-04-14T23:53:44Z
---
# Claude Code Routines - April 2026

**Corrected understanding:** Routines ARE a Claude Code feature, not a claude.ai-only feature. Earlier version of this memory was wrong and has been overwritten.

**Docs:** https://code.claude.com/docs/en/routines
**Management:** https://claude.ai/code/routines (web), `/schedule` in CLI, or Desktop app "New task > New remote task"

## What A Routine Is

A saved Claude Code configuration packaged once and run automatically:
- Prompt
- One or more GitHub repositories
- Set of MCP connectors
- One or more triggers

Runs on Anthropic-managed cloud infrastructure. Laptop can be closed.

**Note:** In research preview as of April 2026. API and behavior may change.

## Three Trigger Types

1. **Schedule:** hourly, daily, weekdays, weekly, or custom cron (minimum 1-hour interval)
2. **API:** per-routine HTTPS endpoint, bearer token auth, POST with optional `text` payload that appends to the prompt
3. **GitHub:** reacts to PR, push, issue, workflow run, and many other events with filters (author, branch, labels, draft state, etc.)

A single routine can combine triggers. Example: PR review routine that runs nightly AND on every new PR AND on deploy webhooks.

## CLI Commands (the ones that matter)

| Command | What it does |
|---------|--------------|
| `/schedule <description>` | Create a scheduled routine conversationally, e.g. `/schedule daily PR review at 9am` |
| `/schedule list` | Show all routines |
| `/schedule update` | Edit an existing routine, including setting custom cron expressions |
| `/schedule run` | Fire a routine immediately |
| `/web-setup` | Required before routines can clone your repos (grants GitHub access) |

**CLI limits:** Only creates scheduled triggers. To add API or GitHub triggers to a routine, edit at claude.ai/code/routines on the web.

## API Trigger (full example)

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

Response includes a session URL so you can watch the run in real time.

Token is shown ONCE when generated. Store securely. Cannot be retrieved later; only regenerated.

## Cross-Surface Sync

- CLI, Desktop app "New remote task," and web UI all write to the same cloud account
- Routine created in CLI shows up at claude.ai/code/routines immediately
- Desktop shows both local scheduled tasks and routines; "New local task" is a different thing (runs on the machine, not the cloud)

## Requirements

- Pro, Max, Team, or Enterprise plan
- Claude Code on the web enabled
- GitHub connected via `/web-setup` (two-step: grants repo cloning access; GitHub App install separately for webhook delivery)

## Autonomy Rules

- No permission prompts during a run (it's autonomous)
- Runs as a full Claude Code cloud session
- Can run shell commands, use skills committed to the cloned repo, call connectors
- Uses your connected GitHub identity and connectors (commits, PRs, Slack messages appear as you)
- Routines are per-individual-account, not shared with teammates
- Branch pushes default to `claude/`-prefixed only; "Allow unrestricted branch pushes" removes restriction per repo

## Use Cases From The Docs

- Backlog maintenance (nightly triage, label, assign, Slack summary)
- Alert triage (webhook from monitoring, pull stack trace, open draft PR)
- Bespoke code review (GitHub trigger on PR open, apply team checklist)
- Deploy verification (API call from CD pipeline, smoke checks, go/no-go to release channel)
- Docs drift (weekly scan of merged PRs, open docs update PRs)
- Library port (sync changes between parallel SDK repos)

## Usage Limits

- Routines count against subscription usage like interactive sessions
- Daily cap per account on routine runs
- GitHub webhooks have per-routine and per-account hourly caps during preview
- Overage metered for orgs with extra usage enabled

## For Timo Specifically

- `/schedule` skill in Claude Code IS the Routines creation interface
- The schedule skill in his workspace can create email triage, deck-update, and blog-monitoring routines
- Routines persist across sessions, machines, and surfaces (CLI edit syncs to Desktop)
- Good fit for: anything currently running via `/loop` that should survive laptop closing

## Related Memories

- feedback_youtube_url_go_to_transcript.md (how to research Anthropic features accurately)
- feedback_verify_before_done.md (why I got this wrong the first time: asserted without checking docs)

## What NOT To Do (lessons from getting this wrong)

- Do NOT assert a feature's availability on Claude Code without checking https://code.claude.com/docs/
- Do NOT conflate `/schedule` with local Desktop scheduled tasks (different: Desktop local tasks run on the machine, Routines run in cloud)
- Do NOT promise API/GitHub triggers can be created from CLI (they can't, only schedule)
