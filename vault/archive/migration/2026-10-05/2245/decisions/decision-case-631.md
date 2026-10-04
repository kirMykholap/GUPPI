---
type: decision
case: "631"
status: archived
defer: ["[[estimate-lint-runs-every-step]]"]
superseded_by: ["[[decision-case-637.3]]"]
origin: raw/2026-10-04/1439/ledger.md#case-631
sprint: migration
created: 2026-10-04
tags: [harness, workflow]
---

## Context

`estimate-lint-runs-every-step` is read by hand at the Baseline of a `/work` whose backlog step is red, a moment no session has met, and `vault/wiki/` is written by no hand, so it cannot be staged as the method reads. In session 1439 the person added the item of a method that spoils `backlog.md` for one run of `make lint` and restores it by `git checkout`, then put it off to go to work.

## Problem

Whether the method of `estimate-lint-runs-every-step` reads `make lint` over a tree whose `backlog.md` is spoiled for the run is put off.

## Deferred

### [[estimate-lint-runs-every-step]]

Whether make lint runs all five steps when an earlier one is red; its reading waits for a Baseline whose backlog step is red, or for a method that stages one

## History

- 2026-10-04 created · raw/2026-10-04/1439/ledger.md#case-631
- 2026-10-05 superseded by decision-case-637.3 · [[decision-case-637.3]]
- 2026-10-05 archived · superseded
- 2026-10-05 archived · cleanup
