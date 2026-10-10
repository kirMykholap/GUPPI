---
type: decision
case: "309"
status: archived
create: ["[[estimate-materialize-refolds-a-reading-on-a-supersede]]"]
update: ["[[rule-materialize]]"]
origin: raw/2026-09-22/1121/ledger.md#case-309
sprint: migration
created: 2026-09-22
tags: [harness, librarian, workflow, ledger]
---

## Context

An `estimate[...]` line of the ledger does not become an entry of its own when the yaml of the unit already holds an unapplied `create` of the same slug: `fold_estimate` writes `status` and `result` into that `create` and keeps the line number in `folded`. The mark `{supersedes:case N}` comes later — on the line of the next Case — and marks every entry of Case N `superseded_by`; `generate` skips them, the folded reading with them. In 0014 the readings L52 and L53 (`estimate-rules-schema-checked`, `estimate-entities-schema-checked`, both `passed`) folded into the creates of 304.2 and 304.3, which 305.1 and 306.1 replaced at once: the pages stand `pending` with no Result, `rule-rules-schema` and `rule-entities-schema` `draft`. The order in `lift_line`: the new `create` is appended to `entries` before `mark_superseded`, so at the moment of the mark the live `create` of the same slug is already there. A yaml is never rewritten — 0014 is not repaired by this; its two readings are taken again by hand (W2) and reach the pages as entries of their own in this session. `rule-materialize` `built`; of its Estimates the Case touches one new one only; `estimate-materialize-marks-superseded` it does not touch.

## Problem

A reading taken between a `create` and its `{supersedes}` is lost in silence — no `failed`, no `incomplete`, no line in the brief; it shows only as an empty Result on the page.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-309
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
