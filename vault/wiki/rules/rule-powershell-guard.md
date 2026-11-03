---
type: rule
kind: Leaf
purpose: Prevents a here-string from feeding a script to an interpreter through the PowerShell tool
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/powershellguard.py, .guppi/tests/test_powershellguard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness]
core: true
---

## Purpose

Prevents a here-string from feeding a script to an interpreter through the PowerShell tool. A script fed inline to Python can rewrite a source file, and on Windows `Path.write_text` leaves CRLF line endings in it. `rule-bash-guard` refuses such a heredoc before a Bash call; a here-string piped into an interpreter is the same script in PowerShell, and no check saw it before the call. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. The interpreters are judged by the one function of `.guppi/guppi/bashguard.py`, so both checks answer alike. A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` pass. The mechanism stands in the docstring of `.guppi/guppi/powershellguard.py`.

## History

- 2026-11-03 shipped with GUPPI
