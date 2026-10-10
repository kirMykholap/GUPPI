---
type: lesson
kind: error
root_cause: the exclusion was a text rule each agent had to apply by hand in each Grep and in the right place, and the Grep tool reads its glob in order, so an exclusion put first still matched every Decision page
status: archived
origin: raw/2026-10-05/1616/ledger.md#L43
sprint: migration
created: 2026-10-05
tags: [harness, workflow]
---

## Trigger

at /pre-spec of session 1616 each of the five ask-guppi runs broke .claude/rules/search-leaves-out-decisions.md — the exclusion put first, or a Grep with no `!**/decisions/**` — and named it under what it did not check

## Root cause

the exclusion was a text rule each agent had to apply by hand in each Grep and in the right place, and the Grep tool reads its glob in order, so an exclusion put first still matched every Decision page

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#L43
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
