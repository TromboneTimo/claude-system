---
name: Verify Referenced Files Before Compacting
description: CRITICAL. Never compact a CLAUDE.md or SKILL.md by moving content to "see reference file" without first verifying the reference file actually contains the full detail. Pointer-swap without verifying the target is a null reference.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# NEVER Compact By Pointer-Swap Without Verifying The Target

**Rule:** Before compacting any file (CLAUDE.md, SKILL.md, MEMORY.md, etc.) by moving content to a reference ("see `feedback_X.md`" or "see `~/.claude/knowledge/Y.md`"), I MUST grep the referenced file for the specific content I'm claiming is there. If the detail is missing, UPDATE the reference file FIRST, then compact the source file.

**Why:** On 2026-04-13 during `/fix-brain`, I trimmed Timo's creator-conservatory CLAUDE.md from 100 to 60 lines. I compacted an 8-item pre-check to a 1-line reference pointing at `feedback_pregeneration_checklist.md`. That file only had 4 items, not 8. Items 6-8 (layout shape, specific proof, bridge slides) and the clamp-ratio detail in item 4 would have been quietly weakened. I only caught it because Timo asked "are you sure you didn't delete important stuff?" Without his prompt, the weakening would have rotted silently. He'd have seen more slide-generation fuckups over the next two weeks and not known why.

**How to apply (mandatory before declaring ANY compaction done):**

1. **Identify every reference pointer** you added or modified in the compacted file. Grep the new version for `see .*\.md` or `memory/feedback_` or `~/.claude/knowledge/`.

2. **For each reference pointer, grep the target file** for the specific rule, item, or detail you claim is there. Use specific terms, not vague ones. Example: if you moved an 8-item checklist, grep for each of the 8 item keywords.

3. **If the target file is missing the detail:** STOP. Update the target file with the full content BEFORE re-confirming the compaction is safe.

4. **Only then mark the compaction done.**

**Where this applies:**
- `/fix-brain` skill (all compactions during brain fix)
- `/self-improve` skill (when it modifies SKILL.md)
- Any manual trim of CLAUDE.md, PRIORITIES.md, MEMORY.md, or SKILL.md
- Any "move details to referenced file" edit
- Any "replace verbose section with a pointer" edit

**The deeper failure pattern this prevents:**
Prioritizing tidy numbers (line count reduction) over content preservation. Smaller line counts feel like progress. They are not progress if the rules rot. Same pattern as fabrication: narrative convenience (here: "I trimmed successfully") over truth.

**Related memories:**
- feedback_fabricated_behavior.md (ASK don't invent, parent lesson)
- feedback_pregeneration_checklist.md (the file that was almost-weakened)
- feedback_read_before_asking.md (re-read from disk, parent discipline)
