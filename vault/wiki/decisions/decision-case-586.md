---
type: decision
case: "586"
status: current
defer: ["[[rule-turn-start-one-judgment]]"]
origin: raw/2026-10-01/1725/ledger.md#case-586
sprint: migration
created: 2026-10-01
tags: []
---

## Context

At `/pre-spec` of session 1725, `ask-guppi` found two places that judge where the person's last prompt stands in a transcript: `turn_of_reply` in `guppi/casecheck.py` starts the turn after the last `user` record that is not `isMeta` and holds more than tool results, and the stretch of `guppi/ledger.py` starts after the last `user` record whose `origin.kind` is `human`. `rule-one-judgment-one-implementation` asks for one module or one test over the same input. Whether the two are one judgment was not checked. Case 584 stays to the docstring and its test; the person chose to put this question off.

## Problem

The decision whether the two predicates are one judgment, and how they come to agree, is put off.

## Deferred

### [[rule-turn-start-one-judgment]]

Prevents the start of the person's turn in a transcript from being judged by two predicates that can answer differently - turn_of_reply in guppi/casecheck.py, after the last user record not isMeta that holds more than tool results, and the stretch of guppi/ledger.py, after the last user record whose origin.kind is human; whether they are one judgment under rule-one-judgment-one-implementation

## History

- 2026-10-01 created · raw/2026-10-01/1725/ledger.md#case-586
