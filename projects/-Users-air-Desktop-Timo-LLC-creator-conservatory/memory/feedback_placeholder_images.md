---
name: Respect Placeholder Image Requests
description: When user says "use placeholder images," use literal styled placeholders, not AI-generated ones
type: feedback
originSessionId: 9e6657f9-1de0-4f36-aded-d6e7a71c7b93
---
When Timo says "use placeholder images" or "placeholders where you wanted to use my photos," he means:
- Styled CSS placeholders (gradient boxes, "YOUR PHOTO HERE" labels, dashed borders)
- NOT Gemini/Nanobanana generated images
- NOT Unsplash stock photos
- Literal placeholder rectangles that show the shape and position his real photos will fill later

## Why
- Specific people (like Timo himself) look wrong when AI-generated. AI-generated portraits don't look like him. Using a Gemini-generated portrait as if it were his headshot is worse than an empty placeholder.
- Placeholder rectangles make it obvious where real content goes, which prompts Timo to swap in real assets before shipping.
- AI generation costs money ($0.04/image via Gemini). Running it when a plain placeholder was requested wastes money.
- AI-generated images of people can create "uncanny valley" moments that undermine the presentation.

## Correct decision tree for image slots in a presentation

1. Did Timo say "use placeholder images"?
   - YES: Use styled CSS placeholder boxes. No AI generation. No stock photos.
   - NO: Continue to question 2.

2. Does the slot need a photo of Timo specifically?
   - YES: Placeholder only, even if no placeholder instruction was given. Ask Timo to provide his real photo.
   - NO: Continue to question 3.

3. Is it generic environmental or conceptual imagery (concert stage, desk, abstract texture)?
   - YES: Gemini generation is appropriate IF budget permits.
   - NO: Use Unsplash/Pexels stock photos with verified URLs.

## Correct placeholder styling
```css
.photo-placeholder {
    background: var(--bg-card);
    border: 2px dashed var(--text-muted);
    display: flex;
    align-items: center;
    justify-content: center;
    aspect-ratio: 4 / 5;
    color: var(--text-muted);
    font-family: var(--font-mono);
    text-align: center;
    padding: 1rem;
}
```
With label text like "YOUR PHOTO HERE" or "[Placeholder - Tim's performance shot]"

## Incorrect (what I did wrong before)
Generated a Gemini portrait of a "male musician in his 30s holding a trombone" and used it as if it were Timo's actual photo on a credibility slide. This was wrong because:
1. He specifically said placeholder
2. It wasn't actually him, so it undermined the credibility pitch
3. It would be misleading in a public-facing ad
