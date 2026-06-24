---
name: Read what Timo attached, not what the tool defaults to
description: When Timo attaches files with specific names (e.g. "Endorsers Carousel.html" plus carousel.jsx), use those. Never fall back to the tool's conventional entry point (like Animation.html) when a more specific entry exists in context.
type: feedback
originSessionId: 5601a336-a003-4d71-a867-052290f3bec8
---
When Timo attaches or references files, read which files correspond to the scene/artifact he cares about NOW. Do not fall back to default entry points just because the tool docs assume them.

**Why:** 2026-04-19. He attached `scene.jsx`, `carousel.jsx`, `Animation.html`, `Endorsers Carousel.html`, `Clean.html`, `Export Frames.html`, plus a new `EXPORT.md`. He said "create mp4 don't remove background." I defaulted to rendering `Animation.html` (the old "Do This Instead" sheet music scene) because my render-animation skill's docs say `Animation.html` is the canonical entry. He actually wanted the NEW thing he'd just built -- the Endorsers Carousel. I ignored the literal file names he pasted and rendered the wrong scene.

**How to apply:**
- When multiple entry HTML files are in the folder/attachments, read the file names. The one most recently attached, most specifically named, or paired with a newly-pasted scene file is the target.
- If ambiguous, list the entry files found and ask which one to render. Don't guess.
- Be especially careful when the tool's skill definition mentions a default file name -- that convention dies the moment Timo attaches something specific.
- Related to "Don't caveat what you can fix": both are forms of letting tool defaults override Timo's context.

**For render-animation specifically:**
- Multiple `*.html` entries in a folder = ask or pick the one matching a newly-pasted scene (e.g., `carousel.jsx` + `Endorsers Carousel.html`).
- Duration detection regex fails on computed values like `duration={window.CAROUSEL_DURATION}`. When regex can't parse, read the linked JSX file and compute it (e.g., ENDORSERS.length * BEAT_DUR = 9 * 5.6 = 50.4s).

**Deeper pattern: generic tools should not hardcode input assumptions.**

2026-04-19: even after I pointed render-animation at Endorsers Carousel.html, the output was STILL the sheet music. Root cause: my driver HTML hardcoded `<script src="scene.jsx">` and `<Scene />`. Those hardcoded values were invisibly overriding the real input. A "generic tool" that silently assumes the input matches its first test case is worse than no tool, because it lies about what it rendered.

Rule: when building a tool driver/wrapper/adapter, extract EVERY structural assumption from the input, not from the template. For render-animation: scan the input HTML for all babel script tags and use those; scan the input for Stage children and render THOSE, not a hardcoded component name.
