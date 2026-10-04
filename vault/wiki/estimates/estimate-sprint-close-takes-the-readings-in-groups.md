---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread
method: "by hand, after the Work Mode of the session that closes a sprint: its closing Case, spec.md and ledger read against the Criterion"
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

## History

- 2026-10-04 created · [[decision-case-628.2]]
