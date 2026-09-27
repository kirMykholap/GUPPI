---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: One Decision page per Case, written before its entries, with its lists, its body and its defers
method: pytest tests/test_generate.py, the tests of the decision page; the live reading in the librarian's run
checked: 2026-09-24
origin: raw/2026-09-16/1955/ledger.md#case-201.2
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

Then:
One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
**＋** The page is written before the first entry of its lines, so their History lines name it.
**＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
**＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
**＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
**＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
**－** The page holds no `## When` and no `## Criterion`: the promise lives on the Estimate.

## Result

2026-09-24, `uv run pytest tests/test_generate.py`: 87 passed

## History

- 2026-09-16 created · [[decision-case-201.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L28
- 2026-09-21 updated: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295) · [[decision-case-295]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L3
- 2026-09-22 updated: one line of the Criterion — the page of a superseded Case without case_text has a two-line body (case 299.4) · [[decision-case-299.4]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L27
- 2026-09-25 updated: the Criterion replaced whole — the Decision page by the model of case 378; the false line on no Given out, the Given left to estimate-generate-writes-the-given (case 398.1) · [[decision-case-398.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L33
- 2026-09-27 updated: the Criterion replaced whole — a supersedes clears deferred_by only on the pages the superseding Case names (case 467.3) · [[decision-case-467.3]]
