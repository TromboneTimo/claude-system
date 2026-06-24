---
name: Gemini Image Generation API (Direct Curl)
description: Working curl invocation for Gemini image generation. Model name and request shape that work as of 2026-04-13.
type: reference
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
Generate an image with Gemini via direct curl (no MCP server needed):

```bash
curl -sS -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key=${GOOGLE_AI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "<your prompt here>"}]}],
    "generationConfig": {"responseModalities": ["IMAGE"]}
  }' > /tmp/gemini-response.json
```

Then extract the base64 image data:

```python
import json, base64
d = json.load(open('/tmp/gemini-response.json'))
parts = d['candidates'][0]['content']['parts']
for p in parts:
    if 'inlineData' in p:
        img_b64 = p['inlineData']['data']
        ext = 'png' if 'png' in p['inlineData'].get('mimeType','') else 'jpg'
        open(f'/path/to/output.{ext}','wb').write(base64.b64decode(img_b64))
```

**Key points:**
- Model name is `gemini-2.5-flash-image` — NOT `gemini-2.5-flash-image-preview` (which 404s) and NOT `gemini-2.0-flash-exp` (deprecated).
- Available image-capable models as of 2026-04-13: `gemini-2.5-flash-image`, `gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview`, plus Imagen models (which use `predict` not `generateContent`).
- API key env var on this machine: `GOOGLE_AI_API_KEY`.
- Image returns at 1024x1024 by default. ~1MB PNG output is normal.
- Specify aspect ratio in the prompt itself (e.g., "Aspect ratio 3:4 portrait") — there's no separate aspect ratio param for `generateContent`.
- For headless Chrome rendering of the resulting deck, copy the asset to `/tmp/assets/` since temp HTML files resolve relative paths from /tmp/, not the original directory.

**When to use Gemini vs other approaches:**
- Public figures (Obama, etc.) → Gemini works, request "stylized editorial illustration" not "photorealistic" to avoid uncanny photo issues.
- Timo's portrait → DO NOT generate (memory: AI portraits of Timo are uncanny, undermine credibility). Use placeholder.
- Brand logos → Try fetch first (Wikipedia/Clearbit). If DNS dead or returns small files (<3KB = error page), draw inline as SVG wordmark.
- Mockups (browser screenshots, phone UIs, data visualizations) → Build inline with HTML/CSS, more reliable than generation.
