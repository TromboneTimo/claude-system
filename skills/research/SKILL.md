---
name: research
description: >
  Cross-workspace Perplexity + NotebookLM research cache. Cache-first protocol
  prevents burning credits on questions already answered. Multi-axis ranked
  search across 312+ entries spanning all of Timo's workspaces. Subcommands:
  check (search cache), query (cache-first Perplexity call with auto-save),
  mine (re-search existing corpus through new lens), synthesize (NotebookLM
  on selected entries), stale (list aging entries needing refresh), rebuild
  (re-extract from session logs), stats. ALWAYS use /research check before
  any llm -m sonar* call. Use when user says "check the research", "what do
  we know about", "is this in the database", "use the research", "look it up
  first", "we already researched this", "/research", or invokes any subcommand.
license: MIT
user-invocable: true
argument-hint: "[check|query|mine|synthesize|stale|rebuild|stats] [topic-or-args]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
---

# Research Cache Skill

The cross-workspace Perplexity + NotebookLM research cache lives at `~/.claude/research/`. This skill is the only way to query Perplexity that respects the cache-first protocol.

## HARD RULE: Cache-first or fail

Before ANY `llm -m sonar*` call (or equivalent Perplexity MCP), run `/research check "<topic>"` first. Cache hit + not stale, use cached. Cache miss, use `/research query` (which auto-saves). Bypassing this burns credits and violates the CACHE GATE in `~/.claude/CLAUDE.md`.

## Subcommand routing

| Subcommand | Action |
|---|---|
| `check <topic>` | Multi-axis search of `~/.claude/research/perplexity/index/_all.jsonl`. Ranks by tags, keywords, category, query, slug. Returns top 10 matches with file paths + dates + stale flags. ZERO tokens. |
| `query "<text>" [--model sonar-pro] [--category C] [--tags a,b]` | Cache-first wrapper around `llm`. Greps cache. Hit returns cached. Miss runs `llm -m <model> "<text>"`, saves to raw/, appends to index, prompts for NotebookLM synthesis. |
| `mine <angle>` | Re-search existing raw/ corpus through a new lens. No new Perplexity calls. Returns relevant cached entries reframed under the new angle. |
| `synthesize <hash> [<hash>...]` | Pipe selected raw entries into NotebookLM, save synthesis to `notebooklm/raw/`, mark source entries `synthesized_in_notebooklm: true`. |
| `stale` | List entries past their `stale_after` date. Suggest refresh queries. |
| `rebuild` | Re-extract from `~/.claude/projects/**/*.jsonl` session logs. Captures any queries that escaped the wrapper. |
| `stats` | DB size, entries by category/workspace, top tags, oldest entries, hit rate (if logged). |

## Workflow examples

### When user asks a research question

```
User: "Is there research on Schwartz awareness levels for trumpet coaching ads?"
Action: run /research check "schwartz awareness levels trumpet coaching"
Result: 2 cache hits, both fresh. Read top match. Answer from cache.
```

### When I'm about to edit a skill or make an architectural decision

Per CACHE GATE: before architecturally significant edits, /research check first.

```
About to redesign pb-script agent fanout.
Action: run /research check "multi-agent claude code subagent architecture"
Result: 4 cache hits. Read them. Use prior findings. Skip redundant research.
```

### When user explicitly says "use the research"

```
User: "use the research to figure this out"
Action: auto-fire /research check with their topic keywords first.
Result: Present cached findings before answering.
```

### When cache miss

```
/research check returns NO CACHE.
Action: "No cache for this. Running fresh query."
Then: /research query "<text>" --category "..." --tags ...
Saves new entry. Prompts NotebookLM synthesis.
```

## Implementation

All subcommands are thin wrappers around scripts in `~/.claude/research/scripts/`:

- `check.py` for multi-axis ranked search
- `save.py` for save with cache check (used by `query`)
- `migrate.py` for one-time migration of legacy DB
- `_lib.py` for shared helpers (slugify, hash, keyword extraction, stale calc)

For `query`, the routing is:

```bash
# Pseudo:
HIT=$(python3 ~/.claude/research/scripts/check.py "<text>" --json)
if cache hit and not stale:
    print cached file
else:
    RESULT=$(llm -m sonar-pro "<text>")
    python3 ~/.claude/research/scripts/save.py --query "<text>" --result "$RESULT" --category C --tags ...
```

## Hard rules

1. **NEVER call `llm -m sonar*` directly.** Always go through `/research query`. The hook at `~/.claude/hooks/cache-check-perplexity.sh` will block direct calls.

2. **NEVER skip NotebookLM synthesis** on substantive research findings. After `/research query` completes a cache miss, prompt: "Run `/research synthesize <hash>` for NotebookLM synthesis?"

3. **Categorize and tag at save time.** Saving an entry with `category: Miscellaneous` and no tags makes it harder to find later. Always pick from canonical 22 categories (see `~/.claude/research/INDEX.md`) and add 3 to 5 tags.

4. **Stale entries**: cache hit + past `stale_after` means re-query AND update existing entry. Do not create a duplicate.

5. **Cross-workspace dedup**: the same query from a different workspace = same entry. The `workspaces` array tracks where it was used.

## Reference files

- `references/categories.md` for canonical 22-category list
- `references/staleness.md` for staleness rules per domain
- `references/tag-conventions.md` for naming conventions for tags
- `~/.claude/research/INDEX.md` for full DB protocol (boot-loaded)

## What this skill is NOT

- Not a replacement for `perplexity-web-research`. It WRAPS perplexity-web-research with cache-first.
- Not a replacement for `notebooklm`. It ROUTES synthesis through notebooklm.
- Not a search engine. It searches Timo's prior research, not the live web.
- Not a way to bypass paying for Perplexity when the cache misses. Cache miss means fresh query is correct.