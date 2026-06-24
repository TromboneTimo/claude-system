---
name: instagram-chrome-cookies
description: Instagram downloads via yt-dlp fail on login-gated posts; use --cookies-from-browser chrome to bypass.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b8047144-6cc0-430e-8c93-795dd205095a
---

For Instagram URLs, run yt-dlp with `--cookies-from-browser chrome` from the start. Safari cookies (`Cookies.binarycookies`) hit macOS permission errors. gallery-dl also redirects to login without auth.

**Why:** 2026-05-15 batch of 6 IG posts. 2 worked anonymously, 4 hit "ConnectionResetError" then "redirect to login". Chrome cookies fixed all 4 instantly. Burned ~4 retry rounds before trying it.

**How to apply:** Default IG command:
`yt-dlp --cookies-from-browser chrome -f "bv*+ba/b" --merge-output-format mp4 -o "%(title).80s [%(id)s].%(ext)s" <url>`
If Chrome cookies also fail, fall back to playwright-driven snapinsta.to (user has history of using that, see `SnapInsta.to_*.mov` files in ~/Downloads).
