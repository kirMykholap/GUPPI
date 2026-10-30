---
type: rule
kind: Leaf
purpose: Prevents a file of the repository from keeping the CRLF line endings, the byte-order mark or the broken encoding that a Bash or PowerShell call left in it
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/shellwrite.py, .guppi/tests/test_shellwrite.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-shell-write-check-repairs-and-reports]]"]
origin: raw/2026-10-07/0636/ledger.md#case-710.1
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow]
core: true
---

## Purpose

Prevents a file of the repository from keeping the CRLF line endings, the byte-order mark or the broken encoding that a Bash or PowerShell call left in it. On Windows, Windows PowerShell 5.1 reads a UTF-8 file in the ANSI code page and writes it back with a byte-order mark, and Python's `Path.write_text` writes CRLF line endings. The guard of `rule-bash-guard`, which reads only heredocs before a Bash call, does not see such writes (the three lessons of `insight-workflow-file-changed-through-a-shell-command` came from them, case 710.1). `uv run --project .guppi guppi shellwrite` runs on `PostToolUse` of `Bash` and `PowerShell` and reads each file that `git` lists as changed or new and not ignored. It turns CRLF into LF and removes a UTF-8 byte-order mark, the form `.gitattributes` sets for every text file, and names each file it repaired in `hookSpecificOutput.additionalContext`; a file in UTF-16 or not valid UTF-8 it names without a change, for the agent to restore with Write. A file whose characters changed but which stays valid UTF-8 with no mark is not caught (case 710.1). A shell call of a subagent is checked the same way, since Claude Code runs the hooks of `.claude/settings.json` inside a subagent too.

## History

- 2026-10-07 created · [[decision-case-710.1]]
- 2026-10-07 estimate estimate-shell-write-check-repairs-and-reports added · [[decision-case-710.1]]
- 2026-10-07 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the lessons of the Purpose move into the bracket of their pointer · [[decision-case-875]]
- 2026-10-31 updated: a shell call of a subagent is checked, since Claude Code runs the project's hooks inside a subagent · [[decision-case-946.2]]
