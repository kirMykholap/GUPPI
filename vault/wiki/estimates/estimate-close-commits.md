---
type: estimate
kind: QA
status: pending
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

live 2026-09-10: git log shows one commit 8bbfa10 `docs(vault): librarian, 2026-09-10` after the Retro commit 893b3d9, 19 files all under vault/, no --amend; the report reached the main agent with the counts per category, thirteen flags and the lint total (169 findings, render --check exit 1); the report is 16 lines

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L93
- 2026-09-12 criterion: case 89.2 added · [[decision-case-89.2]]
- 2026-09-12 updated: the vault-only clause of the criterion names the rendered files too (case 89.2) · [[decision-case-89.2]]
