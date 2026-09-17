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
Items 1–4 of the Definition of done are today what `make lint` checks: fields by schema, Estimate pages present, no broken ref, no orphan, no status contradiction.
**＋** Lint counts the 62 findings of the Decision pages of Cases 1–28 today.

When:
Someone reads `make lint` at the close of the sprint.

Then:
`make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.
**＋** The page `entity-sprint-migration` exists: an Entity MOC, `purpose` the goal of the sprint; `## Purpose` the goal and "open since 2026-09-09"; `## Milestones` — `### Slice 3b`: `rule-work-mode`, `rule-subagent-guppi`; `### Slice 4`: the item of the promise of 209.3; `### Slice 5`: the items of the Estimates of 209.2–209.4 and `rule-spec-box`; `## Backlog` — two plain lines (case 229.1); `## Closed` — Slices 0–3d in one paragraph, 3d closed by session 1955, the recut remainder 42 by lint.
**－** Item F7 is not done on its own: today's `sprint.md` is replaced by the first render.

## History

- 2026-09-17 created · [[decision-case-209.2]]
- 2026-09-18 updated: the Slices under Milestones, a Backlog of two plain lines (cases 229.1, 233.5) · [[decision-case-233.5]]
