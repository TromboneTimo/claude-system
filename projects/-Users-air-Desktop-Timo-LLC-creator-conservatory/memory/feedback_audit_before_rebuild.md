---
name: List Existing Elements Before Rebuilding
description: Before any slide/component rewrite, list every element currently present. After the rewrite, every element must either still be there OR be intentionally removed for a stated reason. Otherwise it's a regression.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
When asked to ADD something to an existing slide/component, ADD it. Do not rebuild from scratch. Rebuilding tears down validated elements that the user already approved, then I have to be told to put them back.

**The exact failure pattern (2026-04-13):**
1. Built case study slides 3-5 with: logo + business desc + THE CHANGE text callout + result number + source. User approved the structure.
2. User asked: "add before/after mockups."
3. I rebuilt each slide from scratch. The new layout had: logo + business desc + BEFORE/AFTER mockups + result number + source. THE CHANGE callout was DELETED because I assumed the visual mockup replaced the text description.
4. User: "slides 3-5 are now missing the information that gave the changes in website context, why the fuck did you remove it?"
5. The text callout and the visual mockup are COMPLEMENTARY. Visual shows what changed; text names the change in plain words. Both are needed.

**Why this happens:** When I think "new element," I subconsciously frame it as "replacement." I prioritize visual cleanliness over information completeness. I edit reactively — focused only on the new request — instead of holistically auditing what's already on the slide.

**The guardrail (apply BEFORE every slide rewrite):**
1. Read the current slide HTML.
2. List every distinct element: eyebrow, logo, business description, mockup, callout, result number, caption, source, image, etc.
3. Decide for EACH listed element: keep, modify, or remove. If removing, state why (truly redundant, replaced by superior version, etc.).
4. Then write the new slide. Verify every "keep" element survived the rewrite.
5. If I can't justify a removal, the element stays.

**The deeper rule:** ADD doesn't mean REPLACE. When user says "add X," the default is X joins the existing structure, not X displaces something. If the existing structure can't accommodate X, ASK before deleting elements to make room.

**How to apply:**
- Use this for any task where I'm modifying existing work (slides, components, copy, designs).
- The list-before-rewrite step takes 30 seconds and prevents the worst regression class.
- "I assumed the new thing covered the old thing" is NEVER an acceptable reason to delete validated content. If they cover the same ground, ASK which to keep.
