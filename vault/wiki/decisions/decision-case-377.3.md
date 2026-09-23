---
type: decision
case: "377.3"
status: current
update: ["[[rule-materialize]]", "[[estimate-materialize-carries-addresses]]"]
origin: raw/2026-09-23/1355/ledger.md#case-377.3
sprint: migration
created: 2026-09-23
tags: [harness, workflow, ledger]
---

## Context

The mark `{addresses:<lesson slug>}` on a decision line gives the lesson entry `addressed_by`, and the synthesis keeps an Insight closed by that field. When the lesson is written after the decision, the lesson line carries the mark, `{addressed_by:case N}` (Case 379); `materialize` must carry it to the same field by the same code. The Criterion of `estimate-materialize-carries-addresses` speaks of the decision's mark alone; it is replaced whole by one promise — the lesson entry gets `addressed_by` whichever line set it. `rule-materialize` stands `built`; its other ten Estimates speak of other things. Shown again in the model of Case 378: the first showing appended a line inside the Criterion, which 378.4 refuses.

## Problem

A lesson can reach the ledger after the decision that already closed its cause. Then the mark has no place, the synthesis opens the Insight again, and a Case is spent on a fact the yaml already holds. Apart from that, the Insight stands `open` now.

## Given

`guppi/materialize.py` — builds the yaml of a unit from its ledger: `parse_line`, `mark_addressed`.
**＋** `tests/test_materialize.py` — fixes the assembly on a temp ledger.
**＋** `rule-materialize` — states the marks in its Purpose.
**＋** `estimate-materialize-carries-addresses` — the promise, its Criterion replaced whole.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-377.3
