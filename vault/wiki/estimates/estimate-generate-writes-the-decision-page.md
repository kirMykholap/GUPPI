---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: One Decision page per Case, written before its entries, with its lists, its body and its defers
method: pytest tests/test_generate.py, the tests of the decision page; the live reading in the librarian's run
checked: 2026-09-21
origin: raw/2026-09-16/1955/ledger.md#case-201.2
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

Given:
`guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
**＋** An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
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
**＋** A record with `superseded_by` and no `case_text` — a Case superseded in its own session and gone from the Spec — gets a two-line body: `## Context` "Superseded by `[[decision-case-M]]` in its own session, before the Spec was approved; the Case left the Spec (case 299)", `## Problem` "Decided under `[[decision-case-M]]`"; its status follows the mechanism as for any superseded page (299.4).
**－** No `## Given`, no `## When`, no `## Criterion` list: the contract lives on the Estimate; pages written before keep theirs.

## Result

2026-09-21, uv run pytest tests/test_generate.py 75 green, one new — the record of a Case with superseded_by and no case_text writes decision-case-2 with Context "Superseded by decision-case-3 in its own session, before the Spec was approved; the Case left the Spec (case 299)" and Problem "Decided under decision-case-3", the update list kept, then superseded by the page of 3 and archived by the cascade; a record with case_text writes its body as before; live — the librarian's run of this session on its ordinary records

## History

- 2026-09-16 created · [[decision-case-201.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L28
- 2026-09-21 updated: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295) · [[decision-case-295]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L3
- 2026-09-22 updated: one line of the Criterion — the page of a superseded Case without case_text has a two-line body (case 299.4) · [[decision-case-299.4]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L27
