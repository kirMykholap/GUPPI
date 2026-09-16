---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
method: tests/test_generate.py with two dated folders; live, the librarian's first run
checked: 2026-09-16
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

Given:
`guppi generate` applies `set` to the frontmatter and `sections` as whole replacements; the failure of one entry touches no other (`estimate-generate-fails-alone`).
**＋** The field `method` is one line; `## Method` of the old shape is the same text as a section.
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `lint`, `materialize` and `pretask` do not change.

When:
The librarian applies the yaml of this session after the build of 211.1.

Then:
`estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-pretask-reconciles`, `-materialize-assembles` carry a `method` field with the text of their `## Method` sections in one line; `## Context` and `## Method` are dropped.
**＋** `unmigrated` reads 34 after the run: these five, `estimate-pretask-hook-gates` (213.2), `estimate-permissions` (215) and `estimate-brief-written` (209.6) leave the old shape; `estimate-documentation-completes` keeps its `### case` blocks.
**－** The Criterion of these pages does not change; no `pending` is set — except on `estimate-generate-writes`, whose Criterion 211.1 changes.

## Result

2026-09-16, `pytest tests/test_generate.py`: 46 green — every unit with a yaml walked in date and folder order, a unit with nothing unapplied silent, a failure on one unit reported and the walk going on with exit 1, a missing yaml named on stderr

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L95
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.3 added · [[decision-case-103.3]]
- 2026-09-14 updated: Context added from the Problem of case 43 (case 112.4) · [[decision-case-112.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L43
- 2026-09-16 updated: the Criterion replaced whole by case 201.5 — the head and block 103.3 recut into one (case 201.5) · [[decision-case-201.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L31
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
