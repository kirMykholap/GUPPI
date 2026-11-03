---
type: estimate
kind: QA
status: passed
target: "[[rule-shell-write-check]]"
purpose: Whether the hook after a Bash or PowerShell call turns CRLF into LF and removes a UTF-8 byte-order mark in each changed or new file of the repository and names each file it repaired, and names without a change a file in UTF-16 or not valid UTF-8
method: uv run --project .guppi pytest .guppi/tests/test_shellwrite.py
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
A call of the `Bash` or `PowerShell` tool ends, and `uv run --project .guppi guppi shellwrite` of `.guppi/guppi/shellwrite.py` on `PostToolUse` reads each file that `git` lists as changed or new and not ignored.

Then:
In each such file the hook turns every CRLF line ending into LF, and removes a UTF-8 byte-order mark at its start.
**＋** For each file it repaired, one line of `hookSpecificOutput.additionalContext` names the file and what it repaired, and tells the agent to change a file with Edit or Write, never through a shell command; a line on a removed mark also asks the agent to check the characters of the file.
**＋** A file that opens with a UTF-16 byte-order mark, or that is not valid UTF-8, is not changed: its line names the file and the fault and tells the agent to restore the file with Write.
**＋** The hook reads every changed or new file at each such call, so a file left faulty is named again at the next call.
**＋** `.claude/settings.json` registers the hook on `PostToolUse` with the matcher `Bash|PowerShell`, by the Render of `rule-hook-registry`.
**－** A file outside the repository, a file that `git` ignores, and a file with a NUL byte and no UTF-16 mark are neither read for a fault nor changed.
**－** A call that leaves no faulty file adds nothing to the context.
**－** A payload the hook cannot read, or a `git` call that fails, gives exit 0 and one line on stderr; the hook never raises.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
