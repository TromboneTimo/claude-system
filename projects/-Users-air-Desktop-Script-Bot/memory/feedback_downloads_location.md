---
name: Downloads always go to ~/Downloads
description: Never save one-off downloads (Instagram/TikTok/YouTube clips, etc.) into the Script Bot project folder. Default to ~/Downloads unless Timo explicitly says otherwise.
type: feedback
originSessionId: 016ec2f0-1515-4fc2-8890-c8471901a686
---
All one-off video/asset downloads go to `~/Downloads/`, NOT into `/Users/air/Desktop/Script Bot/b-roll/instagram/` (or any subfolder of the project).

**Why:** Timo explicitly corrected this on 2026-04-17 after I dumped a 1.1 GB Instagram reel into the project tree. The project folder is for curated b-roll only, not a landing pad for fresh pulls. Downloads are ephemeral and triaged from ~/Downloads.

**How to apply:**
- When Timo pastes a URL (Instagram, TikTok, YouTube, anywhere) with no destination specified, output goes to `~/Downloads/`.
- Still apply the standing rules: auto-convert to ProRes MOV and delete the MP4, log source/creator/URL.
- If the download is clearly part of a curated project collection (e.g. Timo says "add this to the Nikocado b-roll"), then the project folder is fine, but ASK or wait for explicit placement cue.
- Default path: `~/Downloads/<platform>-<type>-<id>.mov`.
