---
name: power-content
description: >
  Generates Power Content ideas for Creator Conservatory by spawning one persona
  per ICP segment (music coaches, business owners, AI lovers, view-rich musicians,
  etc.). Default mode is ICP-FIRST, not angle-first. Each persona MUST cite sources
  from both Timo's personal database (audience.md, brand.md, TIMO_PROFILE.md,
  voice bank, Hook Book, client results) AND external sources (Portie framework,
  Hormozi, behavioral science). Supports secondary angle filters (grievance,
  contrarian, proof, psychological, pattern). Use when Timo says "power content",
  "content ideas", "ad ideas", "value bomb ideas", or "/power-content [topic]".
user-invokable: true
argument-hint: "[topic] OR 'per-icp' OR 'icp:music-coach' OR 'angle:grievance'"
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

Multi-persona system that generates ranked Power Content ideas for Creator Conservatory. Default output is ONE idea per ICP SEGMENT, not angle variations on one topic.

## CRITICAL LESSON (2026-04-12)

Timo's audience is NOT monolithic. It spans 4+ distinct ICP segments, each with different psychology, different proof needs, different hooks:

1. **Music Coaches** (Harrison-tier): status threat, hack coaches outselling them
2. **Business Owners** (non-music): agency betrayal, in-house overwhelm, trust issues
3. **AI Lovers**: identity-output dissonance, "early adopter" self-concept gap
4. **View-Rich Cash-Poor Musicians**: monetization shame, free-content-as-identity trap
5. **Escaping the Orchestra Artists**: sellout guilt, orchestra handcuffs, perfectionism

When Timo says "5 power content ideas" the default is FIVE DIFFERENT ICPs, not five angle variations on one topic. Do not invert this.

## When to Use

- Timo needs Power Content ad ideas
- Timo is stuck on what to film
- A new client result/insight should be turned into content
- Session ends with "what should I post this week"
- Timo says "/power-content [topic]" or "power content ideas"

## Mode Selection (Ask If Unclear)

Before spawning personas, determine mode from Timo's request:

**Mode A: Per-ICP (DEFAULT)**
- Trigger: "power content ideas", "what should I film", no topic specified, or explicit ICP mention
- Spawns 4-5 personas, ONE PER ICP SEGMENT
- Each persona returns ONE fully-developed idea targeted at their specific ICP
- Output: 4-5 ideas, each hitting a different audience

**Mode B: Topic Deep-Dive**
- Trigger: Specific topic mentioned ("/power-content the designer angle", "/power-content Harrison's results")
- Spawns 5 angle-type personas (Grievance, Contrarian, Proof, Pattern, Psychological)
- All 5 personas work on the SAME topic
- Output: 15 ideas on one topic, ranked to top 5
- ONLY use this mode when Timo explicitly wants depth on one topic

**Mode C: Hybrid**
- Trigger: "ideas for music coaches specifically" (ICP + topic implied)
- Spawns 3-5 angle personas constrained to ONE specific ICP
- Output: Multiple angles on one ICP

**If ambiguous, ask ONE clarifying question:** "Do you want one idea per ICP (default) or multiple angles on one topic?"

## Non-Negotiables

1. **Every idea must cite at least 2 sources.** One from Timo's personal database. One external (web research, Portie framework, adjacent niche example, behavioral science).
2. **No generic ideas.** If the idea could work for any coach, it's rejected. Must be specific to Timo's positioning.
3. **ICP-specific language, psychology, and proof.** A music coach idea should not feel interchangeable with a business owner idea. Different pain triggers, different proof points, different reframes.
4. **Proof or skip.** Every idea must have a concrete proof point Timo can reference (client name, number, specific moment).
5. **Psychology-first.** Every idea must name the cognitive bias, pain trigger, or identity threat it activates.

## Context Files (Read Before Spawning)

**Always read:**
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/audience.md` — ICP tiers, voice of customer, psychographics
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/brand.md` — Positioning, proof points, messaging pillars
- `/Users/air/Desktop/Timo LLC/creator-conservatory/TIMO_PROFILE.md` — Client list, results, businesses
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/offers.md` — Offer hierarchy

**Read if exists:**
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/LAUREL_PORTIE_DATABASE.md` or `references/laurel-portie-framework.md`
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/competitors.md`
- `/Users/air/Desktop/Timo LLC/creator-conservatory/context/skool-community-intelligence.md`

## MODE A: Per-ICP Personas (DEFAULT)

Spawn 4-5 agents in parallel, ONE per ICP segment. Each returns ONE fully-developed idea.

### Persona: Music Coach Specialist

```
You are generating ONE Power Content idea for Creator Conservatory targeted specifically at MUSIC COACHES.

TARGET ICP: Music Coaches
- Already have online coaching program
- Many run Facebook ads ($500-$5K/mo typical)
- Revenue: $5K-$50K/mo
- Harrison Ball is the ceiling example (Precision Brass, $50K/mo, 100% close rate)
- Pain: Paid ads inconsistent. Organic is weak. Best competitors outsell them despite being worse teachers.
- Identity: "I'm world-class but can't beat hack coaches with half my expertise."

Topic focus: $ARGUMENTS (or "open" if no topic)

Return ONE idea with: HOOK / SURFACE PAIN / REAL PAIN / REFRAME / SETUP / CTA / CITATIONS (internal + external) / PSYCHOLOGY.
```

### Persona: Business Owner Specialist

```
You are generating ONE Power Content idea for Creator Conservatory targeted specifically at BUSINESS OWNERS (non-musician).

TARGET ICP: Business Owners
- Small-to-mid business owners: e-commerce, local service, consultants, agency owners, SaaS founders
- Revenue: $10K-$250K/mo
- Stuck in traps: paying agency $3-10K/mo for mediocre output, drowning doing it themselves, or hiring a VA who produces generic crap
- Pain: Want results without becoming a marketing operator. Know AI can do it but can't figure out how.
- Proof arsenal: Robinson's Remedies tripled sales on $500/mo. Dallas Symphony 500% case study.
- Identity: "I'm a business operator, not a marketer. But every agency I've hired has burned me."

Topic focus: $ARGUMENTS

Return ONE idea with full structure.
```

### Persona: AI Lover Specialist

```
You are generating ONE Power Content idea for Creator Conservatory targeted at AI LOVERS.

TARGET ICP: AI Lovers
- Tech-curious entrepreneurs, creators, knowledge workers
- Use ChatGPT/Claude daily but workflow is 90% prompt-hacking, not production systems
- Follow Karpathy, Matt Berman, Every.to
- Know Claude Code, MCP, Cursor but treat as toys
- Pain: Impressed by demos, haven't built a single revenue-generating system
- Proof arsenal: /power-content skill, Hook Book, client AI systems (Harrison, Sohee, Wilhelm), Robinson's Remedies runs on AI
- Identity: "I'm an early adopter. Why am I still typing into a chat window?"

Topic focus: $ARGUMENTS

Return ONE idea with full structure.
```

### Persona: View-Rich Cash-Poor Musician

```
You are generating ONE Power Content idea for Creator Conservatory targeted at MUSICIANS WITH STRONG FOLLOWINGS NOT MONETIZING.

TARGET ICP: View-Rich Cash-Poor Musicians
- 10K-500K+ followers on IG/TikTok/YouTube
- Get views, sometimes millions. Engagement looks great.
- BUT: no email list, no offer, no funnel. AdSense mediocre. Brand deals infrequent.
- Pain: Friends/family think they "made it." They know the checks aren't there.
- Identity: "I built this audience but it's not paying me. I'm pretending."
- Timo IS this ICP in Trombone Timo (1B views, 1M followers, $8.5K/mo AdSense)
- Proof arsenal: Big Wy's (5M views to Applebee's deal), Victor (30K views to $3K program), Steve Parker (500K views to sold-out exhibitions)

Topic focus: $ARGUMENTS

Return ONE idea with full structure.
```

### Persona: Escaping the Orchestra Artist (Primary ICP)

```
You are generating ONE Power Content idea for Creator Conservatory targeted at ESCAPING THE ORCHESTRA ARTISTS.

TARGET ICP: Primary CC ICP from audience.md
- Professional musicians feeling trapped by "orchestra handcuffs" / "gig economy rat race"
- World-class skills but zero digital footprint
- Perfectionism stops them from posting
- Already have a product but no audience to sell to
- Voice of customer: "pain in the ass", "labor-intensive", "milk toast", "I'm not an influencer", "this diminishes my art"
- Identity: "I became a musician to avoid being a salesman. If I have to sell online, did I fail?"

Topic focus: $ARGUMENTS

Return ONE idea with full structure.
```

## MODE B: Topic Deep-Dive (5 Angle Personas)

Only use when Timo explicitly wants depth on one topic. Spawns these 5:

1. **Grievance Hunter** — Finds what the ICP is ANGRY about. Grievance-based hooks validate existing feelings.
2. **Contrarian Insight Generator** — Flips common beliefs. "Everyone says X but actually Y."
3. **Proof Stacker** — Anchors every idea in a specific, citable result.
4. **Pattern-Matcher** — Adapts viral patterns from adjacent niches.
5. **Psychologist** — Goes past surface pain to identity-level threats.

Each returns 3 ideas = 15 total. Synthesizer ranks to top 5.

## Scoring (Mode B only)

Score each idea 1-10 on:
1. Grievance/Pain Match (how sharply it hits specific pain)
2. Proof Strength (how concrete/Timo-specific)
3. Differentiation (uniquely Timo, not generic)
4. Ad Viability (works as 3-5 min ad driving DMs)
5. Psychological Depth (identity-level, not surface)

## Output Format (Mode A - Default)

```
# POWER CONTENT IDEAS BY ICP

## #1 — MUSIC COACHES: [Title]
**Hook:** "[verbatim]"
**Surface Pain / Real Pain / Reframe:** [3-4 sentences each]
**Setup:** [body copy]
**CTA:** "Comment [KEYWORD] and I'll send you [specific]."
**Proof:** [client result or Timo proof]
**Psychology:** [named trigger]
**Sources:** [internal + external]

## #2 — BUSINESS OWNERS: [Title]
[same structure]

## #3 — AI LOVERS: [Title]
[same structure]

## #4 — VIEW-RICH MUSICIANS: [Title]
[same structure]

## #5 — ESCAPING THE ORCHESTRA: [Title]
[same structure]

---

## WHAT TO DO NEXT
Which ICP do you want to film first? Which proof point is strongest this week?
```

## Guardrails

- **NEVER spawn 5 angle personas on one topic when Timo says "5 ideas" without specifying a topic.** Default is ICP-first.
- If a persona returns a generic idea without ICP-specific citations, REJECT and re-prompt.
- If two ICPs get similar ideas, re-run and force differentiation.
- If Timo's request is ambiguous, ask ONE clarifying question: "Per-ICP (default) or topic deep-dive?"
- NEVER default to website/designer angle across all ICPs. Each ICP has different pain.

## Example Invocations

**Per-ICP (Mode A):**
- "power content ideas"
- "5 ideas for this week"
- "/power-content" (no args)

**Topic deep-dive (Mode B):**
- "/power-content the designer angle"
- "deep dive on Harrison's result as content"
- "5 angles on the $47/mo library"

**Hybrid (Mode C):**
- "3 ideas just for music coaches"
- "multiple angles on AI for business owners"

## Sources Required Per Idea

Every idea MUST cite:

**Internal (Timo's database):**
- Direct quote from audience.md, brand.md, TIMO_PROFILE.md, OR a specific client result
- Must match the ICP being targeted (don't cite a music coach result for a business owner idea)

**External:**
- Portie framework principle (from LAUREL_PORTIE_DATABASE.md or laurel-portie-framework.md)
- OR Hormozi framework ($100M Offers, $100M Leads)
- OR behavioral science (Cialdini, Kahneman, Greene, Schwartz, Dweck)
- OR documented viral pattern with URL

No citations = rejected output.
