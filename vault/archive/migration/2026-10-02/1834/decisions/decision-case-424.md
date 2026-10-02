---
type: decision
case: "424"
status: archived
defer: ["[[rule-orchestration]]"]
superseded_by: ["[[decision-case-595.2]]"]
origin: raw/2026-09-25/1228/ledger.md#case-424
sprint: migration
created: 2026-09-25
tags: []
---

## Context

Case 416 deferred the split of `case-schema.md`: the form of a Case read by `case-guppi` only, and the orchestration of the main agent — the triage of a Frontier item, the dispatch, the acknowledging reply, `LEDGER`, defers and the one rule — as a rule of its own loaded by `/hi`. Case 419 superseded 416 and took only the core of its scheme, so the defer falls. The new rule has no page yet; this Spec changes `rule-case-protocol` in Cases 419 and 421, so the defer names the new rule, not that page. This session puts every item that needs a decision after the new scheme of Cases.

## Problem

Whether the orchestration of the main agent leaves `case-schema.md` for a rule of its own loaded by `/hi`, and `case-schema.md` goes to `case-guppi` alone.

## Deferred

### [[rule-orchestration]]

The orchestration of the main agent — the triage of a Frontier item, the dispatch of case-guppi, the acknowledging reply, LEDGER, defers and the one rule — as a rule of its own loaded by /hi, and case-schema.md read by case-guppi alone

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#case-424
- 2026-10-02 superseded by decision-case-595.2 · [[decision-case-595.2]]
- 2026-10-02 archived · superseded
- 2026-10-02 archived · cleanup
