---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies, or, on a MOC, neither a make target, nor pytest with a test path, nor by hand, nor guppi test on a MOC with no parent
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, each of the five forms clean, and on a MOC a test path alone, pytest alone, guppi check alone and guppi test alone with a parent as findings, a make target, pytest with a test path, by hand and guppi test alone with no parent clean
checked: 2026-10-17
origin: raw/2026-09-22/1724/ledger.md#case-331
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

Then:
A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a test path, one of the commands `guppi test`, `guppi check` and `guppi style`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
**＋** A `create` of an Estimate with no `method` at all gives the same finding.
**＋** When the target of the Estimate is a MOC as the plan leaves it — the live page, or a `create` or an `update` of the plan that writes `kind: MOC` — a `method` that names neither a `make <target>`, nor the word `pytest` with a test path, nor `by hand`, nor, on a MOC with no `parent`, the command `guppi test`, gives one line `case N: <create|update> <slug>: method of a MOC's Estimate names no make target or test files and is not a reading`, in place of the line of no form.
**＋** Whether the MOC has a `parent` is read as the plan leaves it: the `parent` that the `set` of an `update` of the plan gives, or the `parent` or the `ref` of a `create` of the plan that writes the page, else the `parent` of the live page.
**＋** The predicate is one, lifted out of `.guppi/guppi/lint.py`; `/pre-spec` writes no second one.
**＋** The form of a MOC's `method` is one predicate too, in `.guppi/guppi/lint.py`, which `check_method` of `guppi lint` calls as well, and whether a page has no `parent` is one predicate of `.guppi/guppi/pages.py`, which lint calls as well.
**－** On a MOC with a `parent`, `guppi test` alone gives the line of a MOC's `method`, and on every MOC so does `guppi check` or `guppi style` alone.
**－** Existence is not checked in the plan: the test file is written in Work Mode, and lint checks it later.
**－** Whether the `Makefile` holds the `make <target>` that a MOC's `method` names is left to lint.
**－** Whether every counted Estimate of the MOC's children is a reading, or a sibling Estimate names a form of a MOC, is left to lint.
**－** An `update` of an Estimate that writes no `method` gives no line of the form of a MOC's `method`.

## Result

2026-10-17, Retro of session 0027, uv run --project .guppi pytest .guppi/tests/test_prespec.py: 267 passed; guppi test alone is clean on a live MOC with no parent and a finding on a live MOC with a parent, on a MOC a create of the plan writes under a ref, and on a live MOC an update of the plan places under a parent; guppi check alone is a finding; lint, pre-spec and group_of of glossary.py share has_no_parent of pages.py

## History

- 2026-09-23 created · [[decision-case-331]]
- 2026-09-23 status: pending → passed · raw/2026-09-22/2046/ledger.md#L35
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.3) · [[decision-case-484.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L31
- 2026-10-08 updated: the Criterion replaced whole — pre-spec judges the method of a MOC's Estimate by its form (case 733) · [[decision-case-733]]
- 2026-10-08 status: pending → failed · raw/2026-10-08/0213/ledger.md#L8
- 2026-10-08 status: failed → passed · raw/2026-10-08/2134/ledger.md#L10
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — the commands guppi test, guppi check and guppi style are forms, and on a MOC pytest with a test path is one · [[decision-case-820.4]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L9
- 2026-10-17 updated: the Criterion replaced whole — on a MOC with no parent, guppi test is a form · [[decision-case-877.2]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/0027/ledger.md#L58
