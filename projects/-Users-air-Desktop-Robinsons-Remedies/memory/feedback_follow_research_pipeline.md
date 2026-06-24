---
name: Always follow the full research pipeline
description: Never skip the Perplexity -> NotebookLM workflow for research tasks, even when results seem "clear enough"
type: feedback
---

When the research pipeline hook says "For ANY research task," it means ANY. Do not skip NotebookLM synthesis because results seem obvious. The whole point of the pipeline is that cross-source synthesis catches things you miss from individual results.

**Why:** User built this pipeline specifically for deeper analysis. Skipping steps is the same lazy pattern as saying "it should work" without verifying. NotebookLM catches cross-source patterns, conflicts, and nuances that reading individual Perplexity results does not.

**How to apply:** Every time you run Perplexity queries for research, feed the source URLs into a NotebookLM notebook and query it for synthesis. No exceptions. No "this one seems clear enough." The pipeline exists for a reason.
