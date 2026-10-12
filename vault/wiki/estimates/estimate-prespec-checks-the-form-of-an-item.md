---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: An item of the plan carries one promise per Case, names a page that exists or is created, and no file
method: uv run pytest tests/test_prespec.py
checked: 2026-10-12
origin: raw/2026-09-24/1916/ledger.md#case-399.5
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

Then:
A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
**＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
**＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder, by `has_page` of `guppi/materialize.py`, is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
**＋** The judgment is `has_page` of `guppi/materialize.py`, which the `defer` of `guppi/generate.py` imports too.
**＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
**＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
**＋** A key of an item of any kind that `item_keys` of `guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
**－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
**－** A `defer` of a rule, an entity or an Insight with no page is not this finding.
**－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

## Result

2026-10-12, uv run pytest tests/test_prespec.py: 234 passed; a defer of an Estimate with no page, under a Case heading and under ## Deferred, and one archived outside a folder estimates/ or under raw/, gives "case 2: defer estimate-later: no such Estimate page — defer the page it would check"; a live one, one archived in estimates/ and a defer of a rule with no page give none; prespec.has_page and generate.has_page are materialize.has_page

## History

- 2026-09-25 created · [[decision-case-399.5]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L41
- 2026-09-26 updated: the Criterion replaced whole — a key of an item outside the keys item_keys gives it is a finding (case 436.2) · [[decision-case-436.2]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L27
- 2026-09-28 updated: the Criterion replaced whole — every Estimate item that replaces a Criterion by names_a_part, written or lifted, counts as a promise (case 472.3) · [[decision-case-472.3]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L35
- 2026-10-12 updated: the Criterion replaced whole — a defer of an Estimate with no page is a finding · [[decision-case-783.2]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/2252/ledger.md#L14
