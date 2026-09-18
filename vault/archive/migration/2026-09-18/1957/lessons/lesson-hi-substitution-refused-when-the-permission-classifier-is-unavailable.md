---
type: lesson
kind: knowledge
root_cause: in auto mode a `!` command of a skill goes through the same permission classifier as a Bash call, and when the classifier's model is unavailable the command is not run at all; the SessionStart hook is not affected, so a hand edit is still caught there, and `render --check` by hand is the fallback at /hi
status: archived
source: the local-command-stderr of /hi in session 1119, 2026-09-17 11:19
insight: "[[insight-hi-skill-substitution-checked-by-a-model-call]]"
origin: raw/2026-09-17/1119/ledger.md#L42
sprint: migration
created: 2026-09-17
tags: [harness, session, hooks]
---

## Trigger

at /hi the skill's `!`uv run guppi render --sync`` substitution was refused — "Shell command permission check failed … claude-opus-5[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash"; the Render: line came back empty and `render --check` run by hand exited 0

## Root cause

in auto mode a `!` command of a skill goes through the same permission classifier as a Bash call, and when the classifier's model is unavailable the command is not run at all; the SessionStart hook is not affected, so a hand edit is still caught there, and `render --check` by hand is the fallback at /hi

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#L42
- 2026-09-18 updated: clustered by librarian under insight-hi-skill-substitution-checked-by-a-model-call · raw/2026-09-18/1252/ledger.md#L8
- 2026-09-18 archived · insight actioned
- 2026-09-18 archived · cleanup
