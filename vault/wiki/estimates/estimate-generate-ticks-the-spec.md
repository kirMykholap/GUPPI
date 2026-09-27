---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading or of a deleted Estimate across the Specs of raw/ — never a line of a later or a superseded Case
method: pytest tests/test_generate.py with a Spec beside the yaml, plus one reading of this session's spec.md after the librarian's run
checked: 2026-09-24
origin: raw/2026-09-17/1119/ledger.md#case-226.1
sprint: migration
created: 2026-09-17
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi generate` applied an entry of `materialize.yaml` and marked it `applied`.

Then:
For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes. Each further entry of one kind and slug in one Case ticks the next such line, in order.
**＋** For an `estimate` entry, a `create` entry with `folded` and a `delete` entry, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
**＋** In the Spec beside the yaml, for an `estimate` or a `delete` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
**＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
**＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
**＋** A `delete` entry ticks both its page line in its own Case and the `read` lines of its slug.
**－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
**－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` that fails leaves the `read` lines of its slug as they stand.
**－** A `spec.md` under `vault/archive/` is not read.

## Result

2026-09-24, `uv run pytest tests/test_generate.py`: 87 passed

## History

- 2026-09-18 created · [[decision-case-226.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L13
- 2026-09-20 updated: the Criterion replaced whole — an estimate entry and a create with a folded reading tick the read line, across the Specs of raw/ (case 270.1) · [[decision-case-270.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L53
- 2026-09-20 updated: the Criterion replaced whole — the read line of a later Case of the same unit is skipped by the ledger line numbers (case 280) · [[decision-case-280]]
- 2026-09-21 status: pending → passed · raw/2026-09-20/2106/ledger.md#L2
- 2026-09-21 updated: the Criterion replaced whole — the read line of a superseded Case is skipped by the marks of the yaml beside the Spec (case 286) · [[decision-case-286]]
- 2026-09-21 updated: the purpose by the Criterion of 286 (case 290.3) · [[decision-case-290.3]]
- 2026-09-21 updated: the Criterion of 286 restored whole, replaced by the purpose update of 290.3 (case 291.2) · [[decision-case-291.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L5
- 2026-09-22 updated: every read line of the slug in the first Spec, not the first line (case 312) · [[decision-case-312]]
- 2026-09-22 updated: no Rule-class entry reaches generate (case 320) · [[decision-case-320]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L88
- 2026-09-23 updated: the walk of the Specs in the Criterion — every live Spec, not the first that holds one (case 326) · [[decision-case-326]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L37
- 2026-09-25 updated: the Criterion replaced whole — Given out by the model of case 378, the When and Then as they stood, the case numbers out of the lines (case 401.6) · [[decision-case-401.6]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L36
- 2026-09-27 updated: the Criterion replaced whole — a delete entry ticks the read lines of its slug, with the skips of a reading (case 463) · [[decision-case-463]]
