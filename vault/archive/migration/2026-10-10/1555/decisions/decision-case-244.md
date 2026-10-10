---
type: decision
case: "244"
status: archived
update: ["[[estimate-sprint-migration-lint-clean]]"]
origin: raw/2026-09-18/1252/ledger.md#case-244
sprint: migration
created: 2026-09-18
tags: [sprint, tests]
---

## Context

`estimate-sprint-migration-lint-clean` (`pending`, target `entity-sprint-migration`) promises `make lint` exit 0 at the close of the sprint and, in the second line of its `then`, lists what the sprint page looks like: an Entity MOC, Slice 5 of three Estimates and `rule-spec-box`, a Backlog of two lines (case 229.1). Cases 239 and 241 of this Spec make the page a Leaf under `entity-sprint`, add `[[rule-morph]]` to Slice 5 and leave one line in the Backlog; both said "touches no Estimate of the sprint" — pre-task found that this one is touched. The Case touches one Estimate; `-leftovers-gone` and `-merges` it does not.

## Problem

The Criterion describes a page that will not exist after this Spec; the reading at the close would fail on the shape of the page, not on lint.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-244
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
