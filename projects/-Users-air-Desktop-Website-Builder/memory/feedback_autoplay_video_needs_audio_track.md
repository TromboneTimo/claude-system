---
name: Autoplay videos need a silent audio track, do not strip with ffmpeg -an
description: Chrome and some Safari builds silently refuse to autoplay `<video autoPlay muted>` if the file has zero audio tracks. Encoding hero videos with `-an` produces a file that loads but never plays, showing only the poster.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Never strip audio with `-an` when re-encoding a hero video meant for browser autoplay. Some browsers (Chrome stable, iOS Safari) refuse to autoplay a `<video autoPlay muted>` element if the MP4 has no audio stream, regardless of the `muted` attribute. The video element loads, renders the poster, and sits there.

**Why:** On otto-cristofoli (2026-04-22), I trimmed and re-encoded both hero videos with `-an`. CDN served valid H.264 files, ffprobe confirmed they decoded, but in Safari the videos would not autoplay. Samurai Brass page showed the Eijiro poster image instead of the video; Music System Italy page was solid black (no poster set as fallback either). Fix: re-encode with `-f lavfi -i anullsrc=r=44100:cl=stereo ... -c:a aac -b:a 32k -shortest` to inject a silent AAC track.

**How to apply:**
- For any `<video autoPlay muted loop>` pattern, the encoded MP4 MUST include at least a silent audio track. Canonical ffmpeg:
  ```bash
  ffmpeg -y -i input.mp4 -f lavfi -i anullsrc=r=44100:cl=stereo \
    -map 0:v -map 1:a -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p \
    -c:a aac -b:a 32k -shortest -movflags +faststart output.mp4
  ```
- Always set a `poster` attribute too. If the video fails to play on any browser, the poster shows instead of black, so the issue is visible and debuggable.
- Pre-deploy verification for any hero video change: open the deployed URL in Safari AND Chrome, watch for 3 seconds. No autoplay = ffmpeg step is wrong.
- `curl -I` + ffprobe are not enough. Both will pass for a broken-autoplay file. The only reliable check is visual playback in an actual browser.
