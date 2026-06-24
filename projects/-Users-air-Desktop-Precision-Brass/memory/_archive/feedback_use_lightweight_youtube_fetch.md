---
name: use-lightweight-youtube-fetch
description: "For YouTube metadata, descriptions, thumbnails, and tracked-link extraction, use curl + oEmbed (or yt-dlp if installed). Reserve Playwright for actual rendered-page screenshots. Per Timo 2026-05-15 (\"It's just kind of fucking annoying the way you're doing this. You're doing this in a really inefficient way.\") Helper script at scripts/yt-fetch.sh."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0b9fa848-7b9a-4dda-b396-5cc296f16876
---

# Use the lightest tool that gets the data.

**Rule:** For pulling YouTube metadata (title, author, thumbnails, description, tracked link extraction), use the lightweight stack:

1. **Thumbnails** are predictable URLs, no API call needed: `https://i.ytimg.com/vi/{VIDEO_ID}/mqdefault.jpg` (also `default.jpg`, `hqdefault.jpg`, `maxresdefault.jpg`).
2. **Title + author + provider** via oEmbed (no auth, returns JSON): `curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json"`.
3. **Full description** via curl + regex on the watch page HTML: `curl -s "https://www.youtube.com/watch?v=VIDEO_ID"` then extract `"shortDescription":"..."` from `ytInitialPlayerResponse`.
4. **Convenience helper:** `dashboard/scripts/yt-fetch.sh VIDEO_ID` prints all of the above as one JSON blob, including tracked-link extraction.

**Reserve Playwright for actual rendered-page screenshots** (e.g. Harrison's channel page banner, the rendered dashboard for verification). NOT for scraping HTML data that's already in the page source.

**Why:** 2026-05-15. I used `mcp__playwright__browser_navigate` + `browser_evaluate` to read YouTube descriptions. That spawns a headless Chromium, navigates, waits for hydration, runs JS in the page, then closes. About 100x more expensive than `curl + python3 regex`. Timo: "Why aren't you using YouTube fetch to just get the thumbnail and description and stuff? It's just kind of fucking annoying the way you're doing this. You're doing this in a really inefficient way."

**How to apply:**
- "Need a thumbnail?" -> derive the URL from the video_id pattern. Don't fetch.
- "Need title + author?" -> oEmbed (single curl, no auth).
- "Need the description text or links from the description?" -> `scripts/yt-fetch.sh VIDEO_ID` or inline curl + regex on `shortDescription`.
- "Need full metadata + transcript + comments?" -> `yt-dlp` if installed (canonical for ingestion). Browse `youtube-database/index.json` for what we already have stored.
- "Need a screenshot of the actual rendered page (channel banner, video player UI)?" -> Playwright is correct. That's its job.

**Generalization:** The lightest tool that returns the data is the right tool. Browsers are for rendering verification; HTML is for parsing; APIs are for structured pulls. If the data is in `<meta>` tags or a JSON blob on the page source, never launch a browser.

Related: [[query-destination-schema-first]] (same family of "use the right primitive, not the heaviest tool you have").
