---
type: decision
case: "417"
status: current
update: ["[[rule-prespec]]", "[[estimate-prespec-checks-the-ratified-copy]]"]
origin: raw/2026-09-25/0051/ledger.md#case-417
sprint: migration
created: 2026-09-25
tags: [session, workflow, harness]
---

## Context

`prespec --check` compares the plan with its ratified copy. A section of the copy with no Case in the plan is a finding. There is one exception: a Case a `{supersedes:case N}` of the session's window names. It breaks on a parent. A parent has no ledger lines of its own; its sub-cases carry them. When every sub-case is superseded, the parent leaves the plan with them, but its heading stays in the copy, and no `supersedes` line names it. In session 2214 this happened to Case 407: 412 superseded 407.1–407.5, and pre-spec still printed `case 407: in the ratified copy, not in the plan`. This is `lesson-prespec-parent-of-superseded-sub-cases`. The change touches one sentence of the Render of `rule-prespec` and the Criterion of `estimate-prespec-checks-the-ratified-copy`, and no other Estimate. `frame-guppi` found no contradiction. The lesson gets no mark: it was written in another session. No vault query: both items are an `update` with a `ref`.

## Problem

A parent whose sub-cases are all superseded gives a false finding at every `/pre-spec` of its session, and the agent has to explain it by hand.

## Given

`rule-prespec` — its Render `.claude/skills/pre-spec/SKILL.md`: the sentence on the ratified copy.
**＋** `estimate-prespec-checks-the-ratified-copy` — the Estimate whose Criterion is replaced.
**＋** `guppi/prespec.py` — `check_ratified`, the sections of the copy with no Case in the plan.
**＋** `tests/test_prespec.py` — fixes the comparison with the ratified copy.

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#case-417
