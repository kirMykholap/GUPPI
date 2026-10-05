---
type: decision
case: "594"
status: archived
defer: ["[[rule-ledger-line-withdrawn-on-re-ratification]]"]
superseded_by: ["[[decision-case-671.2]]"]
origin: raw/2026-10-02/1202/ledger.md#case-594
sprint: migration
created: 2026-10-02
tags: []
---

## Context

At `/pre-spec` of session 1202, Cases 590 and 591 were built again on its findings and ratified again. Case 590.1 no longer carried its `update` of `rule-case-check`, and three Estimates of 591.2, 591.5 and 591.6 got new slugs. The ledger hook only appends, so the lines of the first ratification stayed in `raw/2026-10-02/1202/ledger.md`, and `guppi prespec --check` refused the exit from Plan Mode. A line is retired only by `{supersedes:case N}`, which retires every line of Case N and takes Case N out of the plan (`check_lines` of `guppi/prespec.py`). So the four sub-cases were re-issued as Cases 592 and 593. The person asked to think later about a better mechanism.

## Problem

The decision on how a Case ratified again with fewer or renamed items retires the lines of its first ratification, without a new Case that supersedes it whole, is put off.

## Deferred

### [[rule-ledger-line-withdrawn-on-re-ratification]]

Prevents a decision line of the first ratification of a Case from standing in the ledger after the Case is ratified again without its item, so that a rename or a dropped item does not need a new Case that supersedes the whole one

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-594
- 2026-10-05 superseded by decision-case-671.2 · [[decision-case-671.2]]
- 2026-10-05 archived · superseded
- 2026-10-05 archived · cleanup
