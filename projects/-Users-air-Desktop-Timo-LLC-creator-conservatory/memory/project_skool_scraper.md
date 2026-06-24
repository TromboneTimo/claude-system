---
name: Skool Community Scraper Setup
description: Apify-based Skool scraper for Creator Conservatory engagement analysis - ready to deploy when Apify limit resets
type: project
---

## Skool Community Engagement Analyzer

**Goal:** Scrape Creator Conservatory Skool posts weekly, score engagement, surface recurring questions and top-performing content.

**Stack decided:**
- Apify actor: `memo23/skool-posts-with-comments-scraper` (4.68/5, 19 reviews, best for posts + comments)
- Apify token: stored in Hook Book workspace `.env` as `VITE_APIFY_TOKEN`
- Can run directly via curl from Claude Code - no n8n needed for one-off runs
- n8n workflow also built and pushed to timotrombone.app.n8n.cloud (workflow name: "Skool Community Engagement Analyzer")

**Blocker as of 2026-04-06:** Apify monthly usage hard limit exceeded. Need plan upgrade or cycle reset.

**Data pipeline:**
1. Apify scrapes posts + comments + engagement metrics
2. Code transforms: engagement score = (upvotes x2) + (comments x3) + (replies x1)
3. Auto-categorize: question, win, resource, introduction, discussion
4. Flag unanswered questions
5. Extract trending keywords
6. Output to Google Sheets (not yet configured)

**Why:** Timo wants to understand what content resonates in the Conservatory, what questions keep coming up, and where to focus community energy.

**How to apply:** When Apify resets, run the scraper. Consider scheduling via /schedule for weekly runs. Also explore making Skool a top-of-funnel email capture (from PRIORITIES.md backlog).

**n8n workflow file:** `/Users/air/Desktop/N8N Let's Get It Baby/skool-engagement-analyzer.json`
