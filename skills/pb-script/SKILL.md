---
name: pb-script
description: Phase 1 of Harrison Ball's Precision Brass YouTube content engine. Research-driven idea generator that spawns 6 parallel specialist subagents (raw deep-dive, hidden pain hunter, objection dissolver, verified winner pattern, conversion trigger detector, fresh lens) plus a sequential voice-diversity auditor to read across the full voice-of-customer corpus and return 5 conversion-trigger-driven content ideas with verbatim quote evidence and FRESH voices each run. 1-2 ideas anchored on the proven verified-winner pattern (YouTube winners + FB winning ads), 3-4 ideas surfaced from raw transcripts, hidden pain framework, objection lenses, and rotating fresh angles. Voice diversity log prevents recycling the same speakers across runs. Use this skill whenever Timo or Harrison asks for content ideas, video ideas, what to film next, what Harrison should make, "give me angles", "youtube ideas for harrison", "next video for harrison", "precision brass content ideas", "/pb-script", or any variation. Also fire when the user mentions Harrison and content/video/script in the same breath. Do NOT generate the script itself. That is Phase 2 and lives in a future companion skill. This skill stops at the 5-idea menu and waits for Timo to pick one.
---

# pb-script. Phase 1: Conversion-Trigger Idea Generator

## What this does

Generate 5 YouTube content ideas for Harrison Ball that are anchored in **what verifiably caused his prospects to buy**. Not generic trumpet advice. Not what's trending. Ideas backed by the actual language, fears, identity arcs, and conversion triggers found in Precision Brass's voice-of-customer corpus.

This is a **research-first skill**. Every invocation re-reads raw sources. No caching. No relying on synthesized summaries alone. Fresh perspectives every time.

## The 5-idea structure (NON-NEGOTIABLE)

The output mix must be:
- **1-2 ideas anchored on VERIFIED WINNERS** (Agent 4), pattern-matched against `youtube-database/` (status=winner videos) AND `facebook-ads-database/` (status=winner ads). Both are proven-conversion sources.
- **3-4 ideas from variety lenses** (Agents 1, 2, 3, 5, 6), surfaced from raw deep-dive on a rotated corpus, hidden pain framework, objection lenses, conversion triggers from raw testimonials, and a fresh wildcard lens.
- All 5 ideas pass the **Voice Diversity Auditor** (Agent 7) which enforces fresh voices vs. last 3 runs and rejects recycled speakers.

This split exists for a reason. Pure winner-cloning makes the channel narrow. Pure variety ignores what's actually proven to convert. The mix gives Timo a couple safe-bet angles plus fresh territory. The auditor is the structural fix for the recycled-voices problem (April 2026: same 12 voices across 4 dashboard pushes).

**Empty-database handling:** If either winner database has zero entries (or no status=winner items), Agent 4 reads only the populated one. If BOTH are empty, Agent 4 returns "no verified-winner data yet" and the auditor pulls all 5 ideas from the variety pool (Agents 1, 2, 3, 5, 6). Note this in the output so Timo knows the anchor slot was skipped.

## How it works (workflow)

### Step 0. Ask the funnel layer FIRST (before any research)

**Mandatory intake question.** Before spawning any research agents, ask Timo:

> "What funnel layer is this for? **TOFU** (broad reach, problem-unaware audience), **MOFU** (problem-aware, exploring solutions), or **BOFU** (solution-aware, evaluating providers ready to book)?"

Wait for an explicit answer. The funnel layer determines:
- How deep the pain points get named (TOFU light, BOFU surgical)
- What identity wounds surface (TOFU broad curiosity, BOFU comeback grief / age anxiety / failed-method shame)
- What the funnel CTA points to (TOFU another video, MOFU strategy session content, BOFU strategy call)
- Whether to use the proven 12-move converter template (BOFU only) or a lighter structure (TOFU/MOFU)

See `references/funnel-layers.md` for the full spec.

If Timo doesn't answer or says "all of them", default to MOFU and label it. Don't skip the question.

### Step 1. Pre-spawn rotation picks (Bash), then acknowledge

**Before** spawning agents, run two Bash blocks to pick the rotating slots:

```bash
# A. Pick the raw corpus for Agent 1 (avoiding last 3 runs)
python3 - <<'PY'
import json, os, random, pathlib
log_path = pathlib.Path('/Users/air/Desktop/Precision-Brass/voc/voices_used_log.jsonl')
all_corpora = ['sales-A','sales-B','sales-C','testimonials','yt-comments','unsorted-vtt','fb-ads','email-seq']
recent = []
if log_path.exists():
    for line in log_path.read_text().splitlines()[-3:]:
        try: recent.append(json.loads(line).get('corpus_picked'))
        except: pass
remaining = [c for c in all_corpora if c not in recent] or all_corpora
print(random.choice(remaining))
PY

# B. Pick the fresh lens for Agent 6 (avoiding last 3 runs)
python3 - <<'PY'
import json, random, pathlib
log_path = pathlib.Path('/Users/air/Desktop/Precision-Brass/voc/voices_used_log.jsonl')
all_lenses = ['dental-trigger','isolation-pattern','failed-method-grief','identity-aspiration','age-anxiety','mouthpiece-rabbit-hole','comeback-player-arc','section-leader-redemption','teacher-loyalty-grief','livelihood-vs-love','range-for-others','exhaustion-of-hope']
recent = []
if log_path.exists():
    for line in log_path.read_text().splitlines()[-3:]:
        try: recent.extend(json.loads(line).get('lenses', []))
        except: pass
remaining = [l for l in all_lenses if l not in recent] or all_lenses
print(random.choice(remaining))
PY
```

Save both outputs as `CORPUS_ID` and `LENS_NAME`. Then tell Timo:

> "Layer locked: [TOFU/MOFU/BOFU]. Raw corpus this run: [CORPUS_ID]. Fresh lens: [LENS_NAME]. Spawning 6 research agents in parallel + voice diversity auditor. ~3-4 minutes."

Then spawn Agents 1-6 below **in parallel in a single message** (multiple Agent tool calls in one turn). Inject the funnel layer, CORPUS_ID, and LENS_NAME into each agent's prompt as appropriate.

### Step 2. Spawn 6 parallel research subagents

All 6 are `general-purpose` subagents. They read raw files directly, return findings to the main thread.

#### Agent 1. Raw Deep-Dive (ROTATING CORPUS)

Inject CORPUS_ID. Reads ONE raw corpus end-to-end. See `references/raw-deep-dive-rotation.md` for the 8-corpus pool and per-corpus reading instructions.

Prompt:
```
You are doing a deep-dive read of ONE raw corpus from Precision Brass's voice-of-customer database. Your corpus this run: [CORPUS_ID].

Funnel layer for this run: [TOFU/MOFU/BOFU].

Read `~/.claude/skills/pb-script/references/raw-deep-dive-rotation.md` first to see the per-corpus reading instructions. Then read EVERY file in your assigned corpus end-to-end. Do NOT read summary files (voice-bank.md, won-deals-voice-bank.md, etc.). Those are concentrated and you are mining fresh.

Your job:
1. Identify named speakers in your corpus. Note WHICH speakers appear (this feeds the voice-diversity log).
2. Extract 5-10 verbatim quotes from speakers who are NOT in the recycled-12 list (Robbie, Mike, Heather, Phil, Joinville, Rachel, Konstantinos, Tom, Barry, Michael, Julian, Jason). Prefer fresh voices.
3. Surface 2 candidate video ideas anchored in fresh voices and specific pain or identity arcs from this raw read.

Each idea must:
- Pass the ICP checklist (`references/icp-checklist.md`)
- Cite 3+ verbatim quotes WITH source_file paths
- Identify the primary voice (the speaker most heavily quoted)
- Name a limiting belief (Domino) and an identity outcome (not a technique outcome)
- Match the funnel layer's pain-point depth

Return: corpus_id picked, "voices surfaced" list (named speakers + file paths), then 2 candidate ideas.
```

#### Agent 2. Hidden Pain Hunter

Reads sales call transcripts and the deep psychological dive looking for SUBTEXT. See `references/hidden-pain-framework.md` for the 8 hidden problems (HP1-HP8) and detection patterns.

Prompt:
```
You are hunting for HIDDEN PAIN in Harrison Ball's voice-of-customer corpus. Hidden pain is a wound prospects circle around in sales calls without ever naming directly. Naming the unnamed pain is the highest-converting hook pattern.

Funnel layer for this run: [TOFU/MOFU/BOFU].

Read `~/.claude/skills/pb-script/references/hidden-pain-framework.md` first for the 8 hidden problems (HP1-HP8) and detection patterns (compensation clauses, hypothetical distancing, excessive technical detail, apologizing for the goal, repeated reassurance-seeking).

Then read these files for traces of subtext:
- /Users/air/Desktop/Precision-Brass/voc/raw/sales-calls/ (sample 6-8 calls, prefer ones from speakers NOT in the recycled-12 list)
- /Users/air/Desktop/Precision-Brass/voc/raw/research/2026-04-21_deep-psychological-dive_harrisson-ball_19-prospects.md
- /Users/air/Desktop/Precision-Brass/context/prospect-psychology.md

Your job:
1. Pick 1-2 hidden problems (HP1-HP8) that are MOST under-addressed in `youtube-database/index.json` topic_tags.
2. Find 3+ verbatim quotes where prospects CIRCLE the pain without naming it. Show the circling.
3. Propose 1 video idea that NAMES THE UNNAMED PAIN explicitly as its hook.
4. Show the reframe move (the line that grants permission to feel the wound + offers a new identity).

The hook line MUST name the hidden pain with words the prospect would never say themselves. NO technique-only hooks.

Return: which HP IDs picked, 3+ circling quotes with source files, then 1 candidate idea with hook line + reframe move.
```

#### Agent 3. Objection Dissolver

Laser-focused on objections. See `references/objection-lenses.md` for the 8 objection lenses (OBJ1-OBJ8) and the pre-emption pattern.

Prompt:
```
You are pre-empting Harrison Ball's most common sales-call objections. Pick ONE objection lens and propose a video that dismantles it BEFORE the prospect ever gets on a call.

Funnel layer for this run: [TOFU/MOFU/BOFU].

Read `~/.claude/skills/pb-script/references/objection-lenses.md` first for the 8 lenses (OBJ1-OBJ8) and the pre-emption pattern (HOOK / VALIDATION / DISMANTLE / DEMONSTRATION / RESOLUTION).

Then read these files:
- /Users/air/Desktop/Precision-Brass/voc/raw/sales-calls/ (sample 6-8 calls, search for HESITATION/PUSHBACK moments specifically)
- /Users/air/Desktop/Precision-Brass/voc/personas/lost-deals-voice-bank.md
- /Users/air/Desktop/Precision-Brass/voc/personas/objection-library.md
- Facebook ad comments where present (`facebook-ads-database/*/comments-top.md`)

Your job:
1. Pick 1 objection lens (OBJ1-OBJ8) that is least-recently-used per `voices_used_log.jsonl` (the `lenses` field in last 3 runs).
2. Find 3+ verbatim quotes from sales-call moments where this objection appeared, AND 2+ quotes from lost-deals-voice-bank.md.
3. Propose 1 video idea using the pre-emption pattern.
4. Specify the DISMANTLE LINE (the specific reframe that flips the objection) and the DEMONSTRATION (what Harrison shows on camera to falsify the objection).

The video must address ONE objection, not three. The dismantle line MUST be falsifiable on camera.

Return: which OBJ ID picked, 3+ pushback quotes with source files, then 1 candidate idea with dismantle line and demonstration.
```

#### Agent 4. Verified Winner Pattern (THE ANCHOR)

Reads BOTH proven-conversion sources: YouTube winners and Facebook winning ads.

Prompt:
```
You are researching what verifiably converts for Harrison Ball's Precision Brass business across two channels: YouTube long-form and Facebook ads.

Funnel layer for this run: [TOFU/MOFU/BOFU].

PART 1. YouTube winners
READ EVERY VIDEO in /Users/air/Desktop/Precision-Brass/youtube-database/ that is marked status=winner in index.json. For each winner: analysis.md, transcript.md, comments-top.md, metadata.json. If empty, note and continue.

PART 2. Facebook winning ads
READ EVERY AD in /Users/air/Desktop/Precision-Brass/facebook-ads-database/ that is marked status=winner in index.json. For each: analysis.md, creative/copy.md, performance.json, comments-top.md if present, metadata.json. If empty, note and continue.

PART 3. Reference materials (always read)
- /Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md
- /Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/project_proven_converter_template.md (12-move converter template)

PART 4. Extract cross-channel PATTERN: hook structure, identity arc, pain-to-payoff bridge, recurring language, demonstration style.

PART 5. Propose 2-3 NEW video ideas matching this pattern, each targeting a different specific pain point. Each idea must:
- Map to YT-WINNER-PATTERN, FB-WINNER-PATTERN, or CROSS-WINNER-PATTERN (specify) and explain inheritance
- Pass ICP checklist
- Cite 2+ verbatim quotes proving emotional resonance
- Name limiting belief (Domino, one per video)
- Sell identity, not technique

EMPTY-DATABASE: if both YT and FB winners empty, return: "No verified-winner data yet. Skip anchor slot, pull all 5 from variety pool." Do NOT make up patterns.

Return: which databases had data, pattern summary (200 words across both channels), then 2-3 candidate ideas.
```

#### Agent 5. Conversion Trigger Detector

Reads RAW testimonials end-to-end (not the summary). Identifies the exact moment a prospect flipped to buyer.

Prompt:
```
You are detecting CONVERSION TRIGGERS in Harrison Ball's customer corpus. A conversion trigger is the exact line, realization, or demonstration that flipped a prospect into a buyer.

Funnel layer for this run: [TOFU/MOFU/BOFU].

Read RAW testimonial files end-to-end (these are CUSTOMERS who completed the program, not prospects):
- /Users/air/Desktop/Precision-Brass/voc/raw/testimonials/ (all 11 files)

Then for additional signal:
- /Users/air/Desktop/Precision-Brass/voc/quotes/won-deals-quotes.jsonl
- /Users/air/Desktop/Precision-Brass/voc/quotes/sales-call-outcomes.jsonl

Reference the 8-trigger taxonomy in `~/.claude/skills/pb-script/references/conversion-triggers.md` (T1-T8).

Your job:
1. For each testimonial, find the EXACT moment the customer describes flipping to buyer. Quote it verbatim.
2. Map each moment to a trigger (T1-T8).
3. Identify the trigger that is MOST UNDER-USED in recent dashboard pushes (cross-check `voices_used_log.jsonl` if present).
4. Propose 1 video idea built around that under-used trigger.

Each idea must:
- Cite 3+ verbatim quotes from RAW testimonials with source_file paths
- Identify the primary voice (most heavily quoted speaker, MUST be a customer)
- Name the trigger by ID (T1-T8)
- Sell identity, not technique
- Per `feedback_master_lessons.md` rule 3: do NOT mix prospect language with customer language

Return: trigger inventory ranked by under-use, then 1 candidate idea.
```

#### Agent 6. Fresh Lens (ROTATING)

Inject LENS_NAME picked in Step 1.

Prompt:
```
You are researching the [LENS_NAME] angle for Harrison Ball's content. This lens was picked because it has NOT been used in the last 3 runs (per voices_used_log.jsonl).

Funnel layer for this run: [TOFU/MOFU/BOFU].

The 12 possible lenses: dental-trigger, isolation-pattern, failed-method-grief, identity-aspiration, age-anxiety, mouthpiece-rabbit-hole, comeback-player-arc, section-leader-redemption, teacher-loyalty-grief, livelihood-vs-love, range-for-others, exhaustion-of-hope.

Read across these files for traces of [LENS_NAME]:
- /Users/air/Desktop/Precision-Brass/voc/quotes/all-quotes.jsonl
- /Users/air/Desktop/Precision-Brass/voc/raw/sales-calls/ (sample 6-8 random calls)
- /Users/air/Desktop/Precision-Brass/voc/raw/email-sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md
- /Users/air/Desktop/Precision-Brass/voc/personas/harrison-email-voice.md
- /Users/air/Desktop/Precision-Brass/context/harrison-profile.md

Find the most NON-OBVIOUS angle on this lens. Not what Harrison already says publicly. Something the data shows is loaded with emotion but Harrison hasn't directly addressed in a video yet.

Propose 1 wildcard video idea through this lens. Must:
- Pass ICP checklist
- Cite 3+ verbatim quotes with source files
- Be something NOT covered in `youtube-database/index.json` topic_tags
- Sell identity, not technique
- Use a fresh primary voice (not in recycled-12 list)

Return: lens insight (150 words on what's underneath this theme), then 1 candidate idea.
```

### Step 3. Run Agent 7 (Voice Diversity Auditor) sequentially

After Agents 1-6 return, run the auditor as a sequential synthesizer step. See `references/voice-diversity-protocol.md` for the full protocol.

The auditor performs 4 checks on the candidate pool (~9 ideas total: 2+1+1+2+1+1+overlap):

1. **Voice freshness check**: reject any idea whose primary voice appears in last 2 runs (override allowed if agent flagged a genuinely new sub-pain for that speaker).
2. **Final-5 voice diversity**: 5 distinct primary voices, 3+ NOT in last 3 runs, 1+ from raw sales call file, 1+ from raw testimonial file.
3. **Quote-sourcing minimums**: 1+ testimonial quote AND 1+ sales call quote per idea (per `feedback_quote_sourcing_minimums.md`). Harrison-quotes need a `conversion_lens` field.
4. **Plain-English rationale**: no internal jargon ("converter", "voice bank", "the corpus", invented market claims) (per `feedback_no_internal_jargon_in_rationale.md`).

Then enforce the structure mandate: 1-2 ideas from Agent 4's pool (anchor), 3-4 from Agents 1, 2, 3, 5, 6 (variety). Apply ICP checklist + Domino check + identity check to every survivor.

If the auditor cannot satisfy diversity from the pool, FAIL LOUD: report "insufficient fresh voices in pool, request agent re-run with stricter freshness lens" rather than silently shipping recycled voices.

After locking the final 5, append one line to `/Users/air/Desktop/Precision-Brass/voc/voices_used_log.jsonl` with run_id, corpus_picked, idea_ids, primary_voices, secondary_voices, raw_files, lenses (see `references/voice-diversity-protocol.md` for exact format).

Bootstrap: if voices_used_log.jsonl doesn't exist, create empty on first run.

### Step 4. Output the menu

Use the exact template in `references/output-template.md`. Each idea includes:
- Title and 3 alternate title variations
- Anchor source (yt-winner-pattern OR lens name)
- Conversion trigger activated
- Limiting belief shattered
- Identity outcome promised
- ICP segment targeted
- 2-3 verbatim quote citations with source files
- Hook angle (money / problem / curiosity)
- Why this converts (3-sentence rationale)

End with: "Which one do you want to develop into a script? Reply with the number." Phase 2 (script generation) lives in the companion skill `pb-script-write`, which auto-fires the moment Timo replies with a selection ("idea N", "go with #N", "the mouthpiece one", etc.). Do NOT manually continue into script writing inside this skill. Hand off to pb-script-write.

## Hard rules (do not break)

1. **No script generation in this skill.** Phase 1 stops at the menu. If Timo asks for the script in the same turn, say: "Picking the angle first locks in the visual plan. Which of the 5 wins?"

2. **No fabricated quotes.** Every quote must be traceable to a real file in the corpus. Cite the source file path. If you can't find a real quote for an idea, weaken the idea or drop it. Auto-transcripts can lie. When uncertain, say so rather than invent.

3. **ICP checklist runs on every idea.** See `references/icp-checklist.md`. No exceptions.

4. **Hard-block generic ideas.** If an idea would also make sense for a Berklee jazz student or a high-school marching band kid, it's too generic for Harrison's ICP. Reject and replace.

5. **Identity over technique.** "How to play high G" is a technique frame. "Reclaim the range you had at 25, without re-learning trumpet" is an identity frame. Always identity.

6. **Read the actual files. Don't synthesize from memory.** Each invocation, the agents must open and read the raw sources fresh. Do not let the synthesizer skip the agent step and just write 5 ideas from prior knowledge.

7. **Never let Harrison film without script approval.** When presenting the menu, end with the standard reminder: "Once you pick one, I'll generate the full script and visual plan. Send to Timo for review before filming."

## Reference files

- `references/icp-checklist.md`. The 5-question ICP gate
- `references/output-template.md`. Exact format for the 5-idea menu
- `references/conversion-triggers.md`. Taxonomy of triggers (T1-T8) used by Agent 5
- `references/proven-template-pointer.md`. Where the 12-move converter template lives
- `references/example-mouthpieces-script.md`. Proven 7-beat structure (Phase 2 reference)
- `references/script-writing-protocol.md`. Phase 2 ruleset (Phase 2 reference)
- `references/funnel-layers.md`. TOFU/MOFU/BOFU spec. READ in Step 0
- `references/raw-deep-dive-rotation.md`. Agent 1 corpus rotation pool + per-corpus reading instructions. READ before spawning Agent 1
- `references/hidden-pain-framework.md`. Agent 2's 8 hidden problems (HP1-HP8) + subtext detection patterns. READ before spawning Agent 2
- `references/objection-lenses.md`. Agent 3's 8 objection lenses (OBJ1-OBJ8) + pre-emption pattern. READ before spawning Agent 3
- `references/voice-diversity-protocol.md`. Agent 7 auditor protocol + voices_used_log.jsonl format. READ in Step 3

## What this skill is NOT

- Not a script generator (that's Phase 2)
- Not a thumbnail tool
- Not a title-only generator (titles come WITH evidence and structure, not in isolation)
- Not for short-form (HARD RULE: project CLAUDE.md blocks short-form creation; long-form first, always)
- Not for non-Harrison content (Robinson's Remedies, Creator Conservatory, etc. have their own skills)