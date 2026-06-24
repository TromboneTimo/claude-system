---
name: ADHD Tracker Only Works With Forcing Functions
description: Instructions in CLAUDE.md or session-start hooks do not reliably trigger ADHD guardrails. Only per-prompt forced injection works. STATUS 2026-04-13 evening: Timo uninstalled the hook injections — broken time tracking fired false alerts. Do NOT reinstall without an active-engagement clock.
type: feedback
originSessionId: 0f13d961-3a73-4ac3-9187-7ac166a626a7
---

**2026-04-13 evening UPDATE: Hook uninstalled.** Timo removed the ADHD fail-safe injections from `~/.claude/hooks/auto-research-marketing.sh`. Root cause of removal: elapsed-time counter used wall-clock from session start (not active engagement), so alerts fired based on idle time and felt punitive. Backup of prior version at `~/.claude/hooks/auto-research-marketing.sh.bak-2026-04-13-adhd-removal`. Preserved in current hook: prompt counter, research pipeline reminder, Robinson's orchestrator routing. DO NOT reinstall the fail-safe logic without fixing the time-tracking root cause first (needs a signal based on active prompt engagement, not wall-clock from session start).

**2026-04-15 UPDATE: Hook REINSTATED with active-engagement time, JST awareness, and topic-shift detection.** Root cause of 2026-04-13 wall-clock bug addressed by implementing GA4-style engagement time measurement: per-prompt timestamps, sum inter-prompt gaps, filter gaps over 300 seconds as idle breaks. Ref: Perplexity 2026-04-15 (krmdigital.uk/session-duration-engagement-time, louder.com.au/ga-time-metrics). Smoke-tested 4 edge cases: daily reset discrimination, mid-day banner, topic shift detection, gap over 300s filters correctly. New state files: `~/.claude/.engagement_state` (last_ts + cum_seconds), `~/.claude/.engagement_state_date` (JST rollover tracker), `~/.claude/.daily_reset_jst` (manual flag set after reset completes). Prose guardrails in `session-boot.sh` removed (were failing by attention collapse per feedback_enforcement_mechanism_choice.md). Full design memo: NotebookLM notebook 539d2340-3f10-4220-b533-b1640edae051.

Instruction-based ADHD guardrails (rules in SOUL.md, injected at session start) FAIL reliably. Mechanism: attention collapse — rules load at session start, by prompt 10 they're 20k tokens buried, attention weights favor current task, no internal counter or clock runs between turns.

**Why:** Timo has tried "dozens of times" to get ADHD_Tracker working via CLAUDE.md rules and session-boot injection. It keeps failing. Root cause is architectural, not willpower. Models don't self-police once attention is on a task. "Helpful-completion" training actively pulls against interrupting.

**How to apply:**
- The only reliable enforcement is forced `<system-reminder>` injection at thresholds via UserPromptSubmit hook (runs every prompt, always in immediate context).
- Per-prompt context injection beats session-start injection every time.
- Thresholds to inject at: prompt 15, 30; session minutes 45, 90, 120; 3+ topic shifts.
- Do NOT promise better self-discipline. Promise a hook upgrade instead.

**Also noted 2026-04-13:** The existing `~/.claude/hooks/auto-research-marketing.sh` appears broken — `PROMPT COUNT` injects as `1` on every prompt regardless of actual count. Fix this before any ADHD hook upgrade will work.

**What I CAN do within a session without new code:**
- Read the `PROMPT COUNT` number from the UserPromptSubmit system reminder at top of each message.
- Bash-check `~/.claude/.session_meta` (line 2 = session start ISO timestamp) to compute elapsed minutes.
- Use TodoWrite the moment a 2nd topic surfaces.
- Self-interrupt when 3+ paragraphs pass without scope check.
- These compensate partially but do not replace a working hook.
