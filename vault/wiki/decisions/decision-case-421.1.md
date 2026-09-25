---
type: decision
case: "421.1"
status: current
create: ["[[estimate-spec-write-writes-a-defer]]"]
update: ["[[rule-spec-write]]", "[[estimate-spec-write-copies-the-ratified-case]]", "[[estimate-spec-write-checks-the-written-case]]"]
origin: raw/2026-09-25/1228/ledger.md#case-421.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow, session]
---

## Context

Today a defer works by Case 405. When the person asks to defer an item, the agent in the same reply writes a short Case under `## Deferred` of the plan, shows it, and puts the `defer` line into `LEDGER`. The ratification is the person's word itself. The hook of `rule-spec-write` skips a Case that holds only defers, so a deferred Case is the one Case the agent still writes into the plan by hand. Every defer, a repeated one with the same wording included, creates a Decision page and adds it to `deferred_by`; `rule-work-mode` holds 19 decisions there. The brief carries an item of the previous Deferred list on without a new defer when no `supersedes` retired its decision (`rule-brief`). The source of such an item in the Frontier is `deferred`. What `frame-guppi` found entered the Case: the Criterion of `estimate-spec-write-copies-the-ratified-case` said the agent writes a defer, and it is replaced whole; the Criterion of `estimate-prespec-checks-the-frontier` did not know the new closer; the docstring of `guppi/ratified.py` and a test in `tests/test_ratified.py` state the old behaviour, and they are task lines.

## Problem

Who writes a deferred Case into the Spec, and whether an item already deferred and unchanged needs a decision to stay deferred.

## Given

`rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
**＋** `guppi/ratified.py` — the hook
**＋** `tests/test_ratified.py` — its tests
**＋** `estimate-spec-write-copies-the-ratified-case` — its Estimate of the write, whose exception for a defer goes
**＋** `estimate-spec-write-checks-the-written-case` — its Estimate of the check after the write, which names a defer-only Case
**＋** `estimate-spec-write-writes-a-defer` — the new Estimate of the write of a defer
**＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec in the session's folder, where a defer of Retro goes

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#case-421.1
