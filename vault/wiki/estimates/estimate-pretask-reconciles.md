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

Unit: `guppi pretask --check <plan>` against a temp vault — a decision line with its item
under its own Case passes; a line without an item, an item without a line, and an item
under another sub-case's heading are each one finding, exit 1; a `defer` line matches a
`defer` item and a `file` line an item with that `file`; no `hi`, exit 0 with a line on
stderr; the frontier of the `hi` date: a missing file, an open line, a `case N` without
its heading and a `defer case N` without its item are each one finding; a Case with decision lines and
no `tasks` block, and an Estimate created or set `pending` by a `then` block that no
task names, and a `file` item on a path a Rule page governs, are each one finding. One live run before a plan approval: the check runs first and its findings are
fixed in the plan; the event log gains a `pretask` line, the `ask-guppi`
agent is dispatched once with the list of this Plan Mode's decisions, and every finding it
returns is either raised as a Case or named as already known in the reply.

## Method

One reading by hand, written into the estimate line — the exception the Method rule
allows.

## Result

/pre-task at 09:57:45 wrote the pretask line; one ask-guppi dispatch with the 30 decisions of this Plan Mode returned nine findings: five became Case 40, four were named as already known in the reply

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L75
- 2026-09-12 updated: the mechanical check of the plan against the session's decision lines joins the criterion; pending for the reading at this session's pre-task (case 59.1) · [[decision-case-59.1]]
- 2026-09-12 updated: the frontier findings join the criterion (case 59.2) · [[decision-case-59.2]]
- 2026-09-12 updated: the tasks findings join the criterion (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the governed-file finding joins the criterion (case 59.6) · [[decision-case-59.6]]
