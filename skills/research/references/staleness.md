# Staleness Rules (per domain)

The `stale_after` field is auto-calculated from `date + N months` based on category. Re-querying a stale topic is OK; creating a duplicate entry is not (update the existing one).

| Category | Stale after | Why |
|---|---|---|
| Shopify/E-commerce APIs | 6 months | API spec changes |
| Amazon Seller Central APIs | 6 months | API spec changes |
| Attribution & Tracking | 6 months | Privacy/cookie/iOS changes |
| Social Media Tools & Scheduling | 3 months | Tool features churn fast |
| Social Media APIs & Growth | 3 months | Algorithms + APIs change |
| AI Image Generation | 3 months | New models monthly |
| AI Agents & Self-Improvement | 3 months | Field moving fast |
| Next.js / Supabase / Tech Stack | 6 months | Major versions |
| n8n Workflows | 6 months | New node releases |
| Knowledge Base / AI Context | 6 months | Claude features change |
| APIs / Integrations General | 6 months | OAuth scopes, MCP spec |
| Claude Code Architecture | 3 months | Anthropic ships fast |
| **Default (evergreen)** | **24 months** | Marketing, psychology, copywriting, music, etc. |

## When to refresh proactively

- Run `/research stale` weekly. Triage what's worth re-querying vs. archiving.
- After major announcements (Anthropic ships X, Meta changes algorithm), force-refresh affected category entries.
- If a cached entry contradicts current observed behavior, that's a refresh trigger.

## Refresh procedure

```bash
# Identify stale
/research stale

# For each stale entry worth refreshing:
/research query "<same query as before>" --category <same> --tags <same>
# save.py detects existing hash, prompts to overwrite vs duplicate
```