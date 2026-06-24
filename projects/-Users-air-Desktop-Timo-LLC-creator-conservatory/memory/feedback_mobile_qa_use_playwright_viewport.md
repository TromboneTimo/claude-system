---
name: mobile-visual-qa-must-use-real-css-viewport-playwright-not-headless-dsf
description: "For mobile responsive QA, set the CSS viewport directly (Playwright setViewportSize) or use window-size = CSS_px * DSF. Headless Chrome --window-size=390 --force-device-scale-factor=2 renders at 195 CSS px (HALF a phone) and produces FALSE text-overflow/clipping. Verify overflow numerically before \"fixing\" it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2d46792e-6feb-41ad-a168-9139c4c7efe8
---

**The trap:** `chrome --headless --force-device-scale-factor=2 --window-size=390,X` does NOT give a 390px CSS viewport. The DSF halves it to ~195 CSS px, narrower than any real phone, so EVERY line of text clips on the right and the page looks catastrophically broken on "mobile" when it is actually fine.

**2026-06-07 incident:** On the fb-funnel capture page I screenshotted "mobile" this way, saw the headline and all descriptions clipped, and started chasing a phantom horizontal-overflow bug (added minmax(0,1fr), min-width:0, overflow-wrap, shrank the headline). Driving a real browser at a true 390px viewport (Playwright `setViewportSize({width:390})`) reported `documentElement.scrollWidth === 390`, `0` overflowing elements: the page was never broken. The defensive CSS was harmless but the hunt was wasted.

**How to do mobile visual QA correctly:**
1. Prefer Playwright: navigate FIRST, then `browser_resize(390, 844)` (navigation resets the viewport, so resize AFTER load), then measure `document.documentElement.scrollWidth` vs `clientWidth`. `scrollWidth > clientWidth` = real overflow; equal = fine.
2. Find the actual offender, never guess: enumerate `document.querySelectorAll('body *')` and flag any `getBoundingClientRect().right > clientWidth`.
3. If using headless Chrome for the image, window-size must be `CSS_px * DSF` (e.g. 390 CSS at 2x = `--window-size=780`). Even then, trust the numeric overflow check over the eyeball.
4. Playwright blocks `file://`; serve the folder (`python3 -m http.server PORT`) and use `http://localhost:PORT/...`, then kill the server after.

**Rule:** before declaring a responsive bug, confirm it numerically (scrollWidth/clientWidth) at the REAL CSS width. A clipped screenshot alone is not proof. Ties to [[feedback_verify_before_done]] and the visual-self-qa protocol. See also [[reference_conservatory_landing_page]] for the fb-funnel page these screenshots were of.
