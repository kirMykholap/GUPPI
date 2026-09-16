---
type: decision
case: "223"
status: current
defer: ["[[rule-carry-over]]"]
origin: raw/2026-09-16/2238/ledger.md#case-223
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, render]
---

## Context

`rule-carry-over` (`draft`, parent `rule-end-of-work`) carries a `ref: rule-end-of-work` field beside `parent` — the same lift as on the 15 Estimate pages of case 210 (`lesson-materialize-item-ref-lifted-as-a-page-field`), on a rule page; `rules/schema.yaml` names no `ref`. Case 214.1 keeps `ref` off every page from now on; case 210 named the Estimate pages only, and Work Mode left this one as it stood.

## Problem

One live rule page carries a field nobody ratified; the one-off of 210 did not cover it, and Retro ratifies no update.

## Deferred

### [[rule-carry-over]]

drop the stray `ref` field from `rule-carry-over`, a one-off like case 210 — a script run once by path and a History line with the pointer; the next Plan Mode

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-223
