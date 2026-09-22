---
type: lesson
kind: error
root_cause: "`recommend` and `ratification` are the two sections that do not enter the Spec, and the agent grouped them at the end of the reply by where they live instead of keeping the schema's order — the Case was composed in the order the Spec needs (context, problem, given, when, then, tasks) and the two chat-only sections appended as a trailer; nothing checks the order, since no script reads the chat form of a Case."
status: new
origin: raw/2026-09-22/2046/ledger.md#L7
sprint: migration
created: 2026-09-22
tags: [workflow]
---

## Trigger

Cases 341, 342 and 343 of this session were written with `recommend` after `tasks`, not in the schema's eight-section order; the person saw it, no script did.

## Root cause

`recommend` and `ratification` are the two sections that do not enter the Spec, and the agent grouped them at the end of the reply by where they live instead of keeping the schema's order — the Case was composed in the order the Spec needs (context, problem, given, when, then, tasks) and the two chat-only sections appended as a trailer; nothing checks the order, since no script reads the chat form of a Case.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L7
