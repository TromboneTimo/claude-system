---
name: link-law-enforcement-stack
description: "3-layer machine enforcement of email link rules: JIT injection (email-angle-gate.sh), PreToolUse interceptor (email-link-gate.sh), DB trigger (PENDING Timo approval). Docs advise, gates enforce."
metadata: 
  node_type: memory
  type: project
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

2026-06-11. Built after [[wrong-cta-destination-five-guards]]: a rule existed in memory and was still violated 5 times, because memory files are advisory. Timo: "There has to be an undeniable way." Research (cache `2026-06-11_llm-agents-ignoring-written-rules_1ccd6f6f`, LangChain State of Agent Engineering + CSA + arxiv 2605.24309): context-only policies are probabilistic (lost-in-the-middle, recency bias, instruction dilution); guarantees come only from machine gates at tool and data boundaries. Principle: **agent-readable docs are advisory; machine-enforced gates are mandatory.**

**Layer 1 -- just-in-time injection (LIVE):** `~/.claude/hooks/email-angle-gate.sh` now appends a LINK LAW block to every email-work prompt. It reads `CANONICAL_MASTERCLASS_URL` from dashboard/lib/email-lint.js AT FIRE TIME (cannot drift from the enforced truth). Tested: fires with cwd=Precision-Brass, URL present.

**Layer 2 -- tool-boundary interceptor (LIVE):** `~/.claude/hooks/email-link-gate.sh`, registered PreToolUse(Bash) in settings.json. Blocks WRITE commands (POST/PATCH/PUT/--data) touching email_proposals / AC messages / ac-send whose command or @payload-files contain: webinar-registration-pb, a non-canonical training-room variant, or a YouTube link. Read-only commands untouched. Tested on 6 scenarios + 1 live production firing (it blocked my own trigger-install SQL because the SQL quoted the banned string). Inline bypass token `PB_LINK_GATE=skip` in the command text (hooks don't see exported env vars from inside the command), Timo's say-so required.

**Layer 3 -- DB trigger (NOT INSTALLED, needs Timo's explicit approval):** BEFORE INSERT OR UPDATE trigger `trg_email_proposals_link_guard` on email_proposals raising on capture-page or YouTube links in body/cta_url. SQL is ready in SESSION_LOG context; install via Supabase Management API (PAT). The auto-mode classifier denied unsanctioned prod schema migration. This is the only layer that survives a fresh session with zero hooks and zero memory.

Layer 0 (advisory, also done): lint blocks + skills + [[project-canonical-links]] registry mirror.

**2026-06-11 audit hardening (full enforced-vs-advisory audit by agent):** real-list guard on BOTH transports (MCP send gate blocks list!=20 hard, no bypass; Bash gate blocks AC API campaign calls with p[!=20]); LINK LAW + placeholder scan now fire on MCP html_body too (transport parity); AC campaign DELETE requires literal AC_DELETE_OK= token in command; lint adds ps-text-must-be-empty (block), body-needs-cta-anchor (warn), subject-names-student (warn). Known bypass surfaces (documented, accepted): node/python scripted writes don't match the curl-shaped command scan; PB_LINK_GATE=skip token needs Timo say-so. BACKLOG: B4 scheduled-message drift reconciler, B7 credential-save read-back, B8/B9 verify scripts, Layer-3 DB trigger awaiting Timo approval. Playbook: ~/.claude/knowledge/enforcement-first-architecture.md.

**RECALL INFRASTRUCTURE (2026-06-11, model-independence build):** `~/.claude/hooks/rules-router.sh` + `rules-router.json` = declarative intent->route+rules injection on EVERY prompt, all workspaces (10 entries: email draft/push, deploy, dashboard, classifier, script-write, research, compaction, proposals, new-gate). `router-coverage-check.py` = lessons-without-gates ratchet (first run: 178/271 uncovered), MANDATORY in /weekly-review + /fix-brain. `credential-readback.sh` (Stop) = read-back for the inject-only credential gate. New lesson protocol: write the gate/router entry FIRST, memory file last. Playbook: knowledge/enforcement-first-architecture.md.

**Maintenance:** URL rotation = update CANONICAL_MASTERCLASS_URL in email-lint.js + project_canonical_links.md together; layers 1-2 pick it up automatically (they read the registry live). The DB trigger only enforces the unambiguous bans (capture page, YouTube), not the exact URL, so rotation never needs DDL.
