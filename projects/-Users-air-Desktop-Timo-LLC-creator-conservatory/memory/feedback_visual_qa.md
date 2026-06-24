---
name: Visual Self-QA Before Declaring Done
description: Render HTML/PDF/slide/chart/image output to PNG and read it with your own vision tool before reporting done. Never rely on the user to catch visual bugs. Supersedes the earlier "open in Safari" rule.
type: feedback
originSessionId: 620203ae-1dd5-484d-9c81-6e3623000cc3
---
**After any work that produces HTML, PDF, slides, charts, or generated images, you MUST render it and read the rendered image with your own vision tool BEFORE reporting done.** Running `open` to launch Preview or Safari on the user's screen is NOT verification; that outsources QA to the user.

**Why:** Timo caught an embarrassing bug on 2026-04-12: a PDF proposal card split across a page break. The HTML was syntactically fine, Chrome PDF export succeeded, but the rendered output had a broken card. Claude never looked. Timo: "in general when making websites or making pdfs, you never look at the site itself... tell me why you are unable to see errors like this, its embarsassing."

An earlier version of this memory said "open in Safari and scroll through every slide." That was written assuming a human would check. This version fixes it: Claude uses its own vision, not the user's.

## How to Apply

1. **HTML output:** render headless to PNG.
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
     --headless --disable-gpu \
     --screenshot="/tmp/verify.png" --window-size=1440,1800 \
     "file:///absolute/path/to/file.html"
   ```

2. **PDF output:** convert each page to PNG at 150 DPI (optimal for vision models).
   ```bash
   pdftoppm -r 150 -png input.pdf page
   ```
   Produces `page-1.png`, `page-2.png`, etc. Read each one with the `Read` tool.

3. **Generated images:** Read directly, no conversion.

## What to Check in Every Render

- **Page-break splits** (cards or sections cut in half across PDF pages)
- **Text overflow** (text clipped or spilling outside containers)
- **Misaligned elements** (broken grid, overlapping blocks)
- **Color/contrast issues** (unreadable text, wrong palette applied)
- **Missing images** (broken asset loads)
- **Wrong fonts** (system fallback applied, inconsistent typography)
- **Stat card overflow** (numeric sizing applied to long text phrases — still a real risk, see original bug)
- **Responsive regressions** (check mobile viewport separately when applicable)
- **Parent flex/padding/gap squishing child** (2026-04-13: swapped a placeholder `<div>` for an `<img>` and the parent `.cred-portrait` flex+padding+gap left the image tiny inside empty bordered box. Lesson: when overriding a placeholder class, override flex/gap/padding/display too, don't just change border and aspect-ratio)

## Scroll-Snap Presentations

Scroll-snap presentations don't render cleanly in headless mode (only one slide shows). Workaround: write a flattened version NEXT TO the original (so relative image paths resolve) with this injected CSS:
```html
<style>
html, body { scroll-snap-type: none !important; overflow-y: visible !important; }
.slide { scroll-snap-align: none !important; height: auto !important; min-height: 900px; display: block !important; }
.reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-blur { opacity: 1 !important; transform: none !important; }
</style>
```
Then screenshot at window-size 1440x9000, crop each slide at y = index * 900.

## Process

1. Generate output
2. Render to PNG
3. Read each PNG with vision
4. Fix any issue in source
5. Re-render
6. Re-verify
7. Only then report done

## Zero Exemptions (2026-04-13)

Timo: "so never do that again." No task is too trivial to skip this. Not a photo swap. Not a CSS tweak. Not a one-line change. If the judgment call is "this is simple enough to skip QA," the judgment itself is the bug. That's why the rule exists - past me repeatedly mis-calibrated "simple."

## Applies To These Skills

All have inline Visual Self-QA reminders as of 2026-04-12: frontend-slides, marketing-present, marketing-data, blog, blog-write, blog-rewrite, blog-chart, blog-image, marketing-blog, manipulate-image, clone-website, email, cc-email, rr-email.

## Canonical Protocol

`~/.claude/knowledge/visual-self-qa-protocol.md` — full commands, alternative tools (mutool, Playwright, Chrome `--print-to-pdf`), optimal dimensions per output type, installation check.

## Research Backing

Perplexity 2026-04-12 (DB entry "Programmatic visual self-verification for AI coding agents"): Chrome headless wins on speed + native install, pdftoppm wins on ubiquity, 150 DPI is the vision-model sweet spot for detecting layout errors.
