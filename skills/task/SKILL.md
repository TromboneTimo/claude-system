---
name: task
description: Task state CLI. Add, complete, park, block, list, and view today's tasks. Source of truth for the task dashboard. Use when user types /task, asks to add/complete/block a task, or asks what's on deck today. Also use silently to log state changes you infer from conversation (e.g., user says "sent the pitch" and you've confirmed the task they mean).
---

# /task

Unified CLI for the task state layer backing the task dashboard at `~/.claude/dashboard/index.html`.

**All commands run:** `python3 ~/.claude/skills/task/task.py <subcommand> [args]`

## Subcommands

### add
```
/task add "<title>" [--deadline YYYY-MM-DD] [--tier T1|T2|T3] [--project <name>] [--est 30] [--start 14] [--tags a,b]
```
Creates a task. `--start HH` (JST hour 0-23) is what puts it on today's timeline. Without `--start` it lives in side panels only.

### done
```
/task done <id-or-partial-title> [--shipped "one-line note"]
```
Marks complete. Query can be the task id (slug) or a substring of the title. The `--shipped` note appears in the "SHIPPED TODAY" dopamine panel.

### park
```
/task park <id-or-partial-title>
```
Removes from today view, keeps in backlog. For "I don't want to look at this right now."

### block
```
/task block <id-or-partial-title> --on "waiting on Betty for design direction"
```
Marks blocked. Moves to the BLOCKED panel with the waiting-on note.

### start (v2 surface, available now)
```
/task start <id-or-partial-title>
```
Marks started. Highlights the block on the timeline. v2 will add 25-min Pomodoro overlay.

### list
```
/task list [--status active|blocked|parked|completed]
```
Text dump of tasks filtered by status.

### today
```
/task today
```
Quick text summary of today (same data the dashboard renders): timeboxed tasks, deadlines under 72h, blocked, shipped today.

## Operational notes

- Writes are **append-only** to `~/.claude/state/tasks.jsonl`.
- After every mutation the CLI runs `~/.claude/state/derive.py` which rebuilds `tasks.json` and `tasks.js` (the dashboard's data files).
- The dashboard auto-polls every 60s; if Timo has it open, his change appears within a minute.
- Never mutate `tasks.json` directly. Only append to `tasks.jsonl`.
- Never clobber `PRIORITIES.md` from this skill. PRIORITIES.md stays human-authored.

## When to invoke this skill silently (no explicit /task)

You should run `/task done` on Timo's behalf when:
1. He confirms a task is finished in conversation ("sent the pitch", "shipped it", "done with X")
2. You have already verified the task id (don't guess, use `/task list` first if unsure)
3. He has not disputed the inference in the same turn

You should NOT auto-add tasks. Timo adds tasks explicitly. Auto-adding creates noise.

When topic-shift confirmation fires (via the UserPromptSubmit hook), ASK before marking done: "Mark [task] done before moving to [new topic]?"

## Open the dashboard

```
open ~/.claude/dashboard/index.html
```
Opens in default browser. Pin a tab and leave it open as a body-double.
