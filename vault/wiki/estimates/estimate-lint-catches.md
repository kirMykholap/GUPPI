---
type: estimate
kind: QA
status: passed
target: rule-lint
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Context

Lint is the first reader of the whole graph. The unit cases seed one page per defect
class and pin the finding each produces; the live reading is the first pass over the
pages written by hand since Slice 0, whose findings are the debt the brief carries.

## Criterion

Against a temp vault seeded with one page per defect class, `guppi lint` names each
defective page with the class and nothing else, exits 1, and exits 0 with no output on a
clean vault; the two Method classes (case 26.2) are seeded too, and the classes of cases 52 and 53: a decision page with none of the four kind lists or with kind or target_slug still present, a slug in one of the lists naming neither a live nor an archived page, a deferred_by naming no decision, a History wikilink resolving to nothing, an estimate whose target is not an entity or a rule; a lesson without estimates is not a finding; a decision page without ## When is not a finding, a ## Criterion link resolving to no Estimate page is one, and a ### case N block of an Estimate naming no decision page is one. Against the live vault:
the first run's findings are each either an item of the brief's known-false list or
become a Case.

### case 103.5

When:
`uv run guppi lint` checks an `origin` and gathers the known slugs.

Then:
`raw/<date>/ledger.md#…` is looked for at `vault/raw/<date>/ledger.md`, then at `vault/archive/*/<date>/raw/ledger.md`; `raw/<date>/<HHMM>/ledger.md#…` at `vault/raw/<date>/<HHMM>/ledger.md`, then at `vault/archive/*/<date>/<HHMM>/raw/ledger.md`; the `[case N]` or line-number check runs on the file found.
**＋** In neither: the finding `no such ledger`; in both: the finding `two ledgers for <path>`.
**＋** The archived slugs are every `*.md` under `vault/archive/` except those under a `raw/` folder.
**＋** `estimate-lint-catches` gets a `### case 103.5` block; the block of 100.3 is removed.

### case 112.1

When:
`guppi lint` checks the Method of an Estimate whose target is a MOC.

Then:
A Method that names a `make <target>` present in the Makefile passes, whatever else it says.
**＋** Only a Method with no target is judged on "by hand": it passes when every child's Estimate says by hand, and is a finding naming the first child that names a test file.
**＋** `estimate-lint-catches` gets a `### case 112.1` block, `pending`; a test in `tests/test_lint.py` seeds a MOC's Estimate with `make lint` and "by hand" and expects no finding.

## Method

pytest in `tests/test_lint.py`, one test per defect class; the live reading once by hand,
written into the estimate line.

## Result

block 103.5 as before; block 112.1 against test_lint.py (a MOC's Estimate naming make test-root beside "by hand" is no finding) and against the vault: guppi lint 116 → 114 findings, the method findings on estimate-documentation-completes and estimate-harness-pipeline gone

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
