---
type: lesson
kind: knowledge
root_cause: a check that judges the same text as a writer or a ticker had been written as a second implementation of the one rule, and the two drifted apart without a test noticing; the repair in both places was to import the one pattern — `generate.READ_LINE`, `lint.names_a_form` — so the check cannot judge by anything but what the other side does, and `generate.replace_once` was lifted out for the same reason when `pre-spec` came to simulate the pairs of a Spec (case 351).
status: clustered
source: guppi/prespec.py
insight: "[[insight-harness-one-rule-implemented-twice-drifts]]"
origin: raw/2026-09-22/2046/ledger.md#L37
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Trigger

two of the eight findings of the second `ask-guppi` pass on the conserved Spec were one shape — `check_tasks` matched a reading's task line by substring while `generate` ticked it by `READ_LINE`, and the classification of the four forms of a `method` was open-coded in `check_method` where `pre-spec` needed the same judgment (cases 327, 331).

## Root cause

a check that judges the same text as a writer or a ticker had been written as a second implementation of the one rule, and the two drifted apart without a test noticing; the repair in both places was to import the one pattern — `generate.READ_LINE`, `lint.names_a_form` — so the check cannot judge by anything but what the other side does, and `generate.replace_once` was lifted out for the same reason when `pre-spec` came to simulate the pairs of a Spec (case 351).

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L37
- 2026-09-23 updated: clustered by librarian: one rule of the pipeline implemented twice and drifting, with lesson-lint-decision-target-archived-counts-as-missing · raw/2026-09-22/2046/ledger.md#L37
