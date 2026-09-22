---
type: decision
case: "360"
status: current
create: ["[[rule-one-judgment-one-implementation]]", "[[estimate-one-judgment-one-implementation-followed]]"]
update: ["[[rule-claude-md]]", "[[estimate-claude-md-rendered]]", "[[insight-harness-one-rule-implemented-twice-drifts]]"]
origin: raw/2026-09-23/0034/ledger.md#case-360
sprint: migration
created: 2026-09-23
tags: [harness, workflow, render, tests]
---

## Context

Two lessons share one mechanism: one judgment of the pipeline was implemented in two places, and the copies drifted. `check_decision` resolved a `target_slug` against the live pages while `check_refs` resolved every other slug against live and archived pages; after 21 Estimates were archived, lint gave 25 false findings. `check_tasks` matched a reading's line by substring while `generate` ticked it by `READ_LINE`, and the four forms of a `method` were open-coded in `check_method`. Case 351 repaired these: `generate.READ_LINE`, `lint.names_a_form` and `generate.replace_once` are imported by both sides. In both, the suite stayed green, since every test was about one side.
The vault answers that no page and no section of `CLAUDE.md` says this; the Backlog notes on reuse (case 319) speak of modules that use each other, not of one judgment written twice; `make style` is the formatter only; the slug `rule-one-judgment-one-implementation` is free. `rule-claude-md` stands `built`, a MOC with the children `rule-language` and `rule-agent-writing`; its Estimate `estimate-claude-md-rendered` stands `passed`, and its Criterion still names `vault/wiki/index.md`, gone since case 318 — the reading this Case makes due would fail on that phrase, so it is repaired here. The Insight stands `open`, severity 2.

## Problem

A judgment the pipeline makes in two places can be written twice, and no text forbids it; the copies drift while the suite stays green.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-360
