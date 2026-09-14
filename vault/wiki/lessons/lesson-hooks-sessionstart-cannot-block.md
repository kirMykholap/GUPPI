---
type: lesson
kind: knowledge
root_cause: "`SessionStart` cannot block — exit 2 is a no-op there — so gating belongs on `PreToolUse`"
status: new
source: the Hook entry of the glossary before the migration, carried from the earlier harness
origin: raw/2026-09-09/ledger.md#L88
sprint: migration
created: 2026-09-09
tags: [hooks, harness, session]
---

## Trigger

the old glossary's Hook entry, carried since the earlier harness

## Root cause

`SessionStart` cannot block — exit 2 is a no-op there — so gating belongs on `PreToolUse`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L88
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 updated: tags and source filled (case 113) · [[decision-case-113]]
