---
name: weekly-review
description: "Cross-workspace intelligence review. Reads all feedback files across all projects, identifies universal patterns, propagates lessons globally, checks PRIORITIES.md staleness, updates Last Touched dates, and reports WIP limit status. Use when user says 'weekly review', 'review', or 'what needs attention'."
user_invocable: true
---

# Weekly Review Skill

You are the cross-workspace intelligence agent. Your job is to make the entire Claude Code system smarter by propagating lessons, detecting staleness, and keeping the operating system current.

## When to Run
- User says `/weekly-review` or `review` or `what needs attention`
- Scheduled weekly via `/schedule` (Sunday evening JST)
- After any major project milestone

## The Review Process

### Step 1: Scan All Workspaces
Read MEMORY.md from every workspace:
- `~/.claude/projects/-Users-air-Desktop-Robinsons-Remedies/memory/MEMORY.md`
- `~/.claude/projects/-Users-air-Desktop-*/memory/MEMORY.md` (find all)

For each workspace, list:
- Number of feedback files
- Date of most recent feedback file (staleness check)
- Any new feedback files since last review

### Step 2: Cross-Pollinate Feedback
Read ALL `feedback_*.md` files across ALL workspaces. Identify rules that should be universal:
- If a rule exists in 2+ workspaces, it should be in `~/.claude/CLAUDE.md`
- If a rule exists in only 1 workspace but applies broadly, propose adding it globally
- Flag any conflicting rules between workspaces

Output a "Propagation Report":
```
UNIVERSAL RULES (should be in CLAUDE.md):
- No em dashes: EXISTS in Robinson's, App Builder. MISSING from: N8N, Script Bot
- Try before saying no: EXISTS in N8N. SHOULD ADD to: all workspaces

CONFLICTS:
- Robinson's says 750-1250 words. Blog SOP says 1500-2500. Resolution: user override wins.
```

### Step 3: PRIORITIES.md Health Check
Read `~/.claude/PRIORITIES.md`. For each project listed:
- Check file modification dates in the project directory
- Calculate days since last activity
- Flag: 7+ days = "getting stale", 14+ days = "consider pausing", 30+ days = "archive candidate"
- Verify WIP limit (max 3 active) is respected
- Update "Last Touched" dates based on actual file activity

### Step 4: SESSION_LOG.md Review
Read `~/.claude/SESSION_LOG.md`. Check:
- Is it being updated? (look for entries in last 7 days)
- Are there open threads that haven't been addressed?
- Any decisions that need follow-up?

### Step 5: Skill Health Check
For each skill with an eval/ directory:
- Check if eval/improvement-log.md exists
- If so, what's the latest score?
- Flag skills that haven't been tested in 14+ days
- List skills without eval files that should have them

### Step 6: Content Performance Check (Robinson's only)
- Read `references/top-content/best-performing-posts.md`
- Count entries. Flag if under 10 (should be 20+)
- Read `feedback/deliverables-log.md`
- Count entries. Flag if empty or sparse.

### Step 7: Generate Report

Output format:
```
# Weekly Review - [Date]

## Workspace Activity
| Workspace | Last Active | Feedback Files | Status |
|-----------|------------|----------------|--------|

## Cross-Workspace Lessons
[New universal rules to propagate]

## PRIORITIES Health
| Project | Tier | Last Touched | Status |
|---------|------|-------------|--------|

## Skill Scores
| Skill | Last Eval | Score | Needs Attention |
|-------|----------|-------|-----------------|

## Open Threads
[From SESSION_LOG]

## Action Items
1. [Most important thing to do this week]
2. ...
```

### Step 8: Auto-Apply
After generating the report:
- Update PRIORITIES.md "Last Touched" dates automatically
- Add any missing universal rules to CLAUDE.md
- Create missing feedback files in workspaces where rules should exist
- DO NOT ask permission for these updates (they're pre-approved in settings.json)

## Output
Save the report to `~/.claude/weekly-reviews/[date].md`
