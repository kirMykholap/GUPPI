---
type: estimate
kind: QA
status: pending
target: rule-session-start
origin: raw/2026-09-09/ledger.md#case-12
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks]
---

## Context

The children check that each mechanism works on its own. This check is the cross-cutting
one: that the distinction between an ordinary session and a working session holds end to
end, from the mark `/hi` leaves to what the person sees when a line is refused.

## Criterion

In a session opened without `/hi`, a bare `- decision[...]` line in a reply does not reach
`raw/<date>/ledger.md` and the reply the person sees names the cause. In a session opened
with `/hi`, the same line does reach it. Both readings taken end to end.

## Method

Two session starts, by hand, one reading each, recorded in the estimate line.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-12
