---
name: project_marketing_system
description: Complete AI marketing system for Robinson's Remedies — 6 skills, 5 SOPs, 2 agents, browser agent, full brand context files
type: project
---

Complete AI marketing system built on 2026-03-20, expanded 2026-03-23.

## What's Built

### Project Structure (`~/Desktop/Robinsons Remedies/`)
- `context/` — 5 files: brand.md, products.md, audience.md, competitors.md, brand-guidelines.md (all populated with real RR data)
- `sops/` — 5 SOPs: research-strategy, social-content, creative-design, data-analysis, campaign-presentation
- `references/` — storytelling-frameworks.md, platform-specs.md, dashboard-templates.md, presentation-templates.md, content-examples.md
- `assets/` — color-palette.md
- `output/` — campaigns, reports, social, presentations, creatives

### 6 Marketing Skills (`~/.claude/skills/`)
- `/marketing` — orchestrator routing to sub-skills
- `/marketing research` — web research, competitor analysis, strategy briefs
- `/marketing social` — social posts, calendars, carousels, YouTube scripts
- `/marketing creative` — visual design briefs
- `/marketing data` — interactive HTML dashboards (Chart.js)
- `/marketing present` — HTML slide decks and landing pages

### 2 Agents (`~/.claude/agents/`)
- `marketing-researcher` — web research subagent
- `marketing-analyst` — data analysis + visualization subagent

### Browser Agent (`~/.claude/tools/browser-agent/`)
- Custom Chrome automation via puppeteer-core + CDP (port 9222)
- Commands: launch, list, open, screenshot, click, type, content, html, elements, scroll, upload, pdf, close
- Isolated Chrome profile at `~/.claude/tools/browser-agent/chrome-profile/`
- User logged into X on this profile (2026-03-23)
- Note: Chrome blocks `--remote-debugging-port` on default profile path — must use isolated profile
- To start: `node ~/.claude/tools/browser-agent/browser.js launch` then all commands work

### No paid MCPs needed
- WebSearch/WebFetch replace Perplexity MCP (free, built-in)
- HTML creative generation replaces Nano Banana MCP (free, no API)
- Browser agent replaces paid skillsmd.store tool (free, custom-built)

**Why:** User wants full marketing automation — research, create, post, analyze — all from Claude Code with zero extra cost.

**How to apply:** Always load context files before generating content. Use browser agent for social media automation (X login persists in isolated profile). Skills route through orchestrator for multi-skill campaigns.
