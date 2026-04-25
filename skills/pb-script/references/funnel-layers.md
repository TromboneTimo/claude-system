# Funnel Layer Framework

Every Precision Brass content idea or script is generated for a specific funnel layer. The layer dictates:
- Pain-point depth (how raw the wounds get)
- Identity load (how much grief/shame/age-anxiety surfaces)
- CTA destination (next video vs strategy session content vs strategy call)
- Structural template (light TOFU hook vs full 12-move BOFU converter)

Always ask the user for the layer BEFORE drafting. Default to MOFU if they don't specify, and label the default explicitly.

## TOFU. Top of Funnel

**Audience state:** Problem-unaware or just starting to research. Casually browsing trumpet content. May not even identify as "comeback player" yet.

**Pain-point depth:** Light. Surface frustrations only ("I want better range", "high notes are hard"). Avoid surgical naming of identity wounds.

**Hook style:** Curiosity-driven. Visual gag. Universal pain. No comeback/age callout.

**Identity load:** Low. The video is about a topic, not about who the viewer becomes.

**Funnel CTA:** Subscribe. Watch another video on the channel. Stay in the ecosystem.

**Structural template:** Lighter than the 12-move converter. 5-7 beats max. Demo + explanation + curiosity gap + subscribe.

**Examples in the existing system:**
- The "$0 vs $7,200 Trumpet" video skews TOFU (broad gear question, light identity).
- A "Top 5 Trumpet Mistakes" round-up would be TOFU.

**Triggers to USE (from conversion-triggers.md):**
- T1 partial (name a generic problem, not the deepest wound)
- T3 (demonstration that contradicts conventional wisdom)
- T7 (isolation. comeback players feeling alone)

**Triggers to AVOID:**
- T4 (identity restoration. too heavy for TOFU)
- T6 (age frame broken. too specific for TOFU)
- T8 (permission to want it. too emotional for TOFU)

## MOFU. Middle of Funnel

**Audience state:** Knows they have a problem, exploring solutions. Watching multiple videos on the same topic. Has started to identify with the "comeback player" or "stuck for 20 years" framing.

**Pain-point depth:** Specific. Name the mistakes by name (Mouthpiece Reset, Pressure Mash). Reference dead methods (Caruso, Stamp). Use comeback/age callout in the hook.

**Hook style:** Pain hook + comeback/age callout + diagnostic promise. "If you've spent $500 on mouthpieces in the last five years..."

**Identity load:** Medium. The video reframes the viewer ("you're not a gear chaser, you were given the wrong manual"). Identity outcome promised but not the deepest wound.

**Funnel CTA:** Watch the next-deeper video. Drive into BOFU content. The mouthpieces video and the embouchure video are MOFU-to-BOFU bridges.

**Structural template:** The 7-beat interleaved template (Cold Open + Demo + Apparatus Reveal + 3 Mistakes + Funnel) is MOFU's home.

**Examples in the existing system:**
- "Stop Buying Mouthpieces" is MOFU. Names mistakes, gives diagnoses, points to deeper video.

**Triggers to USE:**
- T1 (someone finally named what's wrong)
- T2 (failed methods named)
- T3 (demonstration that contradicts)
- T5 (permission to stop chasing equipment)
- T6 (age frame partially broken)

**Triggers to AVOID:**
- T4 maximum-depth (save full identity restoration for BOFU)
- T8 (save permission-to-want for BOFU)

## BOFU. Bottom of Funnel

**Audience state:** Solution-aware, evaluating providers. Has watched multiple Harrison videos. Self-identifies as the ICP. Considering booking a strategy call.

**Pain-point depth:** Surgical. Name the deepest wounds: comeback grief ("the player you thought you'd be by now"), age anxiety ("am I too old, has my body closed the door"), failed-method shame ("I tried Caruso for 20 years and still couldn't"), isolation ("I haven't had a teacher in 30 years").

**Hook style:** Identity-loaded. Speaks directly to the wound. "If you came back to trumpet after 30 years and you can't get back what you had at 22..."

**Identity load:** Maximum. Sells reclamation of self, not just technique. Uses the converter's "the way we do everything is the way we do anything" identity layer.

**Funnel CTA:** Strategy call. Free consultation. Direct booking link.

**Structural template:** The full 12-move converter template (`project_proven_converter_template.md`). Cold open + universal pain + collapse to one root cause + credibility + invisible problem + anti-conventional + proprietary terminology + name-drop legends + demonstration + identity layer + specific consequences + step recap + cliffhanger.

**Examples in the existing system:**
- The $36K embouchure video (O4a-q93ENAg) is BOFU. Hits 12 of 12 moves. Direct to strategy session.

**Triggers to USE:**
- ALL T1-T8. BOFU is where every trigger fires at maximum.
- Especially T4 (identity restoration), T6 (age frame broken), T8 (permission to want it).

## Decision tree for ambiguous cases

If Timo says "I don't know" or "all of them":
1. Ask: "Is the audience already searching for fixes, or just curious about trumpet content?"
2. If searching for fixes → MOFU. If just curious → TOFU. If they're already evaluating Harrison's specific approach → BOFU.
3. Default = MOFU when in doubt. Label the assumption and ship.

## Output labeling

Every idea in the 5-idea menu must carry a layer label. Format:

```
## Idea 1: [Title]
**Layer:** TOFU | MOFU | BOFU
**Anchor:** YT-WINNER-PATTERN | FB-WINNER-PATTERN | LENS-NAME
... (rest of the idea card)
```

If the menu is generated for a single layer (Timo specified one), all 5 ideas should be that layer. If Timo says "give me a mix across layers", spread the ideas (e.g., 2 TOFU, 2 MOFU, 1 BOFU) and label each.

## Cross-skill effect

The funnel layer flows through to `pb-script-write` (Phase 2). When generating the script, pb-script-write reads the layer and adapts:
- Pain depth in the trap topics
- Identity load in the script
- Funnel CTA destination
- Structural template (12-move BOFU vs 7-beat MOFU vs lighter TOFU)
