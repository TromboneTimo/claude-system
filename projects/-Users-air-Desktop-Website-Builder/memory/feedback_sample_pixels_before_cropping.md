---
name: Sample edge pixels before cropping any image
description: Before writing any image trim/crop script, sample 10-20 edge pixels of a representative source file and observe the actual gradient. Never guess thresholds.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Before cropping white/grey borders off any image, SAMPLE FIRST. Read the actual RGB values at rows 0..20 and cols 0..20 of a representative source file. Observe the full gradient from background to content. THEN pick a threshold or fixed inward inset.

**Why:** On the Otto Cristofoli Samurai Brass album covers (2026-04-22), I guessed threshold=240 on the first pass. The actual edges contained pixels up to (248,245,236) (pure white missed) AND a wide grey gradient from 122 to 205 (CD jewel case highlight, entirely below threshold). Three iterations before edges were clean. One `python3` sampling snippet at the start would have caught both in one pass.

**How to apply:**
- Any time the task involves cropping/trimming an image, first run a small Pillow snippet that prints `im.getpixel((x,y))` for x in range(0,15) and x in range(w-15,w), same for y. Do the same for the TOP and BOTTOM edge.
- If the edge shows a gradient (not a hard transition), do not use a single threshold. Either: (a) use a looser neutral-pixel rule AND apply an additional fixed inward inset of 8-15px, or (b) hardcode the crop box from the sampled data.
- For batches of similarly-laid-out images (e.g., a set of CD covers), sample 2-3 files to confirm layout consistency before batch-processing.
