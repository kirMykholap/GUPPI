---
type: estimate
kind: QA
status: pending
target: rule-pretask
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Context

The skill is a short instruction plus one recorded line. What has to hold is that the line
lands where the hook looks, that the agent is dispatched once with the whole set rather
than per decision, and that nothing it returns is dropped on the floor.

## Criterion

One live run before a plan approval: the event log gains a `pretask` line, the `ask-guppi`
agent is dispatched once with the list of this Plan Mode's decisions, and every finding it
returns is either raised as a Case or named as already known in the reply.

## Method

One reading by hand, written into the estimate line — the exception the Method rule
allows.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
