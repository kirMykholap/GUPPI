---
type: estimate
kind: QA
status: pending
target: rule-documentation
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian]
---

## Context

The phase either turns every ledger line into a page, or the vault and the ledger disagree silently.

## Criterion

make test-documentation runs the tests of materialize, generate and cleanup as one
pipeline, green. Live, after the first librarian run: every decision line of the
session's ledger has a Decision page and its target page; no page exists that no
ledger line produced; the agent read only handoff.md, materialize.yaml, the five
indexes and tags.md unless a script reported a problem; its commands are in
event_log.md; its commit is separate from the session's; it did not stop to ask.

## Method

`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
