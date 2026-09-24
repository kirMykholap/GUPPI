---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: lint reads every live page against the schema of its category and prints one line per finding, exit 1 on any
method: pytest in tests/test_lint.py, one test per defect class; the live reading once by hand, written into the estimate line
checked: 2026-09-24
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` reads the live pages under `vault/wiki/<category>/`.

Then:
Each finding is one line `<category>/<slug>: <class>: <what>`; exit 1 on any finding, 0 and no output on a clean vault; nothing is written.
**＋** `schema`: a missing required field or section, a value outside the list of `values`, a conditional not met, a field of `properties.single` holding a list; `## When` is never required on a Decision page.
**＋** `schema-description`: a field or section the lists of `schema.yaml` name without a description under `fields` or `sections`, or a description of a name no list carries.
**＋** `layout`: a page whose `type` does not match its folder, a page whose `slug` field is not its filename, a `.md` at the root of `vault/wiki/` that no live rule page names.
**＋** `path`: a file named in `implementation_ref` or `governs` that does not exist.
**＋** `markers`: a page with `enforcement: render` without `## Render`, or whose Render does not open with `<!-- slug -->` and close with `<!-- /slug -->`; a page with `render_mode: full` whose Render holds a closing line `<!-- /child -->` for one of its `children`.
**－** A page under `vault/archive/` is not read.

## Result

2026-09-24, `uv run pytest tests/test_lint.py`: 69 passed

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-09 updated: criterion gains the two Method defect classes · raw/2026-09-09/ledger.md#case-26.2
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: the classes of cases 52 and 53 seeded; a lesson without estimates is clean; pending until the suite · [[decision-case-57]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L69
- 2026-09-12 updated: the decision classes of case 59.4 replace those of 52.1 in the criterion · [[decision-case-59.4]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L98
- 2026-09-12 updated: the two shapes of case 72.6 join the criterion; pending until the unit reading · [[decision-case-72.6]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L159
- 2026-09-13 criterion: case 100.3 added · [[decision-case-100.3]]
- 2026-09-13 criterion: case 103.5 added · [[decision-case-103.5]]
- 2026-09-13 criterion: case 100.3 removed · [[decision-case-103.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/0652/ledger.md#L2
- 2026-09-14 criterion: case 112.1 added · [[decision-case-112.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L47
- 2026-09-14 criterion: case 149.3 added · [[decision-case-149.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L1
- 2026-09-15 criterion: case 156 added · [[decision-case-156]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L24
- 2026-09-16 status: passed → passed · raw/2026-09-16/1651/ledger.md#L38
- 2026-09-16 updated: the Criterion replaced whole by case 202 — the head and the blocks 103.5, 112.1, 149.3, 156 recut into one, with unread, the method field and unmigrated (case 202) · [[decision-case-202]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L32
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
- 2026-09-17 updated: the method line of the Criterion — a reading on a MOC's Estimate passes beside a sibling Estimate that names a make target (case 212) · [[decision-case-212]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L51
- 2026-09-22 updated: schema-description for schema-prose — the descriptions live in the yaml, schema.md is gone (case 304.8) · [[decision-case-304.8]]
- 2026-09-22 updated: applies_to and rules under ref — the slugs and the agreement of the pair (case 305.5) · [[decision-case-305.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L58
- 2026-09-22 updated: the layout class of lint (case 323) · [[decision-case-323]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L93
- 2026-09-23 updated: the class `markers` added to the Criterion (case 325.2) · [[decision-case-325.2]]
- 2026-09-23 updated: one spelling of a reading in the Criterion — `by hand` (case 330.1) · [[decision-case-330.1]]
- 2026-09-23 updated: the Criterion names the finding on a single field holding a list (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L33
- 2026-09-25 updated: the Criterion replaced whole — the run, schema, layout, paths and markers by the model of case 378; links, statuses, method and the unmigrated count moved to their own Estimates (case 401.1) · [[decision-case-401.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L42
