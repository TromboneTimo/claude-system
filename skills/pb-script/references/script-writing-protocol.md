# Phase 2 Script-Writing Protocol

Lessons learned from the 2026-04-25 iteration with Timo on the "Stop Buying Mouthpieces" and "$0 vs $7,200 Trumpet" scripts. When Timo picks an idea from the Phase 1 menu and asks for a script, follow these rules.

## RULE ZERO. Scan input for verbatim content BEFORE drafting

The single highest-cost rule to violate. Before writing any beat, re-read Timo's input twice. Find every line, hook, transition, CTA, visual cue, reference link, or specific phrasing he wrote. PRESERVE it character-for-character in the corresponding beat. Do not paraphrase. Do not consolidate. Do not "tighten" his lines. Even if it reads rough. Even if you think you can improve it. He has context you don't, and he can edit later. This rule fails first and costs the most iterations every time.

## Workflow rule. Present in chat BEFORE writing files

When Timo gives feedback that affects content, present the proposed change in chat first. Get sign-off. Then update the file. The "draft a PDF, get yelled at, fix it, re-render" loop is wasteful. Show in chat -> confirm -> ship.

## Adapt structure to thesis

The 7-beat mouthpieces template is the default, NOT mandatory. The mouthpieces video has an "Apparatus Reveal" beat because that's its thesis pivot. Other scripts may have a different structural pivot (e.g., the trumpet-comparison video uses "Demos -> Blind Test -> Reveal -> Funnel" without an apparatus beat). Match the structure to the content's actual logic, not the template.

## Funnel framing default = additive, not contrastive

When funneling between videos in a content chain, default to additive framing ("X matters AND Y matters"), not contrastive ("X doesn't matter, Y does"). Additive is stronger because it doesn't undersell either video and the funnel logic gets cleaner.

## References go at the top, not buried in beats

YouTube references / external links Harrison needs to watch before filming belong in a dedicated "Watch Before Filming" block at the top of the document, NOT inside a beat's action text. Use a dark card with gold heading, blue links, gray descriptions.

## The 7-beat interleaved structure (default for mistake-driven videos)

Use this default unless the topic genuinely needs a different shape:

1. **Cold Open + Hook** (red/coral). Visual gag + locked hook line + comeback/age callout + demo promise.
2. **The Demo** (blue). Part 1: same tune on N mouthpieces. Part 2: same tune with shitty setup.
3. **Apparatus Reveal** (green). Mouthpiece reframe -> BEAT -> apparatus reveal line -> definition.
4. **Mistake 1** (mustard). The Trap -> The Mistake -> The Test.
5. **Mistake 2** (plum). The Trap -> The Mistake -> The Test.
6. **Mistake 3** (magenta). The Trap -> The Mistake -> The Test.
7. **Funnel** (teal). Callback to tests + NEW provocation question + Hint pattern + embouchure video CTA.

The interleaving is non-negotiable. Trap topics, mistakes, and tests must live INSIDE the same beat, not stacked as separate sections.

## What NOT to do (failure modes Timo flagged repeatedly)

1. **Do not write paragraphs of explanation.** Bullet director's notes only. He repeatedly said "too much text", "be efficient", "lower the amount by half".
2. **Do not summarize his locked lines.** When he gives exact phrasing, preserve it character-for-character. He had to repaste his draft when I edited it.
3. **Do not drop visual specs.** When he writes "Harrison sitting in front of all his mouthpieces", that detail is mandatory. Don't compress it away.
4. **Do not stack mistakes/tests separately.** Weave them inside the trap-topic beats. He had to call this out twice.
5. **Do not silently downgrade folders/databases.** If a folder he names is sparse, ask before assuming it's unimportant.
6. **Do not fabricate social proof or stats.** Knowledge gaps that open curiosity are good. Made-up "every single one of them stopped buying" claims are not.
7. **Do not put meta-instructions inside the deliverable.** "Send to Timo for review" is a note for me, not for the page Harrison reads while filming.
8. **Do not write in third-person clinical register.** Harrison talks second-person, conversational ("Now,", "right?"), with metaphors and rhetorical questions. Match that.
9. **Do not treat every sentence as its own shot.** Beats can contain many lines that flow together. He had to merge my over-fragmented shots multiple times.
10. **Do not regress to old patterns after fixes.** Once he corrects something, it stays corrected. Don't slip back.
11. **Do not manhandle Harrison's improv.** Give topics + locked lines, not verbatim every-sentence scripts.
12. **Do not let paragraphs split across PDF pages.** CSS must use `break-inside: avoid` on script paragraphs and `break-after: avoid` on labels/headers.
13. **Do not design for visual flair over readability.** No yellow speech bubbles, no italic body, no chat-bubble metaphor, no dashed dividers. Script readability is sacred.
14. **Do not invent named mistakes from thin air.** Pull them from the corpus or extend a pattern Timo already accepted.

## What TO do (success patterns Timo accepted)

1. **Locked lines + topic riff.** Use italics or quotes for what must be said verbatim. Use prose director's notes for what Harrison rides on.
2. **Each beat = one cycle.** Trap -> Mistake -> Test together. Color-coded. Easy for Harrison to find his place.
3. **Cold open = visual gag.** Get curiosity in 0-5 seconds before any dialogue.
4. **Voice fingerprint:** "Now,", "right?", second person, repeats key terms 3-5x, names the wrong way before the right way, conversational fillers, builds metaphors mid-sentence (like "Think of the middle as a sail flapping in the breeze").
5. **Funnel pattern:** callback to what just happened ("If you struggled with...") + NEW knowledge gap (WHERE on your face / what 99% of teachers get wrong) + "Hint: it's not what you think" + point to embouchure video card.
6. **Provoke at the funnel.** Don't just close. Open one more question that the next video answers.
7. **Save deliverables to BOTH** project output folder AND `~/Downloads/` (per project memory rule).
8. **PDF aesthetic:** warm off-white bg, near-black 22px sans-serif Inter, vibrant 7-color accent palette (coral, blue, green, mustard, plum, magenta, teal), no boxes around script, generous whitespace, single column max-width ~760px.

## Voice cross-reference

When writing locked lines, mimic Harrison's converter video patterns. See `/Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md` for the source. Voice fingerprint also at `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_harrison_voice.md`.

## Concrete example

The fully iterated example is at `references/example-mouthpieces-script.md` and the rendered HTML/PDF live in `~/Downloads/stop-buying-mouthpieces-script.{html,pdf}`. Model future scripts on that structure unless explicitly directed otherwise.
