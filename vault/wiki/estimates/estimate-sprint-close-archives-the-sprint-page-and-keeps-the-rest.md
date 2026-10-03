---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint the sprint page and its own Estimates go to the archive, and every other passed Estimate stays live
method: by hand, vault/wiki/entities/, vault/wiki/estimates/ and vault/archive/ read after the first close of a sprint
origin: raw/2026-10-03/0317/ledger.md#case-612.3
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/entities/`, `vault/wiki/estimates/` and `vault/archive/` after it.

Then:
`entity-sprint-<id>` and each Estimate its `estimates` lists stand under `vault/archive/`.
**－** Every other Estimate that stands `passed` stays under `vault/wiki/estimates/`, and the rule or Entity that lists it keeps it in `estimates`.
**－** The close does not archive the MOC `entity-sprint`.

## History

- 2026-10-03 created · [[decision-case-612.3]]
