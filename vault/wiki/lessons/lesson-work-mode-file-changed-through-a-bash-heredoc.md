---
type: lesson
kind: error
root_cause: the agent changed a file through Bash, which the bashguard rule forbids, since the heredoc held no backslash and passed the guard, and Path.write_text on Windows writes os.linesep
status: clustered
insight: "[[insight-workflow-file-changed-through-a-shell-command]]"
origin: raw/2026-10-07/0211/ledger.md#L49
sprint: migration
created: 2026-10-07
tags: [harness]
---

## Trigger

in Work Mode of session 0211 a python heredoc in Bash rewrote guppi/onward.py with Path.write_text, and git warned that CRLF would be replaced; the file was set back to LF by sed

## Root cause

the agent changed a file through Bash, which the bashguard rule forbids, since the heredoc held no backslash and passed the guard, and Path.write_text on Windows writes os.linesep

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#L49
- 2026-10-07 updated: clustered under insight-workflow-file-changed-through-a-shell-command (synthesis) · raw/2026-10-07/0211/ledger.md#L49
