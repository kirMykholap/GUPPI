---
type: rule
kind: Leaf
purpose: Prevents a session from running on while the person cannot see how full the context window is
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/context.py, .guppi/tests/test_context.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-context-size-shown-after-each-reply]]", "[[estimate-context-size-warns-past-the-limit]]", "[[estimate-context-size-shows-its-error]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, session]
core: true
---

## Purpose

Prevents a session from running on while the person cannot see how full the context window is. In the VS Code extension the context indicator shows only past half of the window, and `/context` is typed by hand; no hook payload carries the size, only `transcript_path`. The size is counted from the transcript, where every API call of the model carries its `usage`.

## History

- 2026-11-03 shipped with GUPPI
