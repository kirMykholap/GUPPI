---
type: decision
case: "283"
status: archived
update: ["[[rule-retro]]", "[[estimate-retro-loads]]"]
origin: raw/2026-09-20/2106/ledger.md#case-283
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness, render]
---

## Context

At `/retro` the agent takes the readings of this session's Estimates whose work is finished and writes their lines into the ledger. The librarian applies the yaml in ledger order: an `update` of an Estimate replaces its Criterion whole and sets `pending`, an `estimate[...]` line sets the status and overwrites the Result; `built` on a Rule is computed once every Estimate of it is `passed`. In session 1749 Case 282 replaced the Criterion of `estimate-retro-loads` and left the render to the librarian; the `/retro` of the same session read the old Criterion of 270.3 — the SKILL that was rendered — for the `read` line of the 1308 Spec and wrote `passed`. `generate` applied the `update` first, then the reading: the page carries the Criterion of 282, the Result of 270.3 and `passed`; `rule-retro` became `built` on it. By the order of the ledger lines the reading stands after 282, and the rule of 280 ticked the line of 282, not 1308:132 — the reading of `estimate-generate-ticks-the-spec` in this session found 280 followed as written.
Bookkeeping: `rule-retro` `built`, its one Estimate `estimate-retro-loads` `passed`; the Case touches this Estimate; the vault not asked — an `update` with a `ref`; `generate` and the rule of 280 do not change.

## Problem

A reading of a Criterion the same session has already replaced lands on the page, sets `passed` on a promise nobody measured, and computes `built` on the Rule. Neither the ledger line nor `generate` can tell it from the normal course — an `update` ratified, built and read in one session — by order or by form. No text says which Criterion a reading measures.

## History

- 2026-09-21 created · raw/2026-09-20/2106/ledger.md#case-283
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
