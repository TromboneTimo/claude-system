---
name: Always use frontend-slides skill for presentations
description: Never use the old RR presentation template. Always use the frontend-slides skill for all slide decks.
type: feedback
---

ALWAYS use the `/frontend-slides` skill (at ~/.claude/skills/frontend-slides/) for any presentation or slide deck. Never fall back to the old marketing-present skill or the RR presentation-templates.md template.

**Why:** The old template produced small text, generic layouts, and "AI slop" aesthetics. The frontend-slides skill enforces viewport fitting (100vh per slide, no scroll), clamp() typography (readable from across the room), distinctive fonts (Fontshare, not Inter/Roboto), cinematic animations, and content density limits.

**How to apply:** When user asks for a presentation, slide deck, or pitch deck:
1. Load frontend-slides SKILL.md
2. Read viewport-base.css and include ALL of it
3. Read animation-patterns.md for the right feeling
4. Use dark premium theme unless user specifies otherwise
5. Big text. Lots of breathing room. Max 4-6 bullets per slide.
6. If content overflows, SPLIT into multiple slides. Never cram.
