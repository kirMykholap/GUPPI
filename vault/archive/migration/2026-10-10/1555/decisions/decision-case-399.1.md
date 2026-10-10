---
type: decision
case: "399.1"
status: archived
update: ["[[estimate-prespec-checks-the-plan]]"]
origin: raw/2026-09-24/1916/ledger.md#case-399.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness, tests]
---

## Context

Of the two Estimates of `rule-prespec` on the list of Case 378, only one needs work. `estimate-prespec-reconciles` was rewritten whole in the new model by Case 388: no `Given:`, no line on the bounds of an edit, its text agrees with the Render `.claude/skills/pre-spec/SKILL.md`; it waits only for its reading, which is W1. `estimate-prespec-checks-the-plan` is a journal: 9 `＋` lines in `then`, a `Given:` of five lines and a `－` line on the bounds of an edit. It repeats three neighbouring Estimates:
- the mark of a `supersedes` — `estimate-prespec-catches-a-superseded-case`;
- a Frontier line of the sprint closed by a Case — `estimate-prespec-binds-a-sprint-line`;
- a `method` without a form — `estimate-prespec-catches-a-method-without-a-form`.

It carries the line on `file` twice, and its `Given:` says the Criterion is `given`, `when` and `then` — the old model.

The cut follows the functions of `guppi/prespec.py`: one function, one check, one promise, as the eleven neighbouring Estimates already stand:
- the run (`resolve_session`, `check`, `check_grammar`, the parse of `then`) stays in `-checks-the-plan`;
- `check_lines`, `check_frontier`, `check_tasks`, and `check_form` with `check_governed` become four new Estimates.

Their slugs are free. `estimate-prespec-checks-the-plan` stands `passed`, `rule-prespec` `draft`. The readings are `pytest` with no change of code. Every item an `update` or a `create` with a `ref`; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the code itself.

## Problem

One Criterion holds six checks, three of them repeat neighbours, and it still describes the old model; a fault in any check turns the whole `failed`.

## Given

`estimate-prespec-checks-the-plan` — the Estimate whose Criterion and `purpose` are replaced.
**＋** `guppi/prespec.py` — `run`, `check`, `resolve_session`, `window_lines`, `check_grammar`.
**＋** `guppi/materialize.py` — `parse_line`, `then_blocks`.
**＋** `tests/test_prespec.py` — fixes `--check`.
**＋** `vault/raw/<date>/<HHMM>/ledger.md` and the event logs — the session's window.
**＋** `raw/<unit>/ledger.md:<n>: does not parse: <text>` — the finding on a ledger line that does not parse.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-399.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
