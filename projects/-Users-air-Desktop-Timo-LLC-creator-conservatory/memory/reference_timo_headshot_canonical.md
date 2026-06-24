---
name: Canonical Timo Headshot Location
description: Master location for Timo's official headshot (trombone on stool, studio portrait). Reference this file for ALL future decks, emails, and marketing materials that need his photo.
type: reference
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
**Canonical path:**
`/Users/air/Desktop/Timo LLC/creator-conservatory/assets/shared/timo-headshot-trombone-stool.jpg`

**File:** 1333x1999 JPEG, 133KB. Portrait orientation. Studio shot: Timo seated on weathered wooden stool, holding trombone, dark suit + purple shirt, neutral grey backdrop, soft lighting, looking down at instrument.

**Saved:** 2026-04-13 from Timo's direct upload. Extracted from conversation JSONL.

**Distributed copies (symlink-equivalent — update when the canonical changes):**
- `/Users/air/Desktop/Timo LLC/creator-conservatory/output/presentations/assets/timo-headshot-trombone-stool.jpg` (designer-vs-marketer deck)
- `/Users/air/Desktop/Timo LLC/creator-conservatory/output/presentations/images/views/timo-headshot-trombone-stool.jpg` (views-that-matter deck)

**Usage rules:**
- For ANY new Timo deck that needs his photo, copy from the canonical path to the deck's assets folder at a consistent filename: `timo-headshot-trombone-stool.jpg`.
- NEVER generate an AI portrait of Timo — per `feedback_placeholder_images.md`, AI portraits of him are uncanny and undermine credibility. Use this real photo instead.
- For "I'm Trombone Timo" intro slides: pair this headshot with credential bullets using the two-column layout (`two-col` class with `photo-placeholder portrait has-image`).
- For CTA slides: same headshot, same layout, different right-column content.
- Resolution 1333x1999 is adequate for most slide uses (typical display width 400-600px on portrait slot). For larger-than-1333px display, Timo should provide higher-res source.

**If a higher-resolution original becomes available:** Timo mentioned the source was 3648x5472. If he drops the high-res original at the canonical path (same filename), overwrite this file — all referencing decks will pick it up automatically on next copy.

**When updating the canonical file, re-run the distribution:**
```bash
CANONICAL="/Users/air/Desktop/Timo LLC/creator-conservatory/assets/shared/timo-headshot-trombone-stool.jpg"
cp "$CANONICAL" "/Users/air/Desktop/Timo LLC/creator-conservatory/output/presentations/assets/timo-headshot-trombone-stool.jpg"
cp "$CANONICAL" "/Users/air/Desktop/Timo LLC/creator-conservatory/output/presentations/images/views/timo-headshot-trombone-stool.jpg"
```
