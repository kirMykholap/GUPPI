---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: The cascade computes built, the archive of a superseded decision that no live page names in deferred_by or addressed_by, and the severity of an Insight, never by hand
method: pytest .guppi/tests/test_generate.py, the tests of the cascade
checked: 2026-11-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi generate` runs the cascade after all entries of a unit.

Then:
An entity or rule whose live Estimates are all `passed` becomes `built`; a `built` one with a live Estimate not `passed` returns to `draft`; an Estimate standing `archived` with its file still under `wiki/estimates/`, or a slug with no page, is not counted; History `status: a → b · cascade`.
**＋** A Decision page with `status: superseded` becomes `archived` with History `archived · superseded`, unless a page of `vault/wiki/` that is no Decision page and does not stand `archived` names it in `deferred_by` or `addressed_by`; `superseded_by` and `deferred_by` are not touched.
**＋** Such a named Decision page stays `superseded` under `vault/wiki/decisions/`, and becomes `archived` at the first run after no such page names it.
**＋** The pages that keep a Decision page are judged by one function and one list of fields of `.guppi/guppi/generate.py`, and `.guppi/guppi/sprint_close.py` imports both for the Decision pages it keeps at the close of a sprint.
**＋** Every `clustered` child of an Insight with `status: actioned` becomes `archived` with History `archived · insight actioned`; the Insight's `children` does not change.
**＋** The `severity` of every Insight is recounted: a child's status is read under `wiki/lessons/`, else in the archive; a child with no page counts live; an `open` Insight at 0 becomes `archived` with History `archived · no live child`, `children` kept; an `actioned` one at 0 stays.
**－** A page without Estimates keeps its status, and the cascade writes no section of any page.

## Result

2026-11-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
