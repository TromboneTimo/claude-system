---
name: Email voice load order is non-negotiable
description: When drafting any Harrison email, load these files in this exact order before writing a sentence. Skipping or reordering produces off-voice drafts that read as Paul-template leakage or generic SaaS copy.
type: feedback
originSessionId: 7f540398-3cb8-4b73-9023-2f87ee04eec4
---
## The rule

Before drafting ANY email for Harrison Ball / Precision Brass, load these files in this exact order. Then write.

1. `voc/emails/extracts/harrison-email-voice.md` (302-line voice catalog, the source of truth)
2. `output/email-PP01-dental-trigger-FINAL.txt`
3. `output/email-PP03-failed-lessons-FINAL.txt`
4. `output/email-PP05-isolation-FINAL.txt`
5. `voc/emails/raw/sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md` (emails 1-7 ONLY, NEVER 8-12)

## Hard exclusions

- Emails 8-12 of the webinar sequence are signed by Paul The Trombonist and target music educators. Per voice catalog Section 10, they are template leakage. Loading them pollutes Harrison's voice.
- "Mastermind" terminology (Email 3 leak from Paul template).
- "Music educators", "profitable, flexible online teaching business" (Paul template phrasings).

## Why

The voice catalog was built 2026-04-21 from 7 known-Harrison emails. The 3 FINAL emails in `output/` are the closest thing to verified production-quality Harrison voice. Paul-the-Trombonist content is in the same project folder but is template leakage we have not cleaned up; loading it gives the agent the wrong fingerprint.

The recurring tagline must appear verbatim in every draft:
> "We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system."

No paraphrase. No reorder. No "improve". Verbatim.

## How to apply

This load order is enforced by `/pb-email` skill at `~/.claude/skills/pb-email/references/email-voice-protocol.md`. Drafting agents (1-6 in `agents/`) all receive these files as load-once context. The auditor (agent 7) rejects any draft that lacks the recurring tagline verbatim or contains forbidden phrases.

Apply this same load order anywhere outside the skill that drafts a Harrison email. Custom one-off requests like "write a quick email to the list about X" still need the load order. Off-voice email > no email.

## Past failure

The voice catalog file itself flags this as a known issue (`feedback_harrison_voice.md` records that voice-spec.md was wrong and harrison-real-voice.md overrode it). The email engine is built to prevent the next iteration of this same drift.
