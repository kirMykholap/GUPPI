---
type: decision
case: "142.5"
status: current
update: ["[[rule-documentation]]"]
origin: raw/2026-09-14/1633/ledger.md#case-142.5
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness, librarian, render]
---

## Context

An Insight of severity 2, `open`, two children of 2026-09-10: `generate` crashed on a `replace` mapping (one entry stopped the run); `materialize` built its index over `e["line"]` and crashed on the three librarian entries without `line`. Pattern: `materialize.yaml` has four writers — materialize, the `then` block of the Spec, the librarian, the marks of `generate` — and each script reads the file as if it alone had written it. Proposal: (1) the shape of an entry is stated in one place and every script reads through it; (2) the rule of Case 47 — an entry fails alone — is extended from `generate` to `materialize`.

## Problem

Both children were fixed in place: `generate` catches any exception per entry since Case 47; `materialize` skips entries without `line`. But `assemble` in `materialize.py` has no guard per entry: any exception while lifting a line is "materialize.yaml not written", exit 1, the walk stops, no entry of the unit is written. And the field list of `rule-materialize` (case 49) is behind: no `path`, `decision`, `derived`, `criterion_block`, `set`, `case_removed`, `status`/`result` of a folded reading, the librarian's marks (`near`, `librarian`, `synthesis`), `superseded_by` from another unit (130.2). Decide: action the Insight by work, reject it, or defer it.

## Given

The marks paragraph of the frame, line 60: "`applied` and `failed` are set by `guppi generate`". After 142.1 `materialize` sets `failed` on an entry without `kind` (pre-task).

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-142.5
