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

Given:
The cascade of `generate` computes `built` on an Entity or a Rule once each of its Estimates is `passed`; `cleanup` sets `archived`.
**＋** The guard refuses `Edit` and `Write` of a file a live Rule page names in `governs`.
**＋** `sprint_id` reads the first `## <id>` heading of `sprint.md`.
**＋** Order is the content of a page, not a field of an Entity MOC ([[rule-atomicity]], [[rule-entities-schema]]).
**－** The script writes no page of `wiki/`: it reads statuses and writes one file.

When:
Someone reads `git log` of `main` at the close of the sprint.

Then:
`make test` is green on the last commit of `migration`.
**＋** `migration` is merged into `main`; the last brief is written by the librarian on `main`.
**＋** The cascade sets `entity-sprint-migration` `built` — that is the close of the sprint; the render shows the three Done-when lines `[x]`.

## History

- 2026-09-17 created · [[decision-case-209.4]]
- 2026-09-22 updated: order as the content of a page named by its rules (case 318) · [[decision-case-318]]
