---
type: lesson
kind: knowledge
root_cause: since client 2.1.282 the check of a skill's ! substitution is a call to the server-side auto mode classifier, which gives no verdict for a substitution the person types ("the request that produced this action did not ask for one"); a command no allow rule matches is refused, and a matching rule in the skill's allowed-tools needs no classifier
status: archived
source: Claude Code 2.1.282, session 1b191eaf 2026-09-26
insight: "[[insight-hi-skill-substitution-checked-by-a-model-call]]"
origin: raw/2026-09-26/1745/ledger.md#L2
sprint: migration
created: 2026-09-26
tags: [harness, session]
---

## Trigger

/hi failed at every run in VS Code with "Shell command permission check failed for pattern" on its ! commands, and a fresh /login did not help

## Root cause

since client 2.1.282 the check of a skill's ! substitution is a call to the server-side auto mode classifier, which gives no verdict for a substitution the person types ("the request that produced this action did not ask for one"); a command no allow rule matches is refused, and a matching rule in the skill's allowed-tools needs no classifier

## History

- 2026-09-26 created · raw/2026-09-26/1745/ledger.md#L2
- 2026-09-26 updated: clustered into insight-hi-skill-substitution-checked-by-a-model-call · raw/2026-09-26/1745/ledger.md#L2
- 2026-09-26 archived · insight actioned
- 2026-09-26 archived · cleanup
