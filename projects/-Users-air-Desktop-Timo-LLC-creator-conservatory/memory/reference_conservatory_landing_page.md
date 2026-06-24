---
name: Creator Conservatory Landing Page vs FB Ads Funnel (DO NOT CONFUSE)
description: Two SEPARATE things that share the same dark "playstation" design system. (1) Creator Conservatory page = output/landing-playstation/index.html. (2) FB ads funnel = output/fb-funnel/ (email capture to VSL to booked). They are NOT the same. Do not bolt funnel parts onto the Conservatory page.
type: reference
originSessionId: bb11f5ff-044e-47bd-9a9d-ecc9b0a26bf5
---
**There are TWO distinct web properties in this workspace. They use the same design system (funnel.css / the dark "playstation" tokens) but are different funnels with different jobs. Confusing them caused a real incident on 2026-06-06 (see below).**

## 1. Creator Conservatory page (the standalone landing)
**Active file:** `output/landing-playstation/index.html`
- Title: "Tim Maines. Scale Your Music Business With Content + Systems."
- Flow: hero, then VSL slot, then 1-min quiz, then results, then `#apply` section.
- CTA: **"Book A Chat With Tim"** (the apply/quiz Typeform is embedded in-page; it does NOT redirect to /booked).
- Clean baseline reference: `references/landing-creator-conservatory-playstation-v2.html`.
- When Timo says "conservatory landing page" / "landing page", open this file.

## 2. FB ads funnel (paid Facebook-ads flow, built 2026-06-05)
**Folder:** `output/fb-funnel/` (own Vercel deploy, own `funnel.css`, Meta Pixel)
- `index.html` = **email capture**, POSTs to `/api/subscribe` (Substack + Sheet), then redirects to `vsl.html`
- `vsl.html` = **VSL video + quiz** (Typeform `wpa0SUAs`), on submit redirects to `booked.html`
- `booked.html` = **post-booking** "watch this before our call" (confirmation + steps + warning + real client results + testimonial modal wall)
- When Timo says "the funnel" / "email capture to VSL to book call" / "the FB ads funnel", this folder is it. THIS is the funnel he cares about.

## DO NOT
- Do NOT treat `landing-playstation/index.html` AS the funnel. It is the Conservatory page.
- Do NOT add a `/booked` redirect, the FB VSL video, or the email-capture flow onto the Conservatory page.
- Do NOT build post-booking pages anywhere except inside `output/fb-funnel/` (as `booked.html`).
- The post-booking page belongs to the FB funnel, not the Conservatory page.

## 2026-06-06 incident (why this file exists in this form)
The OLD version of this note said only "Conservatory page = landing-playstation/index.html" with no mention of the FB funnel. Trusting that note, I (a) bolted funnel content onto the Conservatory page (VSL video, "I'm Ready To Scale" CTA, a `window.location.href='/booked'` redirect) and (b) built the post-booking page twice in the wrong places (`landing-playstation/booked/`, `output/post-booking/`) instead of recognizing `fb-funnel/booked.html` already existed. Timo: "you're confusing my Creator Conservatory page with the funnel... it's a disaster." Fix: restored the Conservatory page from the v2 reference, deleted the two stray booked pages (backup in `output/_cleanup-backup-2026-06-05/`), kept `fb-funnel/` as the source of truth.
**Lesson:** verify a file's actual role from disk (title, CTA, links, mtime) before acting. A stale reference note is a hypothesis, not ground truth. See [[feedback_audit_state_before_prescribing]].

**How to open:** `open -a Safari "output/landing-playstation/index.html"` (Conservatory) or `open -a Safari "output/fb-funnel/index.html"` (funnel).

## 2026-06-08 terminology clash (ASK, do not assume which page)
Timo calls a page his **"email capture page"** and it did NOT match this note's definition. This note says email-capture = `fb-funnel/index.html`. But Timo's edit requests (screenshots of **Script & Content Strategy** + **Meet Tim** sections, "make these bullets," "move Meet Tim to the bottom") referenced sections that exist ONLY on `landing-playstation` and are completely absent from `fb-funnel/index.html` (378 lines: just the "10 minutes you'll learn" hero, 01-04 steps, email form). I edited the landing-playstation restore, opened fb-funnel when he said "open my email capture page," and mislabeled his page the "landing page" while he calls it the "email capture page." He was furious: "Why are you always getting this fucked up... you need to ASK me if you're confused."
**Hard rules going forward:**
1. "Email capture page" is AMBIGUOUS in Timo's mouth. It can mean `fb-funnel/index.html` (this note's def) OR the landing-playstation page (it has a 1-min quiz opt-in). NEVER assume which.
2. Before editing OR opening any web property, CONFIRM the exact file in one line: "the page with X and Y sections, right?" Especially when the user names a page by function ("email capture", "the website").
3. TRIPWIRE: if sections the user references (from a screenshot or by name) do NOT exist on the file you think they mean, STOP. That mismatch is the signal to ASK, not to guess. Grep the candidate file for the named sections first.
4. There are THREE live copies of the landing page in play this session (`landing-playstation/index.html` thin/deployed, `index-NEWER-restored.html` the good one + edits, `_cleanup-backup-2026-06-05/`). Consolidate to ONE canonical file ASAP so "where is my page" has a single answer. See [[feedback_search_content_before_concluding_missing]].
