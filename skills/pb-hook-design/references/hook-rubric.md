# Hook scoring rubric (6 criteria, 10 points each, 60 total)

Used by the 4 parallel ranking agents in pb-hook-design Step 1. Each agent scores every video in its batch against these 6 criteria, then picks its top 3.

Ground every score in **verbatim phrasing from the first30 field** and **specific comment metrics** from the corpus JSON. Do not score on title alone. If a hook is weak, score it weak even if views are high (the title may have done the work, not the hook).

## 1. Curiosity gap (1-10)

Does the FIRST sentence make the viewer NEED to know what comes next?

- 9-10: Cold-open with a stat-shock ("95% of adult beginners practice way too much"), a story hook ("When people heard Paganini play for the first time, many believed it was not humanly possible"), or an empathy disarm with built-in tension ("There is nothing wrong with you").
- 6-8: Clear problem statement with implied promise, but no strong shock or story.
- 1-5: Greeting + generic claim ("Good morning. Today I'll show you...").

## 2. Specificity (1-10)

Does the hook use specific numbers, named methods, identifiable pain (vs generic claims)?

- 9-10: Cites a specific stat (97.8%, 95%, 90%), names the method ("Three Factors of Sound", "Acceleration Protocol", "Four Patterns"), and names a recognizable proof point ("Paganini Moto Perpetuo", "Ode to Joy", a specific student).
- 6-8: Some specificity but at least one slot is generic.
- 1-5: Vague claims, no numbers, no named method.

## 3. Authority anchor (1-10)

Is there a credible authority claim, and is it stacked?

- 9-10: Triple-anchor ("30 years playing + 800 books + hundreds of students") OR a uniquely strong single anchor ("I taught 356 violinists 8 habits").
- 6-8: Single solid anchor (one of: time / books / students).
- 1-5: No authority claim, or vague ("trust me", "as someone who plays").

## 4. Pacing (1-10)

Clean 4-beat structure in 30 seconds (problem -> pivot to authority + named method -> structure preview), under ~85 words, ends mid-sentence into the body?

- 9-10: Exactly 4 beats, ~70-85 words, clean transitions, ends cleanly into the body.
- 6-8: Mostly clean but one beat is bloated or repeated.
- 1-5: Rambling, padded, or missing a beat (e.g. no structure preview).

## 5. Engagement evidence (1-10)

Do the comment metrics back up that this hook actually resonated?

- 9-10: High avg_comment_words (>30), high quote_back relative to surface_praise, multiple questions, high comment_rate relative to channel average.
- 6-8: Decent engagement but mixed signals.
- 1-5: Comments dominated by surface praise ("great", "thanks", "helpful"), few questions, low avg word count, possible accent friction comments.

Specific signals to weigh:
- `quote_back`: comments mentioning specific concepts (factor, rule, step, level, pattern, principle, tip, trick, secret, point, mistake, exercise). High = hook content actually stuck.
- `questions`: comments with "?". High = the hook provoked real curiosity.
- `surface_praise`: short shallow praise. High = the hook was consumable, not memorable.
- `comment_rate`: organic_comments / views. Compare across channel. >0.1% is healthy for educational.

## 6. Semantic match to THIS idea (1-10)

Injected per-run via the idea's pain point, named techniques, and rationale. How well does this Antoine pattern transfer to THIS specific Harrisson video?

- 9-10: The Antoine video uses the same archetype (multi-part mechanical-positioning framework / numbered level diagnostic / gatekeeping reveal / etc.) AND its hook structure clones cleanly with just the named techniques swapped in.
- 6-8: Same archetype but the hook copy needs more reshaping.
- 1-5: Different archetype. Forcing a clone would break the rhythm.

Pass the agent the idea's hook_angle, pain_point, and named_techniques fields verbatim so it has the context to judge transferability.

## Aggregation

Total = sum of 6 criteria (max 60).

Top 3 by total = surfaced as hook options. If two are within 2 points of each other, surface both and let Timo break the tie.

Tie-breaker order if needed: semantic-match > engagement > pacing > curiosity > specificity > authority.
