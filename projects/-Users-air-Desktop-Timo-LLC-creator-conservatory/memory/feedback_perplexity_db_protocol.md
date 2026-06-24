---
name: Perplexity Research Database Protocol
description: Always grep the shared Perplexity research DB BEFORE running any sonar-pro query, and append new findings AFTER. Non-negotiable workflow step.
type: feedback
originSessionId: 620203ae-1dd5-484d-9c81-6e3623000cc3
---
Before firing any `llm -m sonar-pro` query, FIRST grep `/Users/air/.claude/knowledge/perplexity_research_database.md` for the topic. If cached, use it. AFTER any new query, append the findings to the appropriate section of that file and bump the header count + TOC count.

**Why:** Timo called this out explicitly on 2026-04-12 after I burned a Perplexity query on brass endorsement economics without checking the DB (the Ottaviano profile was already in there, adjacent topics might have been too) and without storing results. The DB exists at `/Users/air/.claude/knowledge/perplexity_research_database.md` (139 entries across 5 workspaces as of 2026-04-12). Skipping it wastes tokens and burns the research budget he's paying for.

**How to apply:**
1. Before every Perplexity call: `Grep` the DB for the core nouns/topics of the query. If a hit exists, cite the cached entry instead of calling Perplexity.
2. After every Perplexity call that returns new info: append an entry under the right section (Music Industry, Marketing Frameworks, etc.) with Date, Workspace, Query count, Tags, Key findings, and Sources cited. Match the existing format exactly.
3. Update the header total count (+1) and the Table of Contents subsection count (+1).
4. Workspaces where this applies: all five (Timo-LLC-creator-conservatory, Precision-Brass, Robinsons-Remedies, and the two others in the DB).
5. NotebookLM synthesis is still required per global CLAUDE.md for true research tasks, but single-shot calibration queries can use Perplexity + cache without NotebookLM if scope is narrow.
