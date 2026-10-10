---
type: decision
case: "323"
status: archived
update: ["[[entity-sprint-migration]]", "[[estimate-lint-catches]]", "[[estimate-prespec-checks-the-plan]]", "[[rule-harness]]", "[[estimate-harness-pipeline]]", "[[estimate-materialize-marks-superseded]]", "[[entity-glossary]]"]
origin: raw/2026-09-22/1121/ledger.md#case-323
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness, session, tests, ledger, librarian]
---

## Context

Pre-spec found seven places where a page speaks of a thing this Spec changes and no Case names it. `entity-sprint-migration` names `wiki/index.md` in its `purpose` field and in its Purpose, which 318 deletes, and counts its Estimates — 310.2 writes "four" while 310.3 and 320 create two more, making six. `estimate-lint-catches` enumerates the finding classes of lint, and 315 adds `layout`. `estimate-prespec-checks-the-plan` holds the line "Governed: an `update` item with `file` on a path a live Rule page governs", which 320 revokes. The Purpose of `rule-harness` names three steps of `make lint` without the glossary and "Four more" children — 306.5 added the fourth step, 315 adds the ninth child — while `estimate-harness-pipeline` already demands four steps: the page contradicts its own promise. `estimate-materialize-marks-superseded` describes what the mark does, and 309 adds the move of a folded reading. Two rows of `entity-glossary` — Sprint and Session — describe what 313 and 316 change. Statuses: `estimate-lint-catches` and `estimate-materialize-marks-superseded` are `passed` and go `pending`; `estimate-prespec-checks-the-plan` and `estimate-harness-pipeline` are `pending` already in this Spec.

## Problem

Seven live texts become false the moment the Spec is applied; two of them are Criteria a reading is later taken by.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-323
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
