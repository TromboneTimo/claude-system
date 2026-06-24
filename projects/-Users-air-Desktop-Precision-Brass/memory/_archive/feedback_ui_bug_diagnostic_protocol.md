---
name: ui-bug-diagnostic-protocol
description: "When the user reports a UI / layout / visual bug, follow a specific diagnostic protocol. Pixel coordinates over screenshots. Root cause over symptom-patching. Stop iterating after 2 failed fixes."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d0c10100-009e-4416-b9c9-ee766cc9fe29
---

When the user reports a UI / CSS / layout / visual bug, follow this protocol. Don't deviate.

**Why this exists:** caught 2026-05-17 when the meta-ads dashboard column-misalignment bug took multiple sessions and angry user feedback before I finally ran `getBoundingClientRect()` on the live page and found the real cause (missing `table-layout: fixed`). The user's verbatim feedback: "I've told you this a million times, but every time you say 'Oh, I get it,' but then you don't fucking do shit." Every prior attempt patched a visible symptom instead of diagnosing the structural cause.

## The protocol

### Step 1. Replay the user's exact complaint, with their words

If they said "the SPEND column shows 1 and LEADS shows $7.39," the diagnostic is about those specific column labels and those specific data values. Do not translate to "the columns look weird." Don't lose the specifics in paraphrase.

### Step 2. Get measurable evidence from the live page

For layout bugs: use Playwright `browser_evaluate` to extract `getBoundingClientRect()` for every relevant element (headers, data cells, etc). Compare positions numerically.

```js
const tbl = document.querySelector('table.X');
const ths = [...tbl.querySelectorAll('thead th')];
const tds = [...tbl.querySelectorAll('tbody tr:first-child td')];
const pos = el => ({ left: el.getBoundingClientRect().left, right: el.getBoundingClientRect().right });
// Assert: for each i, ths[i] position == tds[i] position
```

For content bugs: screenshot + Read + assert the specific text the user named is present at the specific location.

For state bugs: log the relevant variables at the point of failure, not at the point of mount.

**Eyeballing a screenshot is NEVER enough.** Anti-aliasing, device pixel ratio, font rendering, and your own pattern-matching biases all distort what you think you see. Use coordinates.

### Step 3. State your hypothesis BEFORE the fix attempt

Write the hypothesis as a falsifiable claim, e.g. "I believe the SPEND header is at x=673 but the SPEND data value is at x=775 because the table uses table-layout: auto which treats col width as hints, allowing column widths to vary per row based on content."

If you can't write the hypothesis as a falsifiable claim with element selectors and CSS property names, you haven't diagnosed the bug. Go back to Step 2.

### Step 4. Fix the root cause, not the symptom

A symptom-fix tweaks a visible value (column width, padding, font size). A root-cause fix changes the underlying mechanism producing the symptom (table-layout, box-sizing, flex-direction). Symptom fixes work in one configuration and break in another. Root-cause fixes are stable.

If two symptom fixes have already failed, the third attempt is forbidden until you have identified the root cause. Write down the root cause hypothesis before coding.

### Step 5. Verify with the same coordinates check that diagnosed the bug

After the fix is deployed, re-run the `getBoundingClientRect()` check from Step 2. Confirm header.left == data.left for every column. The verification protocol must be the SAME as the diagnostic protocol. Otherwise you're checking a different thing than the user's complaint.

### Step 6. Add a code comment explaining why the fix exists

Any non-obvious CSS rule that prevents a specific bug class gets a comment in the file pointing at the bug it prevents. Without that comment, the next session sees a "weird rule" and removes it as cleanup.

### Step 7. Save the lesson to memory if the bug took more than one attempt

If the bug cost more than one fix attempt, write a feedback memory naming:
- The bug class
- The diagnostic technique that finally worked
- The fix
- A short rule for prevention

## Forbidden behaviors

- **"I see the problem" without coordinates.** Forbidden. Either say "I have N hypotheses, let me verify which" or stay silent until coordinates are pulled.
- **Bypassing `dashboard-deploy-gate` for a UI bug.** Forbidden. The gate forces Playwright verification; that friction is the point.
- **Iterating after 2 failed fixes.** Forbidden. Stop, enumerate prior attempts and why each failed, propose a fresh diagnostic plan.
- **Going faster when the user is angry.** Anti-pattern. Slow down. The cost of one slow-but-correct response is far lower than three fast-but-wrong ones.
- **Eyeballing a thumbnail as "visual verification."** Forbidden. Visual verification requires extracted measurable properties, not "the screenshot looks fine."

## Specific to layout / CSS bugs

- Look up the actual W3C / MDN specification behavior of the elements involved (col, sticky positioning, border-collapse, flexbox container queries). These are knowable. Don't guess.
- The default value of every CSS property matters. `table-layout: auto` is default and treats col width as hints. `box-sizing: content-box` is default and excludes padding. `position: static` is default and ignores left/top. Verify what default you're working against.
- When you change one CSS property, document what other properties it now depends on. `table-layout: fixed` only works if col widths are set. `position: sticky` only works inside a scrolling container. Constraints compose.

## Specific to recurring bugs

If the user says "I've told you this multiple times," the next action is NOT another fix attempt. It's:

1. A written enumeration of every prior fix attempt for this bug, with timestamps if visible in git history
2. Why each one failed (what symptom did it address vs what root cause did it miss)
3. A fresh diagnostic plan starting from Step 1 of this protocol

THEN a fix. Skipping the enumeration is what causes the count to keep climbing.
