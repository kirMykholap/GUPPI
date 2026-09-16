---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: One Decision page per Case, written before its entries, with its lists, its body and its defers
method: pytest tests/test_generate.py, the tests of the decision page; the live reading in the librarian's run
origin: raw/2026-09-16/1955/ledger.md#case-201.2
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
`guppi generate` reaches the first entry of a Case, or a `decisions` record with no page yet.

Then:
One page `decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`, `tags` — the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`; `## Deferred` — one `### [[slug]]` per target of the `defer` lines, with its `purpose` verbatim.
**＋** The page is written before the first entry of its lines, so their History lines name it.
**＋** A `supersedes` sets the earlier page `superseded`, appends to its `superseded_by`, removes its slug from the `deferred_by` of every target of its `defer` list; an empty `deferred_by` is dropped.
**＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
**－** No `## Given`, no `## When`, no `## Criterion` list: the contract lives on the Estimate; pages written before keep theirs.

## Result

2026-09-16, `pytest tests/test_generate.py`: 46 green — one page per Case with the lists per kind, Context and Problem, ## Deferred, written before its entries; a supersedes marks the earlier page and clears deferred_by; no ## Given, no ## When, no ## Criterion list even when the record carries one

## History

- 2026-09-16 created · [[decision-case-201.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L28
