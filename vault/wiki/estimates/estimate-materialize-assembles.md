---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: One entry per record line of a ledger, its content lifted from the then block of its Case, nothing invented
method: pytest in tests/test_materialize.py against a temp vault; the live reading once by hand
checked: 2026-09-27
origin: raw/2026-09-10/ledger.md#case-31
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

Then:
`materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented.
**＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
**＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
**＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context`, `problem`, `recommend` and `given` from its parent, never `when`.
**＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
**＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
**＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
**－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.

## Result

2026-09-27, uv run pytest tests/test_materialize.py and raw/2026-09-27/1819/materialize.yaml; 86 passed; 39 ledger lines give entries with line 1–39 in order plus 5 synthesis entries, 11 decision records, 0 unparsed, incomplete only on the prefix-less slug (category) and the superseded 460.2 (criterion)

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31
- 2026-09-10 updated: criterion: an existing yaml gains only the entries of ledger lines it does not hold (the Criterion of case 31 already carries it) · raw/2026-09-10/ledger.md#case-41
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L70
- 2026-09-11 updated: criterion: the standalone estimate create maps to sections; the incomplete rule for a defer-only Case (case 56) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L77
- 2026-09-12 updated: the parent's given is inherited by a sub-case; pending for the unit reading (case 60) · [[decision-case-60]]
- 2026-09-12 updated: new_tags of a line-less Case join the criterion (case 61) · [[decision-case-61]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L99
- 2026-09-12 updated: the derived Estimate entries of case 72.3 join the criterion; pending until the unit reading · [[decision-case-72.3]]
- 2026-09-12 criterion: case 73.5 added · [[decision-case-73.5]]
- 2026-09-12 criterion: case 76 added · [[decision-case-76]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L157
- 2026-09-12 criterion: case 87 added · [[decision-case-87]]
- 2026-09-12 criterion: case 90.1 added · [[decision-case-90.1]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L207
- 2026-09-13 criterion: case 105.2 added · [[decision-case-105.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L44
- 2026-09-14 criterion: case 130.2 added · [[decision-case-130.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L36
- 2026-09-14 criterion: case 142.1 added · [[decision-case-142.1]]
- 2026-09-14 updated: the bare #L<n> of the Criterion prose in a code span, no Obsidian tag (case 148.3) · [[decision-case-148.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L55
- 2026-09-15 criterion: case 158 added · [[decision-case-158]]
- 2026-09-15 criterion: case 161 added · [[decision-case-161]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L25
- 2026-09-15 criterion: case 175 added · [[decision-case-175]]
- 2026-09-15 criterion: case 130.2 removed · [[decision-case-177]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L2
- 2026-09-16 updated: the Criterion replaced whole by this Case; the nine blocks leave — 73.5 to walks-dates, six to their own pages, 90.1 dies with the derivation (case 189) · [[decision-case-189]]
- 2026-09-16 updated: the Criterion replaced whole by case 194.1 — the head recut, the lines of 189 and the shape of the entry; the nine blocks leave (case 194.1) · [[decision-case-194.1]]
- 2026-09-16 updated: the Criterion replaced whole by case 204 — the text of 194.1 with the written Criterion winning on an update, the given without the state of pages (case 204) · [[decision-case-204]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L35
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
- 2026-09-17 updated: one line in the Criterion — fields lifted by the category's schema.yaml, an unknown key marked unknown and never written (case 214.1) · [[decision-case-214.1]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L54
- 2026-09-20 updated: the Criterion names rename among the keys lifted from the then block (case 258.3) · [[decision-case-258.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0527/ledger.md#L20
- 2026-09-20 updated: one line of the Criterion: type and purpose of a defer item reach fields whatever the target's category, the other keys by the schema as 214.1 said; pending for the reading (case 266) · [[decision-case-266]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L29
- 2026-09-20 updated: the Criterion replaced whole — reword among the keys carried from the then block, a list of pairs or incomplete (case 274.3) · [[decision-case-274.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L54
- 2026-09-21 updated: one line of the Criterion — an update item that names a part of the page changes that part alone, pending when the part is inside the Criterion; one that names none, or carries set.status, replaces the Criterion whole (case 296) · [[decision-case-296]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/1315/ledger.md#L19
- 2026-09-25 updated: the Criterion replaced whole — the assembly of an entry by the model of case 378; the filter of keys and the update of an Estimate moved to their own Estimates (case 397.1) · [[decision-case-397.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L27
- 2026-09-26 updated: the Criterion replaced whole — the line on the keys of the shape before case 189 gives way to the line that no Estimate is derived from a key (case 440.2) · [[decision-case-440.2]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L28
