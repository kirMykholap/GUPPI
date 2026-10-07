---
type: insight
pattern: The agent changes a file through a shell command instead of the Edit or Write tool, and the Windows tool on the way rewrites the file's bytes, its encoding or its line endings
status: open
children: ["[[lesson-session-frontier-rewritten-through-powershell]]", "[[lesson-work-mode-file-changed-through-a-bash-heredoc]]", "[[lesson-work-mode-code-rewritten-through-python-write-text]]"]
severity: 3
origin: raw/2026-10-07/0211/ledger.md#L49
sprint: migration
created: 2026-10-07
tags: [workflow, session, harness]
---

## Pattern

Two lessons, one cause. In Plan Mode of session 0115 the main agent appended a closer to frontier.md by Get-Content and Set-Content in PowerShell 5.1, which read the UTF-8 file in the ANSI code page and wrote it back with a BOM and mojibake. In Work Mode of session 0211 a python heredoc in Bash rewrote guppi/onward.py with Path.write_text, which on Windows writes os.linesep, and git warned of CRLF; the heredoc held no backslash, so the bashguard guard let it through.

## Proposal

A suggestion: let the bashguard guard judge any shell command that writes a file of the tree, not only a heredoc that holds a backslash, and name the Edit tool in its refusal; the same for a PowerShell call that writes a file.

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#L49
- 2026-10-07 updated: child lesson-work-mode-code-rewritten-through-python-write-text added (synthesis) · raw/2026-10-07/0425/ledger.md#L27
