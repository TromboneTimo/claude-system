---
name: feedback_rls_anon_reads
description: THE #1 BUG. "0 videos" was reported 30+ times and I attempted 13 different fixes before finding the root cause. NEVER repeat this.
type: feedback
---

## The Worst Bug I Ever Created — 30+ Reports, 13 Failed Fixes

### What Happened
The Hook Book showed "0 videos" after login. The user reported this 30+ times across this session. I attempted 13 different fixes, each one wrong, before finally finding the root cause.

### The 13 Failed Fixes (In Order)
1. Added loading timeout — wrong layer
2. Checked localStorage for session — wrong approach
3. Removed loading screen from ProtectedRoute — cosmetic, not root cause
4. Used getSession() instead of INITIAL_SESSION — still a timing hack
5. Added safety timers — bandaid on bandaid
6. Added TOKEN_REFRESHED handler — right idea, wrong execution
7. Added setSession() before fetch — CAUSED INFINITE LOOP (setSession triggers onAuthStateChange which calls fetch which calls setSession)
8. Simplified to doFetch on mount — still failed because stale token
9. Added "3-layer defense" — overengineered garbage
10. Added failsafe timeout — more bandaids
11. Added initAndFetch with getSession() — MADE IT WORSE (expired JWT is worse than no JWT for anon reads)
12. Added anon RLS policy — RIGHT FIX but then undermined it by keeping getSession() which sent expired token
13. Removed getSession(), just fetch directly — FINALLY WORKS

### Root Cause
Supabase RLS required `authenticated` role for SELECT on the hooks table. An expired JWT stored in the browser's localStorage made every fetch fail because:
- The Supabase JS client automatically attaches any stored token to requests
- RLS sees the expired JWT, treats it as a failed authenticated request, returns empty
- This is WORSE than no token at all — a clean anon request would have worked if the policy existed

### The Fix (2 Lines)
1. **SQL:** `CREATE POLICY "Anon can read hooks" ON public.hooks FOR SELECT TO anon USING (true);`
2. **JS:** Remove ALL getSession()/setSession() calls before the fetch. Just call `supabase.from('hooks').select()` directly.

### Why I Failed 13 Times
1. I kept treating it as a TIMING problem (auth not ready fast enough) when it was an ACCESS CONTROL problem (wrong RLS policy)
2. I never tested with an expired/stale token — my curl tests always used fresh tokens
3. I kept adding complexity instead of questioning the fundamental assumption (that reads need auth)
4. I never asked: "What happens if the Supabase client sends an EXPIRED token vs NO token?"
5. I kept deploying without verifying in the actual browser — my "smoke tests" only tested the API with fresh tokens

### Rules to Prevent This Forever
1. **Public data tables MUST allow anon SELECT.** Hooks, posts, products — if everyone can read it, don't gate it behind auth.
2. **NEVER call getSession() before a data fetch.** If anon reads are allowed, getSession can only hurt (expired token overrides anon).
3. **Test with expired tokens, not just fresh ones.** The browser often has stale sessions.
4. **When the same bug appears 3+ times, STOP fixing the code and examine the database/RLS.** The problem is probably in the access policy, not the fetch timing.
5. **The Supabase JS client automatically attaches stored JWTs.** An expired JWT in localStorage makes authenticated-only queries fail even though getSession returns successfully.
