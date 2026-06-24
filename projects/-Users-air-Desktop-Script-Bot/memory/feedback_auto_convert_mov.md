---
name: Auto-convert all downloads to MOV, save directly to Downloads, never copy old clips
description: Every new video download goes straight to ~/Downloads as ProRes MOV. Never copy existing b-roll clips to Downloads. Never leave MP4s.
type: feedback
---

Every new video download must go directly to `~/Downloads/`, convert immediately to ProRes MOV, and delete the MP4. That's it.

**Why:** User was pissed off when I copied old nikocado b-roll clips into Downloads alongside new downloads. Only new downloads go to Downloads — never pull in previous b-roll clips.

**How to apply:**
- Always download directly to `~/Downloads/` with yt-dlp `-o "/Users/air/Downloads/..."`
- Immediately after: `ffmpeg -i input.mp4 -c:v prores_ks -profile:v 1 -c:a pcm_s16le output.mov -y`
- Delete the .mp4 after successful conversion
- NEVER copy b-roll clips from the project folder to Downloads — only fresh downloads go there
- This is automatic — never ask, never skip
