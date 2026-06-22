# Research Database. Cross-workspace cache for Perplexity + NotebookLM

This directory is Timo's persistent research cache across all Claude Code sessions and workspaces. Every Perplexity query and every NotebookLM synthesis lives here. Stops re-burning credits on questions already answered.

## MANDATORY: Cache check before ANY research query

**This rule is enforced by the CACHE GATE in `~/.claude/CLAUDE.md` and by the cache-check hook on Bash.**

Before running ANY of these:
- `llm -m sonar*`, `llm -m r1-1776`
- `perplexity-*` MCP calls
- New NotebookLM notebook creation on a topic that may already be covered

You MUST first run:

```
/research check "<topic keywords>"
```

If a cached entry covers the topic AND it's not stale (see "Staleness rules" below), USE THE CACHE. Burning credits on a covered topic is an explicit failure.

## Staleness rules

| Domain | Stale after |
|---|---|
| API specs, pricing, tool comparisons, AI model versions | 6 months |
| Marketing frameworks, copywriting principles, psychology | 24 months (essentially evergreen) |
| Algorithm changes (TikTok, Instagram, YouTube) | 3 months |
| Anthropic / OpenAI / Google AI feature releases | 3 months |
| General how-to and definitions | 24 months |

Stale + covered = OK to re-query, but you MUST update the cached entry afterward (do not create a duplicate).

## Directory layout (mirrors coaching-db)

```
~/.claude/research/
├── INDEX.md                                       # This file. Boot-loaded.
├── perplexity/
│   ├── raw/                                       # IMMUTABLE per-query files
│   │   ├── 2026-04-27_claude-code-subagent-context_a3f2.md
│   │   └── ...
│   ├── index/
│   │   ├── _all.jsonl                             # Source of truth. Grep this.
│   │   ├── by-category/                           # Auto-generated views
│   │   └── by-tag/                                # Auto-generated views
│   └── legacy/
│       └── perplexity_research_database.md        # Pre-migration monolith. Read-only.
├── notebooklm/
│   ├── raw/                                       # NotebookLM syntheses
│   └── index/_all.jsonl
└── scripts/
    ├── migrate.py                                 # One-time migration of legacy DB
    ├── rebuild.py                                 # Re-extract from session logs
    ├── check.py                                   # Cache check (used by /research check)
    └── save.py                                    # Append new query to DB
```

## Per-entry schema (raw/*.md frontmatter)

```yaml
---
query: "exact query text"
query_hash: "sha256 first 16 chars"
slug: "claude-code-subagent-context"
model: "sonar-pro"
date: "2026-04-27"
workspaces: ["Precision-Brass","Robinsons-Remedies"]
category: "AI Agents & Self-Improvement"
tags: ["anthropic","subagents","context-isolation"]
citations_count: 8
synthesized_in_notebooklm: false
stale_after: "2026-10-27"
---
```

## _all.jsonl line format

One line per cached entry, append-only:

```json
{"hash":"a3f2...","slug":"...","date":"2026-04-27","category":"...","tags":[...],"workspaces":[...],"file":"raw/2026-04-27_..._a3f2.md","stale_after":"2026-10-27"}
```

Grep this file to find cached entries quickly.

## Categories (canonical order)

Match each entry to one of these. If none fits, use "Miscellaneous" and consider adding a new category.

- Marketing Frameworks
- Dashboard/Analytics Architecture
- Shopify/E-commerce APIs
- Amazon Seller Central APIs
- Attribution & Tracking
- Social Media Tools & Scheduling
- Social Media APIs & Growth
- Presentation Design Best Practices
- Chart/Data Visualization Best Practices
- AI Image Generation
- Email Marketing
- Content Strategy & SEO
- Web Design & Typography
- AI Agents & Self-Improvement
- Next.js / Supabase / Tech Stack
- n8n Workflows
- Music Industry / Musicians
- Sales & Psychology
- Knowledge Base / AI Context
- APIs / Integrations General
- Blog & Content Ops
- Claude Code Architecture
- Miscellaneous

## How to use this DB (workflow)

### Path 1: User asks a research question

1. Run `/research check "<keywords>"`. Returns cached file paths + 1-line summaries.
2. Cache hit + not stale → answer from cache. Do NOT call Perplexity.
3. Cache hit + stale → call Perplexity, update existing entry.
4. Cache miss → call Perplexity via `/research query`, save to raw/, update index.

### Path 2: I'm about to edit a skill or make an architectural decision

Per CACHE GATE in CLAUDE.md, before architecturally significant edits:

1. Run `/research check "<topic of the decision>"`.
2. Use any prior research that informs the decision.
3. If insufficient cached evidence, run `/research query` with focused questions BEFORE editing.

### Path 3: User says "use the research" or "check the database"

Auto-fire `/research check` with their topic keywords. Return cached findings before answering anything else.

## Maintenance

```bash
# Re-extract from all session logs (captures any queries that bypassed /research query)
python3 ~/.claude/research/scripts/rebuild.py

# Migrate legacy monolith (one-time)
python3 ~/.claude/research/scripts/migrate.py

# List stale entries
python3 ~/.claude/research/scripts/check.py --stale
```

## Why this exists

Timo was burning Perplexity credits on questions already answered in prior sessions across other workspaces. Today (2026-04-27) I burned 5 fresh queries on Claude Code subagent architecture and Eugene Schwartz frameworks that were probably already in the legacy monolith. This DB + the CACHE GATE makes that impossible going forward.
