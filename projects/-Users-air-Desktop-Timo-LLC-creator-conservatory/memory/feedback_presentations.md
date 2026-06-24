---
name: Presentation Design Rules
description: Hard rules for building slide presentations - no reused images, show prompts not code, use full screen layouts
type: feedback
---

1. **Never reuse the same image on multiple slides.** Every slide gets a unique image. No exceptions.
   **Why:** Looks lazy and repetitive. User called this out specifically.
   **How to apply:** Track which images are assigned to which slides. Generate enough unique images upfront.

2. **Show what to type in the prompt, not raw code commands.** Steps should show the exact natural language prompt the user would say to Claude, not CLI commands like `npx create-next-app`.
   **Why:** The audience doesn't understand code. They need to know what to SAY to Claude. The whole point is "no developer needed."
   **How to apply:** Every step slide should have a quote block with the exact prompt text. Code output can be shown as a result, but the primary content is the human prompt.

3. **Use full-screen layouts. Never hug content to the left with dead space.** Center content, use the full viewport width.
   **Why:** Left-hugging layouts with empty right side look ugly and unfinished.
   **How to apply:** Default to centered layouts. If using split layouts, fill both sides. If content is text-only, center it with max-width and auto margins.
