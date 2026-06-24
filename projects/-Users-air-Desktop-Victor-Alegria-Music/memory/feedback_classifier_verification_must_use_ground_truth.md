---
name: Classifier verification must use ground truth, not internal consistency
description: When verifying a categorizer (platform inference, intent classifier, etc.), do not check the classifier against a re-implementation of itself. Sample rows and ASK the human if each row's label matches reality. From 2026-05-06 Meta Ads attribution miss.
type: feedback
originSessionId: 8821999f-0897-4321-a621-b7d70e7bf4a4
---
When checking a classifier (HYROS platform inference, email categorization, ad-vs-organic detection, anything that buckets data), do NOT settle for "no leakage between buckets" or "my Python mirror agrees with the JS". That kind of self-consistency check proves nothing about correctness. Two implementations of the same wrong rule will happily agree.

The rule that DOES catch errors:

1. Sample 5 to 10 rows from EACH bucket.
2. Show the user the source data (name, tag, traffic source, any meta fields) plus the assigned label.
3. Ask: "Is each row in the right bucket?"
4. Only after the human confirms is the classifier verified.

**Why:** On 2026-05-06 (within the same conversation), I "verified" Precision Brass HYROS classification by mirroring `inferPlatform` in Python and reporting "PASS: no leakage detected" against 365 days of real sales. I had `adSource.adAccountId` and `adSource.platform=FACEBOOK` in the raw API payload (literally printed it earlier in the same conversation) and ignored it. Result: 89 sales / $261,392 of paid Meta ads were sitting in the "Facebook organic" bucket. Timo had to point at the screen and tell me "you're saying Facebook has made almost $20,000, but it was really mostly Facebook ads I got it to that place. I don't know how you're missing." A $269,558 attribution error went undetected.

**Specific failure modes that produced this miss:**

- **Self-consistency theater:** wrote a Python mirror of the JS rule, ran it on real data, called the cross-platform-leakage check "PASS." But the Python had the same bug as the JS, so of course they agreed. Internal agreement is worthless.
- **Trusted code comments over data.** The existing inferPlatform had a comment saying "CONSERVATIVE rule. Trusting adSourceId swept organic FB/IG sources into Meta Ads." I read it and assumed the rule was correct. Should have tested whether "CONSERVATIVE" was actually right for THIS account's data.
- **Looked for technical leakage, not semantic correctness.** My check was "does a tag with 'youtube' end up in the facebook bucket?" That is contamination detection. The actual question was "does the row in the facebook bucket match what a human would call a Facebook organic click?" I never asked that.
- **Did not use available signals.** The HYROS API returns `adSource.adAccountId` and `adSource.platform`. Both are definitive paid-ad markers. I dumped a sample sale earlier in the conversation that included these fields. Did not connect them to classification.
- **Did not ask the domain expert.** Timo runs Harrison's ads. He knows the naming convention ("we date them, audience name, MF, musical instruments"). I never asked. The naming convention is in his head, not in the data.

**How to apply going forward:**

1. **Before declaring a classifier correct, dump samples per bucket and ask the user.** "Here are 5 rows currently labeled facebook organic. Are these actually organic? If not, tell me what's different about them so I can fix the rule."
2. **List all the signals available in the source data BEFORE writing the classifier.** For HYROS: trafficSource, source.name, source.tag, adSource.adAccountId, adSource.platform, lead.tags, sourceLinkAd.adSourceId. Decide which are decisive vs heuristic. Use the decisive ones first.
3. **For platform/category detection on customer accounts, ask for the customer's naming convention up front.** "What naming pattern do your paid ads vs organic posts follow in HYROS?" 30 seconds of input prevents days of bad attribution data.
4. **A passing self-test is not a passing test.** "My Python matches the JS" or "linting clean" or "no exceptions thrown" is not verification of business correctness.
5. **When the user reports a numbers-look-wrong issue, the FIRST move is to dump the contested bucket and ask them to spot-check. Not patch the rule and re-test against itself.**

**Generalizable rule:** any time I am about to write the words "PASS" or "verified" or "no issues found" about a categorization, I should be able to point at a human confirmation. Until that exists, the categorizer is unverified, regardless of how many internal checks pass.

This applies to ALL workspaces, not just Precision Brass. Any classifier (blog templates, content categories, audience personas, sales funnel stages, anything) gets the same treatment.
