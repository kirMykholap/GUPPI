---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
checked: 2026-09-17
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

When:
A session starts with `CLAUDE.md`.

Then:
The agent states the LEDGER-block rule and the one-Case-at-a-time rule without a read
call.
**＋** The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` — the
`## Deferred` heading, the ticked boxes — and the Frontier
`raw/<date>/<hi HHMM>/frontier.md`.
**－** A reply whose ledger lines sit outside a `LEDGER` block — bare, or in a fence
with another tag or none — adds nothing to the session's ledger.

## Method

One reading at a session start, by hand, plus the preview cases of `tests/test_ledger.py`.

## Result

2026-09-17, the first turn of session 2238 read by hand: the reply to /hi stated the LEDGER-block rule and the one-Case-at-a-time rule before the Frontier, with no read of the rule or of CLAUDE.md; the Spec named as raw/<date>/<hi HHMM>/spec.md with its ## Deferred heading and the Frontier as raw/2026-09-16/2238/frontier.md; every ledger line of the session so far inside a LEDGER block

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.2
- 2026-09-12 updated: the then block form of case 72.1 joins the criterion; pending for the next session's reading · [[decision-case-72.1]]
- 2026-09-12 criterion: case 73.9 added · [[decision-case-73.9]]
- 2026-09-12 criterion: case 75.1 added · [[decision-case-75.1]]
- 2026-09-12 criterion: case 86 added · [[decision-case-86]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L43
- 2026-09-14 criterion: case 144.1 added · [[decision-case-144.1]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L6
- 2026-09-15 criterion: case 157 added · [[decision-case-157]]
- 2026-09-15 criterion: case 159 added · [[decision-case-159]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1448/ledger.md#L4
- 2026-09-15 status: passed → passed · raw/2026-09-15/1448/ledger.md#L5
- 2026-09-15 criterion: case 167 added · [[decision-case-167]]
- 2026-09-15 criterion: case 157 removed · [[decision-case-167]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L3
- 2026-09-16 updated: the Criterion replaced whole — the head text without the dead method clause, plus block 73.9; the other blocks move to their own Estimates (case 188) · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L37
- 2026-09-17 status: passed → passed · raw/2026-09-16/2238/ledger.md#L36
