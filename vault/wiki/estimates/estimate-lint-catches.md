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
clean vault; the two Method classes (case 26.2) are seeded too, and the classes of cases 52 and 53: decision lists of unequal length, a target_slug naming no page, a deferred_by naming no decision, a History wikilink resolving to nothing, an estimate whose target is not an entity or a rule; a lesson without estimates is not a finding. Against the live vault:
the first run's findings are each either an item of the brief's known-false list or
become a Case.

## Method

pytest in `tests/test_lint.py`, one test per defect class; the live reading once by hand,
written into the estimate line.

## Result

tests/test_lint.py 32 green with the classes of cases 52 and 53 seeded: unequal decision lists, a target_slug naming no page, a deferred_by naming no decision, a History wikilink to nothing, an estimate whose target is a lesson, and a lesson that is never an orphan; live 2026-09-11 after the migrations: 259 findings, each on the known-false list — 89 ref to decision-case-52…57 pages the librarian has not written, 20 orphan and 17 status on the 21 Estimates the ledger deletes, 132 schema on the 2026-09-09 backfill and the four clustered lessons without ## Insight, 3 orphan placeholders, 1 method (documentation-completes by hand while materialize-walks-dates names a file)

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-09 updated: criterion gains the two Method defect classes · raw/2026-09-09/ledger.md#case-26.2
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: the classes of cases 52 and 53 seeded; a lesson without estimates is clean; pending until the suite · [[decision-case-57]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L69
