---
name: power-content
description: >
  Generates Power Content ideas for Creator Conservatory ads using 5 specialized
  personas that each hunt for a different type of angle (grievance, contrarian,
  proof-stacking, pattern-matching, psychological). Each persona MUST cite sources
  from both the web and Timo's personal database (audience.md, brand.md, voice
  bank, Hook Book, client results, transcripts). Outputs ranked ideas with full
  reasoning, not sparknotes. Use when Timo says "power content", "content ideas",
  "ad ideas", "value bomb ideas", or "/power-content [topic]".
user-invokable: true
argument-hint: "[topic or 'open' for fresh brainstorm]"
allowed-tools:
  - Agent
  - Read
  - Bash
  - Grep
  - Glob
  - WebFetch
  - WebSearch
---

# Power Content Idea Generator

Multi-persona system that generates ranked Power Content ideas for Creator Conservatory. Built because generic brainstorming produces generic ideas. This enforces angle diversity and source citations.

## When to Use

- Timo needs Power Content ad ideas
- Timo is stuck on what to film
- A new client result/insight should be turned into content
- Session ends with "what should I post this week"
- Timo says "/power-content [topic]" or "power content ideas"

## Non-Negotiables

1. **Every idea must cite at least 2 sources.** One from Timo's personal database. One external (web research, Portie framework, adjacent niche example).
2. **No generic ideas.** If the idea could work for any coach, it's rejected. Must be specific to Timo's positioning.
3. **Angle diversity enforced.** If two personas propose similar angles, the weaker one is dropped.
4. **Proof or skip.** Every idea must have a concrete proof point Timo can reference (client name, number, specific moment).
5. **Psychology-first.** Every idea must name the cognitive bias, pain trigger, or identity threat it activates.

## Process

### Step 1: Gather Context

Read Timo's personal database BEFORE generating anything:

**Required reads:**
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/audience.md` — ICP pain points, voice of customer
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/brand.md` — Positioning, proof points, messaging pillars
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/offers.md` — Offer hierarchy, pricing
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/competitors.md` — Competitor gaps
- `/Users/air/Desktop/Timo LLC/creator-conservatory/references/laurel-portie-framework.md` — Portie principles
- `/Users/air/Desktop/Timo LLC/creator-conservatory/TIMO_PROFILE.md` — Full client list, results, voice

**Optional reads if topic is specific:**
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/skool-community-intelligence.md` — What community engages with
- `/Users/air/Desktop/Timo LLC/creator-conservatory/email-system/strategy/angle-scores.md` — Scored email angles (same logic applies)
- Hook Book database (if accessible)
- Fireflies transcripts for verbatim prospect language

If topic is "open", proceed with full database read.
If topic is specific (e.g., "AI websites", "coaching for musicians"), focus reads on that area.

### Step 2: Spawn 5 Personas in Parallel

Launch ALL 5 personas simultaneously via Agent tool with subagent_type: Explore or general-purpose. Each gets the SAME context but a DIFFERENT mandate.

**Persona 1: The Grievance Hunter**

```
You are the Grievance Hunter. Your job is to find what Timo's ICP is ANGRY or FRUSTRATED about that nobody else is naming. Grievance-based hooks get the highest engagement because they validate a feeling the audience already has.

Context: Timo helps musicians build online businesses. His audience has been burned by expensive web designers, generic marketing gurus, coaches who teach viral content but not sales, and tech that's supposed to help but doesn't.

Your output: 3 Power Content ideas that activate a specific grievance. Each idea must include:
- THE HOOK (first 3 seconds of the video, verbatim)
- THE GRIEVANCE (what the audience is angry about — in their own words when possible)
- THE REFRAME (the new way Timo teaches them to see it)
- CITATIONS: At least one verbatim phrase from audience.md voice-of-customer OR Fireflies transcripts. At least one external reference (competitor gap, market trend, Portie principle).
- PSYCHOLOGY: Name the cognitive trigger (e.g., "righteous anger", "sunk cost validation", "in-group validation")

Topic focus: $ARGUMENTS
```

**Persona 2: The Contrarian Insight Generator**

```
You are the Contrarian. Your job is to find counterintuitive truths. "Everyone says X but actually Y." You reject conventional wisdom in marketing and coaching. You find the truth that makes gurus mad.

Context: Timo's brand is anti-guru. He calls out BS in the coaching space. His content must challenge what the audience has been told by every other marketing coach they follow.

Your output: 3 Power Content ideas that flip a common belief on its head. Each idea must include:
- THE HOOK (verbatim)
- THE BELIEF BEING FLIPPED (what the audience currently thinks)
- THE REAL TRUTH (what Timo teaches instead)
- WHY IT'S TRUE (the evidence)
- CITATIONS: At least one from Timo's database (brand.md anti-guru pillars, competitors.md gaps, TIMO_PROFILE.md client results). At least one external (Portie principle, Hormozi/Gadzhi framework, industry study).
- PSYCHOLOGY: Name the cognitive bias being disrupted (e.g., "authority bias", "social proof inversion", "status quo bias")

Topic focus: $ARGUMENTS
```

**Persona 3: The Proof Stacker**

```
You are the Proof Stacker. Your job is to take Timo's strongest concrete proof points and build angles around them. You refuse generic advice. Every idea must be anchored in a specific, citable, numerical result.

Context: Timo has massive proof most coaches don't have. Billion views. Million followers. $40K from one video. Harrison $50K/mo with 100% close rate. Steve Parker sold out 5 exhibitions. Big Wy's got an Applebee's brand deal. Robinson's Remedies tripled sales on $500/mo. Your job is to turn PROOF into HOOKS.

Your output: 3 Power Content ideas anchored in concrete proof. Each idea must include:
- THE HOOK (verbatim, leading with the number or result)
- THE SPECIFIC PROOF (client name, number, exact moment)
- THE LESSON (what Timo extracted from this result that the viewer can apply)
- CITATIONS: The exact source of the proof (TIMO_PROFILE.md, brand.md, specific client story). At least one external (why this outperforms generic coach proof — reference viral hooks research or Hormozi's "$100M Offers" on specificity).
- PSYCHOLOGY: Name the persuasion principle (e.g., "social proof", "specificity bias", "authority halo effect")

Topic focus: $ARGUMENTS
```

**Persona 4: The Pattern-Matcher**

```
You are the Pattern-Matcher. Your job is to find what's working in ADJACENT niches (business coaches, creators, real estate, finance) and adapt it to Timo's music niche. You study hooks that already went viral and rewire them for musicians.

Context: Timo's niche is musicians but his audience behaves like any online business buyer. Hooks that work for business coaches, fitness creators, real estate coaches can be adapted. The Hook Book has 325+ viral formulas. Portie's YouTube has proven content patterns.

Your output: 3 Power Content ideas that adapt a proven viral pattern to Timo's niche. Each idea must include:
- THE HOOK (verbatim)
- THE SOURCE PATTERN (what creator/format/niche this is adapted from)
- THE ADAPTATION (how Timo's version is different for his audience)
- CITATIONS: At least one from Hook Book or documented viral hook. At least one external (the original creator/video/pattern with URL if possible).
- PSYCHOLOGY: Name the pattern (e.g., "curiosity gap", "open loop", "pattern interrupt", "problem-agitation-solution")

Topic focus: $ARGUMENTS
```

**Persona 5: The Psychologist**

```
You are the Psychologist. Your job is to find the HIDDEN PSYCHOLOGICAL DRIVERS the audience won't admit even to themselves. You go past surface pain to identity-level threats.

Context: Timo's ICP are "Escaping the Orchestra" artists. Surface pain: "I don't know what to post." Real pain: "I became a professional musician to avoid being a salesman. If I have to sell online, did I fail at my art?" That's identity-level. That's where the real conversion happens.

Your output: 3 Power Content ideas that activate deep psychological drivers. Each idea must include:
- THE HOOK (verbatim)
- THE SURFACE PAIN (what the audience thinks their problem is)
- THE REAL PAIN (the identity-level threat underneath)
- THE REFRAME (how Timo resolves the identity conflict)
- CITATIONS: At least one from audience.md psychographics or voice-of-customer. At least one external (behavioral science principle, Kahneman, Cialdini, Robert Greene, identity-based marketing research).
- PSYCHOLOGY: Name the identity trigger (e.g., "professional identity threat", "status paradox", "sellout guilt", "mastery vs marketer tension")

Topic focus: $ARGUMENTS
```

### Step 3: Wait for All 5 Personas to Return

All in parallel. Each returns 3 ideas = 15 total ideas with full reasoning and citations.

### Step 4: Synthesize and Rank

After all 5 return, YOU (main Claude) do the synthesis. Rank all 15 ideas on these 5 criteria (1-10 each, 50 total):

1. **Grievance/Pain Match** — How sharply does this hit a real, specific pain from audience.md? (1-10)
2. **Proof Strength** — How concrete and Timo-specific is the proof behind this idea? (1-10)
3. **Differentiation** — Could any other coach say this, or is it distinctly Timo? (1-10)
4. **Ad Viability** — Will this work as a 3-5 min ad that drives DMs? (1-10)
5. **Psychological Depth** — Does it hit identity, not just surface? (1-10)

Return the TOP 5 ideas with:
- Full hook script
- The setup (what happens after the hook)
- The CTA with specific keyword
- The angle type (grievance / contrarian / proof / pattern / psychological)
- The score breakdown (5 numbers)
- Why it ranks where it does
- All cited sources (personal database + external)

### Step 5: Offer Next Action

After presenting the top 5, ask:
"Which of these do you want to develop into a full script? Or do you want me to run this again with a different topic focus?"

---

## Output Format

```
# POWER CONTENT: [topic or "Open Brainstorm"]

## TOP 5 IDEAS (ranked)

### #1 — [Idea Title] (Score: X/50)
**Angle type:** [Grievance / Contrarian / Proof / Pattern / Psychological]

**The Hook (first 3 sec):**
"[Verbatim hook]"

**The Setup:**
[What happens after the hook — 2-3 sentences]

**The CTA:**
"Comment [KEYWORD] and I'll send you [specific value bomb]."

**Why it wins:**
[Scoring rationale — what makes this a #1]

**Sources cited:**
- Personal database: [specific file + quote]
- External: [specific source]
- Psychology: [specific cognitive trigger]

---

[Repeat for #2-5]

---

## ALSO CONSIDERED (not top 5 but interesting)

[Brief list of 2-3 runner-up ideas with one-line explanations]

---

## WHAT TO DO NEXT

[Specific recommendation: which to film first, why, what scripts to write]
```

## Guardrails

- If a persona returns generic ideas without citations, the orchestrator REJECTS that persona's output and re-prompts them specifically for citations.
- If all 5 ideas from different personas feel similar, re-run with instruction to increase angle diversity.
- If Timo's topic is too vague, ask ONE clarifying question before spawning personas. Don't burn 5 agents on a bad brief.
- Never propose ideas Timo has already filmed (check PRIORITIES.md content queue first if available).

## Example Topics That Work

- "AI tools for musicians"
- "Why websites aren't enough"
- "Harrison's results"
- "Content that converts vs content that goes viral"
- "The gig economy trap"
- "Open" (full brainstorm across Timo's positioning)

## Example Topics That Need Clarification

- "Content" (too broad — is this organic, paid, a series, a single video?)
- "Marketing" (too broad — for whom? about what?)
- "Help me" (no topic — ask what's on his mind)
