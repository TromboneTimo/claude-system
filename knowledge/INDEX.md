# Claude Knowledge Base — INDEX

This directory is a persistent research cache for Claude Code sessions across all of Timo's workspaces. Its purpose is to stop re-burning Perplexity tokens on questions that were already answered in a previous session.

## Files

| File | What it is |
|------|------------|
| `INDEX.md` | This file. Explains the system and how to use it. |
| `perplexity_research_database.md` | All past `llm -m sonar-pro` queries and their cached findings, organized by topic. |

## How to use this (MANDATORY for all Claude Code sessions)

### Before running ANY Perplexity query

1. Grep `/Users/air/.claude/knowledge/perplexity_research_database.md` for the topic first.
   ```bash
   grep -i "keyword1\|keyword2" /Users/air/.claude/knowledge/perplexity_research_database.md
   ```
2. If the topic is already covered, use the cached findings. Do NOT re-query.
3. If the cached entry is older than 6 months and the domain moves fast (APIs, pricing, algorithm changes, tool comparisons), you MAY re-query but MUST update the entry afterward.
4. If the topic does NOT exist, run the Perplexity query as usual.

### After running a NEW Perplexity query

Append the new finding to `perplexity_research_database.md` under the correct category. Use the same entry format:

```markdown
### [Query topic]

- **Date:** YYYY-MM-DD
- **Workspace(s):** workspace-name
- **Query count:** 1
- **Tags:** comma, separated, tags

**Key findings:**

[2-4 paragraph summary — NOT the full Perplexity response]

**Sources cited:**

- https://...
```

## Categories

The database is organized under these categories (in order). Pick the closest fit or add a new category if none fit:

- Marketing Frameworks (Laurel Portie, copy frameworks, ad frameworks)
- Dashboard/Analytics Architecture
- Shopify/E-commerce APIs
- Amazon Seller Central APIs
- Attribution & Tracking (Hyros, UTMs, pixels)
- Social Media Tools & Scheduling (Buffer, Later, Metricool, etc.)
- Social Media APIs & Growth (carousel generators, algorithms, platform APIs)
- Presentation Design Best Practices
- Chart/Data Visualization Best Practices
- AI Image Generation (Gemini, NanoBanana, Midjourney)
- Email Marketing (Klaviyo, Beehiiv, deliverability)
- Content Strategy & SEO
- Web Design & Typography (fonts, color palettes, landing pages)
- AI Agents & Self-Improvement (agent frameworks, feedback loops)
- Next.js / Supabase / Tech Stack
- n8n Workflows
- Music Industry / Musicians
- Sales & Psychology (high-ticket, coaching calls)
- Knowledge Base / AI Context (RAG, Claude Projects limits)
- APIs / Integrations General
- Blog & Content Ops
- Miscellaneous

## Why this exists

Timo was burning through Perplexity tokens because every new Claude Code session started from zero knowledge. The same questions kept getting re-queried across different workspaces. This database is the shared memory that prevents that.

## Maintenance

Re-run the extractor anytime to refresh:

```bash
# Extracts all queries + responses from ~/.claude/projects/**/*.jsonl and rebuilds the DB
python3 /tmp/build_db.py   # script lives in /tmp during sessions; copy to a permanent home if needed
```

The extractor:
1. Finds every `.jsonl` session log under `~/.claude/projects/`
2. Pulls every `tool_use` call where the command invokes `llm -m sonar-pro` (or any sonar model)
3. Pairs each query with its `tool_result`
4. Deduplicates near-identical queries (by first 100 chars, case-insensitive)
5. Categorizes by keyword match
6. Writes the markdown DB
