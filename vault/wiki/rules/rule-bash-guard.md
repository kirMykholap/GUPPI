---
type: rule
kind: Leaf
purpose: Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool
status: built
enforcement: hook
implementation_ref: [guppi/bashguard.py, tests/test_bashguard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [hooks, harness]
core: true
---

## Purpose

Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool. On this Windows machine the tool's shell layer interprets backslash escapes inside a heredoc body before the interpreter reads it, whatever the quoting of the marker; three sessions (H, L, M) broke edit scripts that way with the lesson live, and a heredoc that writes a file fails on quotes in its body. A heredoc with neither, fed to Python, rewrote a source file in three more sessions, and `Path.write_text` left CRLF line endings in it (`insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`): a source file changes by Edit, and a script goes into the scratchpad and runs by path. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. A script run by path or passed by `-c` or `-e` passes. The mechanism stands in the docstring of `guppi/bashguard.py`, and a PowerShell call is the rule `rule-powershell-guard`.

## History

- 2026-10-14 shipped with GUPPI
