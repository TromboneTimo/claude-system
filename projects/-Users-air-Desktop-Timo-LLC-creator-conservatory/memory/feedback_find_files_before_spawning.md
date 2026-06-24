---
name: Find Files Before Spawning Agents
description: When Timo references files on disk ("in Downloads", "in [X] workspace"), locate them with ls/Glob FIRST, then pass real absolute paths to subagents. Never spawn an agent that says "read the PDF in this session's context" when the file is on disk.
type: feedback
originSessionId: 5ceb158a-623a-4ed4-aafa-3de491b0febc
---
When Timo mentions a file is on disk ("transcript is in downloads folder", "robinsons remedies workspace has brand info"), ALWAYS:

1. Run `ls -lt ~/Downloads/ | head -5` or equivalent to find the actual file
2. Grep/ls the referenced workspace to confirm brand context files exist
3. Pass absolute paths in the agent prompt, e.g. `/Users/air/Downloads/filename.pdf`
4. For multi-page PDFs, tell the agent to use Read with `pages` param in chunks

**Why:** 2026-04-23 incident. Spawned a marketing-researcher for Robinson's Remedies Apr 8 transcript analysis. Told the agent "read the transcript attached in this session's context window". the attached PDF in the conversation is NOT the same as a disk file accessible to the subagent. Timo had already mentioned the PDF was in Downloads + RR workspace had brand files. He had to correct me with "fuck you" energy. The fix was one `ls` away.

**How to apply:** Any time a prompt mentions a transcript/document/file:
- If it's attached inline only, paste content or describe it in the agent prompt
- If it's on disk, find the path, pass it explicitly
- Never say "it was just loaded" or "in this session's context". subagents don't have the parent's context window

**Known Robinson's Remedies paths:**
- Workspace root: `/Users/air/Desktop/Robinsons Remedies/`
- Brand context: `/Users/air/Desktop/Robinsons Remedies/context/` (brand.md, products.md, audience.md, competitors.md, brand-guidelines.md)
- CLAUDE.md at workspace root with voice + color + skill rules
- References folder exists for advertorial structure, awareness levels, reusable assets

Related: [Read The Database Before Asking](feedback_read_before_asking.md), [Read Inputs Not Conventions](feedback_read_inputs_not_conventions.md), [YouTube URL = yt-dlp Immediately](feedback_youtube_url_go_to_transcript.md)
