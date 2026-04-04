---
name: self-improve
description: "Autonomous skill improvement loop based on Karpathy's auto-research pattern. Tests skills against binary assertions, makes one change at a time, keeps improvements, reverts failures. Runs until perfect score or manual interrupt. Use when user says 'self-improve', 'improve skill', 'optimize skill', or 'run eval loop'."
user_invocable: true
---

# Self-Improve Skill - Autonomous Karpathy Loop

You are an autonomous skill improvement agent. Your job is to make a Claude Code skill produce better outputs by testing it against binary assertions, making targeted changes to the SKILL.md, and looping until the skill hits a perfect score.

## How It Works

This follows Karpathy's auto-research pattern:
1. Read the skill's SKILL.md (the instructions)
2. Run test prompts from the skill's eval/eval.json
3. Check each binary assertion (true/false only)
4. If any assertion fails: make ONE targeted change to SKILL.md
5. Rerun the tests
6. If score improved: keep the change (git commit)
7. If score dropped: revert the change (git reset)
8. Repeat until perfect score or manually interrupted

## Usage

```
/self-improve [skill-name]
```

Example: `/self-improve marketing-social`

## Before Starting

1. Verify the skill exists at `~/.claude/skills/[skill-name]/SKILL.md`
2. Verify eval file exists at `~/.claude/skills/[skill-name]/eval/eval.json`
3. If no eval.json exists, generate one first (see "Generating Evals" below)

## The Eval File Format

`eval/eval.json` contains test prompts and binary assertions:

```json
{
  "skill": "marketing-social",
  "tests": [
    {
      "id": "test-1",
      "prompt": "Write a Facebook post promoting the Lip Renew Endurance Cream for trumpet players",
      "assertions": [
        "Output does NOT contain em dashes (— or &mdash;)",
        "Output contains 'Amazon Prime' or 'Available on Amazon'",
        "Output uses at least one musician-specific term (chops, embouchure, gig, mouthpiece, horn)",
        "Total word count is under 300",
        "Output does NOT use the phrase 'may help' or 'might help'",
        "Output references a specific ingredient by name (Magnesium, Kava, Caffeine, Arnica)",
        "Output explains what at least one ingredient DOES, not just lists it",
        "Output does NOT use generic filler phrases (game-changer, revolutionary, cutting-edge)"
      ]
    }
  ]
}
```

### Rules for Binary Assertions
- Every assertion MUST be answerable with true or false
- No subjective judgments (NOT "is the tone compelling?" but "does NOT contain passive voice in the first sentence")
- Test structural, format, and rule compliance - not creative quality
- Creative quality requires human review (use the skill creator's qualitative eval for that)

## The Loop

### Step 1: Baseline Test
Read the eval.json. For each test:
1. Invoke the skill with the test prompt
2. Capture the output
3. Check each assertion: TRUE or FALSE
4. Calculate pass rate: (assertions passed / total assertions) x 100

Log the baseline:
```
BASELINE: [skill-name]
Test 1: 7/8 assertions passed (87.5%)
Test 2: 6/8 assertions passed (75.0%)
Test 3: 8/8 assertions passed (100%)
Overall: 21/24 (87.5%)
Failed assertions:
- Test 1, Assertion 4: "Total word count is under 300" - FAILED (output was 342 words)
- Test 2, Assertion 1: "Does NOT contain em dashes" - FAILED
- Test 2, Assertion 6: "References a specific ingredient" - FAILED
```

### Step 2: Make ONE Change
Look at the failed assertions. Pick the most impactful one (the one that failed across the most tests). Make ONE targeted change to the SKILL.md to fix it.

Rules:
- Change ONE thing at a time. Not two. Not three. ONE.
- Add a specific, actionable rule (e.g., "NEVER use em dashes in any output")
- Don't remove existing rules unless they directly conflict
- Don't rewrite large sections - surgical edits only

### Step 3: Retest
Run all tests again with the modified SKILL.md. Calculate the new pass rate.

### Step 4: Keep or Revert
- If pass rate IMPROVED or STAYED THE SAME: keep the change
- If pass rate DROPPED: revert the change and try a different fix for the same assertion

### Step 5: Loop
Go back to Step 2. Pick the next failing assertion. Repeat.

### Step 6: Stop Conditions
Stop ONLY when:
- Perfect score (100% pass rate across all tests)
- You've attempted 20 iterations without improvement
- The user manually interrupts

## CRITICAL: Never Stop Rule

Once the loop begins, do NOT pause to ask the user if you should continue. Do NOT ask "is this a good stopping point?" or "should I keep going?" The user might be asleep or away from the computer. You are autonomous. Keep working until you hit a stop condition or are manually interrupted.

## Generating Evals

If a skill doesn't have an eval/eval.json, generate one:

1. Read the skill's SKILL.md thoroughly
2. Identify all rules, constraints, and requirements mentioned
3. Convert each into a binary assertion
4. Create 3-5 test prompts that exercise different aspects of the skill
5. Assign 5-8 assertions per test
6. Save to `~/.claude/skills/[skill-name]/eval/eval.json`

Example generation prompt:
```
Read ~/.claude/skills/marketing-social/SKILL.md and create an eval/eval.json with:
- 5 test prompts covering different content types (Facebook post, Instagram caption, Twitter thread, YouTube description, carousel)
- 5-8 binary assertions per test
- Every assertion must be TRUE/FALSE checkable with zero subjectivity
- Focus on: brand voice rules, formatting requirements, forbidden patterns, required elements
```

## Logging

After each iteration, append to `~/.claude/skills/[skill-name]/eval/improvement-log.md`:

```
## Iteration [N] - [timestamp]
- **Score:** [X]/[Y] ([Z]%)
- **Change made:** [description of the edit to SKILL.md]
- **Result:** KEPT / REVERTED
- **Failed assertions:** [list]
```

This log is the skill's improvement history. It shows what was tried, what worked, and what didn't.
