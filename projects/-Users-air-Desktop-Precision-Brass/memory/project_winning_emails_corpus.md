---
name: project-winning-emails-corpus
description: "voc/emails/raw/winning-emails/ holds 18 Harrison Daily Email 1 broadcasts (AC list 13), all tier=winner, ranked by unique_clicks DESC. Sibling voc/emails/raw/losing-emails/ is structured but empty pending an AC+sales re-pull. Updated 2026-05-24."
metadata: 
  node_type: memory
  type: project
  originSessionId: 467afc37-9455-4e76-8762-b666eca3bdcb
---

# Winning Emails Corpus. Ranked By Link Clicks

**Updated 2026-05-24 (restructure):** Moved to channel-first layout at `voc/emails/raw/winning-emails/`. Created a sibling `voc/emails/raw/losing-emails/` (structured, EMPTY) per Timo's request to sort winners vs losers by link clicks AND tracked sales. REALITY ON DISK: only **18 broadcasts, all tier=winner**, and NO per-email sales field was ever persisted. The loser tier + sales attribution require a fresh AC + HYROS pull (see losing-emails/README.md). The "rank 398-422 loser / 422 campaigns" framing below is stale and never matched disk. Do not fabricate losers or sales numbers.

**Why:** Per Timo 2026-05-15: "what makes an email a particular winner is actually link clicks. Let's optimize for link clicks." Link clicks correlate most directly with funnel movement. Open rate is vanity; reply rate is sparse; click rate is the signal.

**Corrected 2026-05-16:** Initial build had 422 broadcasts. Wrong. AC's `filters[listid]=13` is a SUBSCRIBER filter (returns any campaign whose recipients overlap with list 13 subscribers), not a campaign-list filter. The 422 included Test-Timo-Solo sends (list 20, Timo on both) and multi-list broadcasts to webinar attendees who happened to also be daily-email subscribers. Correct count is **18 broadcasts** after filtering by `include=campaignLists` containing list 13 AND `send_amt > 50`. List 13 was only created 2025-09-12, so the dataset is genuinely small (~2-3 broadcasts/month).

**How to apply:**

1. **Source of truth for proven winning email patterns.** All 8 pb-email mining agents (and pb-script agents that touch email-adjacent topics) should read `voc/emails/raw/winning-emails/` as the proven-conversion corpus.

2. **Tier-based mining:**
   - `tier: winner` (rank 1-25). Use as POSITIVE examples. Mine for hook formulas, subject patterns, CTA structures, P.S. types, body length, paragraph count.
   - `tier: loser` (rank 398-422). Use as NEGATIVE examples. Filter out 0-click drafts/smokes (`send_amt > 0`) to focus on real flops.
   - `tier: mid` (rank 26-397). Useful for averages, not individual ideas.

3. **Index.json is the fast-lookup layer.** `voc/emails/raw/winning-emails/index.json` has all campaigns with metrics in one JSON. Agents grep that first, dive into the .md files when they need full body.

## Key snapshot stats (2026-05-16)

- 422 campaigns
- 28.19% avg open rate
- 1.21% avg CTR (the baseline)
- 2%+ = above-average. 4%+ = winner.

## Top winner patterns (rank 1-10)

1. Urgency / scarcity in subject ("GONE IN N DAYS")
2. Personalized recall ("Did you forget this, %FIRSTNAME%?")
3. Specific pedagogy hook ("How jaw placement affects your trumpet playing")
4. Authority / news angle ("I got featured on ITG")
5. Content tease (highest CTR is "Quick Video on Lip Puckering" at 7.54%)
6. Identity reframe ("You're not ready for this. Seriously")

## Refresh

Run `/tmp/pb-winning-emails/build.py` to re-pull and re-rank. Takes ~3-5 min for ~420 campaigns. The script:
1. Hits AC `/api/3/campaigns?filters[listid]=13&filters[status]=5` paginated (~6 calls)
2. For each campaign, pulls `/api/3/messages/{message_id}` for the body
3. Joins with Supabase `email_proposals` where `ac_campaign_id` matches (overrides AC label with Harrison-approved subject + body)
4. Sorts by unique_clicks DESC, writes one .md per campaign + index.json

Requires `~/.claude/secrets/precision-brass.env` sourced into the shell (ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY, SUPABASE_URL, SUPABASE_SECRET_KEY).

## Wiring

- The old `winning-emails/` placeholder README is replaced.
- `pb-email/SKILL.md` agent table mentions Channel Performance Analyst (Agent 1) reads winning emails. With this corpus populated, that agent now has real data to chew on (vs the previously-empty folder).
- Cross-reference: [[project-8-agent-restructure-20260515]] for the broader 8-agent roster restructure.

## Known caveats

- Some "loser" tier entries are 0-click drafts/smoke-test sends with send_amt < 10. Filter `send_amt > 100` when mining for real failure patterns.
- Subjects with merge tags like `%FIRSTNAME%` render as raw template syntax in this snapshot. The recipient saw the resolved value, but the corpus stores the template form.
- Body bodies for old campaigns (pre-pb-email-write) come from AC `/api/3/messages` directly. Newer campaigns (with `ac_campaign_id` in email_proposals) come from email_proposals.body for higher fidelity.
- Bottom-of-list contains 91 scheduled-but-not-yet-sent campaigns even though we filtered `status=5`. AC marks pre-scheduled drafts as status=5 once approved. Re-run after sends complete to get true post-send metrics.
