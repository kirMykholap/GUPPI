---
type: estimate
kind: QA
status: passed
target: rule-case-protocol
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Context

An instruction in `CLAUDE.md` has force only if it is in the system prompt from the first
turn. The LEDGER-block rule is the half of it a test can hold; the rest is read off the agent's
first reply.

## Criterion

At session start the agent states the LEDGER-block rule and the one-Case-at-a-time rule
without a read call; and a reply whose ledger lines sit outside a LEDGER block — bare, or in
a fence with another tag or none — adds nothing to `raw/<date>/ledger.md`.

## Method

One reading at a session start, by hand, plus the preview cases of `tests/test_ledger.py`.

## Result

Passing. Session C start, 2026-09-09 16:29: the agent's first reply stated the fence-vs-bare
rule and one-Case-at-a-time, both from the `CLAUDE.md` imports, with no read-tool call
before the reply; the fence case of `tests/test_ledger.py` held. Since case 15.1 the same
test asserts the inverse shape — a LEDGER block records, everything else is a preview — and
the criterion's wording predates that change.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.2
