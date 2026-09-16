---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: The cascade computes built, the archive of a superseded decision and the severity of an Insight, never by hand
method: pytest tests/test_generate.py, the tests of the cascade
origin: raw/2026-09-16/1955/ledger.md#case-201.4
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

Given:
`guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
**＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
**＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `materialize`, `cleanup` and `lint` do not change here.

When:
`guppi generate` runs the cascade after all entries of a unit.

Then:
An entity or rule whose Estimates are all `passed` becomes `built`; a `built` one with an Estimate not `passed` returns to `draft`; History `status: a → b · cascade`.
**＋** A Decision page with `status: superseded` becomes `archived` with History `archived · superseded`; `superseded_by` and `deferred_by` are not touched.
**＋** Every `clustered` child of an Insight with `status: actioned` becomes `archived` with History `archived · insight actioned`; the Insight's `children` does not change.
**＋** The `severity` of every Insight is recounted: a child's status is read under `wiki/lessons/`, else in the archive; a child with no page counts live; an `open` Insight at 0 becomes `archived` with History `archived · no live child`, `children` kept; an `actioned` one at 0 stays.
**－** A page without Estimates keeps its status; no section of any page is derived or touched by the cascade.

## Result

2026-09-16, `pytest tests/test_generate.py`: 46 green — built and draft from the Estimates, a superseded decision archived, the clustered children of an actioned Insight archived, severity recounted with the archive read, an open Insight at 0 archived and an actioned one kept

## History

- 2026-09-16 created · [[decision-case-201.4]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L30
