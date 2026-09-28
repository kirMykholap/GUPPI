---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: make test green on the last commit of migration and the branch merged into main
method: make test on the last commit of migration, then git log of main after the merge
origin: raw/2026-09-16/2238/ledger.md#case-209.4
sprint: migration
created: 2026-09-16
tags: [sprint, git, tests]
---

## Criterion

When:
Someone reads `git log` of `main` at the close of the sprint.

Then:
`make test` is green on the last commit of `migration`.
**＋** `migration` is merged into `main`; the last brief is written by the librarian on `main`.
**＋** The cascade sets `entity-sprint-migration` `built` — that is the close of the sprint; `vault/wiki/sprint.md` shows every Done-when line `[x]`.

## History

- 2026-09-17 created · [[decision-case-209.4]]
- 2026-09-22 updated: order as the content of a page named by its rules (case 318) · [[decision-case-318]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given of another Case out, the count of Done-when lines out (case 494.3) · [[decision-case-494.3]]
