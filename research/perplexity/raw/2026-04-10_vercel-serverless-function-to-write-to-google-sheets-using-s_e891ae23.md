---
query: "Vercel serverless function to write to Google Sheets using service account 2025. Step by step code example. Using @google-cloud/google-sheets npm package or googleapis. Include the"
query_hash: "e891ae237bbba3db"
slug: "vercel-serverless-function-to-write-to-google-sheets-using-s"
model: "sonar-pro"
date: "2026-04-10"
workspaces:
  - Timo-LLC-creator-conservatory
category: "Next.js / Supabase / Tech Stack"
tags:
  - api
  - google
  - next.js
  - vercel
keywords:
  - vercel
  - step
  - service
  - sheet
  - account
  - add
  - google
  - google-sheets
  - include
  - create
  - google-spreadsheet
  - googleapis
  - install
  - npm
  - api
citations_count: 9
synthesized_in_notebooklm: false
stale_after: "2026-10-07"
---

# Vercel serverless function to write to Google Sheets using service account 2025. Step by step code example. Using @google-cloud/google-sheets npm package or googleapis. Include the

## Key findings

## Setup Google Cloud Service Account and Share the Sheet

1. Go to the [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts).
2. Create or select a project, then click **"Create Service Account"**.
3. Enter a name, skip optional steps, and create it.
4. Click the service account → **Keys** tab → **Add Key** → **Create new key** (JSON format). Download the JSON file.
5. Open the Google Sheet → **Share** → Add the `client_email` from the JSON (e.g., `your-service@project.iam.gserviceaccount.com`) with **Editor** access.
6. In Vercel dashboard: Add environment variables via CLI (`vercel env add GOOGLE_SERVICE_ACCOUNT_EMAIL` and `vercel env add GOOGLE_PRIVATE_KEY`) or UI. For `GOOGLE_PRIVATE_KEY`, paste the full value **without quotes**, replacing `\\n` with actual newlines (use a text editor or Word replace `\n` with `^p` then copy)[3][1].

## Install Dependencies

Use `google-spreadsheet` (simpler for service accounts) or `googleapis`. Install in your project root:

```bash
npm install google-spreadsheet
# Or: npm install googleapis
```

## Next.js API Route Example (`app/api/sheet/route.ts` or `pages/api/sheet.js`)

This writes to a sheet using `google-spreadsheet`. Replace `YOUR_SPREADSHEET_ID` (from sheet URL) and sheet index.

```typescript
import { GoogleSpreadsheet } from 'google-spreadsheet';
import { NextRequest, NextResponse } from 'next/server';

const doc = new GoogleSpreadsheet(process.env.SPREADSHEET_ID || 'YOUR_SPREADSHEET_ID');

[...truncated...]

## Sources

- https://console.cloud.google.com/iam-admin/serviceaccounts
- https://your-vercel-app.vercel.app/api/sheet
- https://dev.to/a0viedo/writing-to-a-google-sheet-using-serverless-2ndc
- https://cloud.google.com/blog/products/serverless/serverless-from-the-ground-up-adding-a-user-interface-with-google-sheets-part-2
- https://github.com/vercel/next.js/discussions/38430
- https://www.youtube.com/watch?v=sVURhxyc6jE
- https://vercel.com/kb/guide/how-can-i-use-files-in-serverless-functions
- https://vercel.com/docs/functions
- https://scottspence.com/posts/make-a-simple-api-endpoint-with-vercel