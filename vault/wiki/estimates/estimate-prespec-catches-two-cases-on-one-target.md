---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: Whether the check finds two Cases of one plan that set one field of a page to two values, write one section twice, or replace the Criterion of one Estimate twice
method: uv run pytest tests/test_prespec.py
origin: raw/2026-09-30/2356/ledger.md#case-561.4
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check` runs on a plan file, or the hook of `rule-case-check` runs `judge` of `guppi/prespec.py` on an answer of `case-guppi`.

Then:
It prints one finding for each two Cases of the plan whose `update` items name one page and set one field under `set` to two different values, naming both Cases, the page's slug and the field.
**＋** It prints one finding for each two Cases whose `update` items write one section of one page under `sections`, naming both Cases, the page's slug and the section.
**＋** It prints one finding for each two Cases that each replace the Criterion of one Estimate whole — an `update` of the Estimate that names no part by `names_a_part` of `guppi/materialize.py` — naming both Cases and the Estimate's slug.
**＋** Each such finding opens with the later of the two Cases, so the check that runs after a Case is written into the plan gives it to that Case.
**＋** The comparison is one function of `guppi/prespec.py` that `judge` calls, so the check of an answer of `case-guppi` finds the same between the Cases of one answer.
**－** Two Cases that change different fields, different sections or different anchors of one page are no finding; their `replace` pairs stay judged by the simulation of the pairs.
**－** Two items of one Case are no such finding: a second item of one kind and slug under one Case keeps the finding it has.
**－** A Case under `## Deferred` is not compared.

## History

- 2026-10-01 created · [[decision-case-561.4]]
