---
name: Make long background downloads visibly progressing
description: Don't use -q/silent for long yt-dlp runs. Use stat -f %z (not ls -lah) to check bytes. Show ETA upfront, not after Timo asks.
type: feedback
originSessionId: 711b4668-224d-40c4-ad65-b97fb69efd6a
---
When launching any background download/conversion that takes >2 minutes, make progress visible and give an ETA upfront. Don't make Timo ask "still not done?" twice.

**Why:** On 2026-04-15 Timo pinged "not downloading at all" and "still not done?" within ~5 min of a longform batch that was actually downloading fine at 1-2 MB/s. Two root causes: (1) the script ran `yt-dlp -q --no-warnings` with stdout piped to /dev/null, so there was nothing to tail; (2) I was reporting `ls -lah` which rounds ("1.0G" stayed static on screen for 3 samples while the file grew from 1.13 GB to 1.15 GB). Both made a healthy download look dead.

**How to apply:**
- On long yt-dlp runs, prefer `--newline` (progress per line) and log stdout: `yt-dlp ... --newline >"logs/$base.dl.log" 2>"logs/$base.err"`. Never `-q` on anything Timo might want to monitor.
- For byte-level polling use `stat -f "%z %N" file` on macOS, not `ls -lah`. `ls -lah` rounds to 1-2 sig figs and makes actively-growing files look frozen.
- Give an ETA BEFORE launch: probe `yt-dlp --print "%(duration)s"` for each URL, estimate MP4 size at ~5-10 MB/min of 1080p, divide by observed rate, add 10s cooldown per video plus ProRes conversion time (roughly real-time on M-series Mac). Tell Timo the ballpark window. He would rather hear "15 min" upfront than ask 3 times.
- If a download legitimately looks stuck, verify with `stat -f %z` twice 5s apart before reporting a problem. Don't alarm on rounded numbers.
