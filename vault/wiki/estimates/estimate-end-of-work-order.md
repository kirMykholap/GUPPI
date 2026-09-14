---
type: estimate
kind: QA
status: passed
target: "[[rule-end-of-work]]"
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

## Result

make test-end-of-work green inside the 132; live 2026-09-10: the refusal on a dirty tree was read in session E at 11:18:24 (retro-commit-gates); this session the tree was clean at /handoff; handoff.md existed at 11:48:15 before the dispatch at 11:48:22; git log shows 893b3d9 (Retro) then 8bbfa10 (librarian) with nothing between

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L88
