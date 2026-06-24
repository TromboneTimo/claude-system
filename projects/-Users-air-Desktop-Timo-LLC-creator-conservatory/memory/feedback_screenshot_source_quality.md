---
name: Screenshot Source Quality
description: Never use IDE preview thumbnails from session JSONL as production assets. Always pull from the live source URL at high res.
type: feedback
originSessionId: 793ec4c2-d529-431d-8a47-1773578404b2
---
When user pastes a screenshot in chat, the JSONL stores a downsampled preview (~480px, ~130KB). That is NOT a usable production asset. Using it produces visibly low-res images in slides, decks, and exports.

**Why:** 2026-04-13 designer-vs-marketer.html slide 2. Pasted otto-website.png from JSONL extraction. Looked passable at 1440x900 headless render. Looked like garbage in Safari at native deck scale. Timo correctly furious.

**How to apply:**
1. When user shares a screenshot of a website, treat the chat image as a **reference**, not a source asset.
2. Get the URL: check Chrome history first (`sqlite3 ~/Library/Application\ Support/Google/Chrome/*/History "SELECT url FROM urls WHERE url LIKE '%keyword%' ORDER BY last_visit_time DESC"`), then ask if not found.
3. Capture at 2x or 3x with `--force-device-scale-factor=2` and `--window-size=2560,1440` minimum for full-bleed slide assets.
4. Visual QA: render slide at 1920x1080 minimum AND inspect the inserted image at native size before declaring done. If the source PNG is under 500KB, it's almost certainly too low-res for a deck.
5. Rule of thumb: production deck images should be 1MB+. Conversation-pasted screenshots are typically under 200KB. That's the tell.
