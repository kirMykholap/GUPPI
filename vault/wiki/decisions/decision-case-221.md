---
type: decision
case: "221"
status: current
update: ["[[estimate-pretask-checks-the-plan]]"]
origin: raw/2026-09-16/2238/ledger.md#case-221
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, tests]
---

## Context

`estimate-pretask-checks-the-plan` (its Criterion written whole by Case 213.1 today) promises a finding on a `create` of an Estimate whose `ref` names no live rule or entity. `case-schema.md` says a rule with several promises is a parent Case that creates the rule and one sub-case per Estimate — the form of Case 209. `pretask --check` on this plan prints four findings: `estimate-sprint-renders-the-backlog` → `rule-sprint`, three Estimates → `entity-sprint-migration` — pages that Cases 209 and 209.2 of the same plan create. The Case touches the same promise as 213.1; the Criterion is written whole — the text of 213.1 plus one line.

## Problem

The check contradicts the schema: by its letter an Estimate of a new rule cannot be ratified in the session that creates the rule.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-221
