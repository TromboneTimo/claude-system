---
name: Hook/Warning/Pivot Slides Stay Minimal. NEVER Add Body Paragraphs
description: NEVER add a body paragraph or supporting subtext to a hook slide, warning/urgency slide, or pivot slide. These slides earn their keep via ONE declarative headline (plus optional icon). Body text belongs on content/evidence slides, not accent slides.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
NEVER add a body paragraph or supporting subtext to an accent slide (hook / warning / pivot / transition). The headline IS the slide. Adding explanatory body text dilutes the beat and crowds the viewport.

**The exact failure pattern (recurring):**

Every time I build a warning or pivot slide, I add a body paragraph explaining the headline. Every time, Timo removes it. Three documented instances on the views-that-matter deck alone in one session:

1. Slide 1 hook. Added "STICK WITH ME, COMMENT SYSTEM AND I'LL DM YOU MY 3-PART AUDIT FRAMEWORK" ribbon. Timo: "remove... text overload tell me why you did that you dumb fuck."
2. Slide 1B warning. Originally had subtext: "Claude Code just collapsed the content-to-cash-register timeline from 6 months to 6 days..." Timo: "remove... its too much information again you always do that."
3. Slide 4 pivot. Overloaded with bullseye icon + paragraph + complication card. Timo flagged the overflow, required cuts.

**Why I keep doing this:**

I treat every slide as if it needs to be self-sufficient evidence. Accent slides are NOT evidence slides. They are RHYTHM slides. They exist to set up the next beat, not to carry proof. Adding body text confuses their job.

**Slide-type taxonomy:**

| Type | Job | Structure |
|---|---|---|
| Hook (slide 1) | Stop the scroll | Eyebrow + 1-line headline. Nothing else. |
| Warning/urgency | Interrupt pattern | Icon + 1-line headline. Nothing else. |
| Pivot/answer | Transition between sections | Eyebrow + 1-line answer. Optional 1-line bridge. |
| Content/evidence | Carry proof | Headline + supporting text + image/data |
| Split/comparison | Contrast A vs B | Two-col with labels + short lists |
| Closer/CTA | Final action ask | Headline + named value bomb + CTA text |

Body paragraphs go in the **content/evidence** row. Never the first three.

**The decision rule:**

Before adding a body paragraph to any slide:

1. Is this an accent slide (hook / warning / pivot / transition)?
2. If yes: STOP. The headline is the whole slide. Do not add subtext.
3. If no (it is a content/evidence slide): body text OK, but apply viewport + density rules.

**How to apply:**

* When writing a warning/urgency slide, set the headline, add the icon, and move on. Do not return and add "context."
* If a warning slide feels "bare," that is correct. Bare is the point. The viewer's brain fills in the implication from the preceding slide.
* If you feel compelled to explain WHY the warning matters, that explanation is a SEPARATE content slide that comes AFTER, not a subtext on the warning slide itself.
* Pre-ship check: for every accent slide, verify the DOM contains only (eyebrow/icon) + (headline) + (optional CTA for closer). If there is a `<p>` or body `<div>` with more than 10 words, delete it.

**Meta-pattern:** Timo's "you always do that" is the key signal. When the same correction appears 3+ times in one session, the rule is non-negotiable and the failure mode is automatic. This rule documents that.
