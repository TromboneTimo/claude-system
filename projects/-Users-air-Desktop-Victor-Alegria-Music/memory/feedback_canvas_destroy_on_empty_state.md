---
name: Never overwrite chart parentElement.innerHTML on empty state
description: Empty-state rendering for Chart.js canvases must NEVER do parentElement.innerHTML=... because it destroys the canvas, breaking all subsequent renders for that chart. Use an overlay div pattern instead.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
When a Chart.js canvas has no data to render, the wrong fix is `ctx.parentElement.innerHTML = '<div>No data</div>'`. That obliterates the canvas element. The next time `getElementById(canvasId)` runs (when the user clicks a tab that DOES have data), it returns null, and the chart can never re-render.

**Symptom:** click YouTube tab (no content data) -> see "No content drove clicks in this window" empty state -> click Meta Ads tab (which has data) -> still see empty state, even though the data is in the cache. Charts permanently dead until full page reload.

**Why this happened:** the dashboard caches per-platform data correctly. The data WAS there. But the empty-state code on a prior tab destroyed the canvas DOM nodes. The next tab's renderHorizontalBar call hit `ctx === null` and either crashed silently or kept the dead empty-state in place.

**Fix pattern (use this everywhere a Chart.js canvas might be empty):**

```js
function setEmptyOverlay(ctx, message) {
  if (!ctx) return;
  const parent = ctx.parentElement;
  if (!parent) return;
  let overlay = parent.querySelector('.section-empty');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.className = 'section-empty';
    parent.appendChild(overlay);
  }
  overlay.innerHTML = `<div class="section-empty-title">${message}</div>`;
  ctx.style.display = 'none';
  overlay.style.display = '';
}
function clearEmptyOverlay(ctx) {
  if (!ctx) return;
  const parent = ctx.parentElement;
  if (!parent) return;
  const overlay = parent.querySelector('.section-empty');
  if (overlay) overlay.style.display = 'none';
  ctx.style.display = '';
}
```

Always call `clearEmptyOverlay(ctx)` BEFORE `new Chart(ctx, ...)` and `setEmptyOverlay(ctx, msg)` for empty cases.

**Where this bit:** `dashboard/channel-attribution.html` lines 566 (trend chart), 618 (donut), 658 (horizontal bars). Caught 2026-05-06 after the user reported the bug at least 3 times across the session before the actual root cause was diagnosed.

**Audit prompt for future dashboard pages:** before declaring a Chart.js dashboard done, grep for `parentElement.innerHTML` in the file. Any match is a canvas-destruction bug.
