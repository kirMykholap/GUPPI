---
type: estimate
kind: QA
status: pending
target: rule-end-of-work
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Context

The three steps only work in order: a handoff before the commit folds two layers into one diff; a librarian before the handoff has nothing to read.

## Criterion

make test-end-of-work runs the tests of the commit gate, green. Live: /handoff is
refused while the tree is dirty; handoff.md exists before the librarian is
dispatched; no commit is made between the handoff and the librarian's own.

## Method

`make test-end-of-work`, the pipeline over tests/test_gate.py; the live reading of the order by hand

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
