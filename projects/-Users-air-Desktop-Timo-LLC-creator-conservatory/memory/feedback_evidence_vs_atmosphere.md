---
name: Sales Deck Images Must Be Evidence Not Atmosphere
description: CRITICAL. In sales/persuasion decks, every image must LITERALLY SHOW the claim being made. Atmospheric mood shots fail. Background + foreground + type is the three-layer system.
type: feedback
originSessionId: f48c716d-c5d0-4b99-bba5-c74c4f22aed9
---
In sales/persuasion decks (not editorial pieces), every image must LITERALLY SHOW the specific claim the slide is making. Atmospheric mood imagery fails because it only evokes — it doesn't prove.

**Why:** 2026-04-13 leaking-business deck. I generated five "atmospheric" images (burning money, diverging lines, search bar, chain link, theater stage) and thought I was done. Timo: "I want images with the fucking text, i like the background but I wanted fucking images in front of the brackground image as well you dumb idiot how the fuck did oyu not realize that?" The problem: I was building editorial aesthetic (Apple keynote / New Yorker feel) when the genre needed forensic evidence. A burning dollar bill sets a mood; a laptop screen showing "$47.82 CPC / ROAS -18%" argues the case. Different jobs.

## THE DO / DON'T RULES

### DO
1. **Use the 3-layer system for sales decks:** `hero-image` (atmospheric background, 35% opacity, left gradient overlay) + `hero-foreground` (the literal subject / evidence image, right-side, square, drop shadow) + text (left half). Each layer has a distinct job: mood, proof, thesis.
2. **Run the pause test** on every image: if you paused the slide with audio muted, would a cold viewer know what's being argued? If no, the image is atmosphere and fails.
3. **Generate literal subjects for foregrounds:** a laptop showing the dashboard being discussed, a phone showing the search result, a chained phone for dependency, an actual testimonial card for social proof. Subject-forward, not mood-forward.
4. **For slide 1 / hero slides where the atmosphere IS the evidence** (e.g., burning money literally shows "you're burning money"), either (a) use it as both bg AND generate a stronger hero version as fg, OR (b) use it as fg with a different atmospheric bg. NOT atmospheric only.
5. **Write behavioral threats, not category framings.** "Your competitor just fired three people" beats "you're a one-person team vs a four-person agency." Threats make the stomach drop; framings just name a situation.
6. **Shrink headline clamp on `.has-foreground` slides** to clamp(1.75rem, 4.6vw, 4rem). Full-size headlines overflow the 56vw text zone when a 36vw foreground occupies the right side.
7. **Use HTML-styled cards instead of AI-generated text panels** for testimonials, stats, comparison blocks. AI image gen produces garbled text at small sizes. HTML is pixel-perfect, editable, and authentic.
8. **Close old Safari tabs before opening fresh** when iterating on a deck. Stale tabs confuse the user about which version they're looking at. Use AppleScript to close tabs matching the URL fragment, then open fresh.

### DON'T
1. **Don't default to editorial aesthetic.** Apple keynote sparse-type atmospheric-image style is for brand decks, not sales decks. Sales decks need forensic-evidence energy.
2. **Don't generate one image and assume you're done.** First pass is almost always atmosphere. Second pass is evidence. Plan for both.
3. **Don't stack a foreground on a slide where the background IS the literal subject.** If the slide claim is "you're burning money" and the background is literally money on fire, a second "evidence" layer is redundant. Either the bg IS the fg, or the bg is atmospheric context.
4. **Don't let AI generate readable text inside a foreground image** (dashboard numbers, testimonial content, chart labels). It garbles. Generate the visual container (screens, cards, devices) and either (a) let it be mostly illegible as "scrolling feed" visual noise, or (b) overlay real text as HTML on top.
5. **Don't name specific clients in public content.** The `client_claims` feedback rule still applies. Describe situationally ("one of my clients") and redact specific numbers that would identify them.
6. **Don't generate AI portraits of Timo.** Ever. Uncanny, undermines credibility. Use real photos OR atmospheric objects associated with him (trombone, stage, instruments).
7. **Don't spawn parallel Chrome headless instances** for multi-slide screenshot QA. Sequential only or batches of 3-4 max.
8. **Don't fabricate business numbers.** If the testimonial says "40x subscriber growth" verify it matches the source (175 → 7,150 is actually 40.85x, round to 40x in copy). If you don't have the source, don't claim the stat.
9. **Don't wait for Timo to write the punchline.** Read his content framework, write the behavioral diagnosis in his voice, and let him edit. Don't name a category ("dependency problem") and stop.

## THREE-LAYER CSS SCAFFOLD (copy-paste into any sales deck)

```css
.hero-image {
    position: absolute; inset: 0; z-index: 0;
    pointer-events: none; overflow: hidden;
}
.hero-image img {
    width: 100%; height: 100%; object-fit: cover; opacity: 0.35;
}
.hero-image::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(90deg, rgba(0,0,0,0.97) 0%, rgba(0,0,0,0.85) 40%, rgba(0,0,0,0.55) 75%, rgba(0,0,0,0.3) 100%);
}

.hero-foreground {
    position: absolute;
    right: clamp(2rem, 5vw, 5rem); top: 50%;
    transform: translateY(-50%);
    width: clamp(280px, 36vw, 520px);
    aspect-ratio: 1 / 1;
    z-index: 1; pointer-events: none;
    filter: drop-shadow(0 20px 60px rgba(0,0,0,0.8));
    border-radius: 8px; overflow: hidden;
}

.slide.has-foreground .slide-inner {
    max-width: min(56vw, 820px);
    margin-left: 0; margin-right: auto;
}
.slide.has-foreground .headline { font-size: clamp(1.75rem, 4.6vw, 4rem); }
.slide.has-foreground .subhead { font-size: clamp(.9rem, 1.35vw, 1.2rem); max-width: 48ch; }
```

## HASH NAVIGATION SCAFFOLD (enables `file://deck.html#7` jump + screenshot QA)

```js
function fromHash() {
    const n = parseInt((location.hash || '').replace('#',''), 10);
    if (!isNaN(n) && n >= 1 && n <= slides.length) show(n - 1);
}
window.addEventListener('hashchange', fromHash);
fromHash();
```

## NANO BANANA PROMPT TEMPLATE FOR FOREGROUND SUBJECTS

```
[Literal subject, e.g., "A sleek laptop showing a Facebook Ads Manager dashboard"],
[Specific visible content, e.g., "red CPC graph spiking upward, '$47.82 CPC' in red, 'ROAS -18%' metric"],
[Composition, e.g., "centered in frame, 45-degree angle"],
[Lighting, e.g., "cinematic studio lighting, shallow depth of field, dramatic rim light"],
[Background, e.g., "pure black void"],
[Style, e.g., "35mm film aesthetic, square composition"],
[Negative, e.g., "no text beyond what is naturally visible, no watermark, no real brand logos"]
```

Use square (1024x1024) output from Nano Banana. CSS handles fit via aspect-ratio 1/1 and object-fit cover.
