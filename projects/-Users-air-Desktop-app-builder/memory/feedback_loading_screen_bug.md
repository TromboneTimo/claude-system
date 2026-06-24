---
name: feedback_loading_screen_bug
description: The "Loading..." screen bug was reported 20+ times. NEVER show any loading text. NEVER deploy auth changes without testing in incognito yourself.
type: feedback
---

The user reported "Loading..." / "Loading library..." / "Loading dashboard..." stuck screens over 20 times. Every single fix attempt failed because I kept patching symptoms instead of fixing the root cause.

**The root cause:** Multiple layers all had their own loading states (useAuth, useHooksData, ProtectedRoute, Library, Dashboard). When any one of them stayed true, the user saw a loading screen. Supabase's getSession() is SLOW and can hang, especially on cold starts.

**What NEVER to do:**
1. NEVER show "Loading..." text to the user. Ever. For any reason.
2. NEVER deploy auth/loading changes without testing in a real incognito browser
3. NEVER add loading gates that block rendering — they WILL get stuck
4. NEVER rely on Supabase getSession() resolving quickly
5. NEVER add "safety timeouts" as a fix — they just delay the problem

**What to do instead:**
1. For unauthenticated users: check localStorage synchronously, redirect to login INSTANTLY
2. For authenticated users: render the page shell immediately, load data in background
3. Use skeleton UI or spinners INSIDE the page layout, never a blank page with "Loading..."
4. If auth state is unknown, render `null` (blank) for <1 second, never text
5. TEST EVERY CHANGE in incognito before deploying

**Why I failed 20+ times:**
- I kept adding loading screens to "fix" race conditions instead of removing them
- I never tested in an actual browser before telling the user to try
- I patched one layer but left the same bug in other layers
- I used the QA agent but it only checked code, not actual browser behavior
