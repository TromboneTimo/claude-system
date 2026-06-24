---
name: project-lessons-corpus
description: "Fathom-sourced 1:1 lesson transcripts for Harrison's students. 97 sessions / 57 students. Mining for knowledge gaps + working methods + per-student resonance is the planned Phase 2."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9c5effee-2b95-4a68-9600-6950991b1839
---

Harrison's 1:1 lesson transcripts pulled from Fathom API on 2026-05-17 live at `voc/lessons/raw/`. Trial calls (Calendly "Claim Your 45-Minute Lesson") for students who also have multiple lessons live at `voc/sales-calls/trial-calls/raw/`.

**Why:** Voice-of-customer mining for knowledge gaps (where students get stuck), resonance signals (which Harrison teachings produce breakthrough moments), and working methods (which named techniques produce measurable in-session improvement). Feeds pb-script, pb-email, ad copy, and future curriculum decisions.

**How to apply:**
- New ingestion: re-run `/tmp/fathom_fetch.sh` + `/tmp/fathom_pull.py` + `/tmp/fathom_save.py`. Adjust `SINCE` date in fathom_fetch.sh for incremental pulls.
- Fathom API key lives in `~/.claude/credentials/MASTER.md` under "Precision Brass / Fathom API".
- Lesson detection: classifier filters by Harrison invitee + title patterns + duration 15-110 min, blocks sales-training/office-hrs/collab-calls. Tony Yarbrough excluded as he's staff.
- Student name extraction: title patterns + invitee fallback. Case + whitespace normalized, single-token names absorbed into full-name match where possible.
- 3-lesson-per-student cap was applied for the initial pull. Re-pull without cap if doing deep per-student analysis.
- Per-student index at `voc/lessons/raw/index.json`. Cheat sheet at `voc/lessons/raw/STUDENTS.md`.
- Mining sweep completed 2026-05-17. 4-agent parallel sweep (knowledge gaps / resonance / working methods / per-student profiles) + 1 sequential auditor. 519 deduped quotes at `voc/lessons/extracts/lessons-quotes.jsonl`. Theme-indexed reference at `voc/lessons/extracts/lessons-voice-bank.md`. Executive summary + per-student profiles at `voc/lessons/raw/MINING.md`.
- Re-mining under new lenses (objection patterns, mouthpiece-specific, age-segment, fear-of-failure, etc.) appends to the same JSONL with `mining_angle: <new-lens>`. Coaching-db /mine subcommand pattern.
- Each file has frontmatter (student_name, student_email, fathom_url, share_url, date, duration_min, speakers) + AI Summary + Action Items + diarized transcript. Format mirrors `voc/sales-calls/raw/` so existing agents can read both.

**Initial corpus stats (2026-02-17 to 2026-05-15):**
- 177 Fathom recordings total in window
- 95 lessons across 57 students written
- 2 trial calls written (Rich Worcester, Sandra Woonings)
- 3.6MB of markdown
- 0 missing transcripts

Top-volume students (3 lessons each): Sandra Woonings, Bill Biffle, Emil Winther, Francesco Cangi, Jason Ashbaugh, Johannes Plechinger, Kathryn M Niemasik, Mark Righele, Michael T Maher, Michelle Gutierrez, Peter Roche, Ranbo, Robert Steward.
