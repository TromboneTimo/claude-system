---
name: feedback-concurrent-repo-use-worktree
description: "When another process/agent is actively committing in the same git repo, do your work in an isolated git worktree, not the shared working dir."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6a16b3f6-b8fd-429a-acff-d79a73c1345e
---

When a second Claude session (or any process) is actively working the SAME git repo, the shared working directory is unsafe. The other process's `git checkout` / `git reset` will silently clobber your uncommitted (or even committed-on-a-feature-branch) work.

**What happened (2026-05-28):** While I staged channel-attribution.html + hyros-source-map.js on a new branch off main, a concurrent meta-ads worker committed onto MY branch, then ran `checkout main` + `reset --hard origin/main`, wiping my staged changes. Reflog showed the whole hijack.

**Why:** git's working dir + HEAD are shared state across one checkout. Two agents in it = the 4-failure-pattern "shared state breaks everything."

**How to apply:**
1. `git worktree add -b <branch> ../<repo>-wt-<task> <base>` gives a separate working dir + separate HEAD, immune to the other process's branch switches.
2. Do all edits, commits, and verification in the worktree.
3. Land WITHOUT touching the shared dir: `git push origin <branch>:main` (fast-forward). If rejected, `git fetch && git rebase origin/main` in the worktree and retry. Confirm your files are disjoint from the other agent's first.
4. `git worktree remove --force` + `git worktree prune` when done.

The disjoint-files check is what makes the fast-forward land clean. Here the meta-ads worker only touched meta-ads.html; I only touched channel-attribution.html + hyros-source-map.js. Related: [[project_dashboard_self_verify_authed]] (authed Playwright verify before push).

**ADDENDUM (2026-06-05): the shared working tree can be BEHIND origin/main, so `vercel --prod` from it REGRESSES prod.** The scrape/meta-ads bots had advanced `origin/main` 37 commits ahead while the local working dir sat on an old HEAD (96ca06a) with a giant pile of uncommitted changes. I ran `vercel --prod` from that working dir; it shipped my features but DROPPED 9 `dashboard/thumbnails/*.jpg` that existed in origin/main but not locally, so suggestion tiles 404'd on prod. Before ANY `vercel --prod`: run `git fetch origin main` then `git diff --diff-filter=D --name-only origin/main -- dashboard/ api/`. If that lists ANY deployed file, your tree is stale and you WILL regress prod. Safest pattern: never deploy the shared working tree. Land features to origin/main first (worktree at origin/main, `git apply` a `git diff origin/main -- <files>` patch, push), THEN deploy from a clean origin/main checkout. To recover a stale-tree regression: `git checkout origin/main -- <missing paths>` then redeploy.

**CRITICAL ADDENDUM (2026-05-29): a local commit + `vercel --prod` is NOT durable. You MUST push to origin/main.** This repo has a "Daily PB scrape" bot that pushes commits to `origin/main` on its own schedule, and Vercel auto-deploys from `origin/main`. So a change that is only committed locally (or only deployed via `vercel --prod` from the working dir) gets REVERTED the next time the scrape bot pushes, because Vercel rebuilds from origin/main which lacks your commits. This is what silently reverted my "any sale = winner" classify fix overnight: my commit lived only on local main, never on origin, so the scrape push + git auto-deploy served the pre-fix bundle. **Always finish dashboard/api work with `git push origin main`** (rebase onto origin/main first; the scrape bot only touches `voc/emails/performance/*`, so it never conflicts with dashboard/api files). Verify the prod alias still serves your marker AFTER the git-triggered build settles, not just after your local `vercel --prod`.
