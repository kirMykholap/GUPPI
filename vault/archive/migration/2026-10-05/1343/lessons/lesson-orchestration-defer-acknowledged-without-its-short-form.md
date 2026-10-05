---
type: lesson
kind: error
root_cause: the agent took the earlier showing as enough, while the hook writes a short form only from the reply that carries both its `then` fence and its ledger line
status: archived
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-10-05/1343/ledger.md#L43
sprint: migration
created: 2026-10-05
tags: [session, workflow]
---

## Trigger

in session 1343 the main agent showed the short-form Case 659 in a reply that asked the person, then acknowledged the person's yes with the LEDGER line alone; the Stop hook of rule-spec-write refused it with "case 659: no fence tagged then with its defer items", and a further reply showed the short form again with the line.

## Root cause

the agent took the earlier showing as enough, while the hook writes a short form only from the reply that carries both its `then` fence and its ledger line

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#L43
- 2026-10-05 updated: clustered under insight-workflow-case-schema-silent-on-what-the-scripts-accept (synthesis) · raw/2026-10-05/1343/ledger.md#L43
- 2026-10-05 archived · insight actioned
- 2026-10-05 archived · cleanup
