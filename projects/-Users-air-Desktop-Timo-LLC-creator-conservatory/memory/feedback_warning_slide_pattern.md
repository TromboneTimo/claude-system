---
name: Warning Slide Pattern — Always Use the Triangle
description: NEVER ship a warning/urgency slide with just a text "WARNING" badge. Every warning slide across every Timo deck gets the canonical warning triangle icon at the top. The icon is the signal; the text is the payload.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
NEVER build a warning/urgency/"pay attention" slide with only a text "Warning" badge. Every such slide gets the canonical warning triangle icon (`assets/shared/generated/warning-triangle-gold.png`) at the top, centered, above the headline.

**The exact failure pattern (2026-04-13):**
Slide 1B of views-that-matter was a warning/urgency slide. I had built it with a bordered text badge reading "WARNING" as the signal. Functional but weak — the badge competes with the headline for visual authority. Timo: "every time there is a warning slide in these presentations i want a graphic of a warning symbol."

**The pattern (apply to ANY warning/urgency slide):**

```html
<img src="[path-to]/warning-triangle.png"
     alt="Warning"
     style="max-width: 140px; max-height: 140px; margin-bottom: 22px; mix-blend-mode: screen;"
     onerror="this.style.display='none'; this.nextElementSibling.style.display='inline-block';">
<div style="display:none;font-weight:800;font-size:clamp(12px,1.1vw,16px);letter-spacing:0.3em;text-transform:uppercase;padding:10px 18px;border:2px solid var(--gold);color:var(--gold);background:rgba(212,165,116,0.1);margin-bottom:32px;">
  Warning
</div>
<!-- Then the headline -->
```

Key properties:
- `max-width/max-height: 140px` — icon is prominent but doesn't dominate
- `mix-blend-mode: screen` — makes the black background of the PNG invisible on colored slide backgrounds (magenta, gold, midnight). The gold triangle + black exclamation mark stay intact.
- `margin-bottom: 22px` — ~30% of icon height for visual separation
- **Fallback** — if the image fails to load, the next sibling (text badge) shows via onerror. Belt + suspenders.

**The canonical asset:**
`/Users/air/Desktop/Timo LLC/creator-conservatory/assets/shared/generated/warning-triangle-gold.png` — gold triangle, black exclamation, black background. Use with `mix-blend-mode: screen`.

**Which slides need this treatment:**
- Urgency/warning slides ("What you're about to see wasn't possible 12 months ago", "The gap widens every week", "Warning: this breaks your current playbook")
- "Stop doing this" slides (common mistake callouts)
- Scarcity/time-sensitive CTAs ("Last chance before X")
- Any slide with a "Warning" eyebrow/badge currently rendered as text-only

**How to apply:**
- When building ANY warning slide: drop the icon in FIRST, above the headline.
- When auditing existing decks: grep for `[Ww]arning|URGENCY|urgency` and add the icon to each slide found.
- Never use a text-only "WARNING" badge as the signal. The icon is the signal.
- If the deck's assets folder doesn't have the image yet, copy from canonical: `cp "/Users/air/Desktop/Timo LLC/creator-conservatory/assets/shared/generated/warning-triangle-gold.png" "[deck-assets-path]/warning-triangle.png"`

**Why this works:** Warning slides are interrupt-pattern slides in a sales flow. The viewer is scrolling through argument → proof → argument → and the warning slide is meant to STOP them. A text badge requires reading. An icon is processed pre-attentively. The icon stops the scroll BEFORE the headline has to do work.

**Related memories:**
- `reference_shared_image_library.md` — location of canonical warning asset + inventory
- `feedback_qa_at_safari_real_viewport.md` — render warning slides at 1440x680 to verify the icon doesn't push headline off-screen
