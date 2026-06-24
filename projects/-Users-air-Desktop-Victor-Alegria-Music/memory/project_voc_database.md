---
name: project-voc-database
description: Victor Alegria VOC database built from 29 coaching/sales call transcripts. What it contains and where.
metadata: 
  node_type: memory
  type: project
  originSessionId: 535cfadc-a09e-499b-91b5-baab3f146810
---

# Victor Alegria VOC database (built 2026-05-25)

Source: 37 M4A recordings (Google Drive download), deduped to 29 unique calls (33.3 hrs), transcribed with mlx-whisper base.en via `dashboard/scripts/transcribe_calls.sh`. ~10 of the 29 transcripts are mostly transcription-loop garbage; ~19 usable. Transcripts: `voc/sales-calls/raw/audio*.txt` (+ .srt/.vtt/.json).

Mined in two passes into:
- `voc/synthesis/voice-bank.md` - Victor's voice fingerprint + cited lines
- `voc/synthesis/all-quotes.jsonl` - 138 tagged verbatim quotes (speaker/funnel/use-case/theme)
- `voc/synthesis/objection-library.md` - student objections/fears
- `voc/sales-calls/extracts/student-psychology-findings.md` - student table + ~15 pain themes
- `voc/sales-calls/extracts/ICP-confirmed.md` - confirmed ICP

## Confirmed (verbatim-sourced, not invented)
- Victor = trombonist coaching INTERNATIONAL + US pre-professional trombonists to win conservatory/orchestra auditions.
- Program: "Global Rush Collective" (group ~$50/mo) + 1:1 (~200 euro/hr, ~1700 euro/3mo) + planned ~7-8k euro/yr.
- Method: recording-volume, taper ("2 days before, don't play a note"), mindset-over-talent, accountability bets, "first 30 seconds is all the jury watches", "slow is the fastest way", "average of 5 people".
- Sub-segments: military/army-band track, serious-amateur/certification-seeker.

## VERIFY with Timo (auto-transcription / single-source)
Pricing figures; student/teacher/school names (Marat, Brandon, Ismael, Jose, Carl, etc.); age band (only 2 data points); Victor's claimed wins (Berlin Phil/Karajan, Helsinki principal) = his stated claims per [[feedback_master_lessons]] (client claims != verified fact).

See [[project-clone-status]] for the broader infra clone state.
