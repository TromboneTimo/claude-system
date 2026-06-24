---
name: WeasyPrint technical reference
description: Page density math, height formulas, template system, build commands, and critical technical notes for Digital Product Creator
type: reference
---

## Page Density (THE MOST CRITICAL RULE)

`page-break-after: always` means every `.page` fills a full A4. Short content = huge white gap.

**Usable content area: ~780px** (A4 297mm - 65mm margins - 60px header)

| Page Type | Minimum to fill | Height per item |
|-----------|----------------|-----------------|
| concept_page | 9-10 paragraphs | ~82px each |
| priority_list | 6 items, 2-3 line details | ~100-120px each |
| profiles | 3+ profiles, 4-6 line descriptions | ~100px each |
| action_table | 7+ rows | fills well |
| content_library | 7+ categories | ~60-80px each |

**Before building:** Sum content heights per page. Below 650px = add content. Above 820px = split.

**No CSS fix exists.** WeasyPrint has no auto-fill. Only content density in JSON works.

## Build
```bash
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build.py <product> --open
cp output/<product>.pdf ~/Downloads/<product>.pdf
```

## Products Registered

| Key | Template | CSS | Colors |
|-----|----------|-----|--------|
| voice | template.html | styles.css | Navy #1a1a2e + Coral #e8616a |
| longform | template_longform.html | styles_longform.css | Emerald #0f3d2e + Gold #c9953c |
| shortform | template_shortform.html | styles_shortform.css | Slate #1e2a3a + Electric #3b82f6 |
| harrisson_* (5 products) | template_harrisson.html | styles_harrisson.css | Navy #0d1b2a + Brass #c8943c |
| ipo_proposal* | template_ipo.html | styles_ipo.css | Wine #1e0a12 + Gold #c4952a |
| paul_rivera_reference | template_paul_rivera.html | styles_paul_rivera.css | Burgundy #2d0a1e + Silver #a0a8b0 |

New products must use distinct palette. Check existing ones first.

## Template System
Copy template_harrisson.html, change CSS link. Copy styles_harrisson.css, change :root variables only.

## Technical Notes
- WeasyPrint macOS: always prefix DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
- Content overflow = OVERLAP, not page break. Split in JSON.
- `items` is reserved in Jinja2. Use checks, entries, profiles, categories.
- Inter font for all. InterDisplay at 54pt+ only.
- No CSS Grid, no position:sticky. Use flexbox + block.
- page-break-inside: avoid on .priority-item and .cl-category
