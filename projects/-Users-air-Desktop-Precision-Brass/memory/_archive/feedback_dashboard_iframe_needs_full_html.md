---
name: Dashboard iframe needs FULL HTML doc, not body innerHTML
description: When uploading a script/email/etc to the dashboard with type=html_full, the content field MUST contain the complete HTML document (head + style + body), not just the body innerHTML. The dashboard iframe srcdoc needs the styles to render the colored layout.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
The Precision Brass dashboard renders rich content (`type: 'html_full'`) inside an iframe via `srcdoc=` (see `dashboard/scripts.html` line ~875). The iframe is a sandboxed standalone document. It does NOT inherit the dashboard's CSS. So if you upload only the body innerHTML (which has class names but no `<style>` block), Harrison sees a wall of unstyled plain text instead of the color-coded beat layout.

**Why this happened:** the prior version of pb-script-write said "extract body innerHTML for upload." That was wrong. Caught on 2026-05-06 when Timo opened the famous-method-killing-embouchure script in the dashboard and saw plain text instead of the PDF's colored layout.

**How to apply:** when building the body payload for any dashboard upload (scripts, emails, future content types) that uses `type: 'html_full'`:

```python
with open(html_path) as f:
    full_html = f.read()  # READ THE WHOLE FILE
body = [{'type': 'html_full', 'content': full_html, 'pdf_url': pdf_url}]
```

Do NOT split on `<body>`. Do NOT extract innerHTML. Upload the entire file including `<!DOCTYPE>`, `<html>`, `<head><style>...</style></head>`, and `<body>`.

The iframe's `sandbox="allow-same-origin"` lets the embedded `<style>` apply but blocks scripts. So fonts loaded via `<link href="https://fonts.googleapis.com/...">` may or may not load depending on browser. Inline-define system font fallbacks just in case.

This rule applies to:
- pb-script-write (scripts table)
- pb-email-write (email_proposals table) when emails ever use html_full
- Any future Precision Brass dashboard upload using the html_full pattern
