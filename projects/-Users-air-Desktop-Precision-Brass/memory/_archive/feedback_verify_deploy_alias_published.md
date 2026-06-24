---
name: feedback-verify-deploy-alias-published
description: "After vercel --prod, the production alias can still serve the OLD bundle for a bit (build/alias lag). Always curl the alias and grep a unique marker of THIS change before declaring deployed."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d228715a-5ca5-4603-b90f-9fe73056656e
---

After `vercel --prod`, do NOT declare "deployed" until you curl the production alias (`https://precision-brass-dashboard.vercel.app/<page>?cb=<ts>`) and `grep` for a UNIQUE string that only exists in the change you just made (e.g. a new label, var name, or width). The alias can keep serving the previous bundle while the new deploy is still "Building", so a too-early verification (or one that only checks part of the page) passes on stale code.

**Why:** 2026-05-26, the meta-ads per-ad/metrics change. The first `vercel --prod` reported success and the table looked updated, but the CARD code had NOT published to the alias yet. Timo saw only one ad set with the new stats ("you only updated one, apply to all idiot"). The local file + git HEAD had all the changes; the alias was just serving an older bundle. A redeploy + immediate `grep` of the alias for `Conv Rate`/`cpaDisplay`/`1472px` confirmed it published the second time.

**How to apply:** deploy -> wait ~8s -> `curl -sL "<alias>/<page>?cb=$(date +%s%N)" | grep -c "<unique-marker>"` -> only when >0, load the authed page and verify visually. Combine with [[reference-view-authed-dashboard]] for the visual step. This is the spirit of the dashboard-deploy-gate hook; honor it rather than bypassing blind.

## Detail (moved from index 2026-06-10)
This bit us twice on 2026-05-26: the first "verified" pass ran against the stale bundle still on the alias, and only the redeploy + alias grep confirmed the real publish.
