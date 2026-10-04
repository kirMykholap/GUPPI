---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: make lint exits 0 in the Work Mode of the session that closes the sprint, before the librarian's run, unmigrated included, but for the unread of the sprint page's own Estimates
method: make lint in the Work Mode of the session that closes the sprint, before the librarian's run, exit 0 — or only unread lines on the Estimates of entity-sprint-migration
origin: raw/2026-09-16/2238/ledger.md#case-209.2
sprint: migration
created: 2026-09-16
tags: [sprint, tests]
---

## Criterion

When:
In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone reads `make lint`.

Then:
`make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.

## History

- 2026-09-17 created · [[decision-case-209.2]]
- 2026-09-18 updated: the Slices under Milestones, a Backlog of two plain lines (cases 229.1, 233.5) · [[decision-case-233.5]]
- 2026-09-18 updated: the Criterion replaced whole — the sprint page a Leaf under entity-sprint, its Slices and Backlog as the page holds them, no item named (case 244) · [[decision-case-244]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the one-time build of the sprint page out (case 494.1) · [[decision-case-494.1]]
- 2026-10-04 updated: the Criterion replaced whole — read in the Work Mode of the closing session, before the close (case 628.10) · [[decision-case-628.10]]
