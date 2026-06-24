---
name: feedback_change_breaks_everything
description: Every code change breaks something else. Root cause analysis and prevention protocol.
type: feedback
---

## Why Every Change Breaks Something

### The Pattern
User reports: "every time you change one thing it breaks all buttons." This happened 30+ times in this project. The reason:

1. **Shared state hooks** — useHooksData, useFavorites, useAuth are used by EVERY component. Changing one hook's behavior affects every page.
2. **Async race conditions** — Supabase client has internal state (stored JWT). Any change to fetch timing can cause the stale token bug.
3. **Optimistic vs pessimistic** — switching between update patterns (optimistic add but pessimistic check via ref) creates desync between state and ref.
4. **Ref vs state timing** — useRef updates synchronously but useEffect syncs are async. Reading from ref immediately after setState gives STALE data.

### The Unlike Bug (Example)
- Added optimistic update to favorites (state changes instantly)
- But the isFav check used favoritesRef.current (ref) 
- Ref syncs via useEffect AFTER render
- Click like → state has hookId → but ref doesn't yet
- Click unlike → ref says "not a favorite" → treats as LIKE → inFlightRef blocks

### Prevention Protocol
1. **After ANY change to a shared hook (useHooksData, useFavorites, useAuth, useAssignments):** test ALL features, not just the one you changed.
2. **When using optimistic updates:** update BOTH state AND ref synchronously in the same function. Never rely on useEffect to sync refs after optimistic state changes.
3. **Never add complexity (lazy loading, code splitting, Suspense) to a working app without testing the ENTIRE app afterward.**
4. **The Supabase client is a landmine.** Any change to fetch patterns can trigger the stale token bug. Test with expired tokens, not just fresh ones.
5. **Run ALL 4 agents after EVERY change.** Not 1. Not 2. ALL 4.
