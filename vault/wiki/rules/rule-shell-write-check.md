---
type: rule
kind: Leaf
purpose: Prevents a file of the repository from keeping the CRLF line endings, the byte-order mark or the broken encoding that a Bash or PowerShell call left in it
status: built
enforcement: hook
implementation_ref: [guppi/shellwrite.py, tests/test_shellwrite.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [hooks, harness, workflow]
core: true
---

## Purpose

Prevents a file of the repository from keeping the CRLF line endings, the byte-order mark or the broken encoding that a Bash or PowerShell call left in it. On Windows, Windows PowerShell 5.1 reads a UTF-8 file in the ANSI code page and writes it back with a byte-order mark, and Python's `Path.write_text` writes CRLF line endings. The three lessons of `insight-workflow-file-changed-through-a-shell-command` came from such writes, and the guard of `rule-bash-guard`, which reads only heredocs before a Bash call, did not see them. `uv run guppi shellwrite` runs on `PostToolUse` of `Bash` and `PowerShell` and reads each file that `git` lists as changed or new and not ignored. It turns CRLF into LF and removes a UTF-8 byte-order mark, the form `.gitattributes` sets for every text file, and names each file it repaired in `hookSpecificOutput.additionalContext`; a file in UTF-16 or not valid UTF-8 it names without a change, for the agent to restore with Write. A file whose characters changed but which stays valid UTF-8 with no mark is not caught, and a shell call of a subagent is not checked, since a subagent does not inherit the project's hooks.

## History

- 2026-10-14 shipped with GUPPI
