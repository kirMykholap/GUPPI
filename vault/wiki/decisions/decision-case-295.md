---
type: decision
case: "295"
status: current
update: ["[[estimate-generate-cascades]]", "[[estimate-generate-writes-the-decision-page]]", "[[estimate-generate-fails-alone]]"]
origin: raw/2026-09-21/1315/ledger.md#case-295
sprint: migration
created: 2026-09-21
tags: [harness, workflow, ledger, tests]
---

## Context

`estimate-generate-cascades`, `estimate-generate-writes-the-decision-page` and `estimate-generate-fails-alone` hold one and the same `given` line: "An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`". After 296 an entry of one field carries neither. Their `then` do not depend on the line — `generate` applies what the entry carries — but the line becomes false. Three pages `passed`; `rule-page-generation` `draft`; an `update` with a `ref` each. Before 296 the fix meant three whole Criteria (lesson 0958); after it, three `replace` pairs — the first live use of the rule, and the live reading of `estimate-materialize-assembles`. The pairs sit in `given`, inside the Criterion: the three pages go `pending`, one `pytest tests/test_generate.py` reads all three.

## Problem

Three `given` lines describe a form of the entry that is no longer the only one.

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#case-295
