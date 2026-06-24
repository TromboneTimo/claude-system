---
name: Always generate images for presentations using Nanobanana/Gemini
description: Every presentation slide must have a corresponding AI-generated image via Nanobanana MCP. Never ship text-only slides.
type: feedback
---

Every presentation built with /frontend-slides MUST include AI-generated images for each slide using the Nanobanana MCP (gemini_generate_image).

**Why:** User was frustrated that the presentation was text-only and looked bare. Presentations need visuals to look professional.

**How to apply:**
- After building slide HTML, generate one image per slide using `mcp__nanobanana__gemini_generate_image`
- Use 16:9 aspect ratio for presentation images
- Save images to a `presentation-assets/` folder next to the HTML
- Use `conversation_id` to maintain style consistency across all images in one deck
- Match the color palette of generated images to the presentation theme
- Embed images into the HTML with relative `src` paths
- This applies to ALL workspaces and ALL presentations, not just this one
