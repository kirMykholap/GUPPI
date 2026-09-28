---
type: estimate
kind: QA
status: pending
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

When:
`uv run guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

Then:
A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a path under `tests/`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
**＋** A `create` of an Estimate with no `method` at all gives the same finding.
**＋** The predicate is one, lifted out of `guppi/lint.py`; `pre-spec` writes no second one.
**－** Existence is not checked in the plan: the file under `tests/` is written in Work Mode and lint checks it later.
**－** The branch of a MOC stays with lint: `pre-spec` does not judge whether the Estimate of a MOC needs a `make` target.

## Result

2026-09-22, uv run pytest tests/test_prespec.py -k form: 5 passed — a create whose method is prose gives `case 1: create estimate-x-again: method names no form — a make target, pytest, a tests/ file or "by hand"`, a create with no method at all gives the same line, an update carrying `set: {method: …}` gives it for its slug, and each of the four forms is clean; the predicate is `lint.names_a_form`, called by both scripts

## History

- 2026-09-23 created · [[decision-case-331]]
- 2026-09-23 status: pending → passed · raw/2026-09-22/2046/ledger.md#L35
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.3) · [[decision-case-484.3]]
