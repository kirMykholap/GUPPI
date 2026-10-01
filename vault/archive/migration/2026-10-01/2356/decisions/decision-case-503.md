---
type: decision
case: "503"
status: archived
defer: ["[[rule-prespec]]"]
superseded_by: ["[[decision-case-561.1]]"]
origin: raw/2026-09-29/0137/ledger.md#case-503
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness]
---

## Context

After `/pre-spec` the agent answers the findings in one report. The skill asks for each finding numbered, with its fix, and the decisions of the person. In session 0137 the first report took its numbers from the answer of `ask-guppi`, regrouped the findings by Case, and ran the numbers out of order. The person could not refer to them. The second report numbered the findings in one sequence and split them into two parts: the findings the agent fixes, then the decisions of the person as questions in the shape of the `grill-me` template. The person preferred it and wants it kept.

## Problem

The skill `/pre-spec` sets neither the numbering in one sequence nor the split into two parts, so the form of the report depends on the agent.

## Deferred

### [[rule-prespec]]

The report on the findings of pre-spec numbers them in one sequence and splits them in two parts — the findings the agent fixes, then the decisions of the person as questions in the grill-me shape; the form of the second report of session 0137, put off in session 0137

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-503
- 2026-10-01 superseded by decision-case-561.1 · [[decision-case-561.1]]
- 2026-10-01 archived · superseded
- 2026-10-01 archived · cleanup
