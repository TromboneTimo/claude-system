---
name: Measure real page weight after "perf optimization," do not claim wins without numbers
description: After any perf-optimization task, run `curl` against the deployed URL and tally the bytes for HTML + hero asset + above-fold images. Never claim a site is "optimized" without a before/after number.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Calling a session "optimized" based on code patterns (willChange toggles, memo wrappers, IntersectionObserver) without measuring actual page weight is hollow. The only thing the user experiences is load time, which maps directly to bytes shipped.

**Why:** On otto-cristofoli (2026-04-22), I claimed a dozen "perf wins" in the DiscographyCarousel and Navigation based on code patterns. The user then reported the site was "still slow." Root cause was an 18MB video I never inspected, plus Next.js shipping `w=3840` image fallbacks. Every "win" I listed was real but microscopic compared to the real bottleneck I missed.

**How to apply:**
- After any "optimize / make smoother / fix perf" task, ALWAYS measure deployed bytes before reporting done:
  ```bash
  curl -s -o /dev/null -w "HTML: %{size_download}B  ttfb=%{time_starttransfer}s\n" <URL>
  curl -I <hero-asset> | grep -i content-length
  curl <page> | grep -oE 'src="/_next/image[^"]*"' | head -5
  ```
- Report before/after byte counts in the summary. No byte numbers = no claim of a win.
- If the user complains "still slow" after optimization, the FIRST move is `curl -I` on every hero asset, not more code edits.
- For Next.js: also grep deployed HTML for `srcSet=` and `w=` params to confirm image cap is working.
- Heavy static assets trump any React optimization. Always.
