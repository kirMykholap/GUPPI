---
type: lesson
kind: error
root_cause: the main agent changed a file through a shell command instead of the Edit tool, and Windows PowerShell 5.1 reads a UTF-8 file with no BOM in the ANSI code page and writes utf8 with a BOM
status: archived
insight: "[[insight-workflow-file-changed-through-a-shell-command]]"
origin: raw/2026-10-03/0115/ledger.md#L19
sprint: migration
created: 2026-10-03
tags: [workflow, session]
---

## Trigger

in Plan Mode of session 0115 the main agent appended a closer to a line of frontier.md by Get-Content -Raw and Set-Content -Encoding utf8 in PowerShell 5.1; every em dash and middle dot of the file became mojibake and a BOM was added, and the file was written again whole with the Write tool

## Root cause

the main agent changed a file through a shell command instead of the Edit tool, and Windows PowerShell 5.1 reads a UTF-8 file with no BOM in the ANSI code page and writes utf8 with a BOM

## History

- 2026-10-03 created · raw/2026-10-03/0115/ledger.md#L19
- 2026-10-07 updated: clustered under insight-workflow-file-changed-through-a-shell-command (synthesis) · raw/2026-10-07/0211/ledger.md#L49
- 2026-10-07 archived · insight actioned
- 2026-10-07 archived · cleanup
