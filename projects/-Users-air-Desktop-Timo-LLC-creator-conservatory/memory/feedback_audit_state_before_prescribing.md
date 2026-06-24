---
name: Audit Current State Before Prescribing Action
description: CRITICAL. Before proposing a fix or workflow for a reported problem, audit the actual state. Test the assumption that defines the problem. For security incidents, verify the credential is still live. For missing features, check docs AND available tools. For auth issues, check ALL auth paths, not just the obvious one. Do not leap from "problem" to "fix."
type: feedback
originSessionId: 2026-04-15T00:39:17Z
---
# Audit State Before Prescribing Action

**Rule:** When Timo reports a problem or something appears broken, the FIRST step is auditing the current state of the system that contains the problem. Not proposing a fix. Not writing step-by-step instructions. Verify the problem exists in the shape assumed, and verify the system isn't already healthy in ways that weren't obvious. Only after state is mapped do you propose action.

**Why:** On 2026-04-14/15, I found Timo's GitHub PAT leaked in his `~/.claude/.git/config` and printed in terminal output. I immediately built a rotation workflow: strip token from config, set osxkeychain helper, delete cached cred, step-by-step instructions for pasting new token. Timo rotated, generated a new classic PAT, worried about fine-grained vs classic, asked where to paste it so I wouldn't see it. At the very end of the thread, when I finally tested with `curl -I -H "Authorization: token <leaked>"`, GitHub returned HTTP 401: the token had already been auto-revoked by GitHub's secret scanner the moment the conversation transcript hit their logs. Additionally, `gh auth status` showed he had a perfectly functional gh-CLI OAuth token in keychain since 2026-04-11. The entire rotation workflow was busywork. Everything was already fine. All because step 0 was "propose fix" instead of "audit state."

**How to apply (mandatory before any remediation workflow):**

1. **Test the assumption that defines the problem.** If the report is "credential X leaked," test whether credential X still works. If "feature Y doesn't exist," fetch docs AND check available tools/skills. If "system Z is broken," run its healthcheck.

2. **Check alternative success paths.** The reported-broken system might be failing silently while a parallel system handles the real load. Auth: check `gh auth status`, `security dump-keychain | grep <service>`, `.netrc`, SSH keys, and configured credential helpers. Features: check docs, check `/help`, check available tools, check installed skills. DB: check replicas, cached state, fallback endpoints.

3. **Map the state in one shot.** Don't audit one dimension, propose a fix, then re-audit when it doesn't match. Spend the 30 seconds running ALL the relevant diagnostic commands in parallel BEFORE writing anything about remediation.

4. **Present findings first, solution second.** If the audit shows the problem is different from reported (or doesn't exist at all), say so plainly. Do not proceed with the original remediation plan out of momentum.

**Where this applies:**
- Security incidents (leaked credentials, compromised accounts)
- "X is broken" reports (what does "broken" mean? test it)
- "X doesn't exist" assertions (mine AND the user's)
- Any error message or failure mode Timo describes
- Pre-flight for any multi-step workflow I'm about to propose

**The deeper failure pattern this prevents:**
Leaping from diagnosis to prescription. The verify-before-done rule covers output (before declaring complete, test the claim). This rule covers input (before declaring a fix plan, test the assumption). Same epistemic failure, different phase. Same symptom: confident-wrong claims that turn into wasted work.

**Specific audit recipes:**

*Security/credentials:*
```bash
# Is the leaked credential still live?
curl -s -o /dev/null -w "HTTP %{http_code}\n" -H "Authorization: token <cred>" <api-url>
# What other auth exists?
gh auth status
security dump-keychain | grep -iB2 -A4 <service>
cat ~/.netrc 2>/dev/null
ls ~/.ssh/
git config --get-all credential.helper
```

*"Feature doesn't exist":*
```bash
# My own tools / skills
ls ~/.claude/skills/ | grep -i <feature>
# Docs
WebFetch code.claude.com/docs/en/<feature> platform.claude.com/docs/en/<feature>
# Currently available skills list
# (check system-reminder for available Skill tool list)
```

*"X is broken":*
```bash
# Run the thing and read the actual error
<command> 2>&1 | head -20
# Check logs if applicable
# Check config file the thing reads
```

**Related memories:**
- feedback_verify_before_done.md (parent rule: verify before output claims)
- feedback_read_before_asking.md (read context from disk before asking)
- feedback_youtube_url_go_to_transcript.md (same pattern: specific tool goes first)
- feedback_audit_scope_must_match_usage.md (same pattern: enumerate before acting)

**The meta-principle:**
Problems are hypotheses until tested. "The token leaked" is a hypothesis worth testing before building a rotation workflow. "Routines isn't in Claude Code" is a hypothesis worth testing before arguing with the user. "X is broken" is a hypothesis worth testing before diagnosing. Every time I treat a hypothesis as fact and leap to fix, I create busywork or fight with Timo about things he's right about.
