---
type: estimate
kind: QA
status: archived
target: "[[entity-sprint-migration]]"
purpose: make lint in the Work Mode of the session that closes the sprint, before the librarian's run, shows no finding, unmigrated included, but the unread of the sprint page's own Estimates and of the Estimates read only at or after the closing librarian's run, which the close line carries
method: "make lint in the Work Mode of the session that closes the sprint, before the librarian's run: exit 0, or only unread lines on the Estimates of entity-sprint-migration and on Estimates whose method names a moment at or after that librarian's run and that the close line names by --carry, each such line named in the estimate line"
checked: 2026-10-10
origin: raw/2026-09-16/2238/ledger.md#case-209.2
sprint: migration
created: 2026-09-16
tags: [sprint, tests]
---

## Criterion

When:
In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone reads `make lint` and the close line `uv run guppi sprint-close --sprint migration --apply` of `vault/raw/<date>/<hi HHMM>/spec.md`.

Then:
`make lint` prints no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero — but the `unread` lines below, and exits 0 when it prints none of them.
**－** An `unread` line on an Estimate of `entity-sprint-migration` not yet read at that moment fails nothing.
**－** An `unread` line on an Estimate whose `method` names a moment at or after the librarian's run of the closing session, and that the close line names by `--carry`, fails nothing.

## Result

2026-10-10, make lint in Work Mode of session 1555 before the librarian's run: exit 2, 10 finding lines; excused — unread on the 3 Estimates of entity-sprint-migration (leftovers-gone, lint-clean, merges) and on the 5 carried by the close line (brief-written, hi-takes-a-conserved-spec, hi-writes-frontier, sprint-close-next-session-opens-the-sprint, sprint-close-runs-in-the-librarian-run); not excused — rules/rule-morph: deferred: 3 times since case 239, and estimates/estimate-sprint-close-takes-the-readings-in-groups: unread: pending, read at Retro and not carried

## History

- 2026-09-17 created · [[decision-case-209.2]]
- 2026-09-18 updated: the Slices under Milestones, a Backlog of two plain lines (cases 229.1, 233.5) · [[decision-case-233.5]]
- 2026-09-18 updated: the Criterion replaced whole — the sprint page a Leaf under entity-sprint, its Slices and Backlog as the page holds them, no item named (case 244) · [[decision-case-244]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the one-time build of the sprint page out (case 494.1) · [[decision-case-494.1]]
- 2026-10-04 updated: the Criterion replaced whole — read in the Work Mode of the closing session, before the close (case 628.10) · [[decision-case-628.10]]
- 2026-10-04 updated: the Criterion replaced whole — an unread Estimate that the close line carries because its moment comes at or after the closing librarian's run fails nothing (case 632.4) · [[decision-case-632.4]]
- 2026-10-10 status: pending → failed · raw/2026-10-10/1555/ledger.md#L4
- 2026-10-10 status: failed → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
