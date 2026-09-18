---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: make lint exits 0 at the close of the sprint, unmigrated included, but for the unread of the sprint page's own Estimates
method: make lint, exit 0 — or only unread lines on the Estimates of entity-sprint-migration
origin: raw/2026-09-16/2238/ledger.md#case-209.2
sprint: migration
created: 2026-09-16
tags: [sprint, tests]
---

## Criterion

Given:
Items 1–4 of the Definition of done are what `make lint` checks: fields by schema, Estimate pages present, no broken ref, no orphan, no status contradiction.
**＋** Lint counts the 62 findings of the Decision pages of Cases 1–28 today.
**＋** The sprint page is the Leaf `entity-sprint-migration` under the MOC `entity-sprint` (case 241); its Slices and its Backlog are as the page holds them at the moment of the reading (cases 229.1, 239).

When:
Someone reads `make lint` at the close of the sprint.

Then:
`make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.
**＋** The page `entity-sprint-migration` exists: an Entity Leaf under `entity-sprint`, `purpose` the goal of the sprint; `## Purpose` the goal and "open since 2026-09-09"; `## Milestones` — the Slices in order, each item a wikilink to a page or a plain line; `## Backlog` — the items without a turn; `## Closed` — Slices 0–3d in one paragraph.
**－** Item F7 is not done on its own: today's `sprint.md` is replaced by the first render.

## History

- 2026-09-17 created · [[decision-case-209.2]]
- 2026-09-18 updated: the Slices under Milestones, a Backlog of two plain lines (cases 229.1, 233.5) · [[decision-case-233.5]]
- 2026-09-18 updated: the Criterion replaced whole — the sprint page a Leaf under entity-sprint, its Slices and Backlog as the page holds them, no item named (case 244) · [[decision-case-244]]
