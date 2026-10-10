---
type: lesson
kind: error
root_cause: a test double copies the exact signature instead of accepting extra positional arguments, and a test asserts the complete output of a checker rather than the finding it is about, so any additive change fails tests that are not about it
status: archived
origin: raw/2026-09-22/1121/ledger.md#L97
sprint: migration
created: 2026-09-22
tags: [tests, harness]
---

## Trigger

adding a parameter to materialize.decision_entry broke two tests whose monkeypatched double copied the old signature, and adding the lint class `layout` broke two generate tests that asserted the whole finding list of a synthetic seed

## Root cause

a test double copies the exact signature instead of accepting extra positional arguments, and a test asserts the complete output of a checker rather than the finding it is about, so any additive change fails tests that are not about it

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#L97
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
