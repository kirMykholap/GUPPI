---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its actioned Insights and its error lessons that joined no Insight go to the archive, and its knowledge lessons and open Insights stay
method: by hand, vault/wiki/insights/, vault/wiki/lessons/ and vault/archive/ read after the first close of a sprint
origin: raw/2026-10-03/0317/ledger.md#case-612.2
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/insights/`, `vault/wiki/lessons/` and `vault/archive/` after it.

Then:
Each Insight under `vault/wiki/insights/` whose `sprint` is `<id>` and that stands `actioned` stands under `vault/archive/`.
**＋** Each lesson under `vault/wiki/lessons/` whose `sprint` is `<id>`, whose `kind` is `error` and that stands `new` stands under `vault/archive/`.
**－** A lesson whose `kind` is `knowledge` stays under `vault/wiki/lessons/`.
**－** An Insight that stands `open`, and each lesson its `children` lists, stay live.

## History

- 2026-10-03 created · [[decision-case-612.2]]
