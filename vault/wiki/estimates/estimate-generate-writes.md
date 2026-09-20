---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
method: pytest in tests/test_generate.py against a temp vault; the live reading once by hand
checked: 2026-09-17
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

Given:
`guppi generate` applies `set` to the frontmatter and `sections` as whole replacements; the failure of one entry touches no other (`estimate-generate-fails-alone`).
**＋** The field `method` is one line; `## Method` of the old shape is the same text as a section.
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `lint`, `materialize` and `prespec` do not change.

When:
The librarian applies the yaml of this session after the build of 211.1.

Then:
`estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-prespec-reconciles`, `-materialize-assembles` carry a `method` field with the text of their `## Method` sections in one line; `## Context` and `## Method` are dropped.
**＋** `unmigrated` reads 34 after the run: these five, `estimate-prespec-hook-gates` (213.2), `estimate-permissions` (215) and `estimate-brief-written` (209.6) leave the old shape; `estimate-documentation-completes` keeps its `### case` blocks.
**－** The Criterion of these pages does not change; no `pending` is set — except on `estimate-generate-writes`, whose Criterion 211.1 changes.

## Result

2026-09-17, `pytest tests/test_generate.py`: 48 green — an Estimate update whose set carries method writes the field after purpose and drops ## Context and ## Method, an update without set.method touches no section; the live reading is the librarian's run of this session, on the five recuts of 211.3

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L71
- 2026-09-11 updated: the criteria of the four Estimates of Cases 47–48 folded in; no skip, no paired estimate, the decision-page shape and deferred_by of Case 52; pending until the End of Work reading · [[decision-case-53.2]]
- 2026-09-11 updated: criterion: a stale failed mark is dropped on apply (case 53.3) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L76
- 2026-09-12 updated: the decision page's four lists replace the aligned pair in the criterion (case 59.4) · [[decision-case-59.4]]
- 2026-09-12 updated: the derived Estimate page and the decision page's Criterion links join the criterion (case 72.4); pending until the unit reading · [[decision-case-72.4]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L167
- 2026-09-13 criterion: case 101.1 added · [[decision-case-101.1]]
- 2026-09-13 criterion: case 104.1 added · [[decision-case-104.1]]
- 2026-09-13 criterion: case 104.2 added · [[decision-case-104.2]]
- 2026-09-13 criterion: case 104.3 added · [[decision-case-104.3]]
- 2026-09-13 criterion: case 105.3 added · [[decision-case-105.3]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L1
- 2026-09-14 criterion: case 114 added · [[decision-case-114]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L46
- 2026-09-14 criterion: case 124.2 added · [[decision-case-124.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L33
- 2026-09-14 criterion: case 142.2 added · [[decision-case-142.2]]
- 2026-09-14 criterion: case 148.1 added · [[decision-case-148.1]]
- 2026-09-14 criterion: case 151 added · [[decision-case-151]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L58
- 2026-09-15 criterion: case 124.2 removed · [[decision-case-164]]
- 2026-09-15 criterion: case 166.2 added · [[decision-case-166.2]]
- 2026-09-15 criterion: case 166.3 added · [[decision-case-166.3]]
- 2026-09-15 criterion: case 114 removed · [[decision-case-166.3]]
- 2026-09-15 criterion: case 172 added · [[decision-case-172]]
- 2026-09-15 criterion: case 148.1 removed · [[decision-case-172]]
- 2026-09-15 updated: head Criterion: no ## Children, no ## Estimates — the text of 166.2 (case 174) · [[decision-case-174]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L9
- 2026-09-16 status: passed → passed · raw/2026-09-16/1651/ledger.md#L37
- 2026-09-16 updated: the Criterion replaced whole by case 201.1 — the head recut with 101.1, 105.3, 166.2, 171 and 172; 104.x and 166.3 go to -cascades, 142.2 and 151 to -fails-alone; the ten blocks leave (case 201.1) · [[decision-case-201.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L27
- 2026-09-17 updated: one line in the Criterion — an update of an Estimate with set.method writes the field and drops · [[decision-case-211.1]]
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L49
- 2026-09-20 ref `estimate-pretask-hook-gates` → `estimate-prespec-hook-gates` · [[decision-case-261]]
- 2026-09-20 updated: the word moved: the module pretask → prespec and the slug -pretask-reconciles → -prespec-reconciles in the Criterion; the promise and the reading unchanged, passed kept (case 265) · [[decision-case-265]]
