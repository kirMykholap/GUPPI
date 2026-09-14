---
type: decision
case: "121"
status: current
defer: [rule-pretask]
origin: raw/2026-09-14/0747/ledger.md#case-121
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness]
---

## Context

At pre-task of session M the dispatch to `ask-guppi` carried one summary line per decision; four of its ten findings answered things the plan's `then` blocks already did (`lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary`). `rule-ask` says "one short question"; `rule-pretask` says "dispatch the agent once with that list".

## Problem

The agent judged pages against a paraphrase and could not see the planned wording. The information it lacked must be in the dispatch: the `then` blocks — `replace` pairs, `set`, `sections` — or the path of the plan file, since the agent has Read.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-121
