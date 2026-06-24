---
name: Search inside clients/<name>/, never the workspace root
description: This workspace ships per-client Next.js projects under clients/. Don't grep the bare root or trust agent-reported paths without verifying.
type: feedback
originSessionId: efe5d59b-a2fa-43ee-9318-f6118124796c
---
When working in `/Users/air/Desktop/Website Builder/`, the actual code lives in `clients/<client-name>/` (e.g. `clients/otto-cristofoli/src/...`). The workspace root has only `CLAUDE.md`, `_template/`, `clients/`, `Otto Trumpet/`, `.claude/`. There is **no `src/` at the workspace root** even though sub-agents and tool output sometimes report paths starting with `/Users/air/Desktop/Website Builder/src/...`. Those resolve into the active client folder by way of the IDE workspace context, not because the path literally exists.

**Why:** I told Timo "no Samurai Brass page exists" after grepping `/Users/air/Desktop/Website Builder/src/` (which returned nothing because the dir doesn't exist), when in reality `clients/otto-cristofoli/src/app/samurai-brass/page.tsx` had been built in a prior session. That kind of "I can't find it, must not exist" answer is exactly what burns him.

**How to apply:** Before claiming a page/component/asset doesn't exist in this workspace, grep `clients/` recursively (or at minimum `clients/<active-client>/`). If a sub-agent hands you a path under `Website Builder/src/...`, treat it as a relative reference and resolve it against the client folder before searching elsewhere. When in doubt, `find /Users/air/Desktop/Website\ Builder -name <thing> -not -path "*/node_modules/*" -not -path "*/.next/*"`.
