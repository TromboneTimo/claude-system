---
name: harrison-email-call-2026-05-09
description: First Harrison-direct review of the pb-email system. Verbatim voice rules, hard bans (Forbes, Adams routine, hot air, Jeremy Milosevic), aggressive call-out body voice, send cadence, calendar-state preflight requirement.
type: feedback
originSessionId: e058534c-234c-434c-872f-b6cbfc8ff00d
---
# Harrison Email Review Call. 2026-05-09

> **Enforcement:** the hard bans below are encoded as RegExp rules in
> `Precision-Brass/dashboard/lib/email-lint.js`. The browser dashboard
> banners on hits at modal-open + broadcast-load and offers Auto-fix.
> The pb-email-push skill runs the same lint via Node before any POST
> (see Step 3a in `~/.claude/skills/pb-email-push/SKILL.md`). When you
> add or relax a rule here, ALSO update the RULES array in that file.

## Context

First time Harrison personally reviewed pb-email output. He pulled up an email draft live on screen with Timo and walked through line-by-line feedback on subject lines, body voice, CTA, sign-off, and the broader voice system. Audio: `~/Downloads/transcribethis.m4a`. Transcript: `/tmp/transcribethis.txt`. Harrison portion starts roughly line 510 (after the violin teacher Wilhelm leaves the call).

## Hard rules locked in

### 1. Forbes credential is BANNED, no exceptions

Harrison verbatim: *"I'm not in Forbes, bro… where did Paul get Forbes from?"*

**Why:** the AI hallucinated the credential off Paul The Trombonist's bio. The pb-email skill was contradictorily both REQUIRING it (in voice protocol Section 2 and output template) AND telling the auditor to reject it. Net effect: Forbes shipped to Harrison's eyes.

**How to apply:** the string "Forbes" appears nowhere in any draft, ever. Auditor greps and rejects on hit. Skill files updated 2026-05-09:
- `~/.claude/skills/pb-email/references/email-voice-protocol.md` (Section 3 + self-check)
- `~/.claude/skills/pb-email/references/email-output-template.md` (body template)
- `~/.claude/skills/pb-email/SKILL.md` (auditor checks 5, failure modes 4)
- `~/.claude/skills/pb-email/agents/07-best-practices-auditor.md` (voice fidelity 3)
- `Precision-Brass/voc/emails/extracts/harrison-email-voice.md` (Sections 2, 6, 10)

### 2. Subject line voice. Approved + banned patterns verbatim

**Approved (Harrison wrote these on the call):**
- `"This is why you {verb} {emotional outcome}"`. e.g. "This is why you quit trumpet playing three times"
- `"The real reason why you'll never {verb}"`. e.g. "The real reason why you'll never succeed at coming back"
- `"The reason why you {emotional outcome}"`. e.g. "The reason why you live in regret from your trumpet playing"
- `"What's a {identity} without {thing}? {Pejorative}?"`. e.g. "What's a lead trumpet player without their upper register? Useless?"
- `"I'm too {age}"` (states the prospect's internal monologue). e.g. "I'm too old"

**Banned (Harrison rejected verbatim):**
- `"Why {identity} {polite verb}"`. Harrison: "no, that's lame"
- `"{Identity} quietly lose {thing}"`. Harrison: "too direct, on-the-nose"
- `"Pick up the horn after X years..."`. Harrison: "soft cock"
- `"{Number} year old isn't coming back. Here's what to do"`. Harrison: "lame as fuck"

**Why:** Harrison wants emotional weight that stops the read. Indirect call-out beats direct accusation. Cannot read like marketing copy or trip spam filters.

**How to apply:** Section 1.5 of email-voice-protocol.md. Auditor enforcement check 7 in SKILL.md.

### 3. Body voice. Aggressive call-out energy ("dude this sucks")

Harrison verbatim: *"You're just like, dude, this sucks. It's like the emotional tie to it, 'cause it's like, it needs to be like, stop people."* Harrison reviewed competing creators' emails on the call and called the weak ones "limp dink" and "soft cock."

**Why:** A bold subject followed by a polite, hedging body is the worst combo. The reader opens expecting a punch, gets a hug, and immediately distrusts the sender. Harrison talks like a frustrated coach who's tired of watching the reader get sucker-punched by other methods. The aggression earns the right to deliver the solution.

**How to apply:** Section 1.6 of email-voice-protocol.md. Body must drop the gloves at least once per email (one sentence that would feel uncomfortable to read aloud to a stranger). Banned hedge openers: "I just wanted to say...", "Maybe you've felt...", "If it's okay with you...", "Just checking in...", "No worries if...". Banned corporate hedges: "we believe", "many of our students", "in our experience". Auditor enforcement check 8 in SKILL.md.

### 4. Topic guardrails. HARD ban

Harrison verbatim: *"Let's stay away from shitting on the Adams routine too much… It's gonna piss Jeremy Milosevic off, and him and I have a mutual understanding."*

Timo follow-up 2026-05-09: hard ban, no "a little bit" exceptions. Avoid all talk of the Adams routine. Focus on other popular methods like Arban's, Schlossberg, general etudes.

**Banned (any spelling, case-insensitive):**
- "Adams routine" / "Adam's routine" / "Adams approach"
- "hot air" approach
- "Milosevic" / "Jeremy M"

**Approved roast targets:**
- Schlossberg / Sloshberg
- Clark studies (Claude Gordon Systematic Approach)
- Gordon (any Gordon-named method)
- James Stamp warmups
- Arban's method drills (also Arbans, Arben)
- Generic "more air, tighter corners" pedagogy
- Etudes generally

**Why:** Harrison maintains a personal non-aggression pact with Jeremy Milosevic. The LA trumpet scene reads his emails. One slip burns a peer relationship.

**How to apply:** Section 12 of email-voice-protocol.md. Auditor enforcement check 6 in SKILL.md.

### 5. CTA hard rules

Harrison flagged a draft where the CTA said "watch the training, link below" with no actual link. He also roasted a competing creator's "this will be the easiest thing you'll ever do" CTA as "limp dink."

**Rules:**
- Every CTA must contain a real link or clearly-marked HiRose `?el=` placeholder. No "[link below]" placeholder text.
- No undersold CTAs ("easiest thing you'll ever do", "just hit reply, no big deal", "if you have a second").
- CTA names the asset (training, strategy session, discovery call) plus an adjective (free, complimentary, no-cost).

**Approved verbatim 2026-05-09:** "Click the link to watch the training and book your complimentary strategy session"

**How to apply:** Section 5 of email-voice-protocol.md. Auditor enforcement check 9 in SKILL.md.

### 6. Calendar-state preflight (new feature)

Harrison's last broadcast got 44% engagement and $0 in conversions because his calendar was full at send time. Replies came back saying "no times available."

**Rule:** pb-email asks Timo before every run: "Is Harrison's calendar currently open or full?" If full, drafts use the capacity-aware CTA variant ("we're at capacity, here's the waitlist") instead of "book a call." P.S. type changes from `scarcity` to `social-pressure` or `risk-reversal`. Never `urgency` when calendar is full.

**How to apply:** Step 1b in SKILL.md. Section 5 calendar-full variant in email-voice-protocol.md.

### 7. Send cadence (Phase 2 prep)

Harrison verbatim: *"Every day, 4 a.m., nothing else. One a day, 4 a.m., not multiples."* + *"4 a.m. Los Angeles time."*

**Rule:** Phase 2 (AC publish) must honor 1/day at 4am LA. AC segment exclusions: exclude `booked-call` tag, require `40-day automation completed` tag.

**How to apply:** SKILL.md "Harrison's hard send rules" section. Agent 7 send-cadence note overrides the 2-3x/week best practice.

### 8. AUTO-SEND IS NOT BUILT (loud reminder)

Phase 2 AC publish does not exist yet. Drafts go to dashboard for Harrison's manual review and manual AC send. Never write copy or status messages that imply auto-send.

**How to apply:** Top-of-file warning in SKILL.md. Failure mode 10. Agent 7 send-cadence note.

## Wins captured

- A subject line generated by pb-email beat Harrison's hand-written subject in production A/B test "by far" (script proposal lens). Confirms the system is in the right ballpark when fed Harrison's voice catalog.

## Files changed 2026-05-09

- `~/.claude/skills/pb-email/SKILL.md` (added: AUTO-SEND warning, hard send rules, Step 1b calendar preflight, expanded auditor checks 5-13, expanded failure modes 4-10, wins log, changelog)
- `~/.claude/skills/pb-email/references/email-voice-protocol.md` (added: Section 1 patterns 5-6, Section 1.5 subject patterns, Section 1.6 body voice aggression, Section 5 calendar-full CTA variant, Section 12 topic guardrails, expanded self-check)
- `~/.claude/skills/pb-email/references/email-output-template.md` (stripped Forbes from credential line)
- `~/.claude/skills/pb-email/agents/07-best-practices-auditor.md` (overrode 2-3x/week cadence with Harrison's 1/day rule, expanded voice fidelity checks)
- `Precision-Brass/voc/emails/extracts/harrison-email-voice.md` (struck Forbes from Section 2 sign-offs, marked banned in Section 6 vocabulary, updated Section 10 known issues)

## Next time pb-email runs

1. Step 1b calendar question fires before any drafting
2. Auditor checks 5-10 enforce the new bans
3. Drafts have aggressive call-out energy or get rejected
4. Forbes does not ship
5. Adams routine / hot air / Milosevic do not ship
6. Wins log gets a new entry if Harrison reviews + approves
