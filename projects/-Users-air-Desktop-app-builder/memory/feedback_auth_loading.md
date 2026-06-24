---
name: feedback_auth_loading
description: Supabase auth + profile fetch must NEVER leave the app stuck loading. Always set fallback state on failure.
type: feedback
---

When building auth flows with Supabase, NEVER let profile fetch failures leave the app in an infinite loading state.

**Why:** The app got stuck on "Loading..." multiple times because:
1. Profile fetch failed silently (RLS blocked, network error)
2. `profile` stayed `null` forever
3. ProtectedRoute waited for non-null `profile` → infinite loading screen

**How to apply:**
- ALWAYS wrap profile fetches in try/catch
- On failure, set a FALLBACK profile (e.g. `{ id, role: 'client', email: '' }`) so the app renders something
- ALWAYS use `finally { setLoading(false) }` — loading must resolve regardless of errors
- Test with broken network / wrong credentials / missing profile rows before shipping
- Run the QA agent after EVERY auth-related change
