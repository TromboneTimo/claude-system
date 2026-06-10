# Ed-Lawrence structure + revision lessons (locked 2026-06-07, Hannah email)

The session where Timo and I rebuilt the "Hannah / How many years" email from scratch. These are now defaults for pb-email-write and pb-email. Load this with the voice protocol.

## THE MODEL (run in this order, EVERY email Timo asks us to create)
This is the standing workflow Timo locked 2026-06-07 ("keep this model for future emails"). Do not skip steps.
1. **Resolve the real source.** If a video/link is involved, oEmbed it FIRST to confirm who the student actually is and what they really achieved. The link, not a template's named student, is the source of truth.
2. **Read the FULL source** (transcript / testimonial / sales call) before writing one word. No drafting off a truncated or skimmed pull.
3. **Mine the swipe file + corpus for structure** (`voc/emails/swipe-file/` Ed Lawrence + Dimitri, `analysis/`), and check the live angle ledger so the angle AND proof-student are fresh, not a heavy repeat.
4. **Draft in the DEFAULT structure** (below), in Harrison's voice. One masterclass-sourced mechanism, zero invented facts, no testimonial claim beyond the witness's exact words.
5. **Chat-draft first** in plain markdown; iterate with Timo. Answer his LITERAL ask each round (full email != quote; question != statement).
6. **Run the metrics pass** (word count vs corpus, readability, I:you, paragraph walls) and fix BEFORE saying done. Settle taste with numbers, early.
7. **Build the email HTML** with the centered-video block, render to PNG, and READ it yourself (visual gate).
8. **Test-send to list 20**, verify `send_amt=1`, never delete before confirmed (`project_ac_test_send_mechanism`).
9. **Real list (13) = dashboard only.** Push to the proposal queue; a human reviews + schedules. Never direct-send/schedule the real list from here.

## DEFAULT EMAIL STRUCTURE (Ed Lawrence / Film Booth, Timo-approved)
Mined from `voc/emails/swipe-file/raw/film-booth/` + `analysis/film-booth.md`. Use this scaffold unless the angle demands otherwise:
1. **Open on a SHORT question that names the pain.** One line, punchy. Not a long multi-clause question. e.g. "How many years have you done everything they taught you, and gotten nothing back?" Then one pain beat ("Same notes cracking. Same horn fighting you every day.").
2. **Pivot to first-person confession with "That was me."** Harrison's real sourced struggle (lost his playing, hurt to put the horn on his face, house on quicksand). The reader OPTS IN ("that sounds like me") instead of being cold-read. Do NOT tell the reader their feelings in a long "you did X, you felt Y" stretch.
3. **Reframe (the lesson), woven, not lectured.** One warm sentence: it was never effort, it was alignment; there is no one-size trumpet; upstream/downstream. Masterclass-sourced only.
4. **Proof student as the worked example.** Their before -> the "I watched them play and saw it in minutes" beat -> concrete after. Land their verbatim quote ALONE on its own line at the pivot (storytelling-affect device 5).
5. **Centered, clickable video** (see block below).
6. **Soft sign-off, then P.S. CARRIES THE OFFER** (Ed move). Bridge from "what I do now" into the program + real scarcity + the apply CTA. Do not repeat the body's CTA verbatim; nothing after the P.S.

Pronoun balance: Ed/Dimitri bodies run ~40% "I" / ~60% "you" (measured over 182 emails). A confession-led email may run higher "I"; that is fine. The VAS ad's 77% "I" is an AD shape, not an email shape, do not copy it wholesale.

## READ-FULL-SOURCE + DON'T-OVERSTATE GATE (hard)
- Before writing ONE word about a student, read their ENTIRE transcript/testimonial. I softballed Hannah because I drafted off a truncated pull and missed her real wins (lead playing, improv, music school, "most observant teacher").
- Stay INSIDE the witness's exact words. Hannah said the program gave her "the confidence to do" lead/improv/high-register. That is NOT "she is gigging lead." Write "going after" not "is doing" unless Timo confirms the harder fact from outside the video. Overstating a testimonial is a ship-blocker (CONTENT VERIFICATION GATE).
- The VIDEO/link is the source of truth for who the student is, never the template's named student (Joinville template -> the link was actually Mike, then Hannah). Resolve the real subject via oEmbed FIRST.

## ANSWER THE LITERAL ASK
When Timo asks a precise thing, deliver exactly that. "Show me the full emails" = paste full emails, not quotes. "Reform the question" = give questions, not statements. "Is that verbatim?" = answer yes/no with the exact source line. Substituting a near-version wastes a whole round.

## METRICS PASS (run before declaring a draft done)
Ground taste fights in numbers, not vibes. Script pattern (`/tmp/readability.py` style): compute words, avg sentence length, Flesch Reading Ease, FK grade, paragraph "walls" (>3 sentences OR >~280 chars), and I:you ratio. Compare to the live corpora: Ed value emails median ~480-550w, FRE ~76, grade ~7; Dimitri ~180-330w. Target: land in Ed's band, 0 real walls (your rhythm rule is <=2-3 sentences / ~170 chars), readability >= Ed. Do this EARLY, not after five rounds.

## CENTERED VIDEO HTML BLOCK (email-safe)
Email clients strip iframes. Use a centered clickable thumbnail with a CSS play-button overlay linking to the watch URL. Thumbnail = `https://i.ytimg.com/vi/<VIDEO_ID>/hqdefault.jpg`.
```html
<table role="presentation" width="100%"><tr><td align="center" style="padding:4px 0 26px;">
<a href="https://www.youtube.com/watch?v=<ID>" target="_blank" style="display:inline-block;position:relative;line-height:0;text-decoration:none;">
<img src="https://i.ytimg.com/vi/<ID>/hqdefault.jpg" width="520" alt="Watch ..." style="display:block;width:100%;max-width:520px;border-radius:12px;border:1px solid #e3e3e6;">
<span style="position:absolute;top:50%;left:50%;width:72px;height:72px;margin:-36px 0 0 -36px;background:#FF0000;border-radius:50%;"></span>
<span style="position:absolute;top:50%;left:50%;margin:-12px 0 0 -8px;border-style:solid;border-width:12px 0 12px 20px;border-color:transparent transparent transparent #fff;"></span>
</a></td></tr></table>
```
Render the whole email to PNG (headless Chrome; `file://` is blocked in Playwright so serve via `python3 -m http.server`) and READ it before sending.

## SENDING / SCHEDULING (do not freelance)
Real list (13, ~4,105 subs) is dashboard-only, human-scheduled. Test sends go to list 20. See `project_ac_test_send_mechanism.md` (set sdate=now via v3 PUT + let the scheduler ship; never delete before send_amt confirms; one mechanism only) and `feedback_verify_send_not_ack.md` (the API's "Message sent" is NOT proof; send_amt is).
