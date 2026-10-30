---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: An update of an Estimate changes the part it names alone, or replaces the Criterion whole
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py
checked: 2026-10-30
origin: raw/2026-09-24/1916/ledger.md#case-397.3
sprint: migration
created: 2026-09-24
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts the `update` item of an Estimate.

Then:
An item that carries `set.status` gets `sections.Criterion`, the text it writes under `sections: Criterion` or else the `when` and `then` of its Case, and keeps the status it set.
**＋** An item that writes `sections: Criterion` keeps that text and gets `set: {status: pending}` unless it set a status itself.
**＋** A written `sections.Criterion` beside any other part stands and sets `pending`.
**＋** An item that carries `change` alone gets no `sections.Criterion` and no `set`: `.guppi/guppi/generate.py` writes its History line, and the Criterion and the status of the page stand.
**＋** An item that names a part — `set` without `status`, a `replace` pair, `drop`, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
**＋** `names_a_part` of `.guppi/guppi/materialize.py` is the one judgment of an item that replaces a Criterion: `.guppi/guppi/prespec.py` imports it and `.guppi/guppi/casecheck.py` imports its notes, so an item with `change` alone counts as no promise and gets no note on the lines of the old Criterion.
**－** An item with `change` alone is not `incomplete`.
**－** An item whose `drop` names `Criterion` gets `incomplete: [criterion]`, by `drops_criterion` of `.guppi/guppi/materialize.py`, and the lift adds no `sections.Criterion` and no `set.status` to it, whatever else the item carries.

## Result

2026-10-30, Retro of session 1713, uv run --project .guppi pytest -q .guppi/tests/test_materialize.py: 143 passed; an Estimate update with drop: [Criterion] alone, and one beside set: {status: pending}, gets incomplete: [criterion] and no sections.Criterion; one with drop: [Result] gets no incomplete, no sections and no set

## History

- 2026-09-25 created · [[decision-case-397.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L29
- 2026-10-02 updated: the Criterion replaced whole — change alone lifts nothing and sets no status; set.status or a written Criterion replaces it (case 588.2) · [[decision-case-588.2]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L33
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: the Criterion replaced whole — drop is a named part, and a drop of the Criterion is incomplete · [[decision-case-935.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/1713/ledger.md#L25
