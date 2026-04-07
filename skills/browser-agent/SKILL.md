---
name: browser-agent
description: Control Chrome browser from the terminal. Open pages, click buttons, type text, take screenshots, extract content, upload files, save PDFs. Use for web automation, social media posting, screenshot generation, form filling, and web scraping.
---

# Browser Agent

Control Google Chrome programmatically from Claude Code. No API keys required.

## IMPORTANT GUARDRAILS

1. **Do NOT use browser-agent when curl, WebFetch, or API calls can accomplish the task.** This tool is for browser automation ONLY (clicking, form filling, screenshots, content behind login walls).
2. **Do NOT close, quit, or restart Chrome without explicitly asking the user first.** They may have important tabs open.
3. **For general web browsing, use Safari (open -a Safari).** Browser-agent is for programmatic automation, not casual browsing.

## Setup

Before using any browser command, Chrome must be running with remote debugging:

```bash
# Use your own Chrome (all your logins, bookmarks, tabs restored):
node ~/.claude/tools/browser-agent/browser.js launch --own-profile

# OR use an isolated clean profile (no logins):
node ~/.claude/tools/browser-agent/browser.js launch
```

**The `--own-profile` flag is the default recommended mode.** WARN THE USER before running this as it will:
1. Gracefully quit your running Chrome
2. Relaunch it with remote debugging enabled
3. Restore all your tabs automatically
4. Keep all your logins (X, Instagram, Gmail, etc.)

Run this once per session. If Chrome is already running with debugging, it just connects.

## Command Reference

All commands use this format:
```bash
node ~/.claude/tools/browser-agent/browser.js <command> [args]
```

### Navigation & Tab Management
```bash
browser launch                          # Start Chrome with remote debugging
browser list                            # List all open tabs with indices
browser open <url> [--new-tab]          # Navigate to URL
browser close <tab>                     # Close a tab
```

### Content & Interaction
```bash
browser click <tab> "<text or css>"     # Click element by text content or CSS selector
browser type <tab> "<text>" [--selector "<css>"] [--enter]  # Type into focused/specified element
browser elements <tab>                  # List all interactive elements (links, buttons, inputs)
browser scroll <tab> [up|down]          # Scroll the page
browser wait <tab> <ms>                 # Wait for content to load
browser upload <tab> "<selector>" "<file>"  # Upload a file to a file input
```

### Capture & Extract
```bash
browser screenshot <tab> [-o path] [--full] [--width N] [--height N] [--selector ".css"]
browser content <tab>                   # Extract text content (no HTML)
browser html <tab>                      # Get raw HTML
browser pdf <tab> [-o path]             # Save page as PDF
```

## Common Workflows

### Post to X (Twitter)
```bash
node ~/.claude/tools/browser-agent/browser.js launch
node ~/.claude/tools/browser-agent/browser.js open x.com --new-tab
node ~/.claude/tools/browser-agent/browser.js elements 0          # Find the compose button
node ~/.claude/tools/browser-agent/browser.js click 0 "Post"      # Or whatever the compose trigger is
node ~/.claude/tools/browser-agent/browser.js type 0 "Your post text here" --selector "[data-testid='tweetTextarea_0']"
node ~/.claude/tools/browser-agent/browser.js click 0 "Post"      # Submit
```

### Screenshot Instagram-sized carousel slides
```bash
# Open the HTML carousel file
node ~/.claude/tools/browser-agent/browser.js open file:///path/to/carousel.html --new-tab
# Set viewport to Instagram dimensions and screenshot
node ~/.claude/tools/browser-agent/browser.js screenshot 0 --width 1080 --height 1350 -o slide-1.png
# Scroll to next slide and repeat
node ~/.claude/tools/browser-agent/browser.js scroll 0 down
node ~/.claude/tools/browser-agent/browser.js screenshot 0 -o slide-2.png
```

### Extract data from a webpage
```bash
node ~/.claude/tools/browser-agent/browser.js open "https://example.com" --new-tab
node ~/.claude/tools/browser-agent/browser.js content 0
```

### Fill out a web form
```bash
node ~/.claude/tools/browser-agent/browser.js elements 0     # List all form fields
node ~/.claude/tools/browser-agent/browser.js type 0 "John" --selector "#firstName"
node ~/.claude/tools/browser-agent/browser.js type 0 "john@email.com" --selector "#email"
node ~/.claude/tools/browser-agent/browser.js click 0 "Submit"
```

## Important Notes

- Tab indices start at 0. Use `browser list` to see which tab is which.
- Chrome must be launched via `browser launch` first — it won't connect to a regular Chrome window.
- The `click` command tries CSS selector first, then falls back to text matching.
- For screenshots with specific dimensions (like Instagram 1080x1350), use `--width` and `--height`.
- The `--full` flag on screenshot captures the entire scrollable page.
- Use `browser wait <tab> 2000` after navigation to let dynamic content load.
- The Chrome profile is isolated at `~/.claude/tools/browser-agent/chrome-profile/` — it won't affect your regular Chrome.

## Shorthand

For convenience, you can create an alias:
```bash
alias browser="node ~/.claude/tools/browser-agent/browser.js"
```
