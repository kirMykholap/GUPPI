---
type: rule
kind: Leaf
purpose: Prevents a here-string from feeding a script to an interpreter through the PowerShell tool
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/powershellguard.py, .guppi/tests/test_powershellguard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter]]"]
origin: raw/2026-10-13/1426/ledger.md#case-796.2
sprint: plugin
created: 2026-10-13
tags: [hooks, harness]
core: true
---

## Purpose

Prevents a here-string from feeding a script to an interpreter through the PowerShell tool. A script fed inline to Python can rewrite a source file, and on Windows `Path.write_text` leaves CRLF line endings in it (it did so in three sessions, `insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`, case 796.2). `rule-bash-guard` refuses such a heredoc before a Bash call; a here-string piped into an interpreter is the same script in PowerShell, and no check saw it before the call. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. The interpreters are judged by the one function of `.guppi/guppi/bashguard.py`, so both checks answer alike. A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` pass. The mechanism stands in the docstring of `.guppi/guppi/powershellguard.py` (case 796.2).

## History

- 2026-10-13 created · [[decision-case-796.2]]
- 2026-10-13 estimate estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter added · [[decision-case-796.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-13 status: draft → built · cascade
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the sessions of the Purpose move into the bracket of their pointer · [[decision-case-875]]
