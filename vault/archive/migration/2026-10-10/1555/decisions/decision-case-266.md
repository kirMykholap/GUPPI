---
type: decision
case: "266"
status: archived
update: ["[[estimate-materialize-assembles]]"]
origin: raw/2026-09-20/0958/ledger.md#case-266
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
---

## Context

Case 238 deferred `insight-workflow-code-live-before-the-page-it-reads` with a `defer` block carrying `type` and `purpose`, as `case-schema.md` asks. Since 214.1 `materialize` lifts the keys of an item by the `schema.yaml` of the target's category: a key the schema does not name as a field is `unknown` and never reaches the page. An Insight has no `purpose` field (it has `pattern`), so the `purpose` of the defer became `unknown: [purpose]` and then `incomplete: [purpose]` — the "defer without a purpose" of the brief, though the Spec carries it. `generate.defer` writes `purpose` into a placeholder page only and sets `deferred_by` on an existing one; `deferred_of` reads `purpose` from `fields` for the `## Deferred` section of the Decision page — `decision-case-238` has none. For a Rule and an Entity `purpose` is a schema field and the same line of the Criterion does not break them; the defect shows on an Insight only. `estimate-materialize-assembles` (`passed`) carries that line of 214.1; the other eight Estimates of `rule-materialize` are not touched, and the body of the rule does not describe the lift by the schema.

## Problem

`type` and `purpose` are keys of the `defer` itself, not fields of the target; the check by the target's schema loses them on an Insight, and the Decision page stays without `## Deferred`. One line of the Criterion, `materialize.py` and a test.

## History

- 2026-09-20 created · raw/2026-09-20/0958/ledger.md#case-266
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
