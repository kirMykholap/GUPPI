---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: One Decision page per Case, written before its entries, with its lists, its body and its defers
method: pytest tests/test_generate.py, the tests of the decision page; the live reading in the librarian's run
checked: 2026-09-29
origin: raw/2026-09-16/1955/ledger.md#case-201.2
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

Then:
One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
**＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
**＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
**＋** The page is written before the first entry of its lines, so their History lines name it.
**＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
**＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
**＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
**＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
**－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
**－** The Decision pages already written are not rewritten.
**－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.

## Result

2026-09-29, uv run pytest tests/test_generate.py -k decision: 10 passed (the whole file 100 passed); by hand, git show --name-status d8c1f17: 12 Decision pages added under wiki/decisions and decision-case-511.2 under the archive, no existing Decision page modified; 510, 511.1, 512, 513.1-513.3, 514-516 carry ## Problem and ## History only; 517, 518, 519 carry ## Context, ## Problem, ## Deferred and ## History; 512 carries supersedes 511.2, 511.2 carries superseded_by 512 and the two-line body of case 299, archived; the History of rule-case-build names [[decision-case-512]]; the ## Deferred of 519 holds its purpose verbatim; the tags union and source were not checked

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
