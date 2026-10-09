---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a create item that lacks a field materialize requires, by one function of guppi/materialize.py, and gives none for a missing type
method: uv run pytest tests/test_prespec.py tests/test_materialize.py -k required_field
origin: raw/2026-10-09/0200/ledger.md#case-748.2
sprint: migration
created: 2026-10-09
tags: [harness, workflow, schema]
---

## Criterion

When:
`judge` of `guppi/prespec.py` — run by `uv run guppi prespec --check <plan> --session <id>`, by the check of a case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` item of a page of `rules`, `entities`, `estimates` or `insights` in the `then` blocks.

Then:
A `create` item that lacks a field which `guppi materialize` would name under `incomplete` gives one finding that names the Case, the slug and the missing field.
**＋** The list of required fields and the judgment of what is missing are one function of `guppi/materialize.py`, which the lift and `guppi/prespec.py` both call.
**＋** A field counts as present when the item writes it as a key or under `sections`, and the tags count as present when the item or its decision line carries them.
**－** The finding never names `type`, since the lift fills it from the category.
**－** An Estimate with no `method` gives no second finding beside the one of the form of its method.
**－** A `defer`, an `update` or a `delete` item gives no such finding.

## Result

2026-10-09, Retro, uv run pytest tests/test_prespec.py tests/test_materialize.py -k required_field: 7 passed

## History

- 2026-10-09 created · [[decision-case-748.2]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L21
