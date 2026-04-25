# Proven Template Pointer

The "12-move converter" template comes from Harrison's April 2026 embouchure video (YouTube ID `O4a-q93ENAg`). That video generated approximately $36K in attributed sales.

## Where the source files live

- **Memory pointer:** `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/project_proven_converter_template.md` (the 12-move template, distilled)
- **Full transcript:** `/Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md`
- **YouTube database entry:** `/Users/air/Desktop/Precision-Brass/youtube-database/2026-04_embouchure-truth_O4a-q93ENAg/`
  - `analysis.md`. What worked and why.
  - `transcript.md`. Mirror of the transcript.
  - `comments-top.md`. Highest-engagement comments. Look here for emotional resonance proof.
  - `metadata.json`. View count, sales attribution, like count.
  - `comments.json`. Full raw comment dump.

## How Agent A applies this template

When proposing a YT-WINNER-PATTERN-anchored idea, the agent must explicitly map the proposed video to the 12 moves. For each idea, list:

1. **Hook move:** how does the new video's hook mirror the embouchure video's hook structure?
2. **Identity arc move:** how does it follow the same identity progression?
3. **Demonstration move:** what's the equivalent of the on-camera embouchure demo for this new topic?
4. **Comment-trigger move:** what phrase or moment is engineered to make viewers comment "I needed this"?

If the agent can't map at least 4 of the 12 moves to the new idea, it's not actually anchored on the winner pattern. It's a fresh idea that should go through Agents B/C/D/E instead.

## Why this matters

The 1-2 ideas anchored on YT-WINNER-PATTERN are NOT just "another trumpet topic". They are intentional clones of a proven structural pattern, applied to a new pain point. The point is to reuse what verifiably worked while changing the surface topic.

If the new idea doesn't structurally match the winner, label it as a variety-lens idea instead. Don't pretend something is anchored when it isn't.

## When more winners get added to the database

This skill is forward-compatible. As `youtube-database/index.json` accumulates more `status=winner` entries, Agent A reads ALL of them and extracts patterns common across multiple winners (not just the embouchure video). Cross-winner patterns are stronger signal than single-video patterns. Update this file's "Where the source files live" section as new winners come in.

## Facebook winning ads (parallel proven-conversion source)

Agent A also reads the Facebook ads database, mirrored against yt-vault structure.

- **Database path:** `/Users/air/Desktop/Precision-Brass/facebook-ads-database/`
- **Index:** `index.json` (filter by `status=winner`)
- **Per-ad files:** `analysis.md`, `creative/copy.md`, `performance.json`, optionally `comments-top.md`, `metadata.json`
- **Ingest skill:** `fb-vault` (reference only. don't invoke from pb-script)

**Why both channels matter:** YouTube long-form converts through narrative arc and demonstration. FB ads convert through hook + identity collision in <100 words. The patterns that recur across BOTH (the language, the named pains, the identity arc) are the highest-confidence signal for what truly resonates. When Agent A finds a phrase or angle that appears in winners on both channels, that's a tier-1 anchor for the new idea.

**Empty-database state (currently):** As of 2026-04-25, `facebook-ads-database/index.json` shows 0 ads. Agent A handles this gracefully (see SKILL.md Agent A prompt). When ads start landing, the agent automatically picks them up on the next run.

## Anchor labeling

When labeling an idea as anchored on a winner pattern, use the most specific label:
- `YT-WINNER-PATTERN`: derived from one or more YouTube winners
- `FB-WINNER-PATTERN`: derived from one or more FB ad winners
- `CROSS-WINNER-PATTERN`: derived from elements that appear in BOTH (highest signal)
