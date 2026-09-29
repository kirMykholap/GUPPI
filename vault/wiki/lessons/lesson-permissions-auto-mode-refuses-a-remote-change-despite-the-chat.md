---
type: lesson
kind: knowledge
root_cause: the classifier judges the action against the settings' permission rules, not against the person's word in the chat, and a denial covers the outcome, not only the command; a task that changes a git remote can be done in Work Mode only by the person or under a permission rule in settings.
status: new
source: Claude Code auto mode classifier, session 2026-09-30/0138, reason Remote Repoint
origin: raw/2026-09-30/0138/ledger.md#L7
sprint: migration
created: 2026-09-30
tags: [harness, workflow]
---

## Trigger

in Work Mode the by-hand task of case 528.1, git remote remove origin, was refused by the auto mode classifier twice — the second time after the person wrote in the chat that they allowed it — and a plain sed -n read of the Spec run right after the first refusal was refused with the same reason; the person ran the command by hand with ! in the prompt.

## Root cause

the classifier judges the action against the settings' permission rules, not against the person's word in the chat, and a denial covers the outcome, not only the command; a task that changes a git remote can be done in Work Mode only by the person or under a permission rule in settings.

## History

- 2026-09-30 created · raw/2026-09-30/0138/ledger.md#L7
