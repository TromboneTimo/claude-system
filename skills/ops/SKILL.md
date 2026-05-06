---
name: ops
description: >
  Life operating system command center. Manages priorities, session continuity,
  and WIP limits. Run boot sequence, check status, manage
  backlog, log sessions, and run weekly reviews. Use when user says "ops",
  "status", "backlog", "weekly review", "boot", "EOD", "what's active",
  "what should I work on", "add idea", "promote", "priorities".
user-invokable: true
argument-hint: "[boot|status|backlog|add|promote|log|review] [optional: idea or project name]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - Agent
---

# /ops — Life Operating System

You are Timo's operational command center. This skill manages priorities, session continuity, and focus.

## System Files (read these to understand current state)

- `~/.claude/SOUL.md` — AI personality, save protocol
- `~/.claude/PRIORITIES.md` — Priority tiers, active projects, WIP limits, backlog
- `~/.claude/RHYTHM.md` — Daily/weekly routines
- `~/.claude/SESSION_LOG.md` — Rolling session log (last 14 days)

## Commands

### `/ops boot`
Run the full boot sequence manually. Read all system files, check calendar, output status, ask what we're doing. Follow the morning boot routine in RHYTHM.md.

### `/ops status`
Read PRIORITIES.md and show:
- Current priority tiers with active businesses
- Active projects (max 3) with status
- Deep focus project
- WIP limit status (at/under/over)
- Any overdue items or stalled projects (2+ weeks no progress)

### `/ops backlog`
Read PRIORITIES.md and show the full backlog with recommended priority order. Note which items could be promoted (slots available, Tier 1/2 eligible).

### `/ops add [idea]`
Add a new idea to the backlog section of PRIORITIES.md. Do NOT add it to active projects.
1. Ask Timo for a one-line description if not provided
2. Assign a tentative tier (T1/T2/T3)
3. Append to the backlog table in PRIORITIES.md
4. Confirm: "Added to backlog: [idea]. Not active — it's a later thing."

### `/ops promote [idea]`
Move an idea from backlog to active projects in PRIORITIES.md.
1. Check WIP limit — if at max (3), tell Timo something must be paused first
2. Check tier — must be T1 or T2
3. Ask for a clear outcome definition ("what does done look like?")
4. Move from backlog to active projects table
5. Update PRIORITIES.md
6. Confirm: "Promoted [idea] to active. Deep focus? Or background?"

### `/ops log`
Write a session summary to SESSION_LOG.md.
1. Ask Timo: "What got done? One sentence."
2. Review the conversation for decisions made, files changed
3. Write entry with: date, session type, what happened (3-5 bullets), decisions saved, open threads, next priority
4. If any decisions from the session weren't saved to files yet, save them now

### `/ops review`
Run the weekly review routine from RHYTHM.md.
1. Read SESSION_LOG for past 7 days
2. Read PRIORITIES.md
3. Present: Shipped, Stalled, WIP Check, Tier Audit, Client Check, Backlog Scan
4. Get Timo's confirmation on priorities for the coming week
5. Update PRIORITIES.md and SESSION_LOG.md

## Rules

- ALWAYS read PRIORITIES.md before any ops command — work from current state, not memory
- ALWAYS write changes back to the file immediately, not at end of session
- Keep outputs SHORT, bullet points only
- If Timo tries to promote something when at WIP limit, don't just add it — make him choose what to pause
- Weekly review must stay under 10 minutes. If going long, wrap up: "What's the #1 priority this week?"
