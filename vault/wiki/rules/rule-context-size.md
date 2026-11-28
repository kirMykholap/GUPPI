---
type: rule
kind: Leaf
purpose: Prevents a session from running on while the person cannot see how full the context window is
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/context.py, .guppi/tests/test_context.py, .guppi/guppi/agents.py, .guppi/tests/test_agents.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-context-size-shown-after-each-reply]]", "[[estimate-context-size-warns-past-the-limit]]", "[[estimate-context-size-shows-its-error]]", "[[estimate-context-size-agents-counts-each-agent]]"]
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [hooks, harness, session]
core: true
---

## Purpose

Prevents a session from running on while the person cannot see how full the context window is. In the VS Code extension the context indicator shows only past half of the window, and `/context` is typed by hand; no hook payload carries the size, only `transcript_path`. The size is counted from the transcript, where every API call of the model carries its `usage`. The command `guppi agents` counts from the same records the calls, tokens and seconds of the main agent and of each agent of a session, so that a choice of how agents run rests on a count.

## History

- 2026-11-28 shipped with GUPPI
