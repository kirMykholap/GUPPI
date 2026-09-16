---
type: decision
case: "191"
status: current
defer: ["[[rule-page-generation]]", "[[rule-lint]]", "[[rule-pretask]]"]
supersedes: ["[[decision-case-182]]"]
origin: raw/2026-09-16/1034/ledger.md#case-191
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, session]
---

## Context

Case 182 deferred five pages in one decision: `rule-plan-mode`, `rule-materialize`,
`rule-page-generation`, `rule-lint` and `rule-pretask`. This session took two of them up —
`rule-plan-mode` in Case 187 and `rule-materialize` in Case 189. Slice 3d did not reach the
other three. Cases 186.1, 186.3 and 186.2 change those same three pages for another reason,
and those changes stand.

## Problem

A `deferred_by` mark is cleared only by superseding case 182, and one supersedes clears it
from all five targets at once. Without it the two pages taken up keep a mark that no longer
holds; with it the three untouched pages lose the mark by which they are found. So the
supersedes and a fresh defer for the remaining three belong to one Case.

## Deferred

### [[rule-page-generation]]

Slice 3d — `generate` without Criterion blocks and without `remove_criterion`; the
Criterion replaced whole; the fields `purpose`, `method`, `checked`; the recut of
`estimate-generate-writes` and `estimate-generate-walks-dates` at this touch. The
change of case 186.1 — the `## Deferred` section on a decision page — is not part of
this defer and stands ratified.

### [[rule-lint]]

Slice 3d — the finding `unread` on every `pending` and `failed` Estimate; the Estimate
schema without `## Context` and without the `## Method` section; the `unmigrated`
counter for the transition, and the removal of the old shape when it reaches zero. The
change of case 186.3 — the `deferred` finding on a placeholder — is not part of this
defer.

### [[rule-pretask]]

Slice 3d — pre-task checks the Estimates of the rule named in `context` and asks
`ask-guppi` whether an unnamed one speaks of the same thing; the checks of the old
model are removed — `method` on a Leaf `create`, `contract` on a Leaf `update`, and the
split of a Case with two Leaf contracts. The change of case 186.2 is not part of this
defer.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-191
