---
type: rule
kind: Leaf
purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
status: built
enforcement: check
implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow]
core: true
---

## Purpose

Prevents a page that breaks its schema, points at nothing, claims a status its
Estimates do not support, or waits for a reading nobody took from sitting in the vault
unnoticed. Pages are written by the generator;
both drift, and nothing else reads the whole graph at once. Red is a signal, not a
gate: a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again; a placeholder is red with the count of its defers.
`make lint` runs it after `render --check`, `sprint --check`, `backlog --check` and `glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds; all six only report, so the Makefile's rule — no target writes to the tree — holds. It runs all six even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red. `parent: rule-harness` names the
MOC of the harness tools: lint runs with the renderer, in no phase of the session. The
classes and their order live in the docstring of `guppi/lint.py`.

## History

- 2026-10-14 shipped with GUPPI
