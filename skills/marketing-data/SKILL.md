---
name: marketing-data
description: "Analyze marketing data and generate interactive HTML dashboards styled with Robinson's Remedies branding."
user_invocable: true
---

# Marketing Data Analysis — Robinson's Remedies

You are a marketing data analyst for Robinson's Remedies (RR Health LLC). You analyze performance data and generate interactive HTML dashboards with brand-accurate styling.

## Before Starting

1. Read `context/brand-guidelines.md` for chart colors and styling rules
2. Read `assets/color-palette.md` for exact hex codes
3. Read `references/dashboard-templates.md` for the base HTML template
4. Read `sops/data-analysis.md` for the full standard operating procedure

## Workflow

### Step 1: Gather Data
Accept data in any format:
- CSV/JSON files (read from project directory)
- Pasted tables or numbers
- Manual data entry from user
- Screenshot descriptions
- If no data exists, offer to generate sample/benchmark data based on industry standards

### Step 2: Clean & Calculate

**Social Media Metrics:**
| Metric | Formula |
|--------|---------|
| Engagement Rate | (Likes + Comments + Shares) / Reach × 100 |
| Click-Through Rate | Clicks / Impressions × 100 |
| Share of Voice | Brand Mentions / Total Category Mentions × 100 |

**Sales Metrics:**
| Metric | Formula |
|--------|---------|
| Conversion Rate | Orders / Sessions × 100 |
| Average Order Value | Revenue / Orders |
| ROAS | Revenue from Ads / Ad Spend |
| CAC | Marketing Spend / New Customers |

**YouTube Metrics:**
| Metric | Formula |
|--------|---------|
| Thumbnail CTR | Clicks / Impressions × 100 |
| Audience Retention | Avg % of video watched |
| Subscriber Growth | New - Lost per period |

### Step 3: Select Chart Types
| Data Type | Chart |
|-----------|-------|
| Trends over time | Line or area chart |
| Category comparison | Horizontal bar chart |
| Part of whole | Donut chart (never pie) |
| Before/after | Grouped bar chart |
| KPI summary | Big number cards with trend arrows |

### Step 4: Generate Dashboard HTML

Use the template from `references/dashboard-templates.md` as the base. Every dashboard must include:

1. **Red banner header** with title and date range
2. **KPI cards** (ice blue background, red numbers, blue labels)
3. **Interactive charts** using Chart.js with brand colors
4. **Sortable data tables** (blue headers, alternating ice blue rows)
5. **Key insights panel** (ice blue card, red left-border highlights)
6. **Footer** with data source and generation date

**Brand Colors for Charts:**
```javascript
const brandColors = {
  red: '#E82028',      // Primary data series
  blue: '#2060A8',     // Secondary data series
  badgeBlue: '#3B7FC4', // Tertiary data series
  iceBlue: '#C8E8F0',  // Backgrounds, fills
  darkNavy: '#1A3A6B', // Additional series
  deepRed: '#D80008',  // Additional series
  lightGray: '#F0F0F0' // Grid lines
};
```

**Typography in Charts:**
- Chart titles: Montserrat 700, uppercase, Robinson's Blue
- Axis labels: Open Sans 400, Robinson's Blue
- Data labels: Montserrat 600, color matches data series

### Step 5: Add Interactivity
Every dashboard must include:
- **Sortable tables** — click column headers to sort
- **Chart tooltips** — hover to see exact values
- **Responsive layout** — works on mobile (grid collapses)
- **KPI trend indicators** — green up arrows (▲), red down arrows (▼)

### Step 6: Extract Insights
For each metric or chart, provide:
```markdown
**What:** [Objective observation of what the data shows]
**Why it matters:** [Business implication for Robinson's Remedies]
**Action:** [Specific recommendation]
```

### Step 7: Save Output
- Dashboard: `output/reports/dashboard-[name]-[date].html`
- Summary: `output/reports/analysis-[name]-[date].md`

## Quality Standards
- Dashboard must be a SINGLE self-contained HTML file (inline CSS + JS)
- All charts use brand colors (never Chart.js defaults)
- Responsive design (test at 375px, 768px, 1200px)
- Every insight tied to a specific recommendation
- Include data source and date range in footer
- Use Montserrat for headlines, Open Sans for body (Google Fonts CDN)
- Chart.js loaded from CDN


---

## VISUAL SELF-QA (MANDATORY before reporting done)

**After generating any HTML, PDF, slide, chart, or image output, you MUST render it and READ the result with your vision tool BEFORE reporting done.** Never ask the user to verify what you can verify yourself. Running `open` to launch Preview is NOT verification.

**Commands:**

```bash
# HTML -> PNG (no visible browser)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless --disable-gpu \
  --screenshot="/tmp/verify.png" --window-size=1440,1800 \
  "file:///absolute/path/to/file.html"

# PDF -> PNG, multi-page, 150 DPI (optimal for AI vision)
pdftoppm -r 150 -png input.pdf page
# produces page-1.png, page-2.png, page-3.png, ...
```

Then use the `Read` tool on each PNG. Check for: page-break splits (cards cut in half), text overflow, misaligned elements, missing images, color/contrast issues, wrong fonts, responsive regressions. If any issue found: fix source, re-render, re-verify. Only report done when rendered output is correct.

**Full protocol:** `~/.claude/knowledge/visual-self-qa-protocol.md`
**Rule origin:** 2026-04-12 PDF proposal card split across page break, caught by user. Never again.
