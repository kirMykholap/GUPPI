---
type: lesson
kind: error
root_cause: case-guppi writes the new Criterion from the Case's when and then, and no check compares its lines with the lines of the Criterion it replaces
status: clustered
insight: "[[insight-case-build-promise-lines-compared-by-no-check]]"
origin: raw/2026-09-27/1819/ledger.md#L38
sprint: migration
created: 2026-09-27
tags: [session, workflow]
---

## Trigger

session 1819, Cases 459 and 460.3 replaced the Criteria of estimate-lint-checks-the-method and estimate-lint-finds-a-broken-link whole; the exact text of the method finding and the origin forms raw/<date>[/<HHMM>]/ledger.md#case-N were lost, and ask-guppi found both at pre-spec after ratification

## Root cause

case-guppi writes the new Criterion from the Case's when and then, and no check compares its lines with the lines of the Criterion it replaces

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#L38
- 2026-09-27 updated: clustered under insight-case-build-promise-lines-compared-by-no-check (synthesis) · raw/2026-09-27/1819/ledger.md#L38
