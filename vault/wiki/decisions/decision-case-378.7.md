---
type: decision
case: "378.7"
status: current
create: ["[[estimate-prespec-checks-the-frame]]"]
update: ["[[rule-prespec]]"]
origin: raw/2026-09-23/1355/ledger.md#case-378.7
sprint: migration
created: 2026-09-23
tags: [harness, workflow, session]
---

## Context

The `given` of a Case serves two readers today. For the person it is "how it is now"; the scripts copy it into the Estimate as `Given:`, where it must stay true after the fix, so a Criterion goes stale the moment `given` holds a state or the defect. The bookkeeping — what the Case touches — lies in the prose of `context`, and nothing binds `when` and `then` to it. The operands are loose: "does not apply here" lets in lines on the bounds of an edit, and a grep of the `－` lines of the Criteria of the 104 Estimates finds 38 lines in 31 pages carrying one of "not change", "as today", "nothing else", "unchanged" or "stays as". Since case 296, `replace` pairs append lines inside another Criterion, and journals grow: the largest, `estimate-case-protocol-loaded`, holds 13 `＋` lines, of which 355.1, 355.2, 368 and 370 are signed a second time in `estimate-case-protocol-case-form`. Case 187 makes every change of a Render touch the Estimate of its live reading — the root of the live child of the Insight of C4.
Since case 201.2 the decision page does not hold `given`: `generate` writes only Context, Problem and Deferred, so `given` returns to the decision page, or it leaves the vault with this change.
`rule-case-protocol` and `rule-prespec` stand `draft`, `rule-materialize` and `rule-plan-mode` `built`. This Case changes the rules and the code; the eleven Estimates whose Criterion speaks of the old model are rewritten whole by the one pass over the 104 pages, Slice 3g of the sprint page (Case 381): `estimate-case-protocol-case-form`, `-loaded`, `estimate-materialize-assembles`, `-walks-dates`, `-marks-superseded`, `estimate-generate-writes-the-decision-page`, `-fails-alone`, `-cascades`, `estimate-prespec-reconciles`, `-checks-the-plan`, `estimate-plan-mode-names-its-estimates`. Every item an `update` with a `ref` or a `create` with a `ref`, so no vault query. The Case is written in the new form.

## Problem

One section serves both the history of the Case and the contract of the Estimate, so the contract goes stale at every fix; `when` and `then` are bound by no frame, the operands let in claims on the bounds of an edit, and a Criterion can be appended to part by part — so Cases describe everything and Estimates turn into journals.

## Given

`guppi/prespec.py` — checks the plan before the Spec is approved.
**＋** `guppi/materialize.py` — `split_cases`, `case_texts`, `category_of`: the parse of a Case and the one notion of a slug.
**＋** `guppi/lint.py` — `CODE_SPAN`.
**＋** `tests/test_prespec.py` — fixes the checks.
**＋** `rule-prespec` — the Render `.claude/skills/pre-spec/SKILL.md`: the list of findings.
**＋** `estimate-prespec-checks-the-frame` — the new promise.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-378.7
