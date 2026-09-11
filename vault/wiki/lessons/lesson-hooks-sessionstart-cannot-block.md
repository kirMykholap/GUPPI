---
type: lesson
kind: knowledge
root_cause: "`SessionStart` cannot block — exit 2 is a no-op there — so gating belongs on `PreToolUse`"
status: new
origin: raw/2026-09-09/ledger.md#L88
sprint: migration
created: 2026-09-09
---

## Trigger

the old glossary's Hook entry, carried since the earlier harness

## Root cause

`SessionStart` cannot block — exit 2 is a no-op there — so gating belongs on `PreToolUse`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L88
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
