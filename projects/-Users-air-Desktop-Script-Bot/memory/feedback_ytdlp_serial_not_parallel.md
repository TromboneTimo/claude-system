---
name: yt-dlp serial, not parallel for longform
description: Running yt-dlp in parallel (xargs -P N) against YouTube triggers InnerTube API rate limits and ConnectionResetError on metadata fetch. Default to serial with jitter.
type: feedback
originSessionId: 711b4668-224d-40c4-ad65-b97fb69efd6a
---
Download longform (and really any yt-dlp batch against YouTube) **serially**, not in parallel. The existing `b-roll/download.sh` uses `xargs -P 6` which is fine for TikTok/Instagram but kills longform YouTube.

**Why:** On 2026-04-15, a `-P 6` batch produced 4 of 5 longform `ConnectionResetError` at the `Unable to download API page` step while 1 survived (the one that got past the InnerTube metadata fetch before the per-IP rate limit kicked in). The URLs themselves were fine, confirmed by running `yt-dlp -F` on each afterward. The parallel burst was the only cause.

**How to apply:**
- For longform YouTube: run serially (`for id in ...; do yt-dlp ...; sleep 10; done`).
- Use these flags to survive transient errors without burning the IP: `--retries infinite --fragment-retries infinite --retry-sleep 5 --sleep-requests 1 --sleep-interval 3 --max-sleep-interval 8 --socket-timeout 30 --concurrent-fragments 1`.
- If Timo's batch contains a mix, split the pipeline: parallel for shorts/TikTok/IG, serial for longform YouTube.
- `b-roll/download.sh:57` still has `-P 6`. If it gets re-run with longform in the batch, it WILL fail the same way. Recommend fixing or branching that script by platform.
- The same rate limit hits `yt-dlp -F` / `--print` probes. If probing multiple URLs in a loop, add `sleep 4+` between them or probe one at a time.
