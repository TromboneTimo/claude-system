---
name: score-corrector
description: Proofread large music scores (PDF sheet music) for engraving and layout defects at any scale, from 20 pages to 500+. Uses batched vision subagents so you never blow the image-token budget on long scores. Catches collisions (dynamics stacked on dynamics, accents crushing articulations, text labels jammed), spacing problems (cramped staves, hairpin collisions), layout bugs (inline staff sharing, disappearing staves, bad page turns), consistency breaks across systems, and missing elements (tempo markings, cues, courtesy accidentals). Produces an annotated PDF with colored boxes by severity plus a JSON error report and markdown summary. Use this skill any time the user says "score corrector", "correct this score", "proofread score", "proofread sheet music", "check this score", "score proofread", "find errors in score", "engraving errors", "check my score", "audit this score", "music score review", or hands you a sheet music PDF and asks what's wrong with it. Also use it whenever the user mentions proofreading a large PDF of music notation, regardless of the exact phrasing.
---

# Score Corrector

Engraving proofreader for music scores that scales to hundreds of pages by fanning out vision work to isolated subagents.

## The core problem this solves

Loading all pages of a 100-page score into a single vision call blows the image-token budget and/or exceeds the per-request image count. The previous one-shot proofreader crashed at 20 pages. This skill splits the work: each subagent sees at most 5 pages at 1024px, returns ONLY text findings, and dies. The main orchestrator aggregates text into one annotated PDF without ever seeing a page image itself.

Read these before starting any real run:
- `references/engraving-errors.md`: the complete error taxonomy and severity levels
- `references/subagent-prompt-template.md`: exact prompt sent to each vision worker

## Inputs

The user provides one of:
1. A PDF path. Skill extracts pages first.
2. An existing directory of page PNGs (like `score-proofreader/page-01.png ...`).

Optional:
- `--pages 10-20`: proofread only a range
- `--dpi 120`: reduce resolution for very long scores (default 150)
- `--batch-size 5`: pages per subagent (default 5, never exceed 5)
- `--title "..."` and `--arranger "..."`: metadata for the report

## Outputs

Written to a `score-corrector-output/` folder next to the input PDF (or a path the user specifies):
- `annotated_score.pdf`: original PDF with colored rectangles around each error, numbered badges, severity-colored
- `annotations.json`: full error list with page, measure, staff, category, severity, region coords, description, fix
- `summary.md`: human-readable report grouped by severity, with counts and a page-by-page index

## Pipeline

### Step 1: Normalize input to PNGs

If input is a PDF:
```bash
python ~/.claude/skills/score-corrector/scripts/pdf_to_pngs.py \
    INPUT.pdf OUTPUT_DIR/pngs/ --dpi 150
```

If input is a directory of PNGs, verify they're named `page-NN.png` and downscale any >1568px wide to 1024px long edge using `sips`:
```bash
for f in OUTPUT_DIR/pngs/page-*.png; do
  sips -Z 1024 "$f" --out "$f" >/dev/null
done
```

Count pages. Note the count. You'll need it for metadata.

### Step 2: Batch and spawn vision subagents

Split the page list into batches of 5. For 100 pages that's 20 batches. Spawn them in waves of 4 to 5 parallel Agent calls (so at most 4-5 subagents running at once).

For each batch, call the Agent tool with `subagent_type: general-purpose` and a prompt built from `references/subagent-prompt-template.md`. Replace `{{IMAGE_PATHS}}`, `{{PAGE_NUMBERS}}`, `{{TOTAL_PAGES}}`, and `{{SCORE_TITLE}}`.

For scores over 50 pages, add `model: "haiku"` to the Agent call to run workers on Haiku 4.5. Haiku handles per-page engraving scans at equivalent quality to Opus for this task and costs ~5x less. See "Worker model selection" below for the rule.

Tell each subagent to:
- Read the error taxonomy at `~/.claude/skills/score-corrector/references/engraving-errors.md`
- Visually inspect each PNG in the batch (this is where the subagent's Read tool consumes the images; main context never does)
- Return JSON matching the template schema
- Save the JSON to `OUTPUT_DIR/batches/batch-NN.json`

CRITICAL: tell the subagent to return only text confirming completion plus the path to the saved JSON. Never let the subagent quote back image contents or large regions of the JSON. If it does, main context bloats.

### Step 3: Merge batch JSONs

```bash
python ~/.claude/skills/score-corrector/scripts/merge_annotations.py \
    OUTPUT_DIR/batches/ \
    OUTPUT_DIR/annotations.json \
    --title "SCORE TITLE" \
    --arranger "ARRANGER NAME" \
    --total-pages PAGE_COUNT
```

This globally renumbers errors, sorts by page then severity, and adds a summary block.

### Step 4: Annotate the PDF

```bash
python ~/.claude/skills/score-corrector/scripts/annotate_pdf.py \
    INPUT.pdf \
    OUTPUT_DIR/annotations.json \
    OUTPUT_DIR/annotated_score.pdf
```

### Step 5: Write the summary markdown

Produce `OUTPUT_DIR/summary.md` with:
- Total error count by severity (pull from `annotations.json` severity_counts)
- Pages flagged for higher-res rerun (if any)
- Top 10 BLOCKERs and HIGHs with page, measure, and fix
- A line for every page that has any error
- Link to `annotated_score.pdf`

Do not include raw JSON in the summary. It's for humans.

### Step 6: Optional high-res rerun

If `annotations.json` has a non-empty `pages_needing_higher_res` array, offer to rerun those specific pages at 300 DPI:
```bash
python ~/.claude/skills/score-corrector/scripts/pdf_to_pngs.py \
    INPUT.pdf OUTPUT_DIR/pngs_hires/ --dpi 300 --pages N-M
```
Then batch those at batch-size 2 (because higher res = more tokens) and merge findings into a second annotations file.

## Guardrails (the rules this skill exists to enforce)

1. **Never load more than 5 page images into the main context.** The entire point of this skill. The user's previous proofreader crashed exactly because it tried to hold 20 images simultaneously.
2. **All image processing happens in isolated subagents.** The orchestrator sees text only. Subagent conversations die with their image tokens.
3. **Downscale to 1024px long edge before vision.** Sheet music at 150 DPI is crisp enough for engraving defects at this size. Going higher (2000px+) costs 5x the tokens for marginal accuracy.
4. **Subagents return JSON file paths, not JSON contents.** The orchestrator reads the saved files from disk, which Python parses without burning context.
5. **Proofread visual engraving only in this version.** Pitch / rhythm / harmonic errors are a v2 job that would use Audiveris to extract MusicXML first. Don't invent pitch errors from vision alone.
6. **Zero errors is a valid result.** If a page is clean, the subagent returns `errors: []`. Don't pad findings.

## When to offer Audiveris / MusicXML path (v2)

If the user asks for pitch or rhythm proofreading, tell them: this skill is vision-only for engraving defects. The v2 pipeline is documented in `references/v2-musicxml-path.md`. Short version: Audiveris converts both files to MusicXML, music21 does a semantic diff (not xmldiff, which breaks on voice ordering), and only the ambiguous 5 to 15 percent of measures get escalated to a vision subagent for cropped-measure comparison. That brings a 500-page score cost from ~$2.35 image-only to ~$0.30 hybrid.

Offer to build v2 when the user actually needs pitch/rhythm catches. Don't build it pre-emptively.

## Severity color legend (matches annotate_pdf.py)

- BLOCKER: red (must fix before distribution)
- HIGH: orange (noticeable defect)
- MEDIUM: blue (clarity improvement)
- LOW: gray (polish)

## Example invocation

```
User: "Proofread lake_input.pdf in the score-proofreader folder"

You:
1. Read error taxonomy and subagent template
2. Extract 20 pages at 150 DPI to score-proofreader/pngs/
3. Downscale any oversized PNGs to 1024px
4. Split into 4 batches of 5 pages
5. Spawn 4 parallel Agent subagents, each returning batch-NN.json
6. Merge into annotations.json
7. Render annotated_score.pdf
8. Write summary.md grouped by severity
9. Report: "Found X BLOCKERs, Y HIGHs across N pages. See annotated_score.pdf."
```

## Scaling math (worth memorizing)

Anthropic's official image token formula: `tokens ≈ width × height / 750`. At 1024×1024 that's ~1,400 tokens per image. A 5-page batch at 1024px is ~7k vision tokens plus the prompt scaffold. Plan for 8-10k total tokens per subagent call.

| Score size | Batches | Parallel waves | Vision tokens | Rough runtime | Worker model |
|-----------|---------|----------------|---------------|---------------|--------------|
| 20 pages  | 4       | 1              | ~28k          | 2 to 3 min    | general-purpose (Opus default is fine) |
| 100 pages | 20      | 5              | ~140k         | 8 to 12 min   | Haiku (5x cheaper, quality-equivalent for page-scan) |
| 500 pages | 100     | 25             | ~700k         | 40 to 60 min  | Haiku (mandatory for cost) |

## Worker model selection

For scores over 50 pages, route the batch subagents to Haiku for ~5x cost savings. Anthropic's "Split-and-Merge fan-out" pattern assumes the orchestrator is Opus-class but workers are Haiku-class, because the per-page engraving scan is a well-constrained task that Haiku handles accurately. Pass `model: "haiku"` in the Agent tool call for each batch subagent. Keep the orchestrator (this thread) on whatever model is already running; it never sees images and does pure aggregation.

For 20-50 page scores, default model is fine. The overhead of switching isn't worth it at that scale.
