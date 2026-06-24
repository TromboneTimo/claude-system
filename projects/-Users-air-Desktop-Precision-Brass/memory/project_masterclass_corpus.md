---
name: project-masterclass-corpus
description: "Harrison's masterclass transcript is part of the VOC corpus. Every 6-agent mining sweep across pb-script, pb-email, pb-script-write, pb-email-write reads it. Location, wiring, and ingestion status."
metadata: 
  node_type: memory
  type: project
  originSessionId: 467afc37-9455-4e76-8762-b666eca3bdcb
---

# Harrison's Masterclass is Part of the VOC Corpus

**Why:** The masterclass is the single highest-density source of Harrison teaching the Vertical Alignment System in one sustained sitting. Without it, mining agents reconstruct his voice from sales-call fragments + testimonial fragments + YouTube descriptions. With it, agents have the canonical source. Locked in 2026-05-15 by Timo.

**How to apply:**
- Folder: `Precision-Brass/voc/masterclass/raw/`
- Canonical file: `transcript.md`. Optional sibling files: `transcript.srt`, `slides.pdf`, `notes.md`, `source.json`.
- The folder's README explains structure and versioning rules.
- Wired into [[pb-script]] (shared resource note at top of Step 2, plus Agent 4 Part 3 reference materials, plus masterclass added as the 9th corpus in raw-deep-dive-rotation.md).
- Wired into [[pb-email]] (shared resource note at top of subagent architecture).
- Wired into [[pb-email-write]] (load-order item 11 in hard preconditions).
- Wired into [[pb-script-write]] (vault list line 35).

**Status (2026-05-15, fully integrated):**
- **Layer 1 (raw):** `voc/masterclass/raw/transcript.md` (57KB, 191 paragraphs). Plus `source.json`, `README.md`.
- **Layer 2 (quotes):** `voc/masterclass/extracts/masterclass-quotes.jsonl` (163 entries: 129 Harrison teaching + 34 student demos). Same 163 entries also appended to `voc/synthesis/all-quotes.jsonl` (now 604 total entries, was 441). Schema matches the existing quote files exactly, with `speaker_type: "harrison"` introduced for presenter quotes.
- **Layer 3 (persona voice bank):** `voc/masterclass/extracts/masterclass-voice-bank.md` (421 lines, 7+ sections). Locked teaching lines with frequencies (top hits: "dynamic repetition" 13x, "amisha/amisher" 22x, "upstream/downstream" 18x, "secret" 14x, "vertical alignment" 6x, "check it out" 6x, "James Morrison" 5x, "gravity breath" 5x, "are you ready" 5x, "would it be worth it" 4x). Plus 12 named traps, 6-step apparatus reveal sequence, 5 student demo arcs (Brad/Rachel/Yens/Brandon/Lee), ICP framing verbatim both sides, CTA close pattern.
- **Status in rotation:** PROMOTED OUT of the rotating raw-deep-dive pool. Now ALWAYS-ON for every pb-script + pb-email run. Not rotation-gated. Read every time.
- **5 named students** in live demos: Brad, Rachel, Yens, Brandon, Lee. Cross-reference with `voc/testimonials/raw/` before quoting any of them as customers.
- **Verbatim CTA close:** "Hey, if you're still here, what are you waiting for? Calie.com. Book it in today. See you soon."

**Ingestion process when transcript arrives:**
1. Drop the raw file (PDF, txt, srt, doc, mov) somewhere I can read.
2. If it's a video/audio file, transcribe via mlx-whisper (same pipeline as [[pb-youtube-description]]):
   ```
   ffmpeg -y -i <src> -vn -ac 1 -ar 16000 -c:a pcm_s16le /tmp/mc_audio.wav
   /Users/air/Library/Python/3.10/bin/mlx_whisper /tmp/mc_audio.wav --model mlx-community/whisper-small.en-mlx --output-format srt --output-dir /tmp
   ```
   Use `whisper-small.en-mlx` (not `base.en-mlx`) because masterclass is long-form, so accuracy matters.
3. If it's already a transcript (PDF, txt, doc), convert to markdown. Preserve speaker labels if present.
4. Save to `voc/masterclass/raw/transcript.md` (+ `transcript.srt` if applicable).
5. Write `voc/masterclass/raw/source.json` with provenance: source URL/file, captured_at, transcribed_via, version label, total_seconds.
6. Skim once and extract a chapter map into `notes.md` (locked-line repetitions, trap names, student stories, CTA wording).
7. Update `voc/voices_used_log.jsonl` schema if needed so `corpus_picked=masterclass` is recognized.

**Versioning rule:**
- Old transcript on re-record: rename to `transcript_archive_<YYYY-MM-DD>.md`. Bump version in `source.json`.
- Update this memory file with the new version date.

**Why this is worth the load-order cost:**
- Voice fidelity. Mining 28 sales calls for "the trap Harrison names" is inferential. Reading him say it once is canonical.
- Locked-line detection. Phrases that recur 3+ times across content = Harrison's locked teaching language. The masterclass is where most of them originate.
- Student stories. Cross-reference student names from masterclass against `voc/testimonials/raw/` to know which transformations Harrison considers signature.
- CTA wording. Harrison's masterclass close is the verbatim energy we want in BOFU emails and final script funnels.
