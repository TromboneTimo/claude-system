---
name: Shared Image Library (Canonical Generated Assets)
description: Master location for ALL Gemini-generated images across Timo decks. Every generation saved here for reuse. Future decks reference this first before regenerating.
type: reference
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
**Canonical root:**
`/Users/air/Desktop/Timo LLC/creator-conservatory/assets/shared/`

**Structure:**
- `assets/shared/timo-headshot-trombone-stool.jpg` — Timo's official headshot (per `reference_timo_headshot_canonical.md`)
- `assets/shared/generated/` — ALL Gemini-generated images, permanent
- `assets/shared/generated/[descriptive-filename].png` — one file per generation, named by subject

**Current generated asset inventory (as of 2026-04-13):**

| Filename | Subject | First used in | Reusable for |
|---|---|---|---|
| `obama-portrait-2008.png` | Stylized editorial portrait of Barack Obama, 2008-era, navy bg, painterly | designer-vs-marketer slide 3 | Any Obama reference, campaign-era stories, "the right visual" proof |
| `obama-2008-rally-video-frame.png` | Obama at podium mid-gesture, banners, crowd (mock video still) | designer-vs-marketer slide 3 BEFORE mockup | A/B test "before" visuals, campaign rally content, pre-tested hooks |
| `obama-family-portrait-time-style.png` | Obama family portrait, TIME magazine cover style | designer-vs-marketer slide 3 AFTER mockup | A/B test "after" visuals, warmth/trust/family proof |
| `warning-triangle-gold.png` | Gold warning triangle with black exclamation mark on black bg (use `mix-blend-mode: screen` for colored backgrounds) | views-that-matter slide 1B | EVERY warning/urgency slide across all decks |

**Workflow for NEW image generations:**

1. **Before generating, check the inventory above.** If a similar image already exists, use it. Don't regenerate.
2. **Generate via Gemini curl.** (See `reference_gemini_image_api.md` for the working API shape.)
3. **Save DIRECTLY to `assets/shared/generated/` with a descriptive kebab-case filename.** Pattern: `[subject]-[variant].[png|jpg]`. Never save only to a deck's local assets folder — that strands the asset.
4. **Symlink or copy into the deck's local folder** if the deck uses relative paths:
   ```bash
   ln -sf "../../../assets/shared/generated/[file].png" "output/presentations/assets/[file].png"
   # or for images/[subfolder]/ structure:
   cp "/Users/air/Desktop/Timo LLC/creator-conservatory/assets/shared/generated/[file].png" "output/presentations/images/[subfolder]/[file].png"
   ```
5. **Update this inventory table** with the new entry in the table above — filename, subject, first used in, reusable for.

**Why centralize:** before this was set up, each generated image lived inside one deck's asset folder. Result: regenerating the same concept for every new deck, losing access to prior generations when decks moved/renamed, no way to answer "do we already have an image of X?" before paying for a new generation.

**NEVER-DO list:**
- Never generate into a deck's local assets folder ONLY. Always save to `assets/shared/generated/` first, then copy/symlink into the deck.
- Never regenerate a subject we already have. Check the inventory. If existing image is close enough, use it or edit (image-to-image edits via Gemini are cheaper than full regeneration).
- Never use AI to generate Timo's portrait (see `feedback_placeholder_images.md` — uncanny, undermines credibility).

**When adding a warning/urgency slide to any deck:**
Use `warning-triangle-gold.png` at max 140px, `mix-blend-mode: screen` to blend the black background with colored slide backgrounds. Position: top of slide, centered, as the first element above the warning headline. See `feedback_warning_slide_pattern.md`.
