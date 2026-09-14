---
type: decision
case: "59.1"
status: current
update: ["[[rule-pretask]]", "[[estimate-pretask-reconciles]]"]
origin: raw/2026-09-12/ledger.md#case-59.1
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness]
---

## Context

Plan Mode leaves four things behind: the Frontier it opened with, the ledger lines the
Stop hook wrote at each ratification, the Spec the human approved, and the Decision pages
the librarian generates from both. In sessions G and H the four drifted: three decision
lines had no item under their Case in the Spec (`lesson-spec-then-items-unchecked-against-
ledger-lines`); the Frontier lived in the agent's memory and a plan was closed on one item
of it (`lesson-plan-mode-exited-per-frontier-item`); a Decision page shows its targets as
two lists aligned by position, unreadable; the items left over at the end of a session are
carried by the brief's counter, not by a decision.

## Problem

Each drift has a mechanical check or a form that removes it, and none is written. The
sub-cases below fix one each; they share this context and are ratified apart. In Work
Mode a fork is not a return to Plan Mode: the subagent stops, the fork is written as a
Case in the short form, shown at Retro, appended to the Spec with a `defer`, and the plan
stays unfinished until the next session (the owner, 2026-09-12; a clause of
`rule-work-mode`, Slice 3b).

## Given

`rule-pretask` (Leaf, `built`, `render`, governs `.claude/skills/pre-task/SKILL.md`, no
`implementation_ref`) lists the decisions and dispatches `ask-guppi`; its Estimate
`estimate-pretask-reconciles` (`passed`) reads "the event log gains a `pretask` line, the
`ask-guppi` agent is dispatched once … every finding raised as a Case or named as known".
**＋** `rule-pretask-hook` (`built`, `hook`, `guppi/pretask.py`) gates `ExitPlanMode` on
the `pretask` line; its payload has no plan (`lesson-hooks-exitplanmode-payload`).
**＋** `guppi/materialize.py` has `split_cases`, `then_blocks` and `find_item`, the
parsers the check reuses; `guppi/ledger.py` has `session_event_log`, the `hi` window.
**＋** The decision lines of this session are in `raw/<date>/ledger.md` before approval:
the Stop hook writes them at the reply that acknowledges ratification.
**－** `rule-spec-capture` and `guppi/spec.py` are not touched; the check runs before the
plan exists as a Spec.
**－** An `estimate` or `lesson` line is not checked: it has no item in the Spec.

## When

The person or the agent invokes `/pre-task` in a working session with a plan file.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.1
