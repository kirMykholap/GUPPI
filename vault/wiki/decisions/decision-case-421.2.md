---
type: decision
case: "421.2"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-defers-in-one-reply]]"]
origin: raw/2026-09-25/1228/ledger.md#case-421.2
sprint: migration
created: 2026-09-25
tags: [session, workflow, ledger]
---

## Context

Today a defer works by Case 405. When the person asks to defer an item, the agent in the same reply writes a short Case under `## Deferred` of the plan, shows it, and puts the `defer` line into `LEDGER`. The ratification is the person's word itself. The hook of `rule-spec-write` skips a Case that holds only defers, so a deferred Case is the one Case the agent still writes into the plan by hand. Every defer, a repeated one with the same wording included, creates a Decision page and adds it to `deferred_by`; `rule-work-mode` holds 19 decisions there. The brief carries an item of the previous Deferred list on without a new defer when no `supersedes` retired its decision (`rule-brief`). The source of such an item in the Frontier is `deferred`. What `frame-guppi` found entered the Case: the Criterion of `estimate-spec-write-copies-the-ratified-case` said the agent writes a defer, and it is replaced whole; the Criterion of `estimate-prespec-checks-the-frontier` did not know the new closer; the docstring of `guppi/ratified.py` and a test in `tests/test_ratified.py` state the old behaviour, and they are task lines.

## Problem

Who writes a deferred Case into the Spec, and whether an item already deferred and unchanged needs a decision to stay deferred.

## Given

`rule-case-protocol` — the rule of the Case: the short form of a deferred decision
**＋** `vault/wiki/case-schema.md` — its render
**＋** `estimate-case-protocol-defers-in-one-reply` — the Estimate of the reply that defers
**＋** `rule-spec-write` — the hook that writes the deferred Case

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#case-421.2
