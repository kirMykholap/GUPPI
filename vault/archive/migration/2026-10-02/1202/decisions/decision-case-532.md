---
type: decision
case: "532"
status: archived
defer: ["[[rule-spec-box]]"]
superseded_by: ["[[decision-case-591.5]]", "[[decision-case-593.2]]"]
origin: raw/2026-09-29/2024/ledger.md#case-532
sprint: migration
created: 2026-09-29
tags: [session, workflow, git, harness]
---

## Context

`make lint` reports two findings on `rule-spec-box`: a `schema` finding, since the page lacks the fields `kind` and `estimates`, and an `orphan` finding. The page stands `draft` with `deferred_by` on decisions 207, 219 and 232. The brief of session 1753 names the findings as a Cases item. The person put it off at the close of Plan Mode in session 2024, together with the Slice 5 items of the sprint.

## Problem

`rule-spec-box` breaks the schema of a Rule page and has no parent, so `make lint` stays red on it.

## Deferred

### [[rule-spec-box]]

make lint reports schema (the fields kind and estimates missing) and orphan on rule-spec-box; put off with the Slice 5 items in session 2024

## History

- 2026-09-30 created · raw/2026-09-29/2024/ledger.md#case-532
- 2026-10-02 superseded by decision-case-591.5 · [[decision-case-591.5]]
- 2026-10-02 superseded by decision-case-593.2 · [[decision-case-593.2]]
- 2026-10-02 archived · superseded
- 2026-10-02 archived · cleanup
