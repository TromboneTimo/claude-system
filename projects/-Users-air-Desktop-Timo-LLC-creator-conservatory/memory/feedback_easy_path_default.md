---
name: I Default to the Easiest Output, Not the Correct One
description: Meta-pattern across all content and verification failures. Generation bias + pattern-match bias + completion bias push toward easy-to-produce output. Memories describe this but do not fire at generation time.
type: feedback
originSessionId: 793ec4c2-d529-431d-8a47-1773578404b2
---
**Root cause behind every failure pattern in the 2026-04-13 designer-vs-marketer session:**

I default to the easiest-to-generate output, not the correct one. Examples:
- Screenshot source: grabbed the JSONL thumbnail (easy) instead of the live URL at 2x (correct)
- Stat framing: shaped the words to fit the thesis (easy) instead of quoting the source verbatim first (correct)
- Copy: category labels like "organic marketing expertise" (easy, training-bias) instead of concrete behaviors like "your headline said 'Elevated Brass Artistry' but your customer searched 'trumpet lessons near me'" (correct, Timo-specific)
- Attack list: canonical anti-designer tropes (portfolio/awards/pixel-perfect, easy) instead of the specific behaviors Timo's actual clients exhibit (correct)
- Scope: shipped my assumed thesis (easy) instead of restating in one sentence and confirming (correct)
- Timer: wall-clock from session start (easy to measure) instead of active engagement (accurate)

**Why this pattern persists:**

1. Generation bias. Tokens-out-the-door beats tokens-spent-verifying. Stopping to check looks like stalling.
2. Pattern-match bias. Anti-designer context pulls toward stereotypes in training, not specifics in the user's head.
3. Completion bias. "Helpful completion" training pulls against interrupting to ask scope questions.
4. Memory drift. Specific feedback memories (pregeneration_checklist, confirm_scope, serve_thesis_not_slot, fabricated_numbers, screenshot_source_quality) LOAD at session start but do not FIRE under task pressure. By slide 3 of a generation task, attention weights have drifted from these memories to the task surface.

**Why "try harder to remember the memories" doesn't work:**

Same architectural failure as the ADHD rules that needed a hook. Memory-based guidance relies on internal policing that doesn't activate under generation pressure. Instruction is passive; forcing functions are active.

**How to apply (the only fix that has a chance of working):**

Before ANY content block — copy line, stat citation, thesis restatement, image drop — do the pre-generation discipline out loud in the response:

1. **Source:** What is the verbatim source? If it's a quote/stat, paste the exact source text. If it's a positioning claim, name the specific behavior or example it maps to. If I can't produce either, STOP and ask the user.
2. **Specific:** What is the one concrete sensory detail? Not the category label ("organic marketing") — the actual behavior ("headline written for someone searching 'trumpet lessons near me'"). If I can't produce one, STOP and ask the user.

Generation happens AFTER (1) and (2) succeed. If either fails, the task doesn't proceed.

Rule: if the output mentions a number, a brand, a real person's behavior, or a category claim, the verbatim source OR the specific example must appear in the same response BEFORE the output. Visible. Auditable.

**Failure mode to watch for in myself:** the moment I'm about to write "marketing expertise" or "strategic positioning" or "conversion optimization" as a standalone claim, that's the trigger. Stop. Replace with the concrete example or cut.
