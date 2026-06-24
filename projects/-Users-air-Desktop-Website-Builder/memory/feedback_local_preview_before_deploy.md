---
name: Use local preview, not Vercel, for visual verification
description: For visual changes, run `npm run dev` and open localhost in Safari instead of deploying to Vercel each time
type: feedback
originSessionId: 63a1d3ac-6e75-4ca4-b088-91a9c0a70ba6
---
For visual changes (video swaps, layout edits, image changes), use the local Next.js dev server and open `http://localhost:3000/<route>` in Safari to verify. Do NOT push to Vercel just to eyeball a change.

**Why:** Timo doesn't want a Vercel deploy on every iteration. Each push is slow, costs build minutes, and clutters deployment history. The dev server renders the same components and assets, fast enough for visual QA.

**How to apply:**
- After file/asset changes, run `cd clients/<name> && npm run dev` in the background.
- Open `http://localhost:3000/<route>` in Safari with `open -a Safari ...`.
- Only run `vercel deploy --prod` when Timo explicitly asks to publish or ship. The visual gate is satisfied by the localhost render.
- If a dev server is already running, reuse it; check with `lsof -i :3000` before starting a new one.
