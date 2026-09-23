---
type: decision
case: "371"
status: current
update: ["[[estimate-prespec-binds-a-sprint-line]]"]
origin: raw/2026-09-23/1126/ledger.md#case-371
sprint: migration
created: 2026-09-23
tags: [harness, workflow, sprint]
---

## Context

`guppi prespec --check` reads the Frontier lines; a sprint line closed `· case N` needs an `update` of the sprint page under that Case, and a line `[-] … · sprint` gives no finding. The Criterion of `estimate-prespec-binds-a-sprint-line` says of the second: "needs nothing: the item stays on the page as it is". Since Case 354.1 that is no longer so: an item put off `· sprint` in three sessions in a row goes to the Backlog by `generate`. For `prespec` the line still needs nothing, but "stays on the page as it is" contradicts 354.1; the pre-spec of session 0034 named it a known contradiction.
`estimate-prespec-binds-a-sprint-line` stands `passed`, its target `rule-prespec`; a pair inside its Criterion sets it `pending`; the move is the promise of `estimate-sprint-moves-a-passed-over-item` (`pending`), not touched; the code does not change; no `create`.

## Problem

A line of the Criterion promises the item stays on the page unchanged, while another script's rule moves it after three sessions.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-371
