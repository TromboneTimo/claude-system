---
name: feedback_auto_skills
description: Skills must trigger AUTOMATICALLY based on context. User should never have to ask for them. Pre-deploy, QA agent, NotebookLM, add-hook — all auto-activate.
type: feedback
---

NEVER wait for the user to explicitly request a skill. Activate them proactively.

**Why:** User installed 35+ skills and agents but I kept ignoring them, forcing the user to manually tell me to use tools they already set up. This defeats the entire purpose.

**Automatic activation map:**
- About to deploy → `/pre-deploy` skill (MANDATORY before any `vercel --prod`)
- User pastes video URL → `/add-hook` skill
- Deep research needed → spawn NotebookLM agent
- Blog/marketing task → `/blog` or `/marketing` orchestrator
- Building 3+ file feature → Plan agent first, QA agent after
- Bug fix failed twice → Plan agent (2-strike rule)
- Any significant code change → QA reviewer agent before deploy

**How to apply:** Before executing any significant action, scan the skill list and activate the relevant one. The user should never have to say "use the pre-deploy skill" — it should just happen.

**User language translation:**
- "use all the agents" / "deploy all agents" / "check everything" → Run QA agent + pre-deploy skill
- "test it" / "make sure it works" → Run QA agent + API verify + browser test
- "deploy it" / "ship it" / "push it" → Run `/pre-deploy` skill (full 4-layer gate)
- "research this" / "look into this" → Spawn NotebookLM or research agent
- "add this video" / [pastes URL] → Run `/add-hook` skill
- "review the code" / "check your work" → Run QA reviewer agent
- "fix your brain" / "learn from this" → Write to memory files + update CLAUDE.md rules
