# Enforcement-First Architecture: how this system survives any model

Written 2026-06-11 (Fable 5 session) after the wrong-CTA incident: a rule existed in memory, was violated 5 times anyway, and was fixed permanently only when it became machinery. Research basis: cache entry `2026-06-11_llm-agents-ignoring-written-rules_1ccd6f6f` (LangChain State of Agent Engineering, CSA, arxiv 2605.24309).

## The one principle

**Anything the model is trusted to read is advisory. Anything that fires without the model's cooperation is mandatory.** Model intelligence changes how often advisory rules get honored; it changes NOTHING about enforced ones. That is why this architecture is the answer to "what happens when I switch from Fable to Opus 4.8": the system was never supposed to depend on the model being smart.

## The 5 gate types in this stack (strongest last)

1. **Context injection (UserPromptSubmit hook)** - the rule finds the model at decision time. Example: email-angle-gate.sh injects the live angle ledger + LINK LAW into every email turn, reading the canonical URL from the executable registry at fire time so it can't drift. Fixes lost-in-the-middle / "forgot to read the memory file."
2. **Tool-boundary interceptor (PreToolUse hook)** - the action is inspected before it executes; exit 2 blocks it. Examples: email-link-gate.sh (banned links in write payloads), dashboard-deploy-gate.sh, anti-delete.sh, cache-check-perplexity.sh. Fixes "model decided to do it anyway."
3. **Executable lint with block severity** - content rules as code, run at draft/push/render. Example: email-lint.js RULES (banned claims, wrong destinations, missing tracking), email-rhythm-check.py. Single source of truth constants live HERE, not in prose (CANONICAL_MASTERCLASS_URL).
4. **Data-layer constraint (DB trigger / UNIQUE / RLS)** - the row is refused no matter what client wrote it. Examples: email_send_ledger UNIQUE claim (dup-send), trg_email_proposals_link_guard (pending install). The ONLY layer that survives a fresh session with zero hooks and zero memory.
5. **Permission classifier / allowlists** - the harness itself denies action classes (prod DDL, real-list sends). Configured in settings.json, not in model context.

## The recipe: converting a failure into a gate (works with ANY model)

When something goes wrong, do these in order - this is the prompt sequence to give whatever model you're running:

1. "Write the post-mortem: what rule was violated, where did the rule live, why didn't it fire?" (If the rule lived in a memory file: that IS the root cause.)
2. "Classify the rule: is the violation detectable mechanically (string match, schema, threshold, allowlist)?"
   - YES -> "Implement it as the LOWEST layer that fully covers it: DB constraint if it guards data, PreToolUse hook if it guards an action, lint rule if it guards content, injection hook if it guards judgment."
   - NO (pure judgment call) -> put it in an INJECTED context block (gate type 1), never in a passive memory file alone.
3. "Test the gate by attempting the violation. Show me the rejection." A gate that has never blocked anything is a hypothesis.
4. "Write the memory file LAST, as documentation of the gate, linking to it - not as the enforcement."

## Commissioning gates from a weaker model: what changes

- **Trust the machinery more, the narrative less.** Demand the rejection test output (step 3) every time; don't accept "I added the rule."
- **Smaller asks.** One gate per request. "Add a lint rule that blocks X, run it on these 3 test bodies, show me all 3 results."
- **The registries do the thinking.** Constants (URLs, list IDs, thresholds, allowlists) live in ONE executable file each; every skill says "copy from the registry." A weaker model that can't reason about which URL is right doesn't need to - it copies or the gate rejects.
- **Hooks are model-blind.** Everything in ~/.claude/hooks/ + settings.json keeps working identically. Nothing to migrate.
- **Expect more gate FIRINGS, not more failures.** A weaker model will hit the interceptors more often. That's the system working; the error messages contain the fix (each gate prints the canonical answer in its rejection).

## The recall infrastructure (added same day): rules-router + coverage ratchet

The remaining failure mode after gates: lessons live in 271 feedback_*.md files the model must REMEMBER to read. Two pieces close it:

- **`~/.claude/hooks/rules-router.sh` + `rules-router.json`** (UserPromptSubmit, all workspaces): a declarative registry of {intent regex -> route + imperative rules}. Matching prompts get the route ("use THIS skill") and the rules injected before the model acts. Adding a lesson = adding a registry entry; no hook code. This is how "actually reads the rules" stops being a hope: the rules read themselves into context.
- **`~/.claude/hooks/router-coverage-check.py`** (run by /weekly-review and /fix-brain): lists every feedback file that NO gate, router entry, skill, or knowledge file references -- i.e. lessons the system can still repeat. Each run, the top uncovered files get a router entry, a gate extension, or a written accepted-advisory reason. UNCOVERED must trend to zero and never grow. First run 2026-06-11: 271 files, 178 uncovered -- that number is the honest backlog of repeatable mistakes.
- **Read-back for inject-only gates:** an injection that asks the model to do something needs a Stop-time verifier (e.g. credential-readback.sh blocks the first stop if MASTER.md wasn't modified after a credential was detected). Inject-only without read-back is how rules get ignored politely.

## Maintenance rules

- Rotating a value (URL, token, list ID) = update the ONE registry constant + its mirror memory file together. Injection hooks that read registries live need no edit.
- Every new gate gets: a comment block with origin date + the incident, a bypass token convention (PB_*_GATE=skip in command text, Timo's say-so required), and a line in the relevant memory file pointing AT it.
- Periodically (e.g. /weekly-review): "list rules in memory files that have no gate; rank by blast radius" - the advisory->enforced migration is never finished, it's a ratchet.

## What stays advisory on purpose

Voice, taste, judgment calls (which angle, which student, what's "off-brand"), batch diversity choices. These can't be string-matched. Concentrate them into INJECTED blocks (gate type 1) so they're at least always in context, and keep the human checkpoint (Timo approves drafts; Harrison approves on the dashboard) as the real gate.
