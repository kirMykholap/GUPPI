---
type: decision
case: "455"
status: archived
defer: ["[[rule-one-judgment-one-implementation]]"]
superseded_by: ["[[decision-case-462]]"]
origin: raw/2026-09-27/1255/ledger.md#case-455
sprint: migration
created: 2026-09-27
tags: [harness, workflow, render, tests]
---

## Context

`materialize.case_text` and `ratified.quoted_sections` both read the sections of a Case, and both judge fences by the same functions. The handoff of session 2300 named them as two copies of one judgment.

## Problem

`CLAUDE.md` calls a second copy of one judgment a defect. Which module keeps the reader, and which imports it. The person defers it to a later session.

## Deferred

### [[rule-one-judgment-one-implementation]]

materialize.case_text and ratified.quoted_sections are two copies of one section reader of a Case

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-455
- 2026-09-27 superseded by decision-case-462 · [[decision-case-462]]
- 2026-09-27 archived · superseded
- 2026-09-27 archived · cleanup
