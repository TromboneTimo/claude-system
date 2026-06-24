---
name: Schedule API workaround
description: RemoteTrigger list endpoint returns 500 but create works. Skip list, create directly.
type: feedback
---

When using the RemoteTrigger tool for scheduled agents, the `list` action may return HTTP 500 errors even when the service is operational. The `create` action works fine.

**Why:** Known issue as of April 2026 upgrade. The list endpoint is flaky but create/update/run work.

**How to apply:** Don't waste time retrying `list`. Just go straight to `create` with the full config. If you need to see existing triggers, direct the user to https://claude.ai/code/scheduled instead.
