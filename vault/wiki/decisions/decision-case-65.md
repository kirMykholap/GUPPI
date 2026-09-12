---
type: decision
case: "65"
status: current
defer: [rule-ask]
origin: raw/2026-09-12/ledger.md#case-65
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness]
---

## Context

Case 31 (2026-09-10) discussed and did not decide: `ask-guppi` answers from the four
indexes, which list live pages only; a slug named in a question that was archived is
reported as missing. `vault/archived/migration/2026-09-11/estimates/` holds 21 pages
since the librarian's run of session H, and `guppi cleanup` brings a page back on an
`update` of `status`.

## Problem

A Case may propose a `create` of a slug the archive already holds, and pre-task passes
it. The fix is small — a named slug checked against `vault/archived/` — but it is an
`update` of `rule-ask` with its Estimate, and no session has reached it. Postponed four
times now.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-65
