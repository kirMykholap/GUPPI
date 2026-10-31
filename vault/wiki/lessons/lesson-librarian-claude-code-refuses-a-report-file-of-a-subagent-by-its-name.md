---
type: lesson
kind: knowledge
root_cause: Claude Code refuses the Write of a file named report.md by a subagent whatever its text or folder, and lets the same text through under another name, so the refusal judges the file name
status: new
source: by-hand probe of Case 956.2 in session 2026-10-31/0431, Claude Code 2.1.314, transcript ~/.claude/projects/c--PROJECTS-GUPPI/8727d5ce-2d69-40eb-8203-769b95b5cc28/subagents/agent-aab3ed76d9100444c.jsonl
origin: raw/2026-10-31/0431/ledger.md#L49
sprint: plugin
created: 2026-10-31
tags: [harness, librarian]
---

## Trigger

a general-purpose subagent called Write on report.md with a text in the form of a report and on report.md in a second folder with the one line hello, both outside the repository, and on close.md with the report text; both report.md calls were refused with "Subagents should return findings as text, not write report files. Include this content in your final response instead.", and close.md was written

## Root cause

Claude Code refuses the Write of a file named report.md by a subagent whatever its text or folder, and lets the same text through under another name, so the refusal judges the file name

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#L49
