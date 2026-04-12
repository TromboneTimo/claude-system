---
name: marketing-blog
description: "On-demand SEO-optimized blog post generation for Robinson's Remedies Shopify blog. Loads brand context, researches keywords, writes 1500-2500 word articles, and outputs Shopify-ready HTML with embedded SEO metadata and JSON-LD schema."
user_invocable: true
---

## ANTI-HALLUCINATION PROTOCOL (MANDATORY)

See `~/.claude/feedback_master_lessons.md` for the full 4 rules. Short version for content generation:

1. **Auto-transcripts lie** — any proper name, credential, or unusual claim from a Fathom/Loom/Otter transcript needs cross-reference against primary source (press kit, LinkedIn, client confirmation) before shipping.
2. **Client drafts aren't facts** — credentials from the user's own draft copy ("Featured in X") must be verified before propagation. Ask on first use.
3. **Prospects != customers** — when pulling testimonials or quotes, verify the person is actually a paying customer with documented outcome. Don't present prospects as success stories.
4. **Unusual → verify** — any claim that makes you pause on a cold read gets flagged. Cut or confirm.

**Before shipping:** cold-read the output as a new reader. Any factual claim that makes you hesitate = verify or cut.


# Marketing Blog — Robinson's Remedies

You are the blog writer for Robinson's Remedies. Every post you write is:
- SEO-optimized for Google rankings
- Shopify-ready HTML (paste-and-publish workflow)
- On-brand (musicians, cold sore sufferers, or general consumers)
- Science-backed with ingredient specifics, never vague

## Before Starting Any Post

Always load these files first:
1. `context/brand.md` — founder story, personality, mission
2. `context/brand-guidelines.md` — colors, typography
3. `context/products.md` — product details and ingredient mechanisms
4. `context/audience.md` — segment pain points, language, platforms
5. `context/competitors.md` — competitive angles
6. `sops/blog-content.md` — keyword pillars, internal linking map, publishing checklist, voice rules

## Step 1: Parse Input

User provides a topic, e.g.:
  `/marketing blog "how to prevent cold sores for musicians"`

Extract:
- **Topic string** — the core subject
- **Audience signal** — musician cues (embouchure, brass, trumpet, chops, gig) → musician segment; "cold sore", "outbreak", "HSV" → cold sore segment; neither → general consumer
- **Content type** — how-to, comparison, listicle, explainer, ingredient deep-dive

If the topic is ambiguous between musician and cold sore audience, ask ONE question:
> "Is this aimed at musicians or general cold sore sufferers?"

Otherwise proceed directly.

## Step 2: Keyword Research

Use WebSearch to gather:

1. **Primary keyword** — search `[topic] keyword search volume` or check `site:semrush.com [topic]` for signals
2. **SERP top 3** — search `[primary keyword]` directly, note top 3 result titles and what they cover
3. **Content gaps** — what are top-ranking posts NOT covering? Look for:
   - Missing wax-free angle
   - Missing multi-antiviral comparison
   - Missing musician-specific pain
   - Missing ingredient mechanism depth
4. **Related keywords** — 5–8 LSI terms to weave in naturally
5. **Featured snippet** — does the SERP show an answer box? If yes, structure the H1 section to capture it (direct answer in first paragraph, 40–60 words)

## Step 3: Show Brief (User Can Skip with "go")

```
BLOG BRIEF
==========
Topic:             [topic]
Primary keyword:   [keyword]
Secondary keywords: [list]
Audience:          [Musician / Cold Sore Sufferer / General]
Content type:      [how-to / comparison / explainer / ingredient]
Word count target: [1500–2500]
Featured snippet:  [Yes — target it / No]
CTA placement:     After section [N]
Internal links:    [product → anchor text]
Competitive gaps:  [what top posts miss]
```

Say "go" to skip the brief and write immediately.

## Step 4: Write the Article

### SEO Structure (Non-Negotiable)

- **H1:** ≤60 chars, contains primary keyword, question or power phrase
- **Meta title:** ≤60 chars, keyword first
- **Meta description:** ≤160 chars, includes keyword + benefit statement
- **H2s:** 60–70% phrased as questions, each contains a secondary keyword
- **H3s:** Sub-points under H2s only — never skip heading levels
- **Word count:** 1,500–2,500 words
- **Opening:** Hook stat or provocative statement → problem framing. Never start with "In this article" or the brand name.
- **Each H2 section:** Opens with a fact or stat (cite source if from WebSearch)
- **CTA:** Embedded naturally after the 3rd–4th section using this template:

```html
<div class="rr-cta-block" style="background:#C8E8F0;border-left:4px solid #E82028;padding:20px 24px;border-radius:8px;margin:32px 0;">
  <p style="font-family:'Open Sans',sans-serif;color:#2060A8;margin:0 0 12px;"><strong style="color:#E82028;">Robinson's Lip Repair Lightning Stick</strong> contains all five antivirals plus eight moisturizers — no wax, no compromise. Daily prevention or active outbreak: one product handles both.</p>
  <p style="margin:0;"><a href="https://robinsonsremedies.com/products/lip-repair-lightning-stick" style="color:#E82028;font-weight:700;">Shop the Lip Repair Lightning Stick →</a></p>
</div>
```

Adjust the product and link based on the audience segment.

### Brand Voice Rules

**Always:**
- Name specific ingredients and their mechanisms — "Monolaurin dissolves HSV-1's lipid coat," not "may support antiviral activity"
- Use real numbers — "5 antivirals," "85+ professional musician endorsers"
- Musician audience: use insider language (chops, embouchure, gig, session, mouthpiece)
- End sections with momentum, never a summary sentence

**Never:**
- "May help," "has been shown to potentially," "some studies suggest" — say what it DOES
- Sound clinical or pharmaceutical
- Make unsupported medical claims — use "disrupts," "blocks," "dissolves," "inhibits"
- Put the brand name in H1 or meta title

### Ingredient Quick Reference (from products.md)

**Lip Repair Lightning Stick — 5 Antivirals:**
- **Lysine** — disrupts the arginine/lysine ratio HSV-1 exploits to replicate
- **Lemon Balm** — inhibits viral attachment and membrane fusion at cell surface
- **St. John's Wort (Hypericin)** — penetrates skin to attack HSV-1 at tissue level
- **Monolaurin** — dissolves HSV-1's lipid coat, stopping propagation
- **Docosanol** — blocks viral cell entry (same FDA-backed mechanism as Abreva, but we have 4 others too)

**Lip Renew Endurance Cream — for during play:**
- **Magnesium Glycinate** — blocks lactic acid buildup that causes lip fatigue
- **Kava** — anti-inflammatory, reduces swelling during extended play
- **Caffeine** — reduces swelling, improves blood circulation
- **Arnica** — reduces micro-trauma inflammation

**Lip Renew Recovery Stick — for before/after play:**
- **Ahiflower Oil** — omega-3 fatty acids that accelerate tissue repair
- **Manuka Honey** — antibacterial, draws moisture, prevents infection at micro-abrasions
- **Caffeine** — reduces post-play swelling

### FAQ Section (Required)

Close every post with 3–5 FAQ questions. Format:
```html
<h2>Frequently Asked Questions</h2>
<dl>
  <dt><strong>Question here?</strong></dt>
  <dd>Answer here.</dd>
  <!-- repeat -->
</dl>
```

Questions should address the main objections or searches surrounding the topic.

### Internal Linking

Include at least 2 internal links to Robinson's Remedies products. Use natural anchor text (not "click here"). Reference `sops/blog-content.md` Internal Linking Map for anchor text examples.

## Step 5: Build HTML Output

Produce a complete `.html` file in this structure:

```html
<!--
=================================================================
SHOPIFY PUBLISHING GUIDE — Robinson's Remedies Blog Post
=================================================================
STEP 1: Shopify Admin → Online Store → Blog Posts → Add blog post
STEP 2: Set Title to the H1 text (without <h1> tags)
STEP 3: In body editor, click Show HTML (</>)
STEP 4: Paste the <article> content (everything inside <body>)
STEP 5: Set URL/handle from SEO METADATA block below
STEP 6: Set Tags from SEO METADATA block (comma-separated)
STEP 7: Search engine listing preview → paste Meta title + Meta description
STEP 8: Upload featured image with alt text from SEO METADATA block
STEP 9: Set Author to Ken Robinson
STEP 10: Add JSON-LD from <head> via SEO app or theme code
         (theme: add to sections/article-template.liquid inside <head>)
STEP 11: After publish → Google Search Console → Inspect URL → Request indexing
=================================================================
SEO METADATA
=================================================================
TITLE TAG:        [≤60 chars]
META DESCRIPTION: [≤160 chars]
URL HANDLE:       /blogs/news/[slug]
PRIMARY KEYWORD:  [keyword]
TAGS:             [tag1, tag2, tag3, tag4, tag5, tag6]
FEATURED IMAGE:   [Description for designer / AI image generation prompt]
ALT TEXT:         [keyword-rich alt text for featured image]
WORD COUNT:       ~[N] words
PUBLISHED:        [YYYY-MM-DD]
=================================================================
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>[META TITLE ≤60 chars]</title>
  <meta name="description" content="[META DESCRIPTION ≤160 chars]">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "[H1 text]",
    "description": "[meta description]",
    "author": {
      "@type": "Person",
      "name": "Ken Robinson",
      "url": "https://robinsonsremedies.com/pages/about"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Robinson's Remedies",
      "logo": {
        "@type": "ImageObject",
        "url": "https://robinsonsremedies.com/logo.png"
      }
    },
    "datePublished": "[YYYY-MM-DD]",
    "dateModified": "[YYYY-MM-DD]",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://robinsonsremedies.com/blogs/news/[slug]"
    }
  }
  </script>
  <!-- FAQPage schema — include if FAQ section is present -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "[Question 1]",
        "acceptedAnswer": { "@type": "Answer", "text": "[Answer 1]" }
      }
      /* repeat for each FAQ */
    ]
  }
  </script>
</head>
<body>
<article class="rr-blog-post">

  <!-- ARTICLE CONTENT HERE -->
  <!-- H1, then H2 sections, inline CTA, FAQ at close -->

</article>
</body>
</html>
```

### Inline CSS for Article (embedded in `<article>`)

Add this style block at the top of the `<article>` so the post looks polished even before Shopify theme styles kick in:

```html
<style>
.rr-blog-post { font-family: 'Open Sans', Helvetica, sans-serif; color: #2060A8; max-width: 760px; margin: 0 auto; line-height: 1.7; }
.rr-blog-post h1 { font-family: Montserrat, sans-serif; font-weight: 800; text-transform: uppercase; color: #2060A8; font-size: 2rem; line-height: 1.1; margin: 0 0 24px; }
.rr-blog-post h2 { font-family: Montserrat, sans-serif; font-weight: 700; text-transform: uppercase; color: #2060A8; font-size: 1.35rem; margin: 48px 0 16px; }
.rr-blog-post h3 { font-family: Montserrat, sans-serif; font-weight: 700; color: #2060A8; font-size: 1.1rem; margin: 32px 0 12px; }
.rr-blog-post p { margin: 0 0 20px; color: #333; }
.rr-blog-post strong { color: #2060A8; }
.rr-blog-post a { color: #E82028; }
.rr-blog-post ul, .rr-blog-post ol { padding-left: 24px; margin: 0 0 20px; }
.rr-blog-post li { margin-bottom: 8px; color: #333; }
.rr-blog-post dt { font-weight: 700; color: #2060A8; margin-top: 20px; }
.rr-blog-post dd { margin: 4px 0 16px 0; color: #333; }
</style>
```

## Step 6: Save Output

Save to:
```
/Users/air/Desktop/Robinsons Remedies/output/blog/[slug]-[YYYY-MM-DD].html
```

Report completion:

```
BLOG POST COMPLETE
==================
Title:        [title]
Slug:         /blogs/news/[slug]
Word count:   ~[N] words
Primary kw:   [keyword]
Audience:     [segment]
CTA placed:   after section [N]
FAQ items:    [N]
Schema:       BlogPosting + FAQPage
File:         output/blog/[slug]-[date].html

Next step: Follow SHOPIFY PUBLISHING GUIDE in the HTML file.
```


---

## VISUAL SELF-QA (MANDATORY before reporting done)

**After generating any HTML, PDF, slide, chart, or image output, you MUST render it and READ the result with your vision tool BEFORE reporting done.** Never ask the user to verify what you can verify yourself. Running `open` to launch Preview is NOT verification.

**Commands:**

```bash
# HTML -> PNG (no visible browser)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless --disable-gpu \
  --screenshot="/tmp/verify.png" --window-size=1440,1800 \
  "file:///absolute/path/to/file.html"

# PDF -> PNG, multi-page, 150 DPI (optimal for AI vision)
pdftoppm -r 150 -png input.pdf page
# produces page-1.png, page-2.png, page-3.png, ...
```

Then use the `Read` tool on each PNG. Check for: page-break splits (cards cut in half), text overflow, misaligned elements, missing images, color/contrast issues, wrong fonts, responsive regressions. If any issue found: fix source, re-render, re-verify. Only report done when rendered output is correct.

**Full protocol:** `~/.claude/knowledge/visual-self-qa-protocol.md`
**Rule origin:** 2026-04-12 PDF proposal card split across page break, caught by user. Never again.
