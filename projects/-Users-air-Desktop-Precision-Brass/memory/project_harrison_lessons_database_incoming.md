---
name: harrison-lessons-database-incoming
description: "Bookmark. Timo will provide a database of Harrison's real student lessons. Use it as the primary source for locked-line phrasing in pb-script-write outputs. Until it lands, fall back to scattered Harrison-teaching moments in sales calls + testimonials."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8821999f-0897-4321-a621-b7d70e7bf4a4
---

# What's coming

Timo is going to deliver a database of Harrison's actual student lessons. These are 1-on-1 coaching sessions where Harrison is teaching, demonstrating, and explaining his system in his real voice. Promised 2026-05-06.

# Why this matters

Without it, pb-script-write composes locked lines in Harrison's voice fingerprint (modeled on the $36K converter video) instead of lifting his actual teaching phrasing. That's the proven mouthpieces-script pattern, but it produces hook + rule + identity lines that are stylized approximations, not verbatim Harrison.

On 2026-05-06 Timo flagged this on the mouthpiece-buzzing script: "did you use quotes from Harrison's lessons? I feel like you might be hallucinating some things." Correct callout. The VOC anchors per beat were real prospect quotes (Barry, Mike, Rachel, etc.), but the locked lines themselves were my composition.

# What we have NOW (interim, until the lessons db lands)

Harrison-teaching moments ARE in the corpus, just untagged and scattered:

- `voc/raw/converting-video-embouchure/transcript.md` + `references/converting-video-embouchure-transcript.md`. Harrison's $36K embouchure video. The most concentrated source of his real teaching vocabulary.
- `voc/sales-calls/raw/`. Many calls have Harrison mid-coaching the prospect. Highest-density teaching moments found so far:
  - `2026-03-23_salescall_barry_call-3.md`. Diagnosis lines ("mouthpiece is too high... approach from the south... move 5 to 8% down").
  - `2026-03-23_salescall_eric_call-9.md`. His actual mnemonic ("form, place pressure on the lower lip, breathe, then tongue the note and produce a buzz").
  - `2026-03-23_salescall_tom_call-10.md`. Mike-from-Winnipeg story ("he misinterpreted what I was saying, and we worked it where we hugged the top lip, and then boom") + "passive lip downstream, trumpet player, active lip".
  - `2026-03-23_salescall_michael_call-0.md`. Buzz-warmup discussion.
  - `2026-03-24_salescall_unknown_call-24.md`. "We would be applying the mouthpiece from the north and optimizing it. If you play with more top lip, it'll be bad."
  - `2026-03-24_salescall_joe_call-28.md`. "The top lip is producing the sound... the bottom lip is passive, the top lip is producing the vibration."
- `voc/testimonials/raw/`. Phil, Joinville, Christian, Mike, Kay testimonials all have Harrison teaching mid-conversation.

His real teaching vocabulary surfaced from these:
- Spatial. "approach from the north", "approach from the south", "tracking movement down to the right".
- Anatomical. "passive lip", "active lip", "top lip produces the buzz", "vibrating surface", "downstream / upstream player".
- Procedural mnemonic. "form, place pressure on the lower lip, breathe, tongue the note, buzz".
- Proprietary terms. "Sim setup", "VAS (Vertical Alignment System)", "hug the top lip".
- Diagnostic frames. "the mouthpiece is too high / too low", "you're pinching the buzz", "the buzz won't move from one side of the cup to the other".

# How to apply once the lessons db arrives

When Timo drops the lessons corpus:

1. **Add a 7th mining agent** to the pb-script-write 6-agent VOC sweep, lensed: "Harrison's actual teaching language on [topic]". Spawned in parallel with the existing 6.
2. **Locked-line preference order:**
   - First. Verbatim Harrison quote from the lessons db on the same topic.
   - Second. Harrison teaching quote from a sales call or testimonial.
   - Third. Harrison line from the converter transcript.
   - Fourth (last resort). My composition modeled on his voice fingerprint, marked as `[COMPOSED. confirm with Harrison]`.
3. **Tag the lessons db output**. Each script's locked lines should cite source (e.g. "from Phil's lesson 2025-04-14 minute 12") so Harrison can audit phrasing fidelity at filming time.
4. **Update the pb-script-write SKILL.md** to require Harrison-lesson sourcing for locked lines, not just composition.

# Open questions for Timo (when db arrives)

- Format: video file paths, transcripts, JSON, Supabase table?
- Where will it live? `voc/raw/harrison-lessons/` is the natural home.
- Tagging convention: by student name + date + topic? Or by topic + outcome?
- Are there existing tags for "phrases that landed and converted" vs. "phrases that confused"?

# Cross-reference

- `feedback_pb_script_write_master_lessons.md`. The 7 master lessons. Lesson 1 says VOC mining is the first step. The lessons db is the next-level version of that.
- `feedback_harrison_voice.md`. Current voice fingerprint reference (built from the converter transcript).
