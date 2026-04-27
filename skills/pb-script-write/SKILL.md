---
name: pb-script-write
description: Phase 2 of Harrison Ball's Precision Brass YouTube content engine. Generates a full filming-ready script for a single idea picked from the pb-script menu. Outputs a colorful, scannable HTML doc + PDF (saved to project output AND ~/Downloads/) with the proven 7-beat interleaved structure (Cold Open + Hook, Demo, Apparatus Reveal, Mistake 1 / Mistake 2 / Mistake 3 each woven trap+mistake+test, Funnel). Follows Harrison's voice fingerprint (second-person, "Now,", "right?", repetitions, mid-sentence metaphors) modeled on the $36K embouchure converter. Funnel always points to the embouchure video using the converter's "Hint:" pattern. Use this skill IMMEDIATELY after Timo picks an idea from the pb-script menu (replies with "idea N", "go with #N", "let's do that one", "do the mouthpiece one", or any selection from the menu). Also use whenever Timo says "write the script", "make the script", "draft the script", "phase 2", "/pb-script-write", "now write it", "do it", "let's go on idea X", or names a specific idea title from a recent pb-script run and asks for the script. ALWAYS load the reference files before drafting (`references/example-mouthpieces-script.md`, `references/script-writing-protocol.md`, the project memory file `feedback_script_writing_lessons.md`, and the converter transcript at `Precision-Brass/references/converting-video-embouchure-transcript.md`). Do NOT skip the references. They contain the failure modes that cost 12 iterations on the first script. The skill ships an HTML+PDF deliverable. Not text-only.
---

# pb-script-write. Phase 2: Filming-Ready Script Generator

## When to fire

- Auto: immediately after pb-script outputs the 5-idea menu and Timo replies with a selection ("idea 1", "go with #2", "let's do the mouthpiece one", etc.)
- Manual: any time Timo says "write the script", "make the script", "/pb-script-write", "phase 2", "draft the script for X"

## Hard preconditions (do not skip)

Before drafting a single line, READ all of these:

1. `references/example-mouthpieces-script.md`. Proven 7-beat structural template.
2. `references/script-writing-protocol.md`. Full ruleset. 14 failure modes. Voice fingerprint. Funnel pattern.
3. `references/funnel-layers.md`. TOFU/MOFU/BOFU layer spec. Read this to confirm pain depth, identity load, CTA destination, and structural template based on the picked idea's layer.
4. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_script_writing_lessons.md`. Project-level failure memory.
5. `/Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md`. Source-of-truth Harrison voice.

Skipping these = repeating the 12-iteration mistake from 2026-04-25.

## Funnel layer adaptation (mandatory)

The picked idea carries a TOFU/MOFU/BOFU label from the pb-script menu. Read it. The layer determines:
- **TOFU**: light pain depth, no comeback/age callout, broad curiosity hook, lighter 5-7 beat structure, CTA = subscribe / next video.
- **MOFU**: specific named mistakes, comeback/age callout in hook, 7-beat interleaved template, CTA = next-deeper video.
- **BOFU**: surgical pain depth (comeback grief, age anxiety, failed-method shame), maximum identity load, full 12-move converter template, CTA = strategy call.

If the picked idea has no layer label (older menus or manual invocations), ask Timo for the layer BEFORE drafting. Don't assume.

## The 7-beat interleaved structure (default)

| Beat | Color | Title | Function |
|---|---|---|---|
| 01 | Coral #E63946 | Cold Open + Hook | Visual gag + locked hook + comeback/age callout + demo promise |
| 02 | Blue #2563EB | The Demo | Part 1 (same content, multiple cups) + Part 2 (shitty setup) |
| 03 | Green #059669 | Apparatus Reveal | Mouthpiece reframe -> BEAT -> apparatus reveal -> definition |
| 04 | Mustard #D97706 | Mistake 1: [Name] | The Trap -> The Mistake -> The Test (woven inside one beat) |
| 05 | Plum #7C3AED | Mistake 2: [Name] | Same woven structure |
| 06 | Magenta #DB2777 | Mistake 3: [Name] | Same woven structure |
| 07 | Teal #0891B2 | Funnel | Callback to tests + NEW provocation question + Hint pattern + embouchure video CTA |

**Interleaving is non-negotiable.** Each Mistake beat contains The Trap (named topic), The Mistake (named with "the first/second/third mistake"), and The Test (visual + riff) in one cycle. Never stack them as separate beats.

## Voice rules

Match Harrison's converter fingerprint. Examples in `references/example-mouthpieces-script.md`:

- Second person + "we"
- Conversational fillers: "Now,", "right?", "Look,"
- Names the wrong way before the right way
- Repeats key terms 3-5 times
- Builds metaphors mid-sentence
- Confident declaratives, no hedging
- Demos woven into the talk ("If I play [demo]")

## Funnel pattern (always)

End the video with this exact structural move (modeled on the $36K converter):

1. Callback: "if you struggled with any of those tests..."
2. NEW provocation: a question the tests don't answer (e.g., "WHERE on your face is the mouthpiece supposed to sit?")
3. Hint line: "it's not where 99% of teachers tell you"
4. CTA to embouchure video: "I broke it all down in this video right here. Make sure you watch that next."

The funnel ALWAYS points to the embouchure video (`youtube-database/2026-04_embouchure-truth_O4a-q93ENAg/`) unless explicitly told otherwise.

## Output format

Generate an HTML file with this design (full template lives in `Precision-Brass/references/example-script-mouthpieces.html`):

- Single column, max-width 760px
- Warm off-white bg #FAF7F2, near-black text #1A1A1A
- Inter sans-serif (22px body, 38px beat titles)
- Beat number in filled colored tile (64x64px, 14px radius)
- 🎥 emoji + colored ACTION pill for visual blocks
- 💬 emoji marker before script blocks
- Section labels (THE 99% LIE, etc.) in beat-color caps, no fills
- Script paragraphs flow with whitespace, no boxes
- CSS: `break-inside: avoid` on `.script` paragraphs to prevent mid-paragraph page breaks

Then convert to PDF via Chrome headless and save BOTH HTML+PDF to ALL THREE locations:

1. `/Users/air/Desktop/Precision-Brass/scripts/YYYY-MM-DD_<slug>.{html,pdf}` (CANONICAL ARCHIVE. always go here. see `project_scripts_archive.md` memory)
2. `/Users/air/Desktop/Precision-Brass/output/YYYY-MM-DD_<slug>.{html,pdf}` (working copy)
3. `~/Downloads/YYYY-MM-DD_<slug>.{html,pdf}` (fast handoff per `feedback_pdfs_to_downloads.md`)

After saving, append a row to `Precision-Brass/scripts/README.md` index table with date / slug / topic / status.

## What goes where

- **Locked lines** (italic, must be verbatim): cold open hook, apparatus reveal line, mistake callouts ("That's how you fall into the first/second/third mistake..."), funnel CTA close.
- **Riff topics** (regular weight, director's notes): trap explanations, mistake elaborations, test riffs. Harrison improvises off these.
- **Visual specs**: preserve EXACTLY as Timo writes them. If he says "Harrison sitting in front of all his mouthpieces", that detail is mandatory. Don't compress it.
- **[HARRISON FILLS]**: tag specific gear / tunes / student names that need Harrison's input. Do not invent.

## Hard rules (do NOT break)

These come from the 2026-04-25 iteration. Each was flagged repeatedly:

1. NO paragraphs of explanation. Bullet director's notes only.
2. NO summarizing Timo's locked lines. Verbatim or nothing.
3. NO dropping visual specs. Preserve them exactly.
4. NO stacking mistakes/tests as separate beats. Always interleave inside the trap beat.
5. NO fabricated stats, social proof, or behavioral claims. Open knowledge gaps, do not invent answers.
6. NO meta-instructions inside the deliverable ("send to Timo", "Harrison fills" lists go in conversation, not on the page).
7. NO third-person clinical register. Always second-person, conversational.
8. NO over-fragmenting. Beats hold many sentences that flow together. Don't make every line its own shot.
9. NO regression. Once Timo corrects something, it stays corrected.
10. NO manhandling Harrison's improv. Locked lines for critical moments, riff topics for the rest.
11. NO mid-paragraph PDF breaks. CSS must protect script blocks.
12. NO design over readability. Script is the hero. No yellow speech bubbles, no italic body, no chat-bubble metaphor.
13. NO em dashes anywhere (project hook blocks them).
14. NO inventing named mistakes from thin air. Pull from corpus or extend a pattern Timo has accepted.

## Workflow

1. **Detect dashboard mode.** If invoked with `/pb-script-write i_YYYYMMDD_slug`, this is a dashboard-driven run. Fetch the originating idea from Supabase first:
   ```bash
   source ~/.claude/secrets/precision-brass.env
   curl -s "${SUPABASE_URL}/rest/v1/ideas?id=eq.{idea_id}&select=*" \
     -H "apikey: ${SUPABASE_SECRET_KEY}" \
     -H "Authorization: Bearer ${SUPABASE_SECRET_KEY}"
   ```
   Use the idea's title, pain_point, hook_angle, voc_quotes, source_tags as the conversion-trigger context. If status is not `idea_approved`, STOP and tell Timo (e.g. already scripted, or Harrison hasn't greenlit yet).
2. Confirm the picked idea title and conversion trigger (carry over from pb-script output OR from fetched idea)
3. READ all 4 reference files (preconditions above)
4. Outline the 7 beats. Name the 3 mistakes from the corpus or extend a Timo-approved pattern.
5. Draft each beat in Harrison's voice with the locked-lines / riff-topics split
6. Generate the HTML using the proven aesthetic spec
7. Render PDF via Chrome headless, run visual QA on PNG export of each page
8. Copy HTML+PDF to BOTH project output AND ~/Downloads/
9. **Upload to Harrison's dashboard (REQUIRED in dashboard mode).** Build a script payload with the body filled in, POST to Supabase, then mark idea as scripted. See "Dashboard upload" below.
10. Report file paths AND dashboard link to Timo. Offer to iterate on any beat.

## Dashboard upload (step 9 detail)

Two uploads happen: (1) the PDF goes to Supabase Storage so Harrison can download it, (2) the rich HTML body + PDF URL go into the script row so the dashboard renders the script in-modal AND shows a Download PDF button.

### 9a. Upload the PDF to Supabase Storage

```bash
source ~/.claude/secrets/precision-brass.env
PDF_PATH="/Users/air/Desktop/Precision-Brass/scripts/{filename}.pdf"
PDF_REMOTE="{filename}.pdf"   # e.g. 2026-04-27_lip-bruise.pdf
curl -s -X POST "${SUPABASE_URL}/storage/v1/object/scripts/${PDF_REMOTE}" \
  -H "apikey: ${SUPABASE_SECRET_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SECRET_KEY}" \
  -H "Content-Type: application/pdf" \
  --data-binary @"${PDF_PATH}"
PDF_URL="${SUPABASE_URL}/storage/v1/object/public/scripts/${PDF_REMOTE}"
```

If the file already exists, use PUT instead of POST (or DELETE first). Verify the URL responds 200 before continuing.

### 9b. Build the script row payload

The `body` field is a JSON array with **a single entry containing the full rich HTML AND the PDF URL** (so the dashboard renders the script in-modal AND shows a Download button):

```json
"body": [{
  "type": "html_full",
  "content": "<full <body> innerHTML of the script HTML file>",
  "pdf_url": "https://YOUR-PROJECT.supabase.co/storage/v1/object/public/scripts/{filename}.pdf"
}]
```

This is how Harrison sees the same colorful 7-beat layout (action blocks, script markers, color-coded beats) inside the dashboard modal that he'd see in the local PDF. Reference: `Precision-Brass/scripts/2026-04-25_stop-buying-mouthpieces.html` shows the exact structure to produce.

To extract the body HTML for upload:
```bash
# Pull the inner HTML between <body> and </body> from the just-written script file
HTML_BODY=$(awk '/<body>/,/<\/body>/' /Users/air/Desktop/Precision-Brass/scripts/{filename}.html | sed -e 's/<\/\?body[^>]*>//g')
# Use python3 to JSON-encode it cleanly into the payload
python3 -c "
import json, sys
with open('$HTML_PATH') as f:
    body = f.read().split('<body>')[1].split('</body>')[0]
payload = {
  'id': '$SCRIPT_ID',
  'idea_id': '$IDEA_ID',
  'title': '$TITLE',
  'delivered': '$TODAY',
  'length': '$LENGTH',
  'sections': 7,
  'pain_point': '$PAIN',
  'hook': '$HOOK',
  'status': 'pending',
  'body': [{'type': 'html_full', 'content': body}],
  'history': [{'type':'delivered','who':'Timo','text':'<b>Script written</b> from idea','time':'$NOW'}]
}
with open('/tmp/script_payload.json','w') as f:
    json.dump(payload, f)
"
```

Then POST to Supabase:

```bash
SCRIPT_ID="${idea_id/i_/s_}"
# Construct /tmp/script_payload.json with title, body[], status="pending", idea_id, etc.
# Then POST:
curl -s -X POST "${SUPABASE_URL}/rest/v1/scripts" \
  -H "apikey: ${SUPABASE_SECRET_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SECRET_KEY}" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  --data-binary @/tmp/script_payload.json
# Then PATCH the idea to scripted (removes from Timo's "Ideas Approved" column):
curl -s -X PATCH "${SUPABASE_URL}/rest/v1/ideas?id=eq.${idea_id}" \
  -H "apikey: ${SUPABASE_SECRET_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_SECRET_KEY}" \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"scripted\"}"
```

### Script row schema

| Field | Source |
|---|---|
| id | `s_YYYYMMDD_slug` (replace `i_` with `s_`) |
| idea_id | The originating idea_id |
| title | Idea title |
| delivered | Today's date (YYYY-MM-DD) |
| length | e.g. `8 min final. ~1,400 words` |
| sections | Number of beats (typically 7) |
| pain_point | From idea |
| hook | The hook line from beat 1 |
| status | `pending` |
| body | JSON array of `{kicker, time, heading, copy, visual}` per beat |
| history | `[{type:"delivered", who:"Timo", text:"<b>Script written</b> from idea", time:"..."}]` |

### Dashboard-mode failure modes (do not repeat)

- **Body MUST contain real content.** Never push an empty/stub body. Harrison opening an empty script kills trust. If you can't fill the 7 beats, do not push.
- **Always do step 9b (mark idea scripted).** Otherwise the idea stays in Timo's "Ideas Approved" and confuses the kanban.
- **If the idea is not in `idea_approved`, STOP.** Don't override Harrison's state.

## Reference files (in this skill)

- `references/example-mouthpieces-script.md`. The proven structural template.
- `references/script-writing-protocol.md`. Full ruleset.

These mirror copies in `Precision-Brass/references/` so the skill works even if the project files move.

## What this skill is NOT

- Not Phase 1 (research / 5-idea menu). That's pb-script.
- Not a thumbnail / title generator (titles come WITH the structure).
- Not a teleprompter mode (the doc is for prep + filming, not live-rolling text).
- Not for short-form (long-form first per project CLAUDE.md).