---
name: frontend-slides
description: Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch. Helps non-designers discover their aesthetic through visual exploration rather than abstract choices.
---

# Frontend Slides

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

## Core Principles

1. **Zero Dependencies** — Single HTML files with inline CSS/JS. No npm, no build tools.
2. **Show, Don't Tell** — Generate visual previews, not abstract choices. People discover what they want by seeing it.
3. **Distinctive Design** — No generic "AI slop." Every presentation must feel custom-crafted.
4. **Viewport Fitting (NON-NEGOTIABLE)** — Every slide MUST fit exactly within 100vh. No scrolling within slides, ever. Content overflows? Split into multiple slides.

## Design Aesthetics

You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight.

Focus on:

- Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:

- Overused font families (Inter, Roboto, Arial, system fonts)
- Cliched color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box!

## Viewport Fitting Rules

These invariants apply to EVERY slide in EVERY presentation:

- Every `.slide` must have `height: 100vh; height: 100dvh; overflow: hidden;`
- ALL font sizes and spacing must use `clamp(min, preferred, max)` — never fixed px/rem
- Content containers need `max-height` constraints
- Images: `max-height: min(50vh, 400px)`
- Breakpoints required for heights: 700px, 600px, 500px
- Include `prefers-reduced-motion` support
- Never negate CSS functions directly (`-clamp()`, `-min()`, `-max()` are silently ignored) — use `calc(-1 * clamp(...))` instead

**When generating, read `viewport-base.css` and include its full contents in every presentation.**

### Content Density Limits Per Slide

| Slide Type    | Maximum Content                                           |
| ------------- | --------------------------------------------------------- |
| Title slide   | 1 heading + 1 subtitle + optional tagline                 |
| Content slide | 1 heading + 4-6 bullet points OR 1 heading + 2 paragraphs |
| Feature grid  | 1 heading + 6 cards maximum (2x3 or 3x2)                  |
| Code slide    | 1 heading + 8-10 lines of code                            |
| Quote slide   | 1 quote (max 3 lines) + attribution                       |
| Image slide   | 1 heading + 1 image (max 60vh height)                     |

**Content exceeds limits? Split into multiple slides. Never cram, never scroll.**

### Typography Hierarchy Ratios (NON-NEGOTIABLE)

ONE focal point per slide. Every supporting element must be 20-25% of the hero size, NOT 60-70%. Two elements at 60% of hero size do not read as "hero + support" -- they read as "two things competing." Lessons from 2026-04-13 deck failures where text overflowed viewports because stacked elements at similar sizes couldn't fit.

| Element | Size relative to hero | Example clamp |
|---------|----------------------|----------------|
| Hero headline (1 per slide MAX) | 100% | `clamp(44px, 8vw, 120px)` |
| Eyebrow label (uppercase, letterspaced) | 12-15% | `clamp(12px, 1.2vw, 16px)` |
| Sub-headline / promise line | 20-25% | `clamp(14px, 1.5vw, 20px)` |
| Body / caption text | 18-22% | `clamp(14px, 1.6vw, 22px)` |
| Small proof text | 15-18% | `clamp(12px, 1.4vw, 18px)` |

Hard rules:
- ONE hero per slide. Not two. Not "hook + equally-sized sub-hook."
- Eyebrow labels use letter-spacing 0.15-0.25em + uppercase. Make them read as "label," not "headline."
- Supporting text opacity 0.7-0.85 on busy slides so it recedes.
- Breathing room: minimum 24-36px gap between elements.
- Math the overflow before shipping: if hero is at 20vw on 1440px = 288px per char, an 11-char number = 1980px = overflow. Calculate character count + average letter width * font size before using clamp maxes.
- CTA + image + tagline + subtext cannot all be large simultaneously. One dominates, others support.

### Image Verification (MANDATORY)

After generating ANY presentation, run this audit before declaring done:

1. **Extract all image URLs:** grep for `src=` and `url(` in the HTML
2. **Check remote URLs:** curl each one. Must return HTTP 200. If 429/403/404, replace immediately.
3. **Check local paths:** ls each file path relative to the HTML file. Must exist.
4. **Never use Wikipedia/Wikimedia image URLs** (rate-limited, return 429)
5. **Every image must match its slide's content.** No generic stock photos as filler.
6. **If an external URL is unreliable, replace with styled text.** Text never breaks.
7. **Open in Safari and visually verify every slide** as the final step.

**Do NOT skip this. Do NOT declare done without running the audit.**

### Images Must Be Evidence, Not Atmosphere (SALES DECKS — NON-NEGOTIABLE)

For sales / persuasion / pitch decks, every image must LITERALLY SHOW the specific claim the slide is making. Atmospheric mood shots fail because they evoke without proving. 2026-04-13 leaking-business deck: five atmospheric images (burning money, diverging lines, search bar, chain link, stage) were rejected because they decorated the argument instead of making it.

**The pause test** (apply to every image before shipping): Mute audio, pause the slide. Would a cold viewer know what's being argued? If no, the image is atmosphere. Regenerate as evidence.

#### Three-Layer System (default for sales decks)

| Layer | Job | Position | Example |
|---|---|---|---|
| `.hero-image` (background) | Atmosphere + mood | Full-bleed, 35% opacity, left gradient | Burning money photo, dark theater, chain link |
| `.hero-foreground` (subject) | Literal evidence for the claim | Right-side, ~36vw square, drop shadow | Laptop with dashboard, phone with search, testimonial card |
| `.slide-inner` (text) | Thesis / headline / subhead | Left half, max 56vw | Headline + subhead |

#### DO

- **Generate literal subjects as foregrounds:** a laptop showing the exact dashboard, a phone with the search result, a chained phone for dependency, a styled testimonial card for social proof.
- **Shrink headline clamp on `.has-foreground` slides** to `clamp(1.75rem, 4.6vw, 4rem)`. Full-size headlines overflow the 56vw text zone.
- **Use HTML-styled cards instead of AI-generated text panels** for testimonials, stats, comparisons. AI garbles small text; HTML is pixel-perfect.
- **For hero slides where atmosphere IS the evidence** (e.g., "burning money on ads" with literal burning money), generate a stronger hero version as `.hero-foreground` AND keep atmospheric shot as `.hero-image`. Don't remove the foreground — promote it to subject-forward.
- **Write behavioral threats, not category framings** in copy. "Your competitor just fired three people" beats "you're fighting a four-person agency."
- **Add URL hash navigation** to every deck so `file://deck.html#7` jumps to slide 7. Enables sequential screenshot QA via `chrome --headless --screenshot file://deck.html#N`.
- **Close old Safari tabs before opening fresh.** Use AppleScript to close tabs matching the URL, then reopen. Stale tabs confuse the user.

#### DON'T

- **Don't default to editorial / Apple-keynote aesthetic** for sales decks. That's for brand decks. Sales decks need forensic-evidence energy.
- **Don't generate one image and assume you're done.** First pass is almost always atmosphere. Plan for a second pass that generates evidence.
- **Don't stack a foreground on a slide where the background IS the literal subject.** Redundant.
- **Don't let AI generate readable text inside foreground images** (dashboard numbers, chart labels, testimonial copy). It garbles. Generate containers (screens, devices, cards); overlay real text as HTML if needed.
- **Don't spawn parallel Chrome headless instances** for multi-slide screenshot QA. Sequential or batches of 3-4 max. Parallel spawn hangs the bash tool.
- **Don't fabricate business numbers.** Every stat must trace to real data or be explicitly hypothetical.
- **Don't generate AI portraits of the presenter.** Uncanny, undermines credibility. Use real photos or atmospheric objects associated with them.

#### CSS Scaffold (paste into any sales deck)

```css
.hero-image { position: absolute; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.hero-image img { width: 100%; height: 100%; object-fit: cover; opacity: 0.35; }
.hero-image::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(90deg, rgba(0,0,0,0.97) 0%, rgba(0,0,0,0.85) 40%, rgba(0,0,0,0.55) 75%, rgba(0,0,0,0.3) 100%);
}
.hero-foreground {
    position: absolute; right: clamp(2rem, 5vw, 5rem); top: 50%;
    transform: translateY(-50%);
    width: clamp(280px, 36vw, 520px); aspect-ratio: 1 / 1;
    z-index: 1; pointer-events: none;
    filter: drop-shadow(0 20px 60px rgba(0,0,0,0.8));
    border-radius: 8px; overflow: hidden;
}
.hero-foreground img { width: 100%; height: 100%; object-fit: cover; display: block; }
.slide.has-foreground .slide-inner {
    max-width: min(56vw, 820px); margin-left: 0; margin-right: auto;
}
.slide.has-foreground .headline { font-size: clamp(1.75rem, 4.6vw, 4rem); }
.slide.has-foreground .subhead { font-size: clamp(.9rem, 1.35vw, 1.2rem); max-width: 48ch; }
```

#### Hash Navigation (paste into deck JS)

```js
function fromHash() {
    const n = parseInt((location.hash || '').replace('#',''), 10);
    if (!isNaN(n) && n >= 1 && n <= slides.length) show(n - 1);
}
window.addEventListener('hashchange', fromHash);
fromHash();
```

#### Nano Banana Foreground Subject Prompt Template

```
[Literal subject, e.g., "A sleek laptop showing a Facebook Ads Manager dashboard"],
[Specific visible content, e.g., "red CPC graph spiking upward, '$47.82 CPC' in red, 'ROAS -18%' metric"],
[Composition, e.g., "centered in frame, 45-degree angle"],
[Lighting, e.g., "cinematic studio lighting, shallow depth of field, dramatic rim light"],
[Background, e.g., "pure black void"],
[Style, e.g., "35mm film aesthetic, square composition"],
[Negative, e.g., "no text beyond what is naturally visible, no watermark, no real brand logos"]
```

Use 1024x1024 Nano Banana output. CSS handles fit via `aspect-ratio: 1/1` + `object-fit: cover`.

---

## Phase 0: Detect Mode

Determine what the user wants:

- **Mode A: New Presentation** — Create from scratch. Go to Phase 1.
- **Mode B: PPT Conversion** — Convert a .pptx file. Go to Phase 4.
- **Mode C: Enhancement** — Improve an existing HTML presentation. Read it, understand it, enhance. **Follow Mode C modification rules below.**

### Mode C: Modification Rules

When enhancing existing presentations, viewport fitting is the biggest risk:

1. **Before adding content:** Count existing elements, check against density limits
2. **Adding images:** Must have `max-height: min(50vh, 400px)`. If slide already has max content, split into two slides
3. **Adding text:** Max 4-6 bullets per slide. Exceeds limits? Split into continuation slides
4. **After ANY modification, verify:** `.slide` has `overflow: hidden`, new elements use `clamp()`, images have viewport-relative max-height, content fits at 1280x720
5. **Proactively reorganize:** If modifications will cause overflow, automatically split content and inform the user. Don't wait to be asked

**When adding images to existing slides:** Move image to new slide or reduce other content first. Never add images without checking if existing content already fills the viewport.

---

## Phase 1: Content Discovery (New Presentations)

**Ask ALL questions in a single AskUserQuestion call** so the user fills everything out at once:

**Question 1 — Purpose** (header: "Purpose"):
What is this presentation for? Options: Pitch deck / Teaching-Tutorial / Conference talk / Internal presentation

**Question 2 — Length** (header: "Length"):
Approximately how many slides? Options: Short 5-10 / Medium 10-20 / Long 20+

**Question 3 — Content** (header: "Content"):
Do you have content ready? Options: All content ready / Rough notes / Topic only

**Question 4 — Inline Editing** (header: "Editing"):
Do you need to edit text directly in the browser after generation? Options:

- "Yes (Recommended)" — Can edit text in-browser, auto-save to localStorage, export file
- "No" — Presentation only, keeps file smaller

**Remember the user's editing choice — it determines whether edit-related code is included in Phase 3.**

If user has content, ask them to share it.

### Step 1.2: Image Evaluation (if images provided)

If user selected "No images" → skip to Phase 2.

If user provides an image folder:

1. **Scan** — List all image files (.png, .jpg, .svg, .webp, etc.)
2. **View each image** — Use the Read tool (Claude is multimodal)
3. **Evaluate** — For each: what it shows, USABLE or NOT USABLE (with reason), what concept it represents, dominant colors
4. **Co-design the outline** — Curated images inform slide structure alongside text. This is NOT "plan slides then add images" — design around both from the start (e.g., 3 screenshots → 3 feature slides, 1 logo → title/closing slide)
5. **Confirm via AskUserQuestion** (header: "Outline"): "Does this slide outline and image selection look right?" Options: Looks good / Adjust images / Adjust outline

**Logo in previews:** If a usable logo was identified, embed it (base64) into each style preview in Phase 2 — the user sees their brand styled three different ways.

---

## Phase 2: Style Discovery

**This is the "show, don't tell" phase.** Most people can't articulate design preferences in words.

### Step 2.0: Style Path

Ask how they want to choose (header: "Style"):

- "Show me options" (recommended) — Generate 3 previews based on mood
- "I know what I want" — Pick from preset list directly

**If direct selection:** Show preset picker and skip to Phase 3. Available presets are defined in [STYLE_PRESETS.md](STYLE_PRESETS.md).

### Step 2.1: Mood Selection (Guided Discovery)

Ask (header: "Vibe", multiSelect: true, max 2):
What feeling should the audience have? Options:

- Impressed/Confident — Professional, trustworthy
- Excited/Energized — Innovative, bold
- Calm/Focused — Clear, thoughtful
- Inspired/Moved — Emotional, memorable

### Step 2.2: Generate 3 Style Previews

Based on mood, generate 3 distinct single-slide HTML previews showing typography, colors, animation, and overall aesthetic. Read [STYLE_PRESETS.md](STYLE_PRESETS.md) for available presets and their specifications.

| Mood                | Suggested Presets                                  |
| ------------------- | -------------------------------------------------- |
| Impressed/Confident | Bold Signal, Electric Studio, Dark Botanical       |
| Excited/Energized   | Creative Voltage, Neon Cyber, Split Pastel         |
| Calm/Focused        | Notebook Tabs, Paper & Ink, Swiss Modern           |
| Inspired/Moved      | Dark Botanical, Vintage Editorial, Pastel Geometry |

Save previews to `.claude-design/slide-previews/` (style-a.html, style-b.html, style-c.html). Each should be self-contained, ~50-100 lines, showing one animated title slide.

Open each preview automatically for the user.

### Step 2.3: User Picks

Ask (header: "Style"):
Which style preview do you prefer? Options: Style A: [Name] / Style B: [Name] / Style C: [Name] / Mix elements

If "Mix elements", ask for specifics.

---

## Phase 3: Generate Presentation

Generate the full presentation using content from Phase 1 (text, or text + curated images) and style from Phase 2.

If images were provided, the slide outline already incorporates them from Step 1.2. If not, CSS-generated visuals (gradients, shapes, patterns) provide visual interest — this is a fully supported first-class path.

**Before generating, read these supporting files:**

- [html-template.md](html-template.md) — HTML architecture and JS features
- [viewport-base.css](viewport-base.css) — Mandatory CSS (include in full)
- [animation-patterns.md](animation-patterns.md) — Animation reference for the chosen feeling

**Key requirements:**

- Single self-contained HTML file, all CSS/JS inline
- Include the FULL contents of viewport-base.css in the `<style>` block
- Use fonts from Fontshare or Google Fonts — never system fonts
- Add detailed comments explaining each section
- Every section needs a clear `/* === SECTION NAME === */` comment block

---

## Phase 4: PPT Conversion

When converting PowerPoint files:

1. **Extract content** — Run `python scripts/extract-pptx.py <input.pptx> <output_dir>` (install python-pptx if needed: `pip install python-pptx`)
2. **Confirm with user** — Present extracted slide titles, content summaries, and image counts
3. **Style selection** — Proceed to Phase 2 for style discovery
4. **Generate HTML** — Convert to chosen style, preserving all text, images (from assets/), slide order, and speaker notes (as HTML comments)

---

## Phase 5: Delivery

1. **Clean up** — Delete `.claude-design/slide-previews/` if it exists
2. **Open** — Use `open [filename].html` to launch in browser
3. **Summarize** — Tell the user:
   - File location, style name, slide count
   - Navigation: Arrow keys, Space, scroll/swipe, click nav dots
   - How to customize: `:root` CSS variables for colors, font link for typography, `.reveal` class for animations
   - If inline editing was enabled: Hover top-left corner or press E to enter edit mode, click any text to edit, Ctrl+S to save

---

## Phase 6: Share & Export (Optional)

After delivery, **ask the user:** _"Would you like to share this presentation? I can deploy it to a live URL (works on any device including phones) or export it as a PDF."_

Options:

- **Deploy to URL** — Shareable link that works on any device
- **Export to PDF** — Universal file for email, Slack, print
- **Both**
- **No thanks**

If the user declines, stop here. If they choose one or both, proceed below.

### 6A: Deploy to a Live URL (Vercel)

This deploys the presentation to Vercel — a free hosting platform. The link works on any device (phones, tablets, laptops) and stays live until the user takes it down.

**If the user has never deployed before, guide them step by step:**

1. **Check if Vercel CLI is installed** — Run `npx vercel --version`. If not found, install Node.js first (`brew install node` on macOS, or download from https://nodejs.org).

2. **Check if user is logged in** — Run `npx vercel whoami`.
   - If NOT logged in, explain: _"Vercel is a free hosting service. You need an account to deploy. Let me walk you through it:"_
     - Step 1: Ask user to go to https://vercel.com/signup in their browser
     - Step 2: They can sign up with GitHub, Google, email — whatever is easiest
     - Step 3: Once signed up, run `vercel login` and follow the prompts (it opens a browser window to authorize)
     - Step 4: Confirm login with `vercel whoami`
   - Wait for the user to confirm they're logged in before proceeding.

3. **Deploy** — Run the deploy script:

   ```bash
   bash scripts/deploy.sh <path-to-presentation>
   ```

   The script accepts either a folder (with index.html) or a single HTML file.

4. **Share the URL** — Tell the user:
   - The live URL (from the script output)
   - That it works on any device — they can text it, Slack it, email it
   - To take it down later: visit https://vercel.com/dashboard and delete the project
   - The Vercel free tier is generous — they won't be charged

**⚠ Deployment gotchas:**

- **Local images/videos must travel with the HTML.** The deploy script auto-detects files referenced via `src="..."` in the HTML and bundles them. But if the presentation references files via CSS `background-image` or unusual paths, those may be missed. **Before deploying, verify:** open the deployed URL and check that all images load. If any are broken, the safest fix is to put the HTML and all its assets into a single folder and deploy the folder instead of a standalone HTML file.
- **Prefer folder deployments when the presentation has many assets.** If the presentation lives in a folder with images alongside it (e.g., `my-deck/index.html` + `my-deck/logo.png`), deploy the folder directly: `bash scripts/deploy.sh ./my-deck/`. This is more reliable than deploying a single HTML file because the entire folder contents are uploaded as-is.
- **Filenames with spaces work but can cause issues.** The script handles spaces in filenames, but Vercel URLs encode spaces as `%20`. If possible, avoid spaces in image filenames. If the user's images have spaces, the script handles it — but if images still break, renaming files to use hyphens instead of spaces is the fix.
- **Redeploying updates the same URL.** Running the deploy script again on the same presentation overwrites the previous deployment. The URL stays the same — no need to share a new link.

### 6B: Export to PDF

This captures each slide as a screenshot and combines them into a PDF. Perfect for email attachments, embedding in documents, or printing.

**Note:** Animations and interactivity are not preserved — the PDF is a static snapshot. This is normal and expected; mention it to the user so they're not surprised.

1. **Run the export script:**

   ```bash
   bash scripts/export-pdf.sh <path-to-html> [output.pdf]
   ```

   If no output path is given, the PDF is saved next to the HTML file.

2. **What happens behind the scenes** (explain briefly to the user):
   - A headless browser opens the presentation at 1920×1080 (standard widescreen)
   - It screenshots each slide one by one
   - All screenshots are combined into a single PDF
   - The script needs Playwright (a browser automation tool) — it will install automatically if missing

3. **If Playwright installation fails:**
   - The most common issue is Chromium not downloading. Run: `npx playwright install chromium`
   - If that fails too, it may be a network/firewall issue. Ask the user to try on a different network.

4. **Deliver the PDF** — The script auto-opens it. Tell the user:
   - The file location and size
   - That it works everywhere — email, Slack, Notion, Google Docs, print
   - Animations are replaced by their final visual state (still looks great, just static)

**⚠ PDF export gotchas:**

- **First run is slow.** The script installs Playwright and downloads a Chromium browser (~150MB) into a temp directory. This happens once per run. Warn the user it may take 30-60 seconds the first time — subsequent exports within the same session are faster.
- **Slides must use `class="slide"`.** The export script finds slides by querying `.slide` elements. If the presentation uses a different class name, the script will report "0 slides found" and fail. All presentations generated by this skill use `.slide`, so this only matters for externally-created HTML.
- **Local images must be loadable via HTTP.** The script starts a local server and loads the HTML through it (so Google Fonts and relative image paths work). If images use absolute filesystem paths (e.g., `src="/Users/name/photo.png"`) instead of relative paths (e.g., `src="photo.png"`), they won't load. Generated presentations always use relative paths, but converted or user-provided decks might not — check and fix if needed.
- **Local images appear in the PDF** as long as they are in the same directory as (or relative to) the HTML file. The export script serves the HTML's parent directory over HTTP, so relative paths like `src="photo.png"` resolve correctly — including filenames with spaces. If images still don't appear, check: (1) the image files actually exist at the referenced path, (2) the paths are relative, not absolute filesystem paths like `/Users/name/photo.png`.
- **Large presentations produce large PDFs.** Each slide is captured as a full 1920×1080 PNG screenshot. An 18-slide deck can produce a ~20MB PDF. If the PDF exceeds 10MB, ask the user: _"The PDF is [size]. Would you like me to compress it? It'll look slightly less sharp but the file will be much smaller."_ If yes, re-run the export with the `--compact` flag:
  ```bash
  bash scripts/export-pdf.sh <path-to-html> [output.pdf] --compact
  ```
  This renders at 1280×720 instead of 1920×1080, typically cutting file size by 50-70% with minimal visual difference.

---

## Supporting Files

| File                                               | Purpose                                                              | When to Read              |
| -------------------------------------------------- | -------------------------------------------------------------------- | ------------------------- |
| [STYLE_PRESETS.md](STYLE_PRESETS.md)               | 12 curated visual presets with colors, fonts, and signature elements | Phase 2 (style selection) |
| [viewport-base.css](viewport-base.css)             | Mandatory responsive CSS — copy into every presentation              | Phase 3 (generation)      |
| [html-template.md](html-template.md)               | HTML structure, JS features, code quality standards                  | Phase 3 (generation)      |
| [animation-patterns.md](animation-patterns.md)     | CSS/JS animation snippets and effect-to-feeling guide                | Phase 3 (generation)      |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | Python script for PPT content extraction                             | Phase 4 (conversion)      |
| [scripts/deploy.sh](scripts/deploy.sh)             | Deploy slides to Vercel for instant sharing                          | Phase 6 (sharing)         |
| [scripts/export-pdf.sh](scripts/export-pdf.sh)     | Export slides to PDF                                                 | Phase 6 (sharing)         |

## Learned Presentation Rules (from user corrections)

1. Never same layout twice in a row. Vary: stat, image-dominant, centered, grid, full-bleed.
2. Max 2-3 sentences per slide. More = split into another slide.
3. Every slide needs a relevant image. Not just product shots.
4. Use REAL images from client websites. Verify URLs load (200 status).
5. Never cram multiple concepts into one slide. Each concept = own slide.
6. Include brand logos when referencing specific tools (ChatGPT, Claude, Facebook).
7. Text overlay on dark images is unprofessional. Use side-by-side layouts instead.
8. Explain WHY to non-technical audiences. Plain English.
9. Organize endings: System Overview > Roadmap > Compensation > Close.
10. Never fabricate quotes from real people.
11. NEVER use generic icon placeholders (play-button rectangles, silhouette boxes, fake search results) when the slide cites a specific real-world visual AND an image generator (Gemini) is available. Generate the actual visual. Decision rule: generic UI element (button, browser frame) → CSS mockup OK; specific real-world content (a particular photo, brand page, product UI) → MUST generate.
12. NEVER rebuild a slide from scratch in response to an ADD request. List existing elements first, decide keep/modify/remove for each with stated reason. ADD does not mean REPLACE. Deleting validated content because "the new thing covers it" is the #1 regression pattern.
13. NEVER use a fake browser tab labeled with a company name as a stand-in for the brand's logo. The slide must show the actual brand mark (drawn inline as SVG if no fetch is possible).
14. NEVER cite niche industry brands when household-name brands exist for the same proof point. For "small change → big lift" examples: Obama 2008, Microsoft Bing, Basecamp/37signals beat comScore, Veeam, etc.
15. NEVER use marketing jargon ("CTA", "conversion rate") with non-marketer audiences. Plain English only: "sign-up button", "sign-ups", "people who clicked Buy".
16. NEVER ship a "tiny color difference" / "subtle change" slide without prominent hex swatch chips visible AT THUMBNAIL SCALE. The change must be visible to the eye, not just described in text. Make the BEFORE swatch dim/desaturated and the AFTER swatch vibrant with an accent ring.
17. NEVER spread credentials across 5+ slides when ONE compressed credibility slide hits harder. Pick the strongest 4-5 bullets, put them next to a portrait, move on.
18. NEVER pass a sub-3KB file with a `.png` extension to the Read tool. It is an HTML error page from a failed fetch. Run `file path.png` first. If 2 image fetches fail, switch immediately to inline SVG/CSS mockups.
19. NEVER spawn parallel headless Chrome instances for visual QA (>3-4 simultaneously). Hangs the bash tool. Run sequentially in a for-loop.
20. NEVER outsource visual QA to the user. After ANY slide edit, render at 1920x1080 and READ the screenshot yourself. Check the SPECIFIC criterion the slide is making (e.g., for "tiny color difference" slide, check that the difference is visible — don't just check "looks professional").
21. NEVER use a 3-column parallel triptych when the items share a causal/sequential/pattern-demonstrating relationship. Parallel columns hide causation. Use a roadmap grid (stage-column headers + per-instance rows + arrows between cells + highlighted outcome column). Decision rule: read the slide aloud — "and ALSO this" = triptych OK; "they ALL followed the same path" = roadmap required; "first X, then Y" = numbered timeline; "A vs B" = split-screen.
22. NEVER attribute a verbatim quote to a real person without verifying against the actual source transcript. Perplexity fabricates URLs and conflates speakers (e.g., a podcast DISCUSSING Hormozi's frameworks is NOT Hormozi). Pipeline: (a) Perplexity → candidate, (b) `curl youtube.com/oembed?url=X&format=json` to verify the channel matches the claimed speaker, (c) `~/Library/Python/3.10/bin/yt-dlp --write-auto-sub --skip-download --sub-format vtt --sub-lang en URL` to download transcript, (d) grep transcript for keywords, (e) extract VERBATIM (no paraphrase). 2 failed source verifications → cut the quote slide entirely or write the principle in user's voice (no attribution).
23. NEVER skip a "Why?" question raised by the prior slide. If slide N ends with "Why?", "How?", or any open question, the next slide MUST answer it explicitly before pivoting. Common failure: slide 3 asks "Why?" and slide 5 launches into "Three problems" without an answer slide between. Insert the bridge slide.
24. NEVER write surface-symptom bullet lists for "problem" slides. "You forget to cross-post" is surface; "you ignore the DMs from people who actually commented, you don't track which platform converts, you don't study what's already working for competitors" is diagnosis. Diagnose the actual failure mode, not the obvious one.
25. NEVER reach for the visually-safe layout when the argument needs a clarifying layout. Triptych is the cheapest layout for "3 things"; it costs argument clarity when items share meaning. Pre-ship test: does the visual structure SHOW the argument, or does it hide it behind text claims?
26. NEVER use a generic stock-image placeholder when the slide's job is to be SPECIFIC proof. If the slide says "creators with millions of followers can't sell," the image must be a SPECIFIC documented case (e.g., the Arii/PerthNow headline screenshot), not a generic graphic. Same rule as #11 generalized to any "evidence" slide.
27. NEVER stack multiple instances of the same causal pattern on one slide. One clean instance + the universal principle statement beats three instances. More evidence = more cognitive load, not more credibility. When migrating from a bad layout (e.g. triptych) to a better layout (e.g. roadmap), strip to the MINIMUM that communicates the mechanism. Don't conserve the old content count. Pattern-demonstration slides teach the PATTERN, not the roster of instances.
28. NEVER declare a text-heavy slide done by checking "does it render cleanly." Screenshots at 1920x1080 CROP overflow — text below the fold is invisible in the screenshot. Specifically verify the LAST CHARACTER of source text is within the frame with ~80px breathing room below. Content density rules of thumb for .split two-col slides: body max 3-4 sentences (~220 chars), kicker max 1 line, total vertical text space ~720px after padding. When adding new content to an existing slide, RE-RUN the overflow check — content additions don't shrink existing content automatically.

---

## PRE-SHIP LAYOUT CHECK (run BEFORE writing slide HTML)

Before committing to a layout, answer these 4 questions out loud:

1. **What is the slide's argument in one sentence?** ("Three creators all followed the same content → outcome path." / "Designer takes 6 weeks; marketer + AI takes 40 minutes." / "comScore added one element near a button and lift was 69%.")

2. **What kind of argument is it?**
   - Multiple instances of the SAME mechanism → roadmap grid (stage headers + per-instance rows + arrows)
   - Comparison of TWO things → split-screen
   - Sequential progression → numbered timeline with arrows
   - Single-item with breakdown → hero + supporting bullets
   - Truly parallel unrelated items → triptych OK

3. **What single visual would PROVE the argument?**
   - Specific real-world artifact (campaign photo, screenshot, brand mark) → generate via Gemini or fetch
   - Generic diagram (icon, illustration of concept) → CSS/SVG inline
   - Abstract atmospheric mood → use sparingly, only for transition slides

4. **What's the ANTECEDENT?** Read the prior slide. Does this one bridge from it cleanly? If prior slide ended with a question, does this one answer it?

If any of the 4 questions don't have a confident answer, STOP and ask the user before building.

---

## VISUAL SELF-QA (MANDATORY before reporting done)

**After generating any HTML, PDF, slide, chart, or image output, you MUST render it and READ the result with your vision tool BEFORE reporting done.** Never ask the user to verify what you can verify yourself. Running `open` to launch Preview is NOT verification.

**Commands:**

```bash
# HTML -> PNG (no visible browser)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless --disable-gpu \
  --screenshot="/tmp/verify.png" --window-size=1440,1800 \
  "file:///absolute/path/to/file.html"

# PDF -> PNG, multi-page, 150 DPI (optimal for AI vision)
pdftoppm -r 150 -png input.pdf page
# produces page-1.png, page-2.png, page-3.png, ...
```

Then use the `Read` tool on each PNG. Check for: page-break splits (cards cut in half), text overflow, misaligned elements, missing images, color/contrast issues, wrong fonts, responsive regressions. If any issue found: fix source, re-render, re-verify. Only report done when rendered output is correct.

**Full protocol:** `~/.claude/knowledge/visual-self-qa-protocol.md`
**Rule origin:** 2026-04-12 PDF proposal card split across page break, caught by user. Never again.
