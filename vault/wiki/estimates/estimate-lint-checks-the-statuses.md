---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: A status its Estimates do not support, a draft page with core true that blocks the clean build where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, a one-time Estimate whose target is not a sprint page, and a placeholder are findings of lint, and a draft page with every Estimate passed is none where the command ship is missing
method: uv run --project .guppi pytest .guppi/tests/test_lint.py
checked: 2026-11-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the `status` of the live pages under `vault/wiki/`, and the `method`, the `target` and the `once` of each Estimate.

Then:
`status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged for these two.
**＋** `status`: where `ship_stands` of `.guppi/guppi/pages.py` finds the module of the command `ship`, each entity or rule that `is_draft_core` accepts — one with `core: true` that stands `draft` and whose `## History` holds no line that set it `built`, or one of whose Estimates stands `failed` — with Estimates or without, one finding each, and none on another `draft` page with `core: true`.
**＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
**＋** `status`: an Estimate with `once: true` whose `target` is not a sprint page `entity-sprint-<id>`, as `is_sprint_page` of `.guppi/guppi/ledger.py` judges it, one finding.
**＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
**＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
**＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
**－** `guppi lint` in a project that installed GUPPI, where `ship_stands` answers no, reports none of the pages that `is_draft_core` accepts, and no `draft` entity or rule with every Estimate `passed`, since the clean version keeps the `status` of a page and writes only its `passed` Estimates.
**－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
**－** A `failed` Estimate earns its `unread` finding whatever its `method` says.
**－** An Estimate with `once: true` whose target is a sprint page, and an Estimate without `once`, earn no finding of a one-time Estimate.

## Result

2026-11-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
