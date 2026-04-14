# Visual Self-QA Protocol

**This is the canonical source of the visual verification rule used across all skills that produce HTML, PDF, slide, chart, or image output.**

## The Rule

**Before reporting any visual output as "done," Claude must render it to PNG and read the image with its own vision tool.** Never rely on the user to spot errors. Never trust "the HTML parses" as evidence that it "looks right."

## Why This Exists

Originated 2026-04-12: a PDF proposal was generated where a card split across a page break. The HTML was syntactically fine, Chrome PDF export succeeded, but the visual output had a broken card. The error was invisible until the user caught it. Root cause: Claude never looked at the rendered output.

## The Commands (all CLI-only, no visible browser)

### HTML → PNG

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless \
  --disable-gpu \
  --screenshot="/tmp/verify.png" \
  --window-size=1440,1800 \
  "file:///absolute/path/to/file.html"
```

- Runs in ~200-500ms, no visible browser window.
- `--window-size=1440,1800` is the sweet spot for layout error detection (adjust for mobile or slide dimensions).
- Works for HTML, CSS, inline SVG.

For full-page rendering (captures content below the fold), use `--print-to-pdf` to a temp PDF, then pdftoppm (see below).

### PDF → PNG (multi-page)

```bash
pdftoppm -r 150 -png input.pdf page
# Produces page-1.png, page-2.png, page-3.png, ...
```

- `-r 150` is 150 DPI, optimal for AI vision models.
- Available at `/opt/homebrew/bin/pdftoppm` on macOS.
- Alternative (faster, higher fidelity): `mutool convert -o out_%d.png -r 150 input.pdf` (requires `brew install mupdf-tools`).

### Image (PNG/JPG) — no conversion needed

Use `Read` directly on the file.

## The Workflow

1. Generate the HTML, PDF, chart, or image output.
2. Convert to PNG using commands above.
3. Use the `Read` tool on each PNG to visually inspect.
4. Classify any errors found:
   - **Page-break splits** (cards/sections cut in half across PDF pages)
   - **Text overflow** (text spilling outside containers, clipped at edges)
   - **Misaligned elements** (wrong indentation, broken grid, overlapping blocks)
   - **Color/contrast issues** (unreadable text, wrong palette applied)
   - **Missing images** (broken image icons, failed asset loads)
   - **Wrong fonts** (system fallback applied, inconsistent typography)
   - **Responsive regressions** (mobile view broken when desktop is fine)
5. If any error: fix the source, re-render, re-verify.
6. Only report done once the rendered output is correct.

## Optimal Image Parameters for AI Vision

| Target | Dimensions | DPI |
|---|---|---|
| PDF pages | — | 150 DPI via `-r 150` |
| HTML desktop view | 1440x1800 | default |
| HTML mobile view | 390x844 | default |
| Slides (16:9) | 1920x1080 | default |
| Instagram carousel | 1080x1350 | default |
| Fine typography review | double the above | 300 DPI |

## When This Rule Applies

Any skill that produces:
- HTML pages, emails, blog posts, landing pages
- PDF proposals, reports, certificates
- HTML presentations or slides
- Charts (SVG, inline HTML)
- Generated or manipulated images
- Next.js / React rendered output
- Email HTML templates

## When This Rule Does NOT Apply

- Pure text output (markdown, JSON, code)
- Analytical reports with no visual formatting
- CLI tool output
- Test results (unless they include visual diffs)

## Installation Check

Run this once to confirm tooling is present:

```bash
ls /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome && \
which pdftoppm && \
echo "Visual Self-QA tooling ready"
```

If missing: `brew install poppler mupdf-tools` (Poppler provides pdftoppm, MuPDF provides mutool).

## Research Citation

Protocol derived from Perplexity research 2026-04-12 (see `~/.claude/knowledge/perplexity_research_database.md` entry "Programmatic visual self-verification for AI coding agents"). Chrome headless wins on speed + native install. pdftoppm wins on ubiquity (already available). 150 DPI is the vision-model sweet spot.
