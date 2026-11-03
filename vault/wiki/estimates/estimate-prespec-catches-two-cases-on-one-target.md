---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether the check finds two Cases of one plan that set one field of a page to two values, write one section twice, or replace the Criterion of one Estimate twice
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check` runs on a plan file, or the hook of `rule-case-check` runs `judge` of `.guppi/guppi/prespec.py` on an answer of `case-guppi`.

Then:
It prints one finding for each two Cases of the plan whose `update` items name one page and set one field under `set` to two different values, naming both Cases, the page's slug and the field.
**＋** It prints one finding for each two Cases whose `update` items write one section of one page under `sections`, naming both Cases, the page's slug and the section.
**＋** It prints one finding for each two Cases that each replace the Criterion of one Estimate whole — an `update` of the Estimate that names no part by `names_a_part` of `.guppi/guppi/materialize.py` — naming both Cases and the Estimate's slug.
**＋** Each such finding opens with the later of the two Cases, so the check that runs after a Case is written into the plan gives it to that Case.
**＋** The comparison is one function of `.guppi/guppi/prespec.py` that `judge` calls, so the check of an answer of `case-guppi` finds the same between the Cases of one answer.
**－** Two Cases that change different fields, different sections or different anchors of one page are no finding; their `replace` pairs stay judged by the simulation of the pairs.
**－** Two items of one Case are no such finding: a second item of one kind and slug under one Case keeps the finding it has.
**－** A Case under `## Deferred` is not compared.

## Result

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
