---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: One Decision page per Case, written before its entries, with its lists, its body and its defers
method: uv run --project .guppi pytest .guppi/tests/test_generate.py, the tests of the Decision page
checked: 2026-10-26
origin: raw/2026-09-16/1955/ledger.md#case-201.2
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run --project .guppi guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

Then:
One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, or `superseded` for a record that carries `superseded_by`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
**＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
**＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
**＋** The page is written before the first entry of its lines, so their History lines name it.
**＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
**＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
**＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
**＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
**＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
**＋** The new page of a record that carries `superseded_by`, a Case that a later Case superseded before its entries applied, is written `superseded`, takes each slug of the record's `superseded_by` into its own `superseded_by` with one History line `superseded by decision-case-<M>` and one line of `vault/wiki/log.md` per slug, and the cascade of the same run archives it; this holds whether or not another Case retired that later Case in turn.
**－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
**－** The Decision pages already written are not rewritten.
**－** A page whose `superseded_by` already names the new page gets no second History line and no second line in `vault/wiki/log.md`, whether an earlier run put the name there or an earlier step of the same record did, such as a sub-case page reached through the `children` of its parent and named in `supersedes` too.
**－** A page in `children` that stands `archived` or `superseded` is left as it is.
**－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.
**－** A record that carries `superseded_by`, a Case that a later Case retired, still gets its page with its `supersedes`, but that `supersedes` changes no other page: no earlier page or page in its `children` changes `status` or takes the record into `superseded_by`, no target loses a `deferred_by`, and no History line and no line of `vault/wiki/log.md` names the retired page for such a change; the page of an earlier Case names the retired Case only when its own record carries it in `superseded_by`.

## Result

2026-10-26, Retro of 0118, uv run --project .guppi pytest .guppi/tests/test_generate.py: 143 passed; the new tests of case 888 — a page of A replaced by B that C retired is written superseded with superseded_by decision-case-B alone, one History line and one log.md line, no name of C, and where B stands the line comes once — pass, and the first fails on the old generate.py

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
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L56
- 2026-09-29 updated: the Criterion replaced whole — the body is Problem, Context only for a Case without given, no Given (case 513.2) · [[decision-case-513.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1753/ledger.md#L2
- 2026-09-30 updated: the Criterion replaced whole — Recommend on the page, a page for a parent Case with children and no Context, parent on a sub-case page and no Problem there (case 544.7) · [[decision-case-544.7]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — a superseded page takes the pages of its children with it (case 660.3) · [[decision-case-660.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L6
- 2026-10-06 updated: the Criterion replaced whole — a supersedes leaves an earlier page that stands archived archived, and only appends to its superseded_by (case 683) · [[decision-case-683]]
- 2026-10-06 status: pending → passed · raw/2026-10-05/2249/ledger.md#L22
- 2026-10-11 updated: the Criterion replaced whole — a page whose superseded_by already names the new page, by an earlier step of the same record too, gets no second History line and no second log line; the method is the test run alone · [[decision-case-773]]
- 2026-10-11 status: pending → passed · raw/2026-10-10/2350/ledger.md#L9
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the Criterion replaced whole — the supersedes of a retired Case changes no other page · [[decision-case-883]]
- 2026-10-26 status: pending → passed · raw/2026-10-17/2307/ledger.md#L52
- 2026-10-26 updated: the Criterion replaced whole — the new page of a record with superseded_by is written superseded · [[decision-case-888]]
- 2026-10-26 status: pending → passed · raw/2026-10-26/0118/ledger.md#L17
