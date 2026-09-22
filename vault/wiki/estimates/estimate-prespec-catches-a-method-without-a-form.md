---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies
method: pytest tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, and each of the four forms clean
checked: 2026-09-22
origin: raw/2026-09-22/1724/ledger.md#case-331
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

Given:
`check_method` takes, for the Estimate of a Leaf, `by hand`, a path under `tests/`, the word `pytest` or a `make <target>`; the existence of the file and of the target is checked separately, after the match.
**＋** At the moment of `pre-spec` the test file does not exist: it is written in Work Mode.
**＋** `materialize` lifts `kind`, `purpose` and `method` for a `create` of an Estimate; a missing one is `incomplete`.
**＋** The branch of a MOC depends on the Estimates of its children and of its siblings.

When:
`uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

Then:
A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the four forms, gives one line: `case N: <create|update> <slug>: method names no form — a make target, pytest, a tests/ file or "by hand"`.
**＋** A `create` of an Estimate with no `method` at all gives the same finding.
**＋** The predicate is one, lifted out of `guppi/lint.py`; `pre-spec` writes no second one.
**－** Existence is not checked in the plan: the file under `tests/` is written in Work Mode and lint checks it later.
**－** The branch of a MOC stays with lint: `pre-spec` does not judge whether the Estimate of a MOC needs a `make` target.
**－** The behaviour of lint does not change — lifting the predicate is a refactor, and `estimate-lint-catches` is not touched.

## Result

2026-09-22, uv run pytest tests/test_prespec.py -k form: 5 passed — a create whose method is prose gives `case 1: create estimate-x-again: method names no form — a make target, pytest, a tests/ file or "by hand"`, a create with no method at all gives the same line, an update carrying `set: {method: …}` gives it for its slug, and each of the four forms is clean; the predicate is `lint.names_a_form`, called by both scripts

## History

- 2026-09-23 created · [[decision-case-331]]
- 2026-09-23 status: pending → passed · raw/2026-09-22/2046/ledger.md#L35
