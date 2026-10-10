---
type: decision
case: "184"
status: archived
update: ["[[rule-ledger-write]]"]
origin: raw/2026-09-15/2225/ledger.md#case-184
sprint: migration
created: 2026-09-15
tags: [session, hooks, harness, ledger]
---

## Context

`rule-ledger-write` describes the gate from the side of the Spec: an item without its ledger line is refused, "every item with its line, or no source found, passes silently (case 122)". Block 122 of `estimate-ledger-write-lifts` signs the same: "Every item with its line, or no source found: exit 0, silent", for any call through `Skill`. Case 180 makes a `/retro` with no source and no ledger line a refusal.

## Problem

Two signed texts say "no source: exit 0", and 180 says "no source and no line: exit 2" for `/retro`. Without a line on `rule-ledger-write` its contract contradicts 180 silently.

## Given

`rule-ledger-write` is `built`, with one Estimate — `estimate-ledger-write-lifts`, `passed`; no `estimate_slug` needed.
**＋** How it works, one sentence: "and every item with its line, or no source found, passes silently (case 122)".
**＋** Case 180 is ratified in this session; its tests in `tests/test_gate.py` cover the refusal and the pass.
**－** The contract of `rule-retro-commit` does not change here.

## Criterion

- [[estimate-ledger-write-lifts]] § case 184

## History

- 2026-09-16 created · raw/2026-09-15/2225/ledger.md#case-184
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
