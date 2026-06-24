---
name: Gemini API - Call Directly, Not MCP
description: When using Gemini/NanoBanana for image generation, call the API directly via curl first. Do NOT set up MCP servers.
type: feedback
---

When generating images with Gemini (NanoBanana), call the API directly via curl. Do NOT waste time setting up MCP servers, restarting Claude Code, or troubleshooting MCP configuration.

**Why:** MCP servers require VS Code restarts to load, which wastes time and frustrates the user. Direct API calls via curl work immediately with no setup. The user has been burned multiple times by MCP setup failures.

**How to apply:**
1. First instinct: use `curl` to call `https://generativelanguage.googleapis.com/v1beta/models/` directly
2. API key is stored in settings.json under mcpServers.nanobanana-mcp.env.GOOGLE_AI_API_KEY (or ask user)
3. Decode base64 response and save to file
4. Only fall back to MCP if it happens to already be loaded and working
5. NEVER suggest restarting Claude Code to fix MCP issues
