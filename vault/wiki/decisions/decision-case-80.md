---
type: decision
case: "80"
status: current
defer: [rule-ask]
supersedes: [decision-case-65]
origin: raw/2026-09-12/ledger.md#case-80
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness]
---

## Context

Case 31 (2026-09-10) discussed and did not decide: `ask-guppi` answers from the four
indexes, which list live pages only; a slug that was archived is reported as missing.
`vault/archived/` holds 21 pages; `guppi cleanup` brings a page back on an `update`
of `status`. Deferred as 65 in session I.

## Problem

A Case may propose a `create` of a slug the archive already holds, and pre-task passes
it. The fix is an `update` of `rule-ask` with its Estimate, and no session has reached
it. Postponed five times now.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-80
