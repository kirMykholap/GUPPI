---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: make test green on the last commit of migration, read in the Work Mode of the session that closes it
method: make test on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run
origin: raw/2026-09-16/2238/ledger.md#case-209.4
sprint: migration
created: 2026-09-16
tags: [sprint, git, tests]
---

## Criterion

When:
In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone runs `make test` on the last commit of the branch `migration`.

Then:
`make test` is green on the last commit of `migration`.
**－** The merge of `migration` into `main` is not part of this promise: it is the first work of the session that opens the next sprint, a line of the `## Backlog` of `entity-sprint-migration`.

## History

- 2026-09-17 created · [[decision-case-209.4]]
- 2026-09-22 updated: order as the content of a page named by its rules (case 318) · [[decision-case-318]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given of another Case out, the count of Done-when lines out (case 494.3) · [[decision-case-494.3]]
- 2026-10-04 updated: the Criterion replaced whole — read before the close; the merge into main and the line on sprint.md leave this promise (case 628.9) · [[decision-case-628.9]]
