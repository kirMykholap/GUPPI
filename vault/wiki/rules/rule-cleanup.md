---
type: rule
kind: Leaf
purpose: Prevents an archived page from staying among the live ones
status: built
enforcement: check
implementation_ref: [guppi/cleanup.py, tests/test_cleanup.py]
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow]
core: true
---

## Purpose

Prevents an archived page from staying among the live ones. `archived` is a status the generator sets, and `guppi sprint-close` at the close of a sprint, as `rule-sprint-close` sets it. The file move
is this script's, so a page never disappears by an agent's hand. `raw/<date>/` is not
this script's: `guppi archive` moves an applied session ([[rule-raw-archive]]).

## History

- 2026-10-14 shipped with GUPPI
