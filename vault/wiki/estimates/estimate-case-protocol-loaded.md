---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
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

### case 86

When:
The agent writes a `then` block for a `create` whose Estimate is a Research, or whose
derived slug is taken.
**＋** A session starts with `CLAUDE.md`, which imports `case-schema.md`.

Then:
The item names them `estimate_kind` and `estimate_slug`.
**＋** `case-schema.md` says why the prefix: `kind` and `slug` on the item are the target
page's own fields.
**－** No other key of a `then` item is renamed; `method` and `contract` stay as they are.

## Method

One reading at a session start, by hand, plus the preview cases of `tests/test_ledger.py`.

## Result

live 2026-09-13 session L: the first turn assembled the Frontier without a read call and every Case of the session used the protocol as loaded — LEDGER blocks only in the acknowledging reply, one Case per reply, sub-cases with their own when/then/ratification, then blocks with method and estimate_slug (86), the Spec at raw/2026-09-13/0652/spec.md and the Frontier beside it (73.9), the case N id in every line and supersedes (75.1); the previews in the ratification quotes of ten Cases added nothing — the ledger holds exactly the 41 decision lines of the LEDGER blocks; the clause "states the rule" was met by use, not by a statement at session start

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.2
- 2026-09-12 updated: the then block form of case 72.1 joins the criterion; pending for the next session's reading · [[decision-case-72.1]]
- 2026-09-12 criterion: case 73.9 added · [[decision-case-73.9]]
- 2026-09-12 criterion: case 75.1 added · [[decision-case-75.1]]
- 2026-09-12 criterion: case 86 added · [[decision-case-86]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L43
