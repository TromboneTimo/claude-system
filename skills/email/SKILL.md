---
name: email
description: DEPRECATED 2026-06-10. Do NOT use for drafting Precision Brass emails. The legacy /email Precision Brass Email System is retired; its data files (voice-bank.md, voice-spec.md, harrison-real-voice.md, the precision-brass-emails project) are deleted and it predates every modern gate. Use /pb-email (idea batch) and /pb-email-write (single approved idea to full draft) instead. Unique legacy rules (anti-hallucination protocol, prospect-vs-student name rosters, Richard-email conversion lessons 7a-7g) are preserved at ~/.claude/skills/pb-email/references/legacy-anti-hallucination-rules.md.
---

# /email - DEPRECATED (2026-06-10)

This skill is retired. If invoked, do the following and NOTHING else:

1. Tell the user immediately: "/email is deprecated as of 2026-06-10. It referenced data files that no longer exist and bypassed the modern email gates (voice load order, draft gate, rhythm/lint gates, batch diversity, auditor)."
2. Offer the replacements: `/pb-email` for a fresh 5-draft idea batch, `/pb-email-write <id>` to expand an approved idea into a full proposal. Ask which one they want.
3. Do NOT draft any email content from this skill's instructions.

Preserved content: the unique anti-hallucination rules, prospect-vs-student name lists, and the Richard-email conversion lessons (7a-7g) were ported verbatim to:
`~/.claude/skills/pb-email/references/legacy-anti-hallucination-rules.md`

The full original 286-line SKILL.md is recoverable via git history in `~/.claude` (this file's prior revision).
