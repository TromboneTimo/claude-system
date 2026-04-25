---
name: pb-script
description: Phase 1 of Harrison Ball's Precision Brass YouTube content engine. Research-driven idea generator that spawns parallel subagents to read deeply across the full voice-of-customer corpus (sales calls, testimonials, YouTube winners database, Facebook winning-ads database, lost-deal voice, objection library, deep psychological dive, persona files, quote banks) and returns 5 conversion-trigger-driven content ideas with verbatim quote evidence. 1-2 ideas anchored on the proven verified-winner pattern (YouTube winners + FB winning ads), 3-4 ideas surfaced from other sources for variety. Use this skill whenever Timo or Harrison asks for content ideas, video ideas, what to film next, what Harrison should make, "give me angles", "youtube ideas for harrison", "next video for harrison", "precision brass content ideas", "/pb-script", or any variation. Also fire when the user mentions Harrison and content/video/script in the same breath. Do NOT generate the script itself. That is Phase 2 and lives in a future companion skill. This skill stops at the 5-idea menu and waits for Timo to pick one.
---

# pb-script. Phase 1: Conversion-Trigger Idea Generator

## What this does

Generate 5 YouTube content ideas for Harrison Ball that are anchored in **what verifiably caused his prospects to buy**. Not generic trumpet advice. Not what's trending. Ideas backed by the actual language, fears, identity arcs, and conversion triggers found in Precision Brass's voice-of-customer corpus.

This is a **research-first skill**. Every invocation re-reads raw sources. No caching. No relying on synthesized summaries alone. Fresh perspectives every time.

## The 5-idea structure (NON-NEGOTIABLE)

The output mix must be:
- **1-2 ideas anchored on VERIFIED WINNERS**, pattern-matched against `youtube-database/` (status=winner videos) AND `facebook-ads-database/` (status=winner ads). Both are proven-conversion sources. Either one (or a synthesis of both) qualifies an idea for the anchor slot.
- **3-4 ideas from variety lenses**, surfaced from sales calls, lost-deal voice, objection library, deep psychological dive, comments, won-deal voice, testimonials

This split exists for a reason. Pure winner-cloning makes the channel narrow. Pure variety ignores what's actually proven to convert. The mix gives Timo a couple safe-bet angles plus fresh territory.

**Empty-database handling:** If either winner database has zero entries (or no status=winner items), Agent A reads only the populated one. If BOTH are empty, Agent A returns "no verified-winner data yet" and the synthesizer pulls all 5 ideas from the variety lenses (Agents B/C/D/E). Note this in the output so Timo knows the anchor slot was skipped.

## How it works (workflow)

### Step 0. Ask the funnel layer FIRST (before any research)

**Mandatory intake question.** Before spawning any research agents, ask Timo:

> "What funnel layer is this for? **TOFU** (broad reach, problem-unaware audience), **MOFU** (problem-aware, exploring solutions), or **BOFU** (solution-aware, evaluating providers ready to book)?"

Wait for an explicit answer. The funnel layer determines:
- How deep the pain points get named (TOFU light, BOFU surgical)
- What identity wounds surface (TOFU broad curiosity, BOFU comeback grief / age anxiety / failed-method shame)
- What the funnel CTA points to (TOFU another video, MOFU strategy session content, BOFU strategy call)
- Whether to use the proven 12-move converter template (BOFU only) or a lighter structure (TOFU/MOFU)

See `references/funnel-layers.md` for the full spec.

If Timo doesn't answer or says "all of them", default to MOFU and label it. Don't skip the question.

### Step 1. Acknowledge, then research

Tell Timo: "Layer locked: [TOFU/MOFU/BOFU]. Spawning 5 research agents across the corpus. ~2-3 minutes." Then spawn the 5 subagents below **in parallel in a single message** (multiple Agent tool calls in one turn). Inject the funnel layer into each agent's prompt so they tune their pain-point depth accordingly.

### Step 2. Spawn 5 parallel research subagents

All 5 are `general-purpose` subagents. They read raw files directly, return findings to the main thread.

#### Agent A. Verified Winner Deconstruction (THE ANCHOR)

This agent reads BOTH proven-conversion sources: YouTube winners and Facebook winning ads. They are different formats but same signal: stuff that actually converted.

Prompt:
```
You are researching what verifiably converts for Harrison Ball's Precision Brass business across two channels: YouTube long-form and Facebook ads.

PART 1. YouTube winners
READ EVERY VIDEO in /Users/air/Desktop/Precision-Brass/youtube-database/ that is marked status=winner in index.json. For each winner, read:
- analysis.md (what made it work)
- transcript.md (full script content)
- comments-top.md (what viewers said that proved emotional resonance)
- metadata.json (view count, sales attribution, dates)

If the YouTube winners list is empty, note that and continue to Part 2.

PART 2. Facebook winning ads
READ EVERY AD in /Users/air/Desktop/Precision-Brass/facebook-ads-database/ that is marked status=winner in index.json. For each winner, read:
- analysis.md (why it worked)
- creative/copy.md (primary text, headline, CTA)
- performance.json (spend, ROAS, CPA, sales attributed)
- comments-top.md if present (audience reaction)
- metadata.json (audience targeting, dates)

If the FB winners list is empty, note that and continue.

PART 3. Reference materials (always read)
- /Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md
- /Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/project_proven_converter_template.md (the 12-move converter template)

PART 4. Extract the cross-channel PATTERN
What hook structure works in BOTH long-form video AND short-form ad copy? What identity arc? What pain-to-payoff bridge? What words and phrases recur across winners (these are the highest-signal language)? What demonstration style proves the claim?

Note that ads are short and videos are long, so structural elements differ. Look for what's COMMON: the emotional triggers, the identity framing, the language register, the pain points named, the proof-style.

PART 5. Propose 3 NEW video ideas that would match this verified-winner pattern, each one targeting a different specific pain point. Each idea must:
- Map to either YT-WINNER-PATTERN, FB-WINNER-PATTERN, or CROSS-WINNER-PATTERN (specify which) and explain how the new idea inherits its structure
- Pass the ICP checklist (40-65, US, comeback player, business owner, addresses range/endurance/mouthpiece/age/comeback)
- Cite at least 2 verbatim quotes (from comments, transcripts, ad copy, or ad comments) proving emotional resonance
- Name the limiting belief it shatters (Domino Effect Framework, one belief per video)
- Sell identity, not technique

EMPTY-DATABASE handling: if both YT winners AND FB winners are empty, return: "No verified-winner data yet. Skip the anchor slot, pull all 5 ideas from variety lenses." Do NOT make up patterns. Do NOT propose anchored ideas without source data.

Return: which databases had data, pattern summary (200 words across both channels), then 3 candidate ideas with the structure above.
```

#### Agent B. Won-Deal Conversion Patterns

Prompt:
```
You are researching WHY Harrison Ball's customers bought Precision Brass coaching.

Read these files completely:
- /Users/air/Desktop/Precision-Brass/voc/personas/won-deals-voice-bank.md
- /Users/air/Desktop/Precision-Brass/voc/quotes/won-deals-quotes.jsonl
- /Users/air/Desktop/Precision-Brass/voc/quotes/sales-call-outcomes.jsonl
- /Users/air/Desktop/Precision-Brass/voc/raw/testimonials/ (read every testimonial file)

Your job: identify the SPECIFIC moments, phrases, realizations, and demonstrations that flipped someone from interested to buying. Look for:
- The exact frustration they were stuck on before Harrison
- The "aha" moment they describe
- The identity shift they articulate after working with him
- Words/phrases that repeat across multiple converters (high-frequency = high-resonance)

Then propose 3 video ideas that would activate those same conversion triggers in NEW prospects who haven't bought yet. Each idea must:
- Pass the ICP checklist (40-65, US, comeback, business owner, specific pain)
- Cite at least 3 verbatim quotes from converters
- Identify the conversion trigger it activates by name
- Sell identity, not technique

Return: trigger inventory (top 5 triggers ranked by frequency), then 3 candidate ideas.
```

#### Agent C. Lost-Deal Pain & Objection Surfacing

Prompt:
```
You are researching what stops Harrison Ball's prospects from buying, and what video content could break that resistance.

Read these files completely:
- /Users/air/Desktop/Precision-Brass/voc/personas/lost-deals-voice-bank.md
- /Users/air/Desktop/Precision-Brass/voc/personas/objection-library.md
- /Users/air/Desktop/Precision-Brass/voc/quotes/lost-deals-quotes.jsonl

Your job: identify the top objections, hesitations, and pain points that made prospects walk away. Then think: what kind of video would dissolve that objection BEFORE the sales call?

Look for:
- Failed-method history ("I've tried X for 20 years")
- Identity threats ("I'm too old", "It's too late", "I'll never get range back")
- Skepticism patterns ("how is this different from...")
- Price/commitment fears
- Specific technical fears (embouchure damage, mouthpiece swap fear, etc.)

Then propose 3 video ideas. Each idea must:
- Address one specific objection head-on (name it)
- Pass the ICP checklist
- Cite at least 2 verbatim quotes from lost deals
- Use the "name the invisible problem" approach
- Sell identity, not technique

Return: top 5 objections ranked, then 3 candidate ideas.
```

#### Agent D. Comments + Deep Psychological Dive

Prompt:
```
You are researching the deep psychological wiring of Harrison Ball's audience.

Read these files completely:
- /Users/air/Desktop/Precision-Brass/voc/personas/comments-voice-bank.md
- /Users/air/Desktop/Precision-Brass/voc/quotes/comments-quotes.jsonl
- /Users/air/Desktop/Precision-Brass/voc/raw/research/2026-04-21_deep-psychological-dive_harrisson-ball_19-prospects.md
- /Users/air/Desktop/Precision-Brass/context/prospect-psychology.md

Your job: identify the unspoken fears, secret aspirations, identity wounds, and emotional through-lines that show up across the 19 prospect deep-dives and the public commenter base.

Look for:
- Identity wounds ("I used to be good", grief over lost ability, comparison to past self)
- Isolation patterns (no teacher, no community, embarrassment about asking)
- Dental/age/physical anxieties they don't say out loud in public
- Secret hopes (return to first chair, play with grandkids, prove something to former teacher, recover what they lost)
- Curiosity-loop hooks (what they ALMOST understood but couldn't name)

Then propose 3 video ideas that name an invisible emotional truth Harrison's audience already feels but doesn't say. Each idea must:
- Pass the ICP checklist
- Cite at least 3 verbatim quotes
- Name the specific emotional truth being surfaced
- Sell identity, not technique
- Pass the "would someone OUTSIDE the ICP want this?" test (if yes, reject)

Return: top 5 emotional through-lines, then 3 candidate ideas.
```

#### Agent E. Rotating Bonus Lens (FRESHNESS SLOT)

Pick ONE lens at random from the list below using `python3 -c 'import random; print(random.choice(["dental-trigger", "isolation-pattern", "failed-method-grief", "identity-aspiration", "age-anxiety", "mouthpiece-rabbit-hole", "comeback-player-arc", "section-leader-redemption"]))'` (run this in a Bash call before spawning the agent so the lens is selected fresh each invocation).

Then spawn this agent with the chosen lens injected:

```
You are researching the [LENS_NAME] angle for Harrison Ball's content.

Read across these files for traces of this specific theme:
- /Users/air/Desktop/Precision-Brass/voc/quotes/all-quotes.jsonl
- /Users/air/Desktop/Precision-Brass/voc/raw/sales-calls/ (sample 8-10 random calls)
- /Users/air/Desktop/Precision-Brass/voc/raw/email-sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md
- /Users/air/Desktop/Precision-Brass/voc/personas/harrison-email-voice.md
- /Users/air/Desktop/Precision-Brass/context/harrison-profile.md
- /Users/air/Desktop/Precision-Brass/context/content-sop.md

Your job: find the most NON-OBVIOUS angle on this lens. Not what Harrison already says publicly. Something the data shows is loaded with emotion but Harrison hasn't directly addressed in a video yet.

Propose 2 video ideas through this lens. Each idea must:
- Pass the ICP checklist
- Cite at least 2 verbatim quotes
- Be something Harrison has NOT already covered (cross-check against youtube-database/index.json topic_tags)
- Sell identity, not technique

Return: lens insight (150 words on what's underneath this theme), then 2 candidate ideas.
```

### Step 3. Synthesize the 5

When all 5 agents return, do not just concatenate their outputs. Synthesize:

1. **Pool all candidate ideas** (you'll have ~13: 3+3+3+3+2 minus duplicates).
2. **Enforce the mix**: pick 1-2 from Agent A's pool (the YouTube-winner-anchored ones), and 3-4 from B/C/D/E pools combined. Total = 5.
3. **Apply the ICP checklist** (see `references/icp-checklist.md`) to every survivor. If an idea fails any check, replace it.
4. **Apply the Domino check**: each idea must shatter exactly ONE limiting belief. If an idea is too broad (covers 3 beliefs), narrow it or drop it.
5. **Apply the identity check**: every idea must promise an identity outcome (who they become), not a technique outcome (what they learn).
6. **Apply the freshness check**: cross-reference against `youtube-database/index.json` topic_tags. If an idea overlaps heavily with already-published content, flag it as "refresh" or replace.
7. **Diversify**: of the final 5, no two ideas should target the same conversion trigger. If two collapse onto the same trigger, swap one out.

### Step 4. Output the menu

Use the exact template in `references/output-template.md`. Each idea includes:
- Title and 3 alternate title variations
- Anchor source (yt-winner-pattern OR lens name)
- Conversion trigger activated
- Limiting belief shattered
- Identity outcome promised
- ICP segment targeted
- 2-3 verbatim quote citations with source files
- Hook angle (money / problem / curiosity)
- Why this converts (3-sentence rationale)

End with: "Which one do you want to develop into a script? Reply with the number." Phase 2 (script generation) lives in the companion skill `pb-script-write`, which auto-fires the moment Timo replies with a selection ("idea N", "go with #N", "the mouthpiece one", etc.). Do NOT manually continue into script writing inside this skill. Hand off to pb-script-write.

## Hard rules (do not break)

1. **No script generation in this skill.** Phase 1 stops at the menu. If Timo asks for the script in the same turn, say: "Picking the angle first locks in the visual plan. Which of the 5 wins?"

2. **No fabricated quotes.** Every quote must be traceable to a real file in the corpus. Cite the source file path. If you can't find a real quote for an idea, weaken the idea or drop it. Auto-transcripts can lie. When uncertain, say so rather than invent.

3. **ICP checklist runs on every idea.** See `references/icp-checklist.md`. No exceptions.

4. **Hard-block generic ideas.** If an idea would also make sense for a Berklee jazz student or a high-school marching band kid, it's too generic for Harrison's ICP. Reject and replace.

5. **Identity over technique.** "How to play high G" is a technique frame. "Reclaim the range you had at 25, without re-learning trumpet" is an identity frame. Always identity.

6. **Read the actual files. Don't synthesize from memory.** Each invocation, the agents must open and read the raw sources fresh. Do not let the synthesizer skip the agent step and just write 5 ideas from prior knowledge.

7. **Never let Harrison film without script approval.** When presenting the menu, end with the standard reminder: "Once you pick one, I'll generate the full script and visual plan. Send to Timo for review before filming."

## Reference files

- `references/icp-checklist.md`. The 5-question ICP gate
- `references/output-template.md`. Exact format for the 5-idea menu
- `references/conversion-triggers.md`. Taxonomy of triggers found in the corpus (read this before synthesizing)
- `references/proven-template-pointer.md`. Where the 12-move converter template lives and how to apply it
- `references/example-mouthpieces-script.md`. The proven 7-beat interleaved script structure (Phase 2 reference. READ when generating any new script)
- `references/script-writing-protocol.md`. Phase 2 ruleset. failure modes to avoid + voice fingerprint + funnel pattern. READ before drafting any script
- `references/funnel-layers.md`. TOFU/MOFU/BOFU layer spec. READ in Step 0 to inform research depth and idea framing

## What this skill is NOT

- Not a script generator (that's Phase 2)
- Not a thumbnail tool
- Not a title-only generator (titles come WITH evidence and structure, not in isolation)
- Not for short-form (HARD RULE: project CLAUDE.md blocks short-form creation; long-form first, always)
- Not for non-Harrison content (Robinson's Remedies, Creator Conservatory, etc. have their own skills)