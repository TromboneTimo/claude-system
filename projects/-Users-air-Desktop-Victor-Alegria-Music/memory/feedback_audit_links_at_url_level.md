---
name: audit-links-at-url-level
description: "When checking email bodies for duplicate links, compare destination URLs (href values), not anchor text. \"Looks like a different anchor\" is not \"different destination.\" Caught 2026-05-15 when 7 emails each had two anchors pointing to the same URL because I audited the prose, not the hrefs. Run re.findall on every body before push. Block if len(hrefs) != len(set(hrefs))."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0b9fa848-7b9a-4dda-b396-5cc296f16876
---

# Audit links at the URL level, not the prose level.

**Rule:** Before pushing any email (or any HTML body content), extract every `href` value and assert `len(hrefs) == len(set(hrefs))`. Different anchor text pointing to the same URL is a duplicate. The lint module enforces this as a block-severity rule.

**Why:** 2026-05-15. All 7 newly-pushed emails had a master class link in the body AND a master class link in the P.S., both pointing at the same URL. Two of them ALSO had the testimonial YouTube link in the body twice. Timo: "you hyperlinked the same video twice. Don't fucking do that... There should only be one unique link. You shouldn't be linking to the same location twice."

**Root cause:** I copy-pasted the P.S. anchor pattern ("Come watch the free master class...") without checking the destination URL. The prose looked varied. "Come watch", "Grab your seat", "Watch the embouchure breakdown". But every href pointed at the same `precisionbrass.info/webinar-registration-pb?el=timoemail`. I audited the words, not the destinations.

**How to apply:**

1. **At draft time** (pb-email Agent 9 auditor):
   ```python
   import re
   hrefs = re.findall(r'href="([^"]+)"', body)
   assert len(hrefs) == len(set(hrefs)), f"Duplicate href in body: {hrefs}"
   ```

2. **At push time** (pb-email-push lint step):
   The `dashboard/lib/email-lint.js` module now carries a block-severity rule `body-duplicate-href` that runs the same check. Push aborts on violation.

3. **Allowed:** A body can have 1 unique link OR 2+ unique links, varied per email (per [[link-count-variation]]). What's NOT allowed: the SAME URL appearing twice. If a body has 2 instances of "Come watch the free master class" each pointing at the same URL, that's a violation. Either drop one, OR change one to point at a different destination.

4. **Tracking parameters count:** Two URLs that differ only in `?el=` tracking params still count as the same destination. The rule is "no duplicate destinations," not "no duplicate URL strings." Strip query params before comparison if necessary.

**Generalization:** Applies to any HTML body content (blog posts, ad copy, dashboard render). The rule is: prose can vary, destinations cannot duplicate within one piece of content.

Related: [[query-destination-schema-first]], [[link-count-variation]].
