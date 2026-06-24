---
name: Visual QA must include interacted states, not just first paint
description: Render and read the playing/hovered/scrolled state of any UI before declaring done. Native HTML element defaults (video controls, scrollbars, focus rings) only appear after interaction and are usually ugly.
type: feedback
originSessionId: 0096cd8e-35b8-40dc-aba3-d1ad014711e8
---
When shipping any UI change involving HTML media or interactive elements, render and READ the interacted state (playing video, hover, scrolled, modal open) before reporting done. Static-poster screenshots miss native browser defaults that appear only after interaction.

**Why:** On the Otto Shires theatre section I shipped a cinema video frame and only verified the paused poster screenshot. Timo clicked play and got the hideous default Safari video controls bar covering the bottom of the video plus a 400px black void below from over-eager spacing. He had to call out "look at how dogshit they are" because I never saw the playing state. Same pattern would catch native scrollbars, default focus rings on form elements, and modal stack-order bugs.

**How to apply:**
- Any `<video controls>` ships native UI that I have never seen in static renders. Default to custom controls or hide native UI from the start.
- After any UI edit, list the interaction states (paused/playing, no-hover/hovered, top/scrolled, closed/open) and screenshot at least the most-likely-broken one.
- For video specifically: open the page, click play, screenshot mid-playback. If I can't drive the click in headless, drive Safari and capture or ask Timo to confirm explicitly before saying done.
- Spacing decisions made against a static screenshot lie: a video frame with poster looks tighter than the same frame mid-playback with controls overlaid. Re-eval spacing in the playing state.
