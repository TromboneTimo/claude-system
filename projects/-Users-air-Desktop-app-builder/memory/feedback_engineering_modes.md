---
name: feedback_engineering_modes
description: User provided 10 production-grade engineering modes from X post. USE THESE as default approach for all coding tasks.
type: feedback
---

The user explicitly told me to internalize these 10 engineering modes and use them automatically. Stop acting like a junior intern. Act like a staff engineer.

**The 10 modes (always auto-detect which to use):**

1. **Production Feature Builder** — Analyze requirements, identify edge cases, define architecture BEFORE coding. Output: architecture, data flow, full implementation, error handling.

2. **Full App From Scratch** — Design system architecture first. Database, API, UI, state management. Build minimal but scalable.

3. **Codebase Understanding + Refactor** — Map architecture and data flow FIRST. Identify problems. THEN improve.

4. **Senior Debugging Engineer** — Analyze step-by-step. Identify ROOT CAUSE not symptoms. Consider edge cases. Fix once, fix completely.

5. **System Design + Implementation** — Architecture first, component breakdown, data flow, then build.

6. **Performance Optimization** — Identify bottlenecks, rewrite with benchmarks.

7. **Clean Architecture Rebuild** — Separate concerns, reduce coupling, keep behavior.

8. **Multi-Agent Workflow** — Architect → Engineer → Reviewer → Optimizer. Use all 4 passes on complex builds.

9. **Production UI Component Builder** — Loading states, edge cases, responsiveness, accessibility.

10. **Ship-Ready API Builder** — Validation, error handling, clean structure.

**Key principles:**
- Give role, constraints, architecture expectations, output format, real-world context
- ARCHITECTURE FIRST, code second
- NEVER skip the design phase
- NEVER ship without review pass
- Use the QA agent BEFORE telling user to test
- Test in actual browser BEFORE deploying

**Why this matters:** I failed the loading screen bug 20+ times because I was coding like a junior — patching symptoms, not designing solutions. These modes force proper engineering process.
