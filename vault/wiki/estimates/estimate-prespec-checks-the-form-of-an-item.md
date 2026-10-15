---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: An item of the plan carries one promise per Case, names a page that exists or is created, and no file
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py
checked: 2026-10-13
origin: raw/2026-09-24/1916/ledger.md#case-399.5
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

Then:
A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `.guppi/guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
**＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
**＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
**＋** A `defer` of an Insight, a Lesson or a Decision page whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such page — a placeholder is written only for a rule or an entity`, a short Case under `## Deferred` of the plan included.
**＋** The judgment of both is `defer_writes_no_page` of `.guppi/guppi/materialize.py`, which asks `has_page` and which the `defer` of `.guppi/guppi/generate.py` imports too.
**＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
**＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
**＋** A key of an item of any kind that `item_keys` of `.guppi/guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
**－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
**－** A `defer` of a rule or an entity with no page is not a finding.
**－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

## Result

2026-10-13, uv run pytest tests/test_prespec.py: 242 passed — a defer of an Insight or a Lesson with no page is the finding of defer_writes_no_page, a rule or an entity with no page is none

## History

- 2026-09-25 created · [[decision-case-399.5]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L41
- 2026-09-26 updated: the Criterion replaced whole — a key of an item outside the keys item_keys gives it is a finding (case 436.2) · [[decision-case-436.2]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L27
- 2026-09-28 updated: the Criterion replaced whole — every Estimate item that replaces a Criterion by names_a_part, written or lifted, counts as a promise (case 472.3) · [[decision-case-472.3]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L35
- 2026-10-12 updated: the Criterion replaced whole — a defer of an Estimate with no page is a finding · [[decision-case-783.2]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/2252/ledger.md#L14
- 2026-10-13 updated: the Criterion replaced whole — a defer with no page of anything but a rule or an entity is a finding · [[decision-case-786.2]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L46
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
