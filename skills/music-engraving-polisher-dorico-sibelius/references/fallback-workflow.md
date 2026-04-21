# Fallback Workflow (no MusicXML available)

If the user has only a PDF or image, the polisher needs a MusicXML to re-engrave. Steps:

1. **Prefer direct export from Dorico/Sibelius** if the user has the source file. A clean export beats OMR every time.
2. **Fall back to Audiveris OMR** if only PDF/image is available. The skill auto-installs Audiveris on first run.
3. **Warn the user** that OMR-derived MusicXML typically has 1-10% transcription errors (wrong notes, wrong rhythms, dropped articulations). Review the polished output against the original PDF.

## When OMR will likely fail

- Handwritten scores
- Heavy chromatic music with dense accidentals
- Contemporary / extended notation (quarter-tones, graphic scores, prepared piano)
- Very low resolution scans (below 200 DPI)
- Photocopies with page skew or stains

## What to tell the user

"You gave me a PDF. For clean re-engraving I need MusicXML. If you have the source in Dorico or Sibelius, please export MusicXML from there (it takes 5 seconds and is lossless). If not, I can try Audiveris OMR but expect some transcription errors that you'll need to review against the original."