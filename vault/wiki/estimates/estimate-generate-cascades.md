---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: The cascade computes built, the archive of a superseded decision that no live page names in deferred_by or addressed_by, and the severity of an Insight, never by hand
method: pytest .guppi/tests/test_generate.py, the tests of the cascade
checked: 2026-11-01
origin: raw/2026-09-16/1955/ledger.md#case-201.4
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
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

2026-11-01, Retro of session 1721: uv run --project .guppi pytest .guppi/tests/test_generate.py 154 passed, among them a superseded Decision page that a live page defers by stays superseded, is archived at the run after the last name is cleared, an Insight's addressed_by keeps one, a page standing archived keeps none, and the cascade and the judgment of sprint_close keep the same Decision pages by kept_decisions of generate.py

## History

- 2026-09-16 created · [[decision-case-201.4]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L30
- 2026-09-21 updated: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295) · [[decision-case-295]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L2
- 2026-09-22 updated: one line of the Criterion — the cascade recounts rules (case 305.3; pre-spec) · [[decision-case-305.3]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L60
- 2026-09-23 updated: the archived Estimate out of the count in the Criterion (case 328) · [[decision-case-328]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L57
- 2026-09-25 updated: the Criterion replaced whole — the cascade by the model of case 378; the rules of an Entity left to estimate-generate-writes-rules-from-applies-to (case 398.3) · [[decision-case-398.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L35
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-01 updated: the Criterion replaced whole — a superseded Decision page that a live page names in deferred_by or addressed_by is kept, by the judgment the sprint close imports · [[decision-case-982.1]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/1721/ledger.md#L30
