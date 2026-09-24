---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: A status its Estimates do not support, an Estimate not read, and a placeholder are findings of lint
method: uv run pytest tests/test_lint.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-401.3
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` reads the `status` of the live pages under `vault/wiki/`.

Then:
`status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged.
**＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
**＋** `unread`: every Estimate `pending` or `failed`, one finding each, `unread: <status>`.
**＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.

## Result

2026-09-24, `uv run pytest tests/test_lint.py`: 69 passed

## History

- 2026-09-25 created · [[decision-case-401.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L44
