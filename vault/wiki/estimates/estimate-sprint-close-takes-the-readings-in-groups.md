---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread and those read failed that the sprint page does not list
method: "by hand, after the Work Mode of a session that closed a sprint: the closing Case in the spec.md and the ledger.md of that session read against the Criterion"
checked: 2026-10-10
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Criterion

When:
The session that closes `entity-sprint-<id>` runs its Plan Mode and its Work Mode; someone reads its closing Case in `vault/raw/<date>/<hi HHMM>/spec.md` and its `vault/raw/<date>/<hi HHMM>/ledger.md` after its Work Mode.

Then:
The `context` of the closing Case sorts each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed` into groups by the kind of moment its `method` names.
**＋** The `tasks` of the closing Case hold one `by hand` task per moment that Work Mode sets up, and one `read` line per Estimate of each group.
**＋** Work Mode sets up each such moment, and the ledger holds a reading of each Estimate whose moment came.
**＋** The close line names by `--carry` or `--archive-unread` each Estimate read `failed` in Work Mode that `entity-sprint-<id>` does not list.
**－** The close line names by `--carry` or `--archive-unread` only an Estimate still unread after Work Mode, or one read `failed` in Work Mode that `entity-sprint-<id>` does not list.

## Result

2026-10-10, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
