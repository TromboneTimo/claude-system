---
name: pb-ideas-push
description: Phase 1.5 of Harrison Ball's Precision Brass YouTube content engine. Pushes Timo-approved video ideas from the pb-script chat conversation into the Supabase-backed dashboard so Harrison can review them at dashboard/scripts.html. Takes the ideas Timo greenlit (e.g. "push idea 2 and 4 to the dashboard", "send these to harrison", "upload the chops idea") and inserts them into the ideas table with status=idea_pending. Each idea includes title, pain point, hook angle, 1-paragraph rationale, VOC quote evidence, and source tags. After Harrison greenlights an idea on the dashboard, Timo runs pb-script-write on the approved idea ID. Use this skill any time Timo says "push to dashboard", "send to harrison", "upload these ideas", "queue these for harrison", "/pb-ideas-push", or after a pb-script run when Timo picks 1+ ideas to send for review.
---

# pb-ideas-push. Phase 1.5: Push Ideas to Harrison's Dashboard

## OPERATING PRINCIPLE: Ship right, never ship fast.

Speed is never the priority for this skill. Timo writes proposals carefully. Each section he labels carries information Harrison needs. Dropping any section, summarizing instead of preserving, or shipping incomplete work and waiting for Timo to catch it is a contract violation more severe than any formatting bug or timing issue.

If I am tempted to "just push and we will iterate," that is the failure mode. STOP and run the preflight enumeration below first. Asking Timo a clarifying question takes 5 seconds. Recovering from a silent drop takes 30 minutes of trust damage and is unacceptable.

This principle is also stored in `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_ship_right_not_fast.md` and loads on every session.

## What this does

Bridges `pb-script` (Phase 1, brainstorm in chat) and `pb-script-write` (Phase 2, full filming script). Pushes Timo-approved ideas into the Supabase `ideas` table so Harrison sees them on `Precision-Brass/dashboard/scripts.html` in the "Ideas Pending" column.

Harrison greenlights → idea moves to "Ideas Approved" → Timo runs `pb-script-write` → full script lands in "Script Pending".

## When to fire

Trigger when Timo says (after a `pb-script` run):
- "push idea 2 to the dashboard"
- "send ideas 1 and 3 to harrison"
- "upload these"
- "queue these for harrison's review"
- "/pb-ideas-push"
- "ship the chops one to the dashboard"

Do NOT fire if Timo has not yet seen ideas in chat. Run `pb-script` first.

## Two input modes

### Mode A: Casual chat ideas (post-`/pb-script` brainstorm)
Pull each greenlit idea from prior conversation context. Map to the schema below.

### Mode B: Structured script proposal (Timo pastes a "Script Proposal N" doc)
The proposal has these labelled sections: Layer, Idea origin, Concept (with Rough flow), The wound we're naming, Why this will convert, Source evidence (with attributed quotes), ICP segment target, How this video connects to Harrison's existing channel.

Parse those sections into the schema. The `rationale` field is composed as styled HTML with 5 colored section blocks (see template below).

## Schema mapping

| Field        | Source                                          | Required |
|--------------|-------------------------------------------------|----------|
| id           | `i_{YYYYMMDD}_{slug}` from title                | yes      |
| title        | The idea title                                  | yes      |
| pain_point   | 1-line summary of "The wound" or pain named     | yes      |
| hook_angle   | identity / failed-method / specific-result / curiosity / money | yes |
| rationale    | HTML with 5 colored sections (Mode B) OR 1 paragraph (Mode A) | yes |
| voc_quotes   | array of `{text, source}`. Source line includes name + age + call type + conversion data when available | yes |
| source_tags  | array of lowercase tags: layer (mofu/tofu/bofu) + corpus tags (won-deals, sales-calls, yt-comments, fb-winners, etc.) | yes |

If any required field is missing, ask Timo. Never invent VOC quotes (4 failure patterns: prospects ≠ customers, auto-transcripts lie).

## Funnel layer (REQUIRED)

Every idea MUST include exactly one of `mofu`, `tofu`, `bofu` as the FIRST tag in `source_tags`. The dashboard renders this as a prominent funnel badge near the title and a small pill on the list row. If the proposal has a "Layer:" line, copy that value.

## ZERO-DROP CONTRACT (READ BEFORE PUSHING)

Timo's proposals are the source of truth. **Every labeled section in his input MUST appear on the dashboard.** Silent omission is the highest-severity failure mode for this skill, ranked above formatting issues, above timing, above everything.

### Mandatory preflight before any curl POST

Run this check OUT LOUD to Timo (write it in chat) before pushing:

1. **Dedup check FIRST.** Before mapping anything, GET the current ideas table:
   ```bash
   source ~/.claude/secrets/precision-brass.env
   curl -s "${SUPABASE_URL}/rest/v1/ideas?select=id,title" \
     -H "apikey: ${SUPABASE_PUBLISHABLE_KEY}" \
     -H "Authorization: Bearer ${SUPABASE_PUBLISHABLE_KEY}"
   ```
   For each new proposal, check:
   - Exact id collision (same `i_YYYYMMDD_slug`)
   - Title similarity (3+ overlapping non-stopword tokens with existing title, OR same core noun phrase)
   - **DEFAULT: silently skip duplicates and proceed with the rest.** Per Timo's standing rule (2026-04-26): "always skip the duplicates, always, don't ask, remember that." Do NOT ask per-dup. Note the skip in the preflight summary and move on. Only ask if Timo has explicitly said earlier in the same session "ask me about dups this time."
2. **Enumerate**. List every labeled section heading in his proposal text. Examples: Layer, Idea origin, Concept, Rough flow, The wound we're naming, Why this will convert, Source evidence, What these quotes show together, ICP segment target, How this video connects to Harrison's existing channel.
3. **Map**. For each enumerated section, name the destination in the schema (rationale section class, voc_quotes, source_tags, pain_point, hook_angle, etc.).
4. **Account for every word**. If any section in the input has no mapping destination, STOP. Ask Timo where it should go or whether to add a new section. Do not push.
5. **Show Timo the map**. Display dedup result + enumeration + mapping as a numbered checklist in chat. Wait for explicit "go" before curling.

### Example preflight (do this in chat)

```
Proposal sections found:
1. Layer: MOFU                          → source_tags[0]
2. Idea origin                          → rationale .origin
3. Concept (incl. Rough flow + promise) → rationale .concept
4. The wound we're naming               → rationale .wound
5. Why this will convert                → rationale .why
6. Source evidence (5 quotes)           → voc_quotes[]
7. What these quotes show together      → rationale .synthesis
8. ICP segment target                   → rationale .icp
9. How this video connects              → rationale .channel

Every section accounted for. Push? (y to proceed)
```

If Timo's proposal has a section not in this list (e.g. "Production notes", "B-roll requirements"), surface it: "I don't have a mapping for X. Add it as a new colored section, append it to an existing one, or skip?"

## Rationale HTML template (Mode B)

Use these 7 section classes in this order (updated 2026-04-26 per Timo). Dashboard CSS colors them per section.

**MANDATORY sections in this exact order** (every proposal push includes ALL that are present in the input). Updated 2026-04-26 per Timo's correction.

**Rationale top half (renders BEFORE the voc-quotes block):**
1. `origin`    Idea Origin (where this came from, why the format works)
2. `why`       Why This Converts
3. `concept`   The Promise
4. `wound`     The Wound

**Voc quotes render here** (auto-injected by dashboard between the two rationale halves).

**Rationale bottom half (renders AFTER the voc-quotes block):**
5. `synthesis` What These Quotes Show Together (sits directly under the quotes)
6. `channel`   Channel Connection
7. `icp`       ICP Target (LAST. final section in the card)

The dashboard splits the rationale at the first `<div class="r-section synthesis"` tag, renders the top half, then renders the voc quotes, then renders the bottom half. Build the rationale HTML in the order above and the split happens automatically.

If the proposal includes ANY of these, push ALL of them. Dropping one without explicit Timo approval is a contract violation.

**Plain-language standard for `why` (REQUIRED).** No internal jargon. No "converter", "the corpus", "the voice bank", "the database", "failed-method-grief", "BOFU floor", or similar dev-speak. No hallucinated market-positioning claims like "the X wars" without evidence. Every bullet must answer "what makes a viewer book a strategy call after watching this?" using plain English with concrete evidence (a real student, a real ad, a real testimonial, a real won deal amount). See `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_no_internal_jargon_in_rationale.md`.

```html
<div class="r-section origin">
  <span class="r-kicker">Idea Origin</span>
  <p>{Idea origin paragraph from proposal. Where this came from in the VOC corpus, why the title format works.}</p>
</div>
<div class="r-section concept">
  <span class="r-kicker">The Promise</span>
  <p>{Concept paragraph from proposal. End with the hook line as a separate <p> with <strong>Hook:</strong> prefix.}</p>
</div>
<div class="r-section wound">
  <span class="r-kicker">The Wound</span>
  <p>{The wound paragraph from proposal.}</p>
</div>
<div class="r-section why">
  <span class="r-kicker">Why This Converts</span>
  <ul>
    <li>{Why-this-converts bullet 1}</li>
    <li>{Why-this-converts bullet 2}</li>
    <li>...</li>
  </ul>
</div>
<div class="r-section icp">
  <span class="r-kicker">ICP Target</span>
  <p>{ICP segment target paragraph.}</p>
</div>
<div class="r-section channel">
  <span class="r-kicker">Channel Connection</span>
  <p>{How this connects to Harrison's existing channel.}</p>
</div>
<div class="r-section synthesis">
  <span class="r-kicker">What These Quotes Show Together</span>
  <p>{First paragraph: name each quote-giver and what they reveal.}</p>
  <p><strong>The pattern:</strong> {The synthesis insight from the proposal.}</p>
</div>
```

Important: write the rationale as a SINGLE-LINE JSON-safe HTML string. Inside JSON, escape inner `"` as `\"`. NEVER use em dashes (project rule). Replace any em dash with `,` or `.` or `:`.

## VOC quote source attribution

Every quote must trace to a real source. Format the `source` field richly:
- Sales call quotes: `"{Name}, age {N}. Sales call {context}. Signed up for ${amount}."` (or "Did not sign up" / "Pending")
- Testimonial quotes: `"{Name}. Video testimonial after working with Harrison, describing {context}."`
- Public YouTube/FB comments: `"{Username}. Public YouTube comment."` or similar
- DMs: `"{Name}. Instagram DM, {date}."`

If the proposal's "Source evidence" section already includes attribution, copy it verbatim.

## MANDATORY MINIMUM SOURCING (added 2026-04-26)

Every `voc_quotes` array MUST include at least:
1. **One quote from a testimonial** (someone who worked with Harrison and recorded a video testimonial). Source: `voc/raw/testimonials/`.
2. **One quote from a sales call** (someone Harrison did a discovery call with). Source: `voc/raw/sales-calls/`.
3. Comments / DMs / ads are supplementary, not required.

If either is missing, STOP and pull a real quote from the corpus before pushing. Do not skip this check.

## Harrison-quote conversion-lens rule (added 2026-04-26)

If a quote in the array has Harrison as the speaker (his own ad copy, his own video transcript, his own social post), the `source` field must do two things:
1. Name the source (which ad, which video, which post).
2. Explain WHY that language is causing people to convert. What permission does it grant? What reframe does it land? What audience reaction does it trigger?

Without the conversion lens, Harrison-quotes are self-citation. Bad example: `"Harrison Ball's own Facebook ad copy. Hook line of currently-performing ads."` Good example: `"Harrison Ball's own Facebook ad copy. The reason this exact framing converts on cold traffic: it gives comeback players permission to stop blaming their own body for damage a teacher caused. That permission is the prerequisite for being open to a new program."`

See `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_quote_sourcing_minimums.md`.

## Workflow

### Step 1. Confirm what to push

If Timo says "push 2 and 4", read back the titles and confirm:
> "Pushing these 2 ideas to Harrison's dashboard:
> 1. {title 1}
> 2. {title 2}
> Confirm? (y to push, or tell me what to change)"

Only proceed on explicit confirmation.

### Step 2. Load Supabase config

Read `/Users/air/Desktop/Precision-Brass/dashboard/lib/config.js`. If the file does not exist or still contains the placeholder `YOUR-PROJECT-REF`, STOP and tell Timo:
> "Supabase isn't configured yet. Open dashboard/setup/README.md and run the 3-step setup (~5 min), then come back."

### Step 3. Build idea IDs

Generate stable IDs in the format: `i_{YYYYMMDD}_{slug}` where slug = first 3-4 words of the title, lowercased, hyphenated. Example: `i_20260426_chops_recovery_protocol`.

If an idea with that ID already exists in the table, append `_v2`, `_v3`, etc.

### Step 4. POST to Supabase

For each greenlit idea, run a Bash curl POST to the Supabase REST API:

```bash
SUPABASE_URL="$(grep SUPABASE_URL /Users/air/Desktop/Precision-Brass/dashboard/lib/config.js | cut -d\' -f2)"
SUPABASE_KEY="$(grep SUPABASE_ANON_KEY /Users/air/Desktop/Precision-Brass/dashboard/lib/config.js | cut -d\' -f2)"

curl -X POST "${SUPABASE_URL}/rest/v1/ideas" \
  -H "apikey: ${SUPABASE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_KEY}" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{
    "id": "i_20260426_chops_recovery",
    "title": "The 7-day chops recovery protocol",
    "pain_point": "Comeback players over 50 with damaged embouchure",
    "hook_angle": "specific-result",
    "rationale": "VOC repeatedly cites...",
    "voc_quotes": [{"text":"I lost 9 months...", "source":"Fathom call 2026-03-12"}],
    "source_tags": ["fb-winners","fathom","lost-deals"],
    "status": "idea_pending",
    "history": [{"type":"delivered","who":"Timo","text":"<b>Pushed</b> from pb-script","time":"2026-04-26 20:30"}]
  }'
```

Use heredoc-style JSON, never shell-escape complex strings. Use `python3 -c` to JSON-encode if quotes get hairy, then write each idea to a temp JSON file and curl `--data-binary "@file.json"`.

**Do NOT use Python's urllib/requests to POST.** macOS system Python often lacks linked CA certs and fails with `SSL: CERTIFICATE_VERIFY_FAILED`. Always POST via `curl` (which uses the system keychain). Pattern:

```bash
# Build JSON with python (safe quote handling), POST with curl (works through TLS)
python3 build_payloads.py  # writes /tmp/pb-ideas/{0,1,2,3}.json
for f in /tmp/pb-ideas/*.json; do
  curl -s -X POST "${SUPABASE_URL}/rest/v1/ideas" \
    -H "apikey: ${SUPABASE_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_KEY}" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=representation" \
    --data-binary "@${f}"
done
```

### Step 5. Confirm + open dashboard

After all POSTs return 201:
> "✓ Pushed N ideas to the dashboard.
> Harrison can review them at: dashboard/scripts.html (Ideas Pending column).
> Want me to open it?"

If Timo says yes, run `open -a Safari /Users/air/Desktop/Precision-Brass/dashboard/scripts.html`.

### Step 6. Log to PRIORITIES.md (silent)

Add a one-liner to `~/.claude/projects/-Users-air-Desktop-Precision-Brass/SESSION_LOG.md`:
> "Pushed N ideas to Harrison dashboard: [titles]. Awaiting greenlight."

## Failure modes to avoid

1. **Inventing VOC quotes.** Every quote must trace back to a real file in `voc/` or a Fathom transcript Timo shared in chat. If you don't have it, ask. Never paraphrase a quote and pass it as verbatim.
2. **Pushing ideas Timo didn't pick.** Only push the ones Timo explicitly named. If Timo says "push the good ones", ASK which numbers.
3. **Silent failures.** If curl returns 4xx/5xx, surface the full error to Timo. Don't pretend it worked.
4. **Skipping the greenlight wait.** Do NOT auto-run `pb-script-write` after pushing. Harrison has to greenlight first on the dashboard.

## What this skill does NOT do

- Does not generate ideas (that's `pb-script`)
- Does not write the full filming script (that's `pb-script-write`)
- Does not approve ideas on Harrison's behalf (Harrison clicks the button)
- Does not push without Timo's explicit confirmation
