---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread and those read failed that the sprint page does not list
method: "by hand, in the session that changes this page: the closing Case in the spec.md and the ledger.md of the last session that closed a sprint, now vault/raw/2026-10-10/1555/, read against the Criterion"
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
**＋** The close line names by `--carry` or `--archive-unread` each Estimate read `failed` in Work Mode that `entity-sprint-<id>` does not list.
**－** The close line names by `--carry` or `--archive-unread` only an Estimate still unread after Work Mode, or one read `failed` in Work Mode that `entity-sprint-<id>` does not list.

## Result

2026-10-10, Retro of session 1713, on the Criterion of Case 763.2, by hand over vault/raw/2026-10-10/1555/: the context of Case 755 in spec.md sorts the 9 pending Estimates into four groups by the moment of their method; its tasks hold a by hand task per moment Work Mode set up and one read line per Estimate; ledger.md holds the readings of group 1, whose moment came in Work Mode, and of group 2 at Retro; the close line names by --carry only the 5 Estimates of groups 3 and 4, still unread after Work Mode, and names neither `estimate-sprint-migration-lint-clean`, read failed but listed by the sprint page, nor any other; no Estimate read failed outside the sprint page, so the new line is not exercised; the new step 4 of rule-skill-sprint-close in the Spec names the same two kinds as the Criterion

## History

- 2026-10-04 created · [[decision-case-628.2]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1555/ledger.md#L5
- 2026-10-10 updated: the Criterion replaced whole — the close line also names an Estimate read failed in Work Mode that the sprint page does not list; the purpose and the method set anew · [[decision-case-763.2]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1713/ledger.md#L22
