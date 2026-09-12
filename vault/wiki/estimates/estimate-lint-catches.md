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

## Method

pytest in `tests/test_lint.py`, one test per defect class; the live reading once by hand,
written into the estimate line.

## Result

tests/test_lint.py green in the 258 with the three classes of 72.6 seeded: a decision page without ## When is no finding even when the yaml requires it, a ## Criterion link resolving to no Estimate page is a ref finding, a ### case N block of an Estimate naming no decision page is a ref finding, and a ### line is not a section boundary; live 2026-09-12 session J after the render and the Work Mode of Cases 72–76: guppi lint 129 findings, the same count and classes as the brief's known-false list (124 schema of the backfill and the missing ## Insight sections, 3 orphans, 1 ref literal in rule-page-generation, 1 method), none new

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
