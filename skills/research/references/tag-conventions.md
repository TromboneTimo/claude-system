# Tag Conventions

Tags are the primary findability axis after category. Add 3-5 tags per entry. Be consistent or grep misses.

## Format

- All lowercase
- Hyphens for multi-word tags: `claude-code` not `claude_code` not `claudeCode`
- No leading underscores
- No spaces

## Required tags by category

| Category | Always include |
|---|---|
| Marketing Frameworks | author/source name (e.g., `schwartz`, `halbert`, `portie`) |
| Claude Code Architecture | `claude-code` |
| AI Agents & Self-Improvement | `multi-agent` if relevant + framework name (e.g., `crewai`, `autogen`) |
| Social Media APIs & Growth | platform name (`instagram`, `tiktok`, `youtube`) |
| Email Marketing | platform name (`klaviyo`, `beehiiv`) |
| Music Industry / Musicians | instrument (`trumpet`, `trombone`) |

## Common tag families (use these names, don't reinvent)

- `anthropic`, `openai`, `google-ai` (AI providers)
- `subagents`, `hooks`, `skills`, `mcp` (Claude Code primitives)
- `api`, `webhook`, `oauth` (integration concepts)
- `copywriting`, `awareness-levels`, `frameworks` (marketing)
- `landing-page`, `vsl`, `funnel` (conversion)
- `schwartz`, `halbert`, `portie`, `brunson` (named frameworks)

## Bad tag examples

- `Claude Code` (has space + capitals)
- `_internal` (leading underscore)
- `temp` (meaningless)
- `important` (subjective, never findable)
- `2026` (date already in entry's `date` field)

## When in doubt

Look at existing tags: `cat ~/.claude/research/perplexity/index/_all.jsonl | python3 -c "import json,sys; from collections import Counter; c=Counter(); [c.update(json.loads(l).get('tags',[])) for l in sys.stdin]; print('\n'.join(f'{n} {t}' for t,n in c.most_common(30)))"`

Reuse names that already exist before inventing new ones.