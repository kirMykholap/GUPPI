---
type: estimate
kind: QA
status: pending
target: rule-case-protocol
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Context

An instruction in `CLAUDE.md` has force only if it is in the system prompt from the first
turn. The fence rule is the half of it a test can hold; the rest is read off the agent's
first reply.

## Criterion

At session start the agent states the fence/bare-line rule and the one-Case-at-a-time rule
without a read call; and a reply whose ledger lines sit only inside a fence adds nothing to
`raw/<date>/ledger.md`.

## Method

One reading at a session start, by hand, plus the fence case of `tests/test_ledger.py`.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
