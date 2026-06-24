---
name: Always verify output after testing
description: After testing workflows, check the actual output (Google Sheets, emails, etc.) to confirm it worked correctly
type: feedback
---

After running any workflow test, ALWAYS verify the actual output — read the Google Sheet data, check email content, etc. Don't just confirm the workflow executed successfully; verify the data is correct and formatted properly.

**Why:** User was furious that I tested the workflow but never checked if the Google Sheet was populated correctly. Just seeing "execution succeeded" is not enough — the output could be malformed, empty, or wrong.

**How to apply:** After every workflow test, create a temp n8n workflow (HTTP Request + webhook) to read back the output destination (Google Sheets, database, etc.) and verify the data. Report findings to the user with specifics.
