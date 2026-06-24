---
name: uppercase-breaks-cjk
description: CSS text-transform uppercase breaks CJK (Japanese/Chinese/Korean) characters and emoji flags - always use normal-case override
type: feedback
---

Never apply CSS `text-transform: uppercase` (Tailwind `uppercase`) to elements containing Japanese, Chinese, Korean text or emoji flag sequences. The uppercase transform corrupts or hides these characters.

**Why:** Applied `uppercase` to a nav item containing Japanese text (日本語) and flag emoji. The characters rendered incorrectly/invisibly in the browser. Required a fix with `normal-case` override.

**How to apply:** Whenever a UI element contains CJK text or emoji alongside uppercase-styled siblings, always add `normal-case` (and `tracking-normal` if letter-spacing is also set) to that specific element. Check this proactively when building navs, buttons, or labels that mix Latin and non-Latin scripts.
