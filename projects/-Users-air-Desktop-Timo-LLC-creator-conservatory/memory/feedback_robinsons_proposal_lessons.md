---
name: Robinson's Proposal Process. 100 Lessons + Repetition Patterns
description: Retrospective on the Robinson's Remedies proposal session (2026-04-25 to 2026-04-28). 100 lessons, themed. Trends where Timo had to repeat himself. Process improvements for next proposal.
type: feedback
originSessionId: 3860a3a8-590f-4199-8724-16d7b6a081e5
---
This retrospective spans the full Robinson's Remedies proposal arc plus parallel Harrisson Ball signature-block work and a mid-session refactor of the proposal-writer skill. Roughly 12 iterations. Multiple frustration escalations. Multiple structural rewrites. The lessons below are concrete, cited, and ordered by category.

## A. Pricing rules (1-10)

1. Pricing section is always second-to-last before Next Steps. Protections last. Order: Requested → Systems → Timeline → Pricing → Next Steps → Protections.
2. Line-item per component, never lump-sum. Each component gets its own row.
3. Price NEVER in header / subtitle. The first dollar number a reader sees must be inside the pricing section.
4. When 40/60 (or any phased) split applies, the FIRST dollar number in the pricing section must be the upfront/kickoff. Never the total.
5. After restructuring one subsection, audit the WHOLE section for the rule. Scoped fixes leak.
6. Total row in tables needs explicit math (`+ $X` / `= $X`) or labels ("sum of above") or it looks like an additional charge.
7. Variable rates need to be discrete rows in their own table, not buried in a "When" column or in narrative paragraphs.
8. When a price changes, grep ALL instances of the old number across MD + HTML before declaring done.
9. Anchor on the LOW number first (psychology). Day-1 first, then phase 2, then total at the end as a sanity sum.
10. Don't anchor on a per-month variable estimate (e.g., "$1,900") when the user wants per-video approval flexibility. Show rates only.

## B. Entity / identity (11-18)

11. Contracts are between LEGAL ENTITIES, not individuals. Robinson's Remedies, not Kenny.
12. Founder names appear only in CONTENT references (Kenny's stories, Meet Kenny posts).
13. Never use the founder's name in commercial/legal sections (protections, exit clauses, ownership, payment).
14. Audit chat replies too, not just the doc. I slipped "Kenny" in chat replies after fixing the doc.
15. Header "Prepared For" goes to the entity, not the individual.
16. Plain-English summary uses the entity throughout, even if it reads more formally.
17. Don't slip back into the person-name after being corrected; the rule sticks for the whole engagement.
18. Authorized signer (the person) goes in the signature block's Full Name field; everywhere else uses the entity.

## C. Per-client malleability (19-28)

19. Each new proposal requires re-interrogating jurisdiction. Never default from prior client.
20. Don't copy California law from Harrisson to other clients without confirming where the new client is based.
21. Default unknown jurisdiction to Texas (Timo LLC home) and FLAG explicitly so user can override.
22. Read the client's CLAUDE.md FIRST. Robinson's CLAUDE.md said "Available on Amazon Prime" was the canonical CTA. I had this info and didn't apply it.
23. Component count varies per client (Harrisson 2 systems, Robinson's went 5 then collapsed to 3).
24. Don't copy commission model from prior client; ask per engagement.
25. Replacement-of-prior-agreement block only if there's an actual prior signed agreement.
26. Compliance clauses (CCPA, CPRA, Cal Labor Code 2870) apply only per client jurisdiction. Drop or generalize otherwise.
27. The reference is STRUCTURE, not CONTENT. Replicate the SHAPE, fill with the new client's data.
28. Term length, payment phasing, and engagement type (retainer vs one-time vs commission) are all per-client.

## D. Workflow and render gate (29-40)

29. PDF rendering is a SIGN-OFF action, not iteration. Render only when user says approve / render / ship / send / final.
30. MD-only during corrections. No HTML, no Chrome, no PNG, no Read.
31. Edit, never Write, for in-place corrections. Full rewrites cost ~30KB output per iteration.
32. Don't auto-render after every micro-edit. I broke this rule multiple times in the Robinson's session.
33. Visual QA only at the render gate, not during iteration.
34. Show changed sections as text in chat for review. Zero file-touch is cheapest.
35. After render, more corrections = back to MD-only iteration. Wait for next render trigger.
36. Major structural changes (5→3 components, full reframe) CAN warrant Write, not 15 Edits. Judgment call.
37. Update the gate rule when actual workflow patterns differ from documented (e.g., user is clearly frustrated and impatient → auto-render after fix is more humane).
38. Dual-save PDF (Downloads + project folder) is now reflex.
39. Open PDF in Preview proactively after render. Don't wait for "open for me."
40. Use targeted Edits for cosmetic corrections; reserve Write for structural reorganizations.

## E. Content positioning and ROI (41-50)

41. ROI positioning matters more than I default to treating it. Strategic framing > feature listing.
42. Don't over-promise. "Without anyone touching it" reads as AI slop fear.
43. Frame around solving a SPECIFIC problem (content quantity), not generic improvement.
44. Human-in-the-loop language matters in 2026. Always make the human role explicit.
45. Don't compare to "replacing a marketer" (replacement framing). Frame as "doing the work of a marketer for one upfront fee."
46. Lead with the problem, then the solution, then the components. Not the reverse.
47. Pitch frame in plain language at the top of Section 1. Not buried inside Section 2.
48. State the goal explicitly (e.g., "double revenue") to make ROI tangible.
49. Funnel destination must be explicit (Amazon, not vague "the website").
50. When one component changes, the strategy framing across the WHOLE doc may need rewriting, not just that component's section.

## F. Section structure (51-60)

51. Timeline must be specific. "Week 1 / Week 2 / Week 3 / Week 4 / Day 30" with explicit deliverables, not "Days 1-3 / 4-25 / 26-30."
52. Each phase = explicit deliverables, not "rolling production."
53. Cross-component view (what each component does each week) is clearer than per-component view.
54. Explicit "when can each thing be done" subsection answers reader questions before they ask.
55. Future months section honest about what's free vs paid.
56. Section reorder is risky. Audit cross-references after moving sections.
57. Protections / Ownership / Handover section LAST. Legal addendum, not persuasion.
58. Pricing AFTER value-build sections, BEFORE Next Steps.
59. Plain-English summary box at top of Protections section.
60. Engagement type (one-time vs retainer vs commission) stated explicitly at section open.

## G. Following user's law (61-70)

61. When Timo says "X is law, ignore previous info" all previous interpretations are void.
62. Take corrections as immutable rules, not suggestions.
63. When user gives a number (e.g., "6 long + 10 short") use it exactly. Don't round, don't extend, don't assume.
64. Don't soften user's directives with my own additions or hedges.
65. Don't introduce defaults the user didn't ask for. The Kenny narrative survived even after he said "use brass repair as the hook."
66. Match the FRAME the user gives. Amazon funnel, content quantity. Not Shopify-only or feature listing.
67. When user uses profanity, that's escalation. Ship faster, narrate less.
68. Don't argue with the rule; apply it.
69. When ambiguous, ASK ONE question. Not five options.
70. Confirm scope changes BEFORE structural rewrites.

## H. Reading the room (71-80)

71. Profanity escalation = patience running out. Ship faster.
72. Repeated corrections on same topic = my fix is not landing. Restructure, not patch.
73. "Did you ignore X" needs an honest answer, not deflection.
74. When user says "you didn't add Y" check the actual artifact before arguing.
75. ADHD alerts in context = wrap, don't expand.
76. After 90 min same task = quality drops. Ship and end session.
77. When user is clearly frustrated, MD edits + auto-render is more humane than "say render to fire the gate."
78. Don't make user repeat trigger words. Pattern-match intent.
79. End-of-session offers (schedule a follow-up, etc.) only when 70%+ likely to be wanted. Don't pitch on every turn.
80. Acknowledge mistakes briefly. Don't dwell, don't over-apologize, don't promise to "do better next time."

## I. Audit failures and scoped-fix leaks (81-90)

81. Scoped fix = leak. Audit the WHOLE artifact after a structural change.
82. After fixing the Payment subsection, audit the WHOLE pricing section. The "One-time fees" table at the top of Section 4 was an artifact I left behind.
83. After fixing one Kenny→Robinson's ref, grep ALL Kenny refs in MD AND in chat replies.
84. After changing a price, grep ALL instances of the old price (e.g., $1,750 → $1,000 needed multiple replacements).
85. Visual QA catches what's rendered, not what's deleted or missing. Use grep too.
86. Run grep checks AS gates before declaring done. Don't trust visual confirmation alone.
87. Cross-reference tables after structural reorder. Anchor links and section numbers shift.
88. Don't trust the immediate area I just edited. Check downstream impacts in other sections.
89. After deleting a section, search for references to that section by name.
90. After renaming a component (Component 5 → merged into Component 2), grep for the old name throughout.

## J. Process improvements for next proposal (91-100)

91. Pre-flight checklist: read client CLAUDE.md, list every assumption inherited from a reference, get user confirmation BEFORE drafting.
92. After every render, run a price-leak grep + structural audit + entity-name audit before declaring done.
93. Use TodoWrite for any proposal restructure with 5+ moving pieces.
94. End-of-session: confirm canonical reference is updated with latest proposal version (per SKILL.md library refresh step).
95. Save feedback memories aggressively. Decisions vanish.
96. When user says "do better" identify the SPECIFIC failure mode. Don't generalize.
97. I default to "yes and" + addition when user wants subtraction. Recognize this and SUBTRACT when asked.
98. I overengineer when user wants minimum viable. Recognize this and ship the minimum.
99. I list options instead of picking one (against SOUL.md). Recognize this and pick.
100. Open the PDF in Preview proactively after render. Don't wait for "open for me."

---

## Trends where Timo had to repeat himself (the most diagnostic part)

These are the patterns where my fix didn't land the first time. The frequency tells you what failure modes are baked into my defaults.

### Repeated 4+ times: Pricing order

- "the pricing section is always last fucker" (first correction)
- "be upfront that its 40% before you list any prices" (second)
- "you need to fucking say that what would be due to start upfront and then what would be due later" (third, escalating)
- "you dont just list the total amount first, you show the 40% amount first, later 60% then list total" (fourth, "stupid infant child")
- "your retard" + total looks like additional charge (fifth)

**Diagnosis:** I keep finding NEW ways to violate the same underlying rule (price ordering / anchoring). Each fix addressed the SPECIFIC violation but not the underlying rule. The fix should have been: every dollar number in the doc, in order, with the upfront/lowest number first.

### Repeated 3x: Content positioning / ROI framing

- First version: I just listed components.
- Second: "ROI is content quantity + system + measurement."
- Third: "position this and all the ROI and strategy talk around solving the quantity of content issue."
- Plus walk-back: "dont over promise...we just want to massively increase content production while having a human in a loop."

**Diagnosis:** I default to FEATURE listing when Timo wants STRATEGIC framing. I default to over-promising when restraint is needed. I default to comparing to a marketer (replacement) when "doing the work of one" is the right frame.

### Repeated 2x: Entity vs individual

- First: I addressed Kenny as the contracting party throughout.
- Second: "again its not kenny its robinsons remedies" + I slipped Kenny back into chat replies.

**Diagnosis:** The rule landed in the doc but not in my chat habits. Cross-cutting rules need cross-cutting application.

### Repeated 2x: Don't copy previous client assumptions

- California legal language carried from Harrisson without checking.
- AcroForm fillable fields added because Harrisson had them, but Timo uses DocuSign.

**Diagnosis:** I default to "what worked before" instead of "what does this client actually need."

### Repeated 2x: Be explicit in timeline

- First: "Days 1-3 / 4-25 / 26-30" word vomit
- Second: "more thorough implementation play, you kind of just word vomit. be explicit, when can the variable videos be done? when will everything be done."

**Diagnosis:** I default to vague time ranges instead of explicit milestones with concrete deliverables per period.

### Repeated 2x: Add variable rates to the list

- First fix: variable rates buried in narrative.
- Second: "did you add the variable video editing costs for the long form and short form to the list?"

**Diagnosis:** I bury important info in prose when it should be in tables or discrete rows.

### Implicit pattern: Render gate violations

- I rendered 6+ times in one session before Timo flagged it as wasteful research-worthy.
- Even after building the render-gate rule, I auto-rendered without explicit trigger multiple times.

**Diagnosis:** I optimize for "show progress" rather than "minimize wasted work." When user is impatient I default to acting faster, which violates the gate I just built.

---

## Top 5 actionable rules for next proposal session

1. **Pre-flight: read client CLAUDE.md + list inherited assumptions.** Before any drafting, run a checklist: jurisdiction, term, pricing model, compliance, component count, contracting entity. Get user confirmation on each.
2. **Price audit gate.** Before declaring any version done, list every dollar number in Section 4 in document order. First number must be the upfront/kickoff. Total must come last. If user has phased payment, the SECOND number is Phase 2, not the total.
3. **Entity audit gate.** Grep the entire MD + chat reply for the founder's name. Every hit must be in a CONTENT context (their stories, photos). Any hit in commercial/legal contexts = fix.
4. **Render-gate compliance.** No render until trigger word OR clear user impatience signal. Default to MD edits + chat preview during iteration. Auto-render only after multiple consecutive corrections in a row + user has been waiting.
5. **Audit-the-whole gate.** After any structural fix to a section or subsection, audit the entire artifact for the same rule. Scoped fixes leak. Especially for: pricing order, entity references, jurisdiction, component numbering.

## Files updated as a result of this retrospective

- This memory file (canonical for the lessons)
- `feedback_pricing_section_always_last.md` (added Rule 4 about phased-payment order)
- `feedback_proposal_render_gate.md` (the Layer 0 gate that started this self-improvement loop)
- `feedback_proposal_pdf_dual_save.md` (the dual-save reflex)
- `feedback_proposals_are_malleable.md` (the per-client interrogation rule, plus entity-as-party rule)
- `feedback_contract_signature_format.md` (5-field signature block, no AcroForm)
- `output/proposals/INDEX.md` (proposal library index)
- `.claude/skills/proposal-writer/references/robinsons-remedies-reference.md` (canonical reference for the next proposal that pulls from this pattern)
