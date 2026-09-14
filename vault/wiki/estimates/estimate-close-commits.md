---
type: estimate
kind: QA
status: passed
target: rule-close
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
---

## Context

The commit separates the librarian's layer from the session's; the report is the only thing the main agent sees of the run.

## Criterion

After a live librarian run: git log shows one commit after the Retro commit,
touching vault/ and the governed files the render wrote and nothing else, with the
message convention (case 89.2); the report reached the
main agent with the counts, the flags and the lint total; the report is twenty
lines or fewer.

### case 89.2

When:
The librarian commits.

Then:
The commit takes `vault/` and the files the render wrote: `git add vault CLAUDE.md
.claude`.
**＋** It stays one commit, separate from the session's, with the same message
convention, and never `--amend`.
**－** No path outside those three.

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## Result

the librarian of session L: commit 18907ec "docs(vault): librarian, 2026-09-13" after the Retro commits 57d68e2 and 5c4ea2a, touching vault/, .claude/agents, .claude/skills and CLAUDE.md only; its report in the transcript of 19b07bbc is 15 non-empty lines with the counts, the flags and the lint total (block 89.2)

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L93
- 2026-09-12 criterion: case 89.2 added · [[decision-case-89.2]]
- 2026-09-12 updated: the vault-only clause of the criterion names the rendered files too (case 89.2) · [[decision-case-89.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L40
