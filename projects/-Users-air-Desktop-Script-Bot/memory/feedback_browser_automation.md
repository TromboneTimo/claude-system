---
name: Use playwright for browser automation — screenshots, downloads, scraping
description: Always use playwright (headless Chromium) for screenshots, browser-based downloads, and web scraping instead of saying it's not possible.
type: feedback
---

Use playwright with headless Chromium for any browser-based task: screenshots of web pages, interacting with download sites, scraping content, etc.

**Why:** User needed YouTube screenshots and I wasted time saying I couldn't do it. Playwright was installable via pip and worked perfectly with `pip3 install playwright && playwright install chromium`.

**How to apply:**
- Playwright is installed globally via npm (`npx playwright`) with Chromium — use it for all browser tasks
- Screenshots: use Node.js script with `const { chromium } = require('playwright')` + `page.screenshot()`
- Set `locale: "en-US"` to avoid Japanese/other locale issues
- For TikTok/YouTube downloads: use `yt-dlp` (install path: `/Users/air/Library/Python/3.10/bin/yt-dlp`)
- For YouTube search: `yt-dlp --flat-playlist -j "ytsearch:query"` to find video URLs
- **For Instagram downloads: use `gallery-dl` with Chrome cookies** (`gallery-dl --cookies-from-browser chrome -d /Users/air/Downloads "<url>"`). yt-dlp's Instagram support is broken as of April 2026 (connection resets, API access denied). gallery-dl installed via `brew install gallery-dl`.
- For download sites (tikmate.io, sssinstagram.com): automate with playwright as last resort only
- Always try the programmatic approach first, never punt to the user
