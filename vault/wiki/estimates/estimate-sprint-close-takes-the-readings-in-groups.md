---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread
method: "by hand, after the Work Mode of the session that closes a sprint: its closing Case, spec.md and ledger read against the Criterion"
checked: 2026-10-10
origin: raw/2026-10-04/1439/ledger.md#case-628.2
sprint: migration
created: 2026-10-04
tags: [sprint, workflow]
---

## Criterion

When:
The session that closes `entity-sprint-<id>` runs its Plan Mode and its Work Mode; someone reads its closing Case in `vault/raw/<date>/<hi HHMM>/spec.md` and its `vault/raw/<date>/<hi HHMM>/ledger.md` after its Work Mode.

Then:
The `context` of the closing Case sorts each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed` into groups by the kind of moment its `method` names.
**＋** The `tasks` of the closing Case hold one `by hand` task per moment that Work Mode sets up, and one `read` line per Estimate of each group.
**＋** Work Mode sets up each such moment, and the ledger holds a reading of each Estimate whose moment came.
**－** The close line names by `--carry` or `--archive-unread` only an Estimate still unread after Work Mode.

## Result

2026-10-10, Retro of session 1555, Case 755 in vault/raw/2026-10-10/1555/spec.md and its ledger: the context sorts the 9 pending Estimates (none failed) into 4 groups by the moment of their method; the tasks hold a by hand task for each moment Work Mode set up (the commit before make test, the preview of the close) and one read line for each of the 9; Work Mode set up both moments, and this block holds the readings of group 1 whose moment came; the close line carries only the 5 Estimates of groups 3 and 4, still unread after Work Mode, and does not name group 2, read here

## History

- 2026-10-04 created · [[decision-case-628.2]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1555/ledger.md#L5
