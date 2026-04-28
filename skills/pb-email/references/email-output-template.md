# Email proposal menu output template

This is the exact format pb-email returns to Timo in chat. The auditor (agent 7) builds this. Do NOT deviate. pb-email-push parses against this shape.

---

## Header

```
=== EMAIL PROPOSAL MENU ===
Audience(s): {comma-separated audience tags}
Run date: {YYYY-MM-DD}
Voices fresh this run: {names not used in last 2 runs}
Voices skipped (off-limits): {names used in last 2 runs}
```

## Per-draft block (5 of these)

```
---

### Draft {N}: {Subject Line}

**Audience:** {broadcast | reengagement | webinar-push | discovery-followup}
**Hook angle:** {identity | failed-method | specific-result | curiosity | money}
**Pain point:** {1-line summary}
**P.S. type:** {scarcity | timing | urgency | social-pressure | risk-reversal}
**CTA:** {discovery-call | strategy-session | training-rewatch | youtube-watch}

**Subject line alternates:**
- {Alt subject 1}
- {Alt subject 2}

**Preheader:** {Preheader text, 50-90 chars}

**Body:**

```
Hey %FIRSTNAME%,

{opening line, matches one of 4 patterns from voice catalog Section 1}

{body paragraph 1}

{body paragraph 2}

{body paragraph 3 with student name proof if applicable}

{transition to CTA}

{CTA line, exact phrasing from voice catalog Section 5 templates}

We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system.

Looking forward to {meeting you / hearing how it goes / etc.},
Harrisson Ball
{credential line if formal email: "CEO, Precision Brass / Featured in Forbes"}

P.S. {P.S. text matching declared P.S. type}
```

**CTA URL placeholder:** `https://precisionbrass.com/{path}?el=email_{slug}`

**Rationale (plain English, 3 sentences):**
{Why this draft. What sales call or testimonial inspired it. What the prospect feels reading the subject line that makes them open. No internal jargon (no "the corpus", "BOFU", "the converter", etc.).}

**Source tags:** [{audience}, {hook angle}, {corpus origin: sales-calls / testimonials / fb-winners / fresh-lens-X}]

**VOC quotes (minimum 1 testimonial + 1 sales call):**

> "{testimonial quote}"
> SOURCE: {Name}. Video testimonial after working with Harrison, describing {context}.

> "{sales call quote}"
> SOURCE: {Name}, age {N}. Sales call {context}. Signed up for ${amount}. (or "Did not sign up" / "Pending")

```

## Footer

```
---

Pick which to push to Harrison's dashboard.
Reply "push 1, 3, 5" or "push 2" or "all of them".
I'll run /pb-email-push to land them in dashboard/emails.html.
```

---

## Required fields per draft (zero-drop check)

If any field is missing, the auditor MUST send the candidate back to its agent for repair before including in the final 5. The 14 required fields:

1. Subject line
2. 2 subject alternates
3. Audience tag (one of 4)
4. Hook angle (one of 5)
5. Pain point (1 line)
6. P.S. type label (one of 5)
7. P.S. text matching the type
8. CTA type (one of 4)
9. Preheader text
10. Body (Harrison voice, recurring tagline verbatim, real student name if cited)
11. CTA URL placeholder (HiRose `?el=` format)
12. Rationale (3 sentences plain English)
13. Source tags (array)
14. VOC quotes (1+ testimonial AND 1+ sales call, with full source attribution)

If a candidate is missing any of these, the auditor returns it to the agent with the missing-field list. Repeat until all 14 are present, OR drop the candidate and pick from another agent's overflow.
