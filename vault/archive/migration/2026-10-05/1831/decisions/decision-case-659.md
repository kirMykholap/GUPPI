---
type: decision
case: "659"
status: archived
defer: ["[[estimate-case-check-sends-back-a-faulty-case]]"]
supersedes: ["[[decision-case-658]]", "[[decision-case-653]]", "[[decision-case-653.1]]", "[[decision-case-653.2]]"]
superseded_by: ["[[decision-case-669.6]]"]
origin: raw/2026-10-05/1343/ledger.md#case-659
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Context

Case 658 put off Case 653 with one mark, `{supersedes:case 653}`. Case 653 has no decision line of its own; its lines are those of 653.1 and 653.2. `materialize` and the pre-spec check mark superseded only the entries that carry the named Case, so the three lines of 653.1 and 653.2 stand unsuperseded, and `uv run guppi prespec --check` prints three findings "no Case 653.x heading in the plan".

## Problem

Case 658 does not supersede the decision lines of 653.1 and 653.2, so the librarian would apply the updates the person put off.

## Deferred

### [[estimate-case-check-sends-back-a-faulty-case]]

A Case of case-guppi that the checks refuse goes back to it before the main agent sees it; the removal of the old path of guppi casecheck --subagent, taken by Case 653 and put off by session 1343 until estimate-case-build-writes-the-case passes live

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#case-659
- 2026-10-05 superseded by decision-case-669.6 · [[decision-case-669.6]]
- 2026-10-05 archived · superseded
- 2026-10-05 archived · cleanup
