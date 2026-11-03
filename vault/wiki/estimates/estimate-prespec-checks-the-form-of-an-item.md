---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: An item of the plan carries one promise per Case, names a page that exists or is created, and no file
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

Then:
A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `.guppi/guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
**＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
**＋** A `defer` of a Lesson or a Decision page, whether its page stands or not, is the finding `case N: defer <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it`, a short Case under `## Deferred` of the plan included.
**＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
**＋** A `defer` of an Insight whose page stands neither under `vault/wiki/insights/` nor in a folder `insights/` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such page — a placeholder is written only for a rule or an entity`, a short Case under `## Deferred` of the plan included.
**＋** The judgment of a Lesson or a Decision page is `defers_a_record` of `.guppi/guppi/materialize.py`, and the judgment of a page that does not stand is `defer_writes_no_page` of the same module, which asks `has_page`; the `defer` of `.guppi/guppi/generate.py` imports both.
**＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
**＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
**＋** A key of an item of any kind that `item_keys` of `.guppi/guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
**－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
**－** A `defer` of a Lesson or a Decision page with no page gives the finding of a Lesson or a Decision page alone, not the finding of a page that does not stand.
**－** A `defer` of a rule or an entity with no page is not a finding.
**－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
