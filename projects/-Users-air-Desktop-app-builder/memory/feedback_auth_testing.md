---
name: feedback_auth_testing
description: NEVER ship auth code without testing the full login flow yourself. The login page was broken 6+ times in a row.
type: feedback
---

NEVER tell the user to "try it" without testing auth yourself first. The login system was broken 6+ times consecutively because I kept deploying without verifying the actual user-facing flow.

**What went wrong:**
1. LoginPage showed "Loading..." forever because useAuth loading state never resolved for fresh visitors
2. After fixing that, clicking "Sign In" hung because signIn() went through useAuthContext which triggered a chain of state changes that never completed
3. After fixing that, navigating to / showed "Loading..." because ProtectedRoute waited for profile which hadn't loaded yet
4. The root cause every time: relying on indirect state chains (auth event → state change → re-render → redirect) instead of direct imperative code (call API → check result → navigate)

**Rules to follow:**
1. For auth flows, use DIRECT Supabase calls in the component, not indirect hooks-of-hooks chains
2. Login page must NEVER show a loading state — it's a public page, show the form immediately
3. After signIn succeeds, navigate IMMEDIATELY — don't wait for onAuthStateChange
4. ProtectedRoute must NEVER hang — if profile fetch fails, use a fallback, don't block rendering
5. ALWAYS test login in an incognito window (no existing session) before deploying
6. ALWAYS run the QA agent after ANY auth-related change
7. If something breaks, don't patch one thing — read the ENTIRE auth chain end-to-end and fix all issues at once
