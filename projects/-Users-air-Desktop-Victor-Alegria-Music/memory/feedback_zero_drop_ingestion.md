---
name: Zero-drop ingestion of structured user content
description: When ingesting/transforming user-provided structured content (proposals, drafts, briefs, scripts), every labeled section MUST be preserved or explicitly flagged. Silent dropping is the worst-severity failure.
type: feedback
originSessionId: 4bce74b5-3905-4e74-a852-0df3f6f7abc4
---
When the user pastes structured content with labeled sections (e.g. "Idea origin:", "The wound we're naming:", "Source evidence:") and asks me to upload/transform/store it, **every labeled section must end up in the destination**. Silent omission of any section is the highest-severity failure mode for these tasks. Worse than formatting issues. Worse than slow execution.

**Why:** Timo writes these proposals carefully. Each section carries information he needs Harrison to see. When I drop sections (Idea origin → forgotten, What these quotes show together → forgotten), Harrison reviews an incomplete picture, decisions get made on partial context, and Timo has to babysit me through 3-4 rounds of "you forgot X again." This compounds into wasted hours and broken trust. He has explicitly called this out as the #1 thing to fix.

**How to apply:** Before any curl/POST/transform that ships user content somewhere:

1. **Enumerate every labeled section in the input.** Write the list out loud (in chat or as a comment in the script).
2. **Map each section to its destination.** Field name, location, file. No section may have an empty mapping.
3. **If any section has no destination, STOP and ask.** "I don't have a place for X. Add a new section, append to existing, or skip?" Never decide alone to drop it.
4. **Show Timo the map and wait for confirmation** before pushing.

This rule applies to ALL structured ingestion tasks across all workspaces: blog briefs into MDX, proposal docs into dashboards, transcripts into VOC banks, sales call notes into customer profiles, anything where the user's input has labeled parts that flow to a different target schema.

Pattern violations recorded:
- 2026-04-26: Pushed lip-bruise script proposal to dashboard, dropped "Idea origin" section. Caught by Timo. Fixed by adding mandatory preflight enumeration to /pb-ideas-push skill.
- 2026-04-26: Same proposal, also initially dropped "What these quotes show together" synthesis section. Caught by Timo. Fixed.

The skill SKILL.md files for ingestion-type skills must include a "ZERO-DROP CONTRACT" or equivalent preflight enumeration step. Apply this to /pb-ideas-push, /coaching-db, /yt-vault, /fb-vault, /blog-rewrite, /blog-write, and any new skill that takes user-pasted structured input.
