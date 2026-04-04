# Session Log

Rolling log of sessions. Keeps the last 14 days. Older entries archived to `~/.claude/session-archive/`.

---

## 2026-04-02

### Session 1 (System Setup)
**What happened:**
- Condensed global CLAUDE.md from 418 → 126 lines (removed duplication, collapsed 10 engineering modes to 5-row table)
- Updated user_timo_profile.md with data from "For David" PDF: new clients (Victor Alegria, Steve Parker, Big Wy's Brass Band, Norfolk Chamber, Third Coast, Brass Witch), expanded ICP framework, 9 tool ideas, high ticket barriers, competitor references
- Updated Trombone Timo stats: billion views, $40k from one video, NBC mention, TED talk invite
- Designed and built Kuro-adapted life operating system: SOUL.md, PRIORITIES.md, RHYTHM.md, SESSION_LOG.md, /ops skill

**Decisions saved:**
- Priority tiers defined: Engine (Trombone Timo, Conservatory), Infrastructure (Hook Book, automations), Satellite (Robinson's)
- WIP limits set: max 3 active, 1 deep focus (currently Hook Book)
- 9 tool ideas logged to backlog with recommended priority order
- Robinson's capped at 5 hr/week until renegotiated

**Open threads:**
- Test boot sequence in a fresh session to confirm it fires automatically
- Obsidian vault opened and working

### Session 2 (Landing Page + Offer + Funnel Strategy)
**What happened:**
- Built irresistible offer worksheet (GOH framework adapted for Timo)
- Built landing page v1 (too complex), v2 (Andrews Bodega cream style, still too much text), v3 (VSL + book a call — minimal, research-backed)
- Fixed dream outcome: "I help musicians with businesses and music coaches massively increase sales through organic social media and systems — without wasting time on strategies that don't work"
- Cut $5 ads from offer — no proof yet, future upsell after Robinson's data
- Decided: AI = "how" shown on calls, not the headline. Say "systems" not "AI" on VSL.
- VSL structure outlined: hook → pain → story → insight → what I do → CTA (under 10 min)

**Decisions saved:**
- Dream outcome updated in offer worksheet
- Landing page is VSL-first (video + CTA + minimal results below)
- Priorities updated: deep focus = Hook Book + Conservatory funnel
- Consulting content channels: Facebook, Instagram, YouTube (Tim Maines brand, separate from Trombone Timo)

**Open threads:**
- Record the VSL (bottleneck — unlocks the whole funnel)
- Get Calendly link set up and plugged into landing page
- Move domains to Porkbun
- Update landing page + offer worksheet to remove all $5 ads references
- Write full VSL script

## 2026-04-03

### Session 1 (Hook Book Content + Bug Fixes)
**What happened:**
- Added 37 new entries to Hook Book (now 325 total): 15 Dimitri Fantini (drums, 150K+), 14 Andrea Scaffardi (clarinet, 2K+ likes), 2 guptaviolin, 1 sophiereidfit (412K likes), 1 jettfranzen, 1 cafeandy, 1 garyvee, 1 Tony Polecastro, 1 magbakk carousel
- Fixed sorting: "Most views" → "Most popular" (uses views for YT, likes for IG). Date sort uses ID tiebreaker.
- Fixed "videos" → "posts", "Watch Original" → "See Original"
- Fixed admin assignment bug: auto-retry after 1.5s + error UI with Retry button
- Added creator search: dedicated `activeCreator` filter with pill UI, not just text search
- Fixed 2 broken carousel thumbnails (Nahre Sol, wiam_architect)
- Reclassified all Victor Alegria entries from Trumpet → Trombone
- Logged all client commitments from coaching call to memory

**Decisions saved:**
- Priorities updated with client deliverables: AI systems, training content, Hook Book expansion
- Deep focus after Hook Book ships = Client AI Systems

**Open threads:**
- Record VSL (still the bottleneck)
- Expand Hook Book to 100+ carousels (currently ~35 carousels)
- Build AI content creation systems for Harrison + Sohee
- DaVinci Resolve tutorial suite
- Fathom call analyzer for Harrison

## 2026-04-04

### Session 1 (Robinson's Remedies + System Optimization)
**What happened:**
- Built 3 landing pages (Lightning Stick, Recovery Stick, Endurance Cream) with Blueprint-style design
- Wired real product images into landing pages and carousel
- Installed Perplexity MCP server + perplexity-web-research skill
- Built self-improving system: /self-improve skill (Karpathy loop), eval.json for 3 skills, /weekly-review skill
- Created feedback/deliverables-log.md for deliverable tracking
- Researched and applied CLAUDE.md best practices via Perplexity -> NotebookLM pipeline
- Optimized all global MD files: CLAUDE.md (132->65), SOUL.md (129->44), PRIORITIES.md (95->43)
- Fixed notify.sh SESSION_LOG spam

**Decisions saved:**
- Research pipeline: ALWAYS Perplexity then NotebookLM. No exceptions.
- CLAUDE.md best practice: under 60 lines, critical rules at top AND bottom, compaction orders
- CLAUDE.md instructions only 70-80% followed - use hooks for 100% enforcement rules

**Open threads:**
- Optimize Digital Product Creator MEMORY.md (139 lines, bloated)
- Run /self-improve on marketing-social to test the Karpathy loop
- Set up /schedule for weekly-review cron job
- Record VSL (still the bottleneck for Hook Book)
