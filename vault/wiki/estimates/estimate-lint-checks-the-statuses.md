---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: A status its Estimates do not support, a draft page with core true that blocks the clean build where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, a one-time Estimate whose target is not a sprint page, and a placeholder are findings of lint, and a draft page with every Estimate passed is none where the command ship is missing
method: uv run --project .guppi pytest .guppi/tests/test_lint.py
checked: 2026-11-02
origin: raw/2026-09-24/1916/ledger.md#case-401.3
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
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

2026-11-02, Retro of session 2227, uv run --project .guppi pytest .guppi/tests/test_lint.py: 124 passed — the draft core finding only on a page never built or with a failed Estimate where ship stands, none where it is missing, a draft page with every Estimate passed a finding only where ship stands, and the other status, unread, once and deferred findings as before; guppi check of the working tree now prints rule-case-build, rule-morph and rule-skill-approve-spec as draft core pages, in place of eight

## History

- 2026-09-25 created · [[decision-case-401.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L44
- 2026-10-13 updated: the Criterion and purpose replaced whole — a pending Estimate whose method waits for a later moment earns no unread finding (case 799) · [[decision-case-799]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1426/ledger.md#L26
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — a draft page with core: true is a status finding where the module of ship stands · [[decision-case-822.9]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L8
- 2026-10-31 updated: the Criterion replaced whole — a one-time Estimate whose target is not a sprint page is a status finding · [[decision-case-969.2]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/1831/ledger.md#L31
- 2026-11-02 updated: the purpose names the draft pages with core: true that block the clean build, and the draft page that is no finding in an installed project · [[decision-case-996.1]]
- 2026-11-02 updated: the Criterion replaced whole — lint reports only the draft pages with core: true that block the clean build, and none shipped as draft in an installed project · [[decision-case-996.3]]
- 2026-11-02 status: pending → passed · raw/2026-11-01/2227/ledger.md#L24
