---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: A status its Estimates do not support, a draft page with core true where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, and a placeholder are findings of lint
method: uv run --project .guppi pytest .guppi/tests/test_lint.py
checked: 2026-10-15
origin: raw/2026-09-24/1916/ledger.md#case-401.3
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the `status` of the live pages under `vault/wiki/` and the `method` of each Estimate.

Then:
`status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged for these two.
**＋** `status`: where `ship_stands` of `.guppi/guppi/pages.py` finds the module of the command `ship`, each entity or rule that `is_draft_core` accepts, with Estimates or without, one finding each.
**＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
**＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
**＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
**＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
**－** `guppi lint` in a project that installed GUPPI reports none of these pages, since `ship_stands` answers no there.
**－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
**－** A `failed` Estimate earns its `unread` finding whatever its `method` says.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_lint.py: 110 passed, exit 0

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
