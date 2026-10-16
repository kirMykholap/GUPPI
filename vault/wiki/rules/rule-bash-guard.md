---
type: rule
kind: Leaf
purpose: Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/bashguard.py, .guppi/tests/test_bashguard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-bash-guard]]"]
origin: raw/2026-09-14/1029/ledger.md#case-127
sprint: migration
created: 2026-09-14
tags: [hooks, harness]
core: true
---

## Purpose

Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool. The tool's shell layer may interpret backslash escapes inside a heredoc body before the interpreter reads it, whatever the quoting of the marker, and a heredoc that writes a file fails on quotes in its body (on the Windows machine where GUPPI is built, three sessions broke edit scripts that way with the lesson live, case 127). A heredoc with neither, fed to Python, can rewrite a source file, and on Windows `Path.write_text` leaves CRLF line endings in it, so a source file changes by Edit, and a script goes into the scratchpad and runs by path (it did so in three more sessions, `insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`, case 796.1). A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. A script run by path or passed by `-c` or `-e` passes. The mechanism stands in the docstring of `.guppi/guppi/bashguard.py`, and a PowerShell call is the rule `rule-powershell-guard` (cases 127, 796.1).

## History

- 2026-09-14 deferred, placeholder · [[decision-case-120]]
- 2026-09-14 defer by decision-case-120 superseded · [[decision-case-127]]
- 2026-09-14 created over placeholder · [[decision-case-127]]
- 2026-09-14 estimate estimate-bash-guard added · [[decision-case-127]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-23 deferred · [[decision-case-382]]
- 2026-09-24 defer by decision-case-382 superseded · [[decision-case-384]]
- 2026-09-24 updated: the refusal message says the refusal is by design and no finding for Retro; the log line named as the code writes it (case 384) · [[decision-case-384]]
- 2026-09-30 updated: the refusal text sends a whole file to Write and only a script to the scratchpad (case 530.2) · [[decision-case-530.2]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 status: draft → built · cascade
- 2026-10-13 updated: a heredoc whose marker line runs an interpreter is refused; How it works removed by hand, a one-off, its facts in the docstring of guppi/bashguard.py (case 796.1) · [[decision-case-796.1]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the machine and the sessions of the Purpose move into the brackets of their pointers · [[decision-case-875]]
