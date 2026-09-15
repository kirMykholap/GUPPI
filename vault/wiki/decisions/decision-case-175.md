---
type: decision
case: "175"
status: current
update: ["[[rule-materialize]]"]
origin: raw/2026-09-15/1809/ledger.md#case-175
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

`guppi materialize` builds the session's `materialize.yaml` from the ledger and the Spec: one entry per ledger line, the word of the second bracket as `kind`, plus derived entries with no line of their own — the Estimate's `create` from `method`, its `update` with a block from `contract: changed`, the removal of a `### case N` block from `{supersedes:case N}` under the internal word `remove_criterion`. A line with `{supersedes:case N}` marks the entries of Case N `superseded_by` — in this yaml or in the yaml of another session (case 130.2); `generate` does not apply a marked entry, it only writes the Decision page of N as `superseded`. `mark_superseded` sets the mark by the filter "an entry of Case N whose `kind` is one of the four decision kinds". In session R 166.2 superseded 164: two entries of 164 were marked, the third — the removal of block 124.2 — was not; `generate` applied it in the name of the superseded 164.

## Problem

A superseded Case keeps acting through one of its entries. The filter by kind is superfluous: when Case N is superseded, everything it yielded is superseded. `estimate` and `lesson` entries carry no Case number, so a mark by the number alone catches nothing else.

## Given

`guppi/materialize.py`, `mark_superseded`: marks an entry when `entry.case == N` and `entry.kind in DECISION_KINDS`; `mark_superseded_elsewhere` calls the same for a foreign yaml.
**＋** `derived_entries` gives a derived entry the line's `case` and `derived: true`; the block-removal entry is `kind: remove_criterion`, `case_removed: N`, no `slug`.
**＋** `estimate_entry` and `lesson_entry` write an entry without a `case` key.
**＋** `guppi generate`: an entry with `superseded_by` is not applied (case 151); a `remove_criterion` with no block prints `no Estimate holds a block` and does not fail.
**＋** `rule-materialize` is `built`, `estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]`, both `passed`, the first named by `estimate_slug` (a fact corrected at pre-task: the Case said one Estimate); `tests/test_materialize.py`: `test_a_supersedes_chain_marks_the_earlier_entry`, `test_a_supersedes_marks_the_earlier_entry_in_another_units_yaml`, the `seed` fixture.
**－** `1448/materialize.yaml` and the History of `estimate-generate-writes` are not rewritten: block 124.2 is gone, which 171 wanted; the History says what the script did.

## Criterion

- [[estimate-materialize-assembles]] § case 175

## History

- 2026-09-15 created · raw/2026-09-15/1809/ledger.md#case-175
