# Audit State Before Prescribing Action

**Canonical protocol for diagnostic hygiene. Applies across all workspaces.**

Companion to verify-before-done (output-side verification). This rule covers input-side: before proposing a fix or remediation workflow, audit the state of the system that contains the reported problem. Do not leap from "problem reported" to "here is the fix."

## The Core Problem

Problems are hypotheses until tested. "The token leaked" is a hypothesis. "Feature X does not exist" is a hypothesis. "System Y is broken" is a hypothesis. Every time Claude treats a hypothesis as fact and builds a remediation workflow around it, there is a significant chance the workflow is solving a problem that does not exist or exists in a different shape.

## When To Run

Mandatory before proposing any of the following:
- Security incident response (credential rotation, access revocation)
- Feature availability claims ("X does not exist in system Y")
- Diagnostic explanations ("the reason Z is broken is...")
- Multi-step remediation workflows
- "Here is how to fix..." instructions with 3+ steps

Basically: if about to give Timo a numbered list for something he reported as broken, stop and audit first.

## The Procedure

### Step 1: Identify the load-bearing assumption
Every reported problem has one or more assumptions. Name them explicitly. Examples:
- "Token leaked" assumes the token is still live
- "Feature missing" assumes the system's current capabilities match mental model
- "Broken" assumes the error is where the user thinks it is

### Step 2: Test each load-bearing assumption with a concrete command
One audit command per assumption. Run them in parallel if independent.

### Step 3: Check alternative success paths
The reported-broken system might be failing silently while a parallel system handles the real load. Check adjacent layers:
- Auth: `gh auth status`, `security dump-keychain`, `.netrc`, SSH keys, configured credential helpers
- Features: official docs, `~/.claude/skills/` list, current session's Skill tool list, `/help`
- DB: replicas, cached state, fallback endpoints
- APIs: circuit breakers, failover, cached responses

### Step 4: Present findings first, solution second
If audit shows the problem is different from reported (or does not exist at all), say so plainly. Do not proceed with the original remediation plan out of momentum.

## Specific Audit Recipes

### Security / leaked credentials

```bash
# Is the leaked credential still live?
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
  -H "Authorization: token <cred>" <api-url>
# 401 means dead. 200 means active. 403 means rate-limited (still active).

# What other auth exists for the same service?
gh auth status
security dump-keychain 2>&1 | grep -iB2 -A4 <service>
cat ~/.netrc 2>/dev/null
ls ~/.ssh/
git config --get-all credential.helper
git config --get remote.origin.url
```

### "Feature does not exist"

```bash
# My own tools / skills (what Claude actually has right now)
ls ~/.claude/skills/ | grep -i <feature>
# Check current session's Skill tool list in the system-reminder

# Official docs
WebFetch code.claude.com/docs/en/<feature>
WebFetch platform.claude.com/docs/en/<feature>
WebFetch docs.anthropic.com/en/<feature>

# Follow redirects if the URL redirects
```

### "X is broken"

```bash
# Run the thing and read the actual error
<command> 2>&1 | head -20
# Exit code matters: 0 means succeeded
# Check logs if applicable
# Check config files the thing reads
# Verify inputs are what you think they are
```

### "Attachment missing" / "File missing"

```bash
# Re-read the user's message front to back
# Check IDE-opened file context in system reminders
# Check for <document> tags
# Check /temp/readonly paths
ls -la <expected_path>
```

## What Audit Is NOT

- Not the same as brainstorming what could be wrong (that is hypothesis generation)
- Not the same as asking the user clarifying questions (ask only if audit is insufficient)
- Not running exhaustive diagnostics on everything (scope to load-bearing assumptions)

## Failure Modes This Prevents

2026-04-15 GitHub token: proposed full rotation workflow before testing if token was still live (it was already HTTP 401 dead). Before checking if gh CLI handled auth (it did, since 2026-04-11). Result: Timo rotated a token he did not need to, generated a new PAT he now must delete.

2026-04-14 Routines: asserted "Routines is a claude.ai feature, not Claude Code" without fetching code.claude.com/docs/en/routines. Wrong. `/schedule` was literally the Routines interface in the available skills list.

2026-04-14 YouTube URL: went to WebFetch first instead of yt-dlp. Had the rule in memory but narrowly scoped it to "quote verification."

2026-04-14 Skill attachment: treated "I do not see it in my rendering" as "therefore nothing is attached" without re-reading the user's message or checking document tags.

All four share the epistemic failure: treating "what I believe about the state" as equivalent to "what the state actually is."

## Relationship To Other Meta-Rules

- `verify-before-done.md`: output-side verification (before declaring complete, test the claim)
- `audit-state-before-prescribing.md`: input-side verification (before proposing a fix, audit the state)
- `reviewer-pass-protocol.md`: fresh-eyes verification (after compaction, diff for losses)
- `gates-come-from-fuckups.md`: meta about where gates originate

These four together cover the full verification lifecycle: input, action, output, review.

## Enforcement

- Global CLAUDE.md AUDIT GATE (fires on every conversation)
- Workspace feedback: `memory/feedback_audit_state_before_prescribing.md`
- Escalation target: if this rule keeps failing, consider extending fix-brain to audit the audit pattern (ironic but valid)

## The Meta-Principle

Diagnostic haste is more expensive than a 30-second audit. Every incident where Claude leapt to prescription created either (a) wasted work for Timo, (b) friction with Timo, or (c) both. Thirty seconds of audit prevents either outcome. The ROI is never negative.
