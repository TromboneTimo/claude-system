---
name: Toggle both languages and grep for hardcoded strings after touching any lang-aware component
description: After editing any component that consumes a `lang` prop or `useLanguage()` hook, grep the full component for hardcoded English strings AND toggle the language in the browser before declaring done.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Any component that uses `lang === "ja"` branches is a bilingual contract. After editing it (or an adjacent component), verify BOTH languages render correctly.

**Why:** On Samurai Brass DiscographyCarousel (2026-04-22), I edited the image rendering but never toggled the JA button. The component had `SIDE A` / `SIDE B` hardcoded and track titles showed `{t.title}` (always English) with JP in parens regardless of lang. User discovered it after I shipped. Would have been caught in 30 seconds by clicking 日本語.

**How to apply:**
- After editing a component used in a `useLanguage()` context, run: `grep -nE '"(SIDE|Next|Prev|Read|More|Buy|Shop|Click|Album|Artist|Member|Official)" |>[A-Z][a-z]+ [A-Z]' <component_file>` to surface hardcoded English strings.
- Scan the component for any string literal that is NOT already inside a `lang === "ja" ? ... : ...` ternary or pulled from a `titleJa`/`titleEn` pair.
- In the browser, click the JA language toggle and scroll through the affected section before reporting the task complete.
- When consuming a data shape like `Track = { title, jp? }` where `title` is English and `jp` is an annotation (not a full translation), propose changing the component to swap primary/secondary based on lang, OR confirm with the user that the annotated format is intentional in JA mode.
