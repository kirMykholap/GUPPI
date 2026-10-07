---
type: lesson
kind: error
root_cause: Path.write_text on Windows turns each newline into CRLF, and the agent took a shell script for an edit of several anchors instead of the Edit tool, which keeps the bytes of the file
status: clustered
insight: "[[insight-workflow-file-changed-through-a-shell-command]]"
origin: raw/2026-10-07/0425/ledger.md#L27
sprint: migration
created: 2026-10-07
tags: [workflow, harness]
---

## Trigger

in Work Mode of session 0425 the agent changed guppi/onward.py through a Python script in a Bash heredoc, Path.write_text, and git reported that CRLF would be replaced; the file held 412 CRLF line endings against 0 at HEAD, and the agent rewrote its bytes with LF before the commit

## Root cause

Path.write_text on Windows turns each newline into CRLF, and the agent took a shell script for an edit of several anchors instead of the Edit tool, which keeps the bytes of the file

## History

- 2026-10-07 created · raw/2026-10-07/0425/ledger.md#L27
- 2026-10-07 updated: clustered under insight-workflow-file-changed-through-a-shell-command (synthesis) · raw/2026-10-07/0425/ledger.md#L27
