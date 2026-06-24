---
name: API Keys Location
description: Where API keys are stored on Timo's machine. Check here FIRST before searching the filesystem.
type: reference
originSessionId: 1c7e814e-9291-4825-901f-28fef5aa6803
---
# API Keys Storage Convention

All API keys are exported from `~/.zshrc` as environment variables.

**Before searching anywhere else for an API key, grep `~/.zshrc` for `API_KEY` or the service name.**

## Known keys
- `GOOGLE_AI_API_KEY`: Gemini (also see `reference_gemini_image_api.md`)
- `FIREFLIES_API_KEY`: Fireflies GraphQL API (https://api.fireflies.ai/graphql)

## How to use in Bash tool
Zsh loads `~/.zshrc` for interactive shells, but Bash tool invocations may not. Either:
- `source ~/.zshrc && echo $FIREFLIES_API_KEY` (one-liner)
- Or grep the value directly: `grep FIREFLIES_API_KEY ~/.zshrc`

## Fireflies API quick reference
- Endpoint: `https://api.fireflies.ai/graphql`
- Auth header: `Authorization: Bearer $FIREFLIES_API_KEY`
- Transcript by ID: `query { transcript(id: "...") { id title sentences { index speaker_name text start_time } } }`
- Transcript URLs look like `https://app.fireflies.ai/view/<slug>::<TRANSCRIPT_ID>`. The ID is after the `::`.
