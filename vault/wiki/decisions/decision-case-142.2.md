---
type: decision
case: "142.2"
status: current
update: ["[[rule-page-generation]]"]
origin: raw/2026-09-14/1633/ledger.md#case-142.2
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

An Insight of severity 2, `open`, two children of 2026-09-10: `generate` crashed on a `replace` mapping (one entry stopped the run); `materialize` built its index over `e["line"]` and crashed on the three librarian entries without `line`. Pattern: `materialize.yaml` has four writers — materialize, the `then` block of the Spec, the librarian, the marks of `generate` — and each script reads the file as if it alone had written it. Proposal: (1) the shape of an entry is stated in one place and every script reads through it; (2) the rule of Case 47 — an entry fails alone — is extended from `generate` to `materialize`.

## Problem

Both children were fixed in place: `generate` catches any exception per entry since Case 47; `materialize` skips entries without `line`. But `assemble` in `materialize.py` has no guard per entry: any exception while lifting a line is "materialize.yaml not written", exit 1, the walk stops, no entry of the unit is written. And the field list of `rule-materialize` (case 49) is behind: no `path`, `decision`, `derived`, `criterion_block`, `set`, `case_removed`, `status`/`result` of a folded reading, the librarian's marks (`near`, `librarian`, `synthesis`), `superseded_by` from another unit (130.2). Decide: action the Insight by work, reject it, or defer it.

## Given

`insight-harness-yaml-entry-shape-assumed`: `open`, severity 2, children `lesson-generate-replace-mapping-crashes`, `lesson-materialize-assumes-every-entry-has-a-line`, both `clustered`; the cascade of 104.2 archives them on `actioned`.
**＋** `rule-materialize` `built`, `estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]`, both `passed`; its text: "An error on one date stops the walk with exit 1"; "A line the grammar does not parse goes under `unparsed`; the script continues" — for an unparsed line only. Code: `materialize_date` catches `Exception` around the whole of `assemble` → "materialize.yaml not written", return 1; `run` stops the walk at the first non-zero code.
**＋** `rule-page-generation` `built` holds the rule of Case 47: "An entry that fails — … a field whose shape the script does not expect, any exception raised while applying it — is reported on stderr, marked `failed` and skipped; the rest apply; the exit code is 1. No entry ends the run." The three Estimates of Case 47 were archived on 09-11; no live Estimate carries the criterion, it is read through `estimate-generate-writes`. Code: `apply` sends an entry without `kind` to `vault.error("unknown kind None")` and marks it `failed` with that text.
**＋** `archive.py` (`uncovered_lines`, `kept_reason`) and `tail.py` read entries through `isinstance(dict)` and `.get`; `known = {e["line"]: e … if "line" in e}` in `assemble` is the fix of the second lesson.
**＋** The librarian's marks `near`, `librarian`, `synthesis` are described in `rule-documentation`; `applied`/`failed` in `rule-page-generation`; `superseded_by` from another unit in 130.2. No page lists all of them together.
**＋** `case-schema.md` pins the shape of `replace`; `rule-index-check`, `rule-brief`, `rule-raw-archive`, `rule-ledger-tail` read the yaml by named marks — unchanged.
**－** An Insight is not a Leaf: no `contract`, no Estimate. No other live Lesson or Insight is about a script crashing on a yaml entry (`ask-guppi`).
**－** `rule-lint` does not read the yaml; `case-schema.md` is not touched.

## Criterion

- [[estimate-generate-writes]] § case 142.2

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-142.2
