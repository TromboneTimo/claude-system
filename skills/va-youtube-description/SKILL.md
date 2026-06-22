---
name: va-youtube-description
description: Generates Victor Alegria Music YouTube description + chapters from a finished video file. Transcribes the video with mlx-whisper, identifies beat boundaries with real timestamps (no guessing), writes curiosity-driven chapter titles (NOT generic labels like "Intro"), assembles the description using Victor's locked template (Free Masterclass link line 1, Testimonials playlist line 2, 3-paragraph hook, Chapters block, hashtags), and presents it as plain markdown in chat for Timo to approve BEFORE any file write. Use this skill whenever Timo says "make a YouTube description", "write the description for this video", "youtube description for X", "description and chapters", "/va-youtube-description", "describe this video for YouTube", or pastes a video file path (.mov / .mp4) and asks for the description. ALWAYS load the locked template at `references/description-template.md` before drafting. Output plain markdown in chat first (chat-draft-before-render rule). Never write to files until Timo approves.
---

> **CLONE NOTE (2026-05-25):** Cloned from Precision Brass. The orchestration logic and infra paths are re-pointed to Victor Alegria Music. BUT the VOICE, ICP, example scripts, conversion-trigger taxonomy, lens names, and locked-line templates in `references/` and `agents/` STILL CONTAIN PRECISION BRASS / HARRISON CONTENT. They must be re-derived from Victor's own VOC before this skill is run to produce real Victor content (Phase 5). This build excludes paid Meta ads.


# pb-youtube-description. YouTube description + chapters for Victor's videos

## When to fire

- Auto: any time Timo says "make a YouTube description", "write the description", "description for this video", "description and chapters", "youtube description"
- Auto on: a video path (`.mov`, `.mp4`, etc.) in `~/Downloads/` or `Precision-Brass/output/` mentioned alongside "YouTube" or "description"
- Manual: `/va-youtube-description`

## Hard preconditions (do not skip)

1. **Load `references/description-template.md`.** Locked format. Voice fingerprint. Hashtag set. Curiosity-chapter rules.
2. **Confirm the video file exists.** Don't pretend to transcribe a path that isn't there.
3. **Read the project memory `feedback_chat_draft_before_render.md`.** This skill is a deliverable-producing skill. Show draft in chat FIRST. No file writes until Timo approves.

## Pipeline

### Step 1. Locate the video

- Default: `~/Downloads/<name>.mov` or `~/Downloads/<name>.mp4`
- If Timo gave a fuzzy reference ("mouthpiece test final video"), `ls ~/Downloads/` and match. If 2+ files match, ASK before transcribing.
- Confirm the file exists before doing anything else.

### Step 2. Get duration + extract audio

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "<video>"
ffmpeg -y -i "<video>" -vn -ac 1 -ar 16000 -c:a pcm_s16le /tmp/pb_yt_audio.wav 2>&1 | tail -3
```

### Step 3. Transcribe with mlx-whisper (timestamped SRT)

```bash
/Users/air/Library/Python/3.10/bin/mlx_whisper /tmp/pb_yt_audio.wav \
  --model mlx-community/whisper-base.en-mlx \
  --output-format srt \
  --output-dir /tmp 2>&1 | tail -3
```

Output: `/tmp/pb_yt_audio.srt`. Use this for chapter timestamps. NEVER guess timestamps. They must come from the SRT.

For long-form (>30 min), upgrade model to `mlx-community/whisper-small.en-mlx` for accuracy. Default base.en is fine for <15 min content.

### Step 4. Identify chapter beats

Read the SRT and mark each topic shift. Victor's videos typically follow:
- 0:00 Hook (problem statement, money/pain anchor)
- ~0:30-1:00 Demo or apparatus reveal
- Middle beats: 3 mistakes / 3 traps / pedagogical insights (each ~60-90s)
- One at-home test (signature move)
- Why Victor built [system / VAS / converter]
- Correct sequence / final framework
- Free masterclass CTA + what to watch next

Each beat = one chapter. Aim for 8-12 chapters in a 5-15 min video. YouTube requires:
- First chapter at 0:00 exactly
- Minimum 3 chapters
- Each chapter at least 10 seconds long
- Format: `M:SS Title` or `MM:SS Title`. Be consistent across the list.

### Step 5. Write CURIOSITY-DRIVEN chapter titles

This is the highest-leverage step. Generic labels ("Intro", "Demo", "Conclusion") kill click-to-section behavior and weaken CTR on the description preview.

**Bad (banned):**
- Introduction
- The demonstration
- Three mistakes
- Conclusion
- Free masterclass

**Good (proven from the mouthpiece-test description):**
- "The $3,000 mouthpiece collection that won't fix your high C"
- "Same lick, three different mouthpieces. Listen for yourself."
- "The truth: a mouthpiece is just an amplifier"
- "The lie every teacher and manufacturer keeps selling you"
- "The questions nobody asks about your face"
- "Wayne Bergeron mouthpiece: locked-in vs misaligned embouchure"
- "Try this at home. Swap mouthpieces, watch your placement."
- "The one-handed pistol-grip high C test"
- "Why I built the Vertical Alignment System"
- "The correct order: form, place, breathe, play"
- "Free masterclass + what to watch next"

**Rules:**
- Each title is a mini-hook on its own. A scroller scanning chapters should feel pulled into 2-3 of them.
- Lead with concrete nouns (mouthpiece, embouchure, Wayne Bergeron, $3,000, pistol-grip), not abstractions.
- Use Victor-voice fragments: "The truth:", "The lie:", "Why I built", "Try this at home", "The correct order"
- Last chapter = the CTA chapter, but title it like content not a CTA. "Free masterclass + what to watch next" works because the user already saw the link at the top.

### Step 6. Write the 3-paragraph hook

Locked structure (from the approved mouthpiece-test description):

**Paragraph 1. Name the dollar pain.**
Format: "You've spent $X, $Y, maybe $Z on [thing] and you still can't [outcome]. The [thing] isn't the problem. Your setup is."
2-3 short sentences. The flip from "the gear" to "your setup / your face / your apparatus" is the signature move.

**Paragraph 2. What's in the video.**
Format: "In this video I [demonstrate X], then I walk you through [N mistakes / tests / framework], and the [signature move that gives them a 30-second decision tool]."
One sentence, can be long. Always promise a concrete at-home test.

**Paragraph 3. The punchline / reframe.**
Format: One sentence that flips the user's mental model. "If [old behavior produces inconsistent results], that's not a [gear thing]. That's [a face/setup/embouchure thing] dressed up as a [gear thing]."
This is what gets quoted in comments.

### Step 7. Assemble using locked template

See `references/description-template.md` for the exact byte-for-byte structure. The skeleton:

```
Free Masterclass on how to improve your set up -
[VICTOR_MASTERCLASS_URL_PLACEHOLDER]

Testimonials -    • Student Wins/Testimonials  

<3-paragraph hook>

Chapters

0:00 <curiosity title>
0:35 <curiosity title>
...
8:20 <curiosity title>

#trumpetlife #trumpet #trumpetgear
```

Notes on the literal byte format Victor uses:
- Masterclass URL: `[VICTOR_MASTERCLASS_URL_PLACEHOLDER]`. YouTube will truncate it visually in the description preview (renders as `webin...`); paste the full URL.
- The Testimonials line uses a YouTube playlist embed. The plain-text representation is `   • Student Wins/Testimonials  ` with leading/trailing spaces around a bullet. That's how YouTube renders the playlist link. In the deliverable, write the actual playlist URL. Ask Timo for it if not yet stored in `references/links.md`.
- "Chapters" is a plain header. No `##`, no colon, no bold.
- Hashtags are exactly `#trumpetlife #trumpet #trumpetgear` unless the video topic clearly calls for an additional one (e.g. `#embouchure` for embouchure-focused content). Never more than 4. Never use generic hashtags like `#music` or `#tutorial`.

### Step 8. Optional HiRose tracking suffix

If Timo wants tracking, append `?el=<video-slug>` to the masterclass URL. Slug = lowercase, kebab-case, derived from video filename or topic (e.g. `mouthpiece-test-final`). Ask Timo for the slug if the filename is ambiguous. Default to the filename minus extension.

## Output rules (CRITICAL)

### Chat-draft-before-render

Per `feedback_chat_draft_before_render.md`:

1. Show the FULL description as plain markdown in chat first. No code blocks except for the Chapters list itself. Hashtags on the final line.
2. Flag any unknowns at the bottom (slug, testimonials URL, hashtag deviations).
3. Wait for Timo's approval ("looks good", "ship it", "save it") before writing to any file.
4. ONLY after approval: save to `Precision-Brass/output/<YYYY-MM-DD>_<slug>-youtube-description.md` and copy to `~/Downloads/<slug>-youtube-description.md`.

### Never auto-publish

This skill produces a description for Victor/Timo to paste into YouTube manually. There is no auto-upload.

## Failure modes to avoid

1. **Generic chapter titles.** "Intro", "Demonstration", "Outro" kill CTR. Every chapter is a hook. (See Step 5.)
2. **Made-up timestamps.** Always derive from the SRT. If the SRT shows the apparatus reveal at 1:08, write `1:08`, not `1:10` or `1:00`.
3. **Hashtag spam.** Three to four hashtags max. Topic-relevant only. No `#music`, `#tutorial`, `#youtube`.
4. **Skipping the 3-paragraph hook structure.** The reframe paragraph (paragraph 3) is what gets quoted. Skipping it loses the conversion lever.
5. **Writing the description from the script instead of the actual filmed video.** Victor often changes wording on-set. Always transcribe the FINAL filmed file, not the pre-shoot script. If only the script is available, ASK before proceeding.
6. **Pretending you can verify a video file you haven't actually seen.** `ls` first. If the path doesn't resolve, stop and ask.
7. **Writing to files before Timo approves.** Chat-draft-before-render is non-negotiable.
8. **Em dashes.** Global rule. Use periods, commas, colons, or slashes. Hook enforced.

## Reference files

- `references/description-template.md`. Locked byte-for-byte template.
- `references/links.md`. Masterclass URL, testimonials playlist URL, tracking slug conventions.

## When to update this skill

- Victor changes the standing CTA URL or testimonials playlist
- A new hashtag enters Victor's rotation
- Timo flags a chapter-title pattern that consistently works (or doesn't)
- A new video proves a better 3-paragraph hook structure (update template, mark old as deprecated)
