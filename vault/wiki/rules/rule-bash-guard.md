---
type: rule
kind: Leaf
purpose: Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/bashguard.py, .guppi/tests/test_bashguard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-bash-guard]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness]
core: true
---

## Purpose

Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool. The tool's shell layer may interpret backslash escapes inside a heredoc body before the interpreter reads it, whatever the quoting of the marker, and a heredoc that writes a file fails on quotes in its body. A heredoc with neither, fed to Python, can rewrite a source file, and on Windows `Path.write_text` leaves CRLF line endings in it, so a source file changes by Edit, and a script goes into the scratchpad and runs by path. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. A script run by path or passed by `-c` or `-e` passes. The mechanism stands in the docstring of `.guppi/guppi/bashguard.py`, and a PowerShell call is the rule `rule-powershell-guard`.

## History

- 2026-11-03 shipped with GUPPI
