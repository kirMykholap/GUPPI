---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its Decision pages go to the archive, but those a live page names in deferred_by or addressed_by
method: by hand, vault/wiki/decisions/ and vault/archive/ read after the first close of a sprint
origin: raw/2026-10-03/0317/ledger.md#case-612.1
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/decisions/` and `vault/archive/` after it.

Then:
Each Decision page under `vault/wiki/decisions/` whose `sprint` is `<id>` stands under `vault/archive/`.
**－** A Decision page that a live page names in `deferred_by` or `addressed_by` stays under `vault/wiki/decisions/`.
**－** A Decision page whose `sprint` is another sprint does not move.

## History

- 2026-10-03 created · [[decision-case-612.1]]
