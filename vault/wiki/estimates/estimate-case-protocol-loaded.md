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
turn. The LEDGER-block rule is the half of it a test can hold; the rest is read off the agent's
first reply.

## Criterion

At session start the agent states the LEDGER-block rule and the one-Case-at-a-time rule
without a read call, and the `then` block of a Leaf `create` it writes carries `method` and no nested `estimate` (case 72.1); and a reply whose ledger lines sit outside a LEDGER block — bare, or in
a fence with another tag or none — adds nothing to `raw/<date>/ledger.md`.

### case 73.9

When:
A session starts with `CLAUDE.md`.

Then:
The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` (the Deferred heading,
the ticked boxes) and the Frontier `raw/<date>/<hi HHMM>/frontier.md`.

### case 75.1

When:
A session starts with `CLAUDE.md`; someone reads `case-schema.md` or `index.md` §4.

Then:
The table of `case-schema.md`, §4 of the map and the ledger paragraph of the Render
show `- decision[case 12][update][rule-x]{ref:rule-x}` and
`- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` and say: the id is `case N`
with the word and a space, in `{supersedes:case N}` too.
**－** The estimate and lesson rows do not change.

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
- 2026-09-12 updated: the then block form of case 72.1 joins the criterion; pending for the next session's reading · [[decision-case-72.1]]
- 2026-09-12 criterion: case 73.9 added · [[decision-case-73.9]]
- 2026-09-12 criterion: case 75.1 added · [[decision-case-75.1]]
