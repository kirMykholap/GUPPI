---
type: decision
case: "364.3"
status: current
update: ["[[estimate-prespec-reconciles]]"]
origin: raw/2026-09-23/1126/ledger.md#case-364.3
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Context

Case 318 deleted `vault/wiki/index.md`: each of its `§N` was to be covered by a rule page and every pointer at the file was to go. The reading L63 found two live pointers: the docstring of `guppi/materialize.py:11` ("route computed from `index.md` §5") and the Given of `estimate-case-protocol-case-form`. The same `rg` run again in this session found a third: the Then of `estimate-prespec-reconciles` has `ask-guppi` asked what contradicts "a page, `index.md` or each other", while the Render of `/pre-spec` already says "a page of the vault, a rule of the vault, or each other". And §5, the Routing Table, did not move: `rule-materialize` says "Its route is the Routing Table of this page", and the page holds no table; the version of `index.md` before its removal holds it — decision × `ref` → effect on the target.
`entity-sprint-migration` stands `draft`; `estimate-sprint-migration-index-dissolved` stands `failed`, its Criterion stands and it is read again after Work Mode; `rule-materialize` stands `built`, and none of its 11 Estimates speaks of the route, so none is touched; `estimate-case-protocol-case-form` (`pending`) is touched by 364.2; `estimate-prespec-reconciles` (`passed`) is touched by 364.3 and goes `pending`; no `create`, so no vault query is due.

## Problem

The Estimate stands `failed` because three live texts send the reader to a file that is gone, and the Routing Table the docstring points at stands on no live page.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-364.3
