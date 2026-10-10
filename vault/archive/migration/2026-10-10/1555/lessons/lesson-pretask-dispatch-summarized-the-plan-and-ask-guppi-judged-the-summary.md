---
type: lesson
kind: error
root_cause: the dispatch carried one summary line per decision instead of the then blocks (replace old/new, set) of the plan, so the agent compared the pages with a paraphrase that omitted what was being replaced; rule-ask's "one short question" was read as "no plan text", and the agent had no way to see the planned wording.
status: archived
origin: raw/2026-09-14/0747/ledger.md#L53
sprint: migration
created: 2026-09-14
tags: [harness, librarian, workflow]
---

## Trigger

at pre-task of session M ask-guppi returned four findings that the plan already answered — the rule-event-log sentence 111.1 replaces, the rule-skill-hi Purpose sentence 111.4 replaces, a source on error lessons that 113 never sets, an old fragment of 112.6 called not unique — beside six true ones.

## Root cause

the dispatch carried one summary line per decision instead of the then blocks (replace old/new, set) of the plan, so the agent compared the pages with a paraphrase that omitted what was being replaced; rule-ask's "one short question" was read as "no plan text", and the agent had no way to see the planned wording.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#L53
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
