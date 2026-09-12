---
type: decision
case: "79"
status: current
defer: [rule-ledger-tail]
supersedes: [decision-case-63]
origin: raw/2026-09-12/ledger.md#case-79
sprint: migration
created: 2026-09-12
tags: []
---

## Context

Case 45 (2026-09-10) deferred `rule-ledger-tail`: the ledger lines written after the
librarian's commit reach the next Frontier only two sessions later, because `/hi` reads
`brief.md` alone. Slice 3c grew around it: `decided_by`, `origin` as a ledger pointer,
`raw/<date>/` of an applied date archived by run stamp, the fresh ledger as the tail
`/hi` prints, lint on both fields. Deferred as 63 in session I. Case 73 (session J)
took the session folder out of it: what 3c archives is now `raw/<date>/` with its
session folders.

## Problem

`/hi` still shows nothing of what was written after the librarian's commit; the
memory file that carried the tail is gone (case 62). Postponed four times now.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-79
