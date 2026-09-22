---
type: decision
case: "312"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-22/1121/ledger.md#case-312
sprint: migration
created: 2026-09-22
tags: [harness, workflow, ledger]
---

## Context

`generate`, on an `estimate` entry (or a `create` with a folded reading), ticks the *first* unticked line `- [ ] read `<slug>`` in the first Spec that holds one, skipping the sections of Cases ratified after the reading (280) and superseded (286) — one line per entry. In 0014 two Cases touched `estimate-lint-catches` — 304.8 and 305.5, one `replace` pair each, from different parents — and the Spec holds two `read` lines. The reading after Work Mode was one, the page is `passed`; the line of 304.8 was ticked, the line of 305.5 stands open — a false debt at Retro. A reading is taken of the page, not of a Case: the Criterion is one, and after Work Mode it holds both changes, so one reading answers for both lines. Pages: `rule-page-generation` `built`, of its nine Estimates the Case touches `estimate-generate-ticks-the-spec` (`passed`).

## Problem

Two Cases of one session that touched one Estimate leave one `read` line open for ever; either it is a form `pre-spec` refuses, or a tick `generate` adds.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-312
