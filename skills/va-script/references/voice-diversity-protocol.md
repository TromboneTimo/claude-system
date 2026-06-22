# Voice Diversity Protocol

Used by Agent 7 (Voice Diversity Auditor). Runs sequentially in the main skill after the 6 parallel research agents return. Prevents recycling the same voices across runs.

## Why this exists

Mechanism carried over from Precision Brass: agents tend to read summary files that concentrate the loudest voices, so the same handful of speakers recur across runs. The auditor is the structural fix. The recycled-voice exclusion list for Victor is built up from `voices_used_log.jsonl` as runs accumulate (bootstrap empty on first run). [PLACEHOLDER: there is no pre-seeded recycled-12 list for Victor; populate from real run history, do NOT reuse Precision Brass names.]

## Inputs to the auditor

1. Pool of ~10 candidate ideas from agents 1 to 6.
2. `/Users/air/Desktop/Victor Alegria Music/voc/voices_used_log.jsonl` (last 3 lines).
3. The 5-idea final-mix mandate (1-2 from Agent 4 winner pattern, 3-4 from agents 1, 2, 3, 5, 6).

## The 4 auditor checks

### Check 1. Voice freshness

For each candidate idea, extract its **primary voice** (the speaker most heavily quoted) and **secondary voices** (other named speakers cited).

If primary voice appears in last 2 runs of voices_used_log, REJECT the idea unless the agent included an explicit `voice_freshness_override` field with justification (e.g., "this surfaces a new sub-pain from this speaker not previously mined").

If primary voice appears in last 1 run only, allow but flag.

### Check 2. Final-5 voice diversity

The final 5 ideas combined must satisfy:
- 5 distinct primary voices (no overlap across the 5).
- 3 or more primary voices NOT in the last 3 runs.
- At least 1 voice from a raw sales call file (file path matches `voc/sales-calls/raw/*.md`).
- At least 1 voice from a raw testimonial file (file path matches `voc/testimonials/raw/*.md`).

If any of these fail, swap candidates from the pool until they pass. If the pool can't satisfy the constraints, the auditor reports "insufficient fresh voices in pool, request agent re-run with stricter freshness lens".

### Check 3. Quote-sourcing minimums (per `feedback_quote_sourcing_minimums.md`)

Every final idea must include:
- 1+ testimonial quote (from `voc/testimonials/raw/*.md` or testimonial entries in quotes jsonl).
- 1+ sales call quote (from `voc/sales-calls/raw/*.md` or sales call entries in quotes jsonl).

Harrison-quotes (from his own ad copy, transcripts, or DMs) require a `conversion_lens` field explaining WHY that line converts. Source field cannot just say "Harrison's ad". It must say something like "Harrison's ad copy that converted at ROAS 4.2x because it [reframe pattern]".

No fabricated quotes. Every quote needs `source_file` + (timestamp OR character span). Auditor rejects any quote without a verifiable trace.

### Check 4. Plain-English rationale (per `feedback_no_internal_jargon_in_rationale.md`)

The rationale field cannot use internal jargon: "converter", "the corpus", "the voice bank", "the database", or invented market claims. Auditor strips and rewrites.

## Voices_used_log append format

After all 4 checks pass and the final 5 are locked, append ONE line to `voices_used_log.jsonl`:

```json
{"run_id": "2026-04-27_run1", "timestamp": "2026-04-27T10:30:00Z", "corpus_picked": "sales-B", "idea_ids": ["pb-2026-04-27-1","pb-2026-04-27-2","pb-2026-04-27-3","pb-2026-04-27-4","pb-2026-04-27-5"], "primary_voices": ["Speaker1","Speaker2","Speaker3","Speaker4","Speaker5"], "secondary_voices": ["Speaker6","Speaker7"], "raw_files": ["voc/sales-calls/raw/file1.md","voc/testimonials/raw/file2.md"], "lenses": ["age-anxiety","mouthpiece-rabbit-hole","HP3","OBJ4"]}
```

Run_id format: `{date}_run{N}` where N increments if multiple runs same day.

## Bootstrap

If `voc/voices_used_log.jsonl` doesn't exist, create it empty on first run. The auditor treats an empty log as "no voice constraints from history yet" and only enforces Check 2 (final-5 diversity) and Check 3 (quote sourcing).

## Lens picker (Bash, run in Step 1 of SKILL.md before spawning Agent 6)

Picks one of 12 lenses, avoiding any used in the last 3 runs:

```bash
python3 - <<'PY'
import json, random, pathlib
log_path = pathlib.Path('/Users/air/Desktop/Victor Alegria Music/voc/voices_used_log.jsonl')
# PLACEHOLDER lens set for Victor (audition-prep). Replace with mined lenses after VOC pass; do NOT use Precision Brass brass-comeback lenses.
all_lenses = ['audition-odds-anxiety','unstructured-practice','peaking-and-taper','sound-concept-panel','mindset-self-belief','accountability-commitment','recording-method','talent-vs-preparation','pro-track-identity','deadline-pressure','teacher-loyalty','comparison-to-top-players']
recent = []
if log_path.exists():
    for line in log_path.read_text().splitlines()[-3:]:
        try: recent.extend(json.loads(line).get('lenses', []))
        except: pass
remaining = [l for l in all_lenses if l not in recent] or all_lenses
print(random.choice(remaining))
PY
```

The corpus picker for Agent 1 lives in `raw-deep-dive-rotation.md`. Run both before spawning agents in parallel.

## Hard rules

- Auditor runs AFTER agents 1-6 return. Not in parallel.
- If auditor rejects all candidates and pool cannot satisfy diversity, the skill REPORTS THE FAILURE rather than silently shipping recycled voices. Fail loud.
- Auditor does NOT generate new ideas. It selects, rejects, and orders existing candidates.
- Log append is the LAST step before output. If output fails, log is not written (so a re-run starts clean).
