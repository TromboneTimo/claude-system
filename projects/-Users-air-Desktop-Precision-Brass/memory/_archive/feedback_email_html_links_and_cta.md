---
name: email-html-links-and-cta
description: Standing rules for every email Precision Brass sends. Bodies must be HTML, CTAs must be hyperlinked text not raw URLs, master class is the only CTA destination, testimonial links come from the testimonial's source_url front-matter, P.S. lives inside body. Locked 2026-05-10 with Timo.
type: feedback
originSessionId: aeff5f91-8235-469c-a243-71648976c5f2
---
# Precision Brass email rules. Locked 2026-05-10

These rules apply to every email written, pushed, sent, or stored. They are encoded in `dashboard/lib/email-lint.js` and enforced at three points: pb-email-write at draft time, pb-email-push at insert time, and the broadcast UI at send time. When you change a rule, also update the lint module.

**Why:** session 2026-05-10. Timo flagged that approved emails were storing the body as plain text with a "MASTERCLASS_URL" placeholder and a separate `ps_text` field that never got sent. CTAs were raw URLs ("Click here: https://...") instead of clickable anchor text. Testimonial links pointed to the wrong place (the webinar reg, not the YouTube video). And `ps_text` was a dead field stored separately and never appended to body before send. Three approved bodies were patched in-place and the rules below were locked in.

## 1. Bodies are HTML, not plain text

Store and send bodies as HTML. Use `<p>` for paragraphs, `<ul><li>` for bullet lists, `<br>` for hard line breaks (signature only), `<a href="...">` for links. Do NOT rely on `\n\n` for paragraph breaks or `white-space: pre-wrap` rendering. AC's HTML compose collapses raw newlines.

**How to apply:** when pb-email-write generates a draft body, output HTML directly. When pb-email-push inserts, post HTML in the `body` column. When the dashboard renders preview, run through DOMPurify with `ALLOWED_TAGS = ['p','br','ul','ol','li','strong','b','em','i','a','span']`. The lint module accepts both forms today; future drafts must be HTML.

## 2. Every CTA is a hyperlinked anchor, not a raw URL

Bad: `Click here to watch: https://example.com/page`
Good: `<a href="https://example.com/page">Click here to watch the free master class</a>`

Bad: `Click here: MASTERCLASS_URL`  (placeholder)
Good: `<a href="https://www.precisionbrass.info/webinar-registration-pb?el=timoemail">Come watch the free master class where I talk about this in detail</a>`

The reader sees clickable text. The URL is never visible in the body. Lint blocks any placeholder string (REPLACE_TOKEN, MASTERCLASS_URL, .example, TODO_LINK) before send.

## 3. Master class CTA. Canonical URL + canonical wording

- **URL (LOCKED, no variants):** `https://www.precisionbrass.info/webinar-registration-pb?el=timoemail`
- **Anchor text:** `Come watch the free master class where I talk about this in detail`
- The `?el=timoemail` query param is the HYROS attribution tag for "came from a Timo-curated email send". Include it on EVERY master class link in EVERY email. Set 2026-05-13 by Timo (replaces the previous "optional `?el=email-<slug>`" pattern).

Replaces all prior "complimentary strategy session" CTAs. The "Step 1: Watch training / Step 2: Book strategy session" two-step framing is OUT. One CTA per email, one ask, one click.

## 4. Testimonial links come from the source file's front-matter

Every file under `voc/testimonials/raw/` has YAML front-matter with `source_url` and `video_id`:

```yaml
source_url: https://www.youtube.com/watch?v=JTKmXZEAuT0
video_id: JTKmXZEAuT0
speaker_name_inferred: Joinville
```

When an email quotes a testimonial, the email body MUST include a clickable anchor pointing at that exact `source_url`. Pull the URL from the cited file at draft time.

**Placement: where the writer marks it inline. Never default to the P.S.**

If the writer uses an inline placeholder like `[YOUTUBE TESTIMONIAL LINK]` or `[INSERT TESTIMONIAL]`, the publish step swaps that exact spot for the anchor. The placeholder lives where the testimonial is naturally introduced ("You can watch Joinville's full story right here: ...") -- that's the writer telling you where the link belongs. Do NOT relocate the link to the P.S. and do NOT duplicate it.

If there is no inline placeholder AND no inline mention of the testimonial, then and only then put a single anchor in the P.S.

Anchor text format: turn the natural sentence into the anchor itself. Good: `You can <a>watch Joinville's full story right here</a>`. Bad: `You can watch Joinville's full story right here. <a>Click</a>`.

Caught 2026-05-10: I dropped the testimonial anchor at the end of the P.S. while the writer had already marked `[YOUTUBE TESTIMONIAL LINK]` mid-body. Timo: "It seems kind of obvious that you would put the YouTube link where it says 'insert YouTube link.'"

Lint rule `bracketed-placeholder` BLOCKS any `[ALLCAPS PLACEHOLDER]` from shipping, so an unresolved marker can never reach the inbox.

## 5. P.S. lives inside body. ps_text is metadata only

The `ps_text` column on `email_proposals` is a categorization field. It is NEVER separately sent. The actual P.S. text must be appended to the `body` field as the final `<p>...</p>` paragraph, with the testimonial link embedded.

**How to apply:** when pb-email-write outputs a draft, the body string must already end with the P.S. as its last paragraph. The `ps_text` field stays for analytics but `/api/ac-send` only ships `body`.

## 6. Hard banned phrases (already enforced by lint)

- `Featured in Forbes` (Forbes credential is a hallucination, not real)
- `Adams routine` / `Adams method` / `Adams exercise`
- `hot air`
- `Jeremy Milosevic` (full name banned)
- `Harrisson Ball` (correct spelling: `Harrison Ball`)

Auto-fix is enabled for the standalone Forbes signature line and the Harrisson typo. Inline mentions get flagged but not silently rewritten.

## 7. Sender info on broadcast page pulls from the selected source campaign

`fromname` and `fromemail` come from the AC source campaign the user picks. Never hard-code the sender display in the inbox preview. The dashboard updates the avatar initial + sender chip on dropdown change.

## 8. Subject is read-only in the inbox preview

The Gmail-style preview is display only. The single source of truth for subject + body is the "Edit subject + body" tab. The preview reflects edits made there, never the other way around. Removed contenteditable on the inbox subject 2026-05-10 because dual-edit surfaces confused which value would actually ship.

## Lint module summary

`dashboard/lib/email-lint.js` enforces #2-#6. UMD module loads in the browser (emails.html, broadcast.html) AND in Node (pb-email-push pre-insert lint). Update the RULES array there when adding bans.

## Files touched on the 2026-05-10 lock-in

- `dashboard/lib/email-lint.js` (canonical rule list)
- `dashboard/emails.html` (modal preview renders HTML, lint banner + auto-fix)
- `dashboard/broadcast.html` (Gmail-style preview, single-source subject, HTML body render, grouped campaign dropdown)
- `~/.claude/skills/pb-email-push/SKILL.md` (Step 3a: lint pre-insert)
- `~/.claude/skills/pb-email/references/email-output-template.md` (HTML body, master class CTA, Harrison spelling fix)
- `memory/feedback_harrison_email_call_20260509.md` (enforcement pointer)
