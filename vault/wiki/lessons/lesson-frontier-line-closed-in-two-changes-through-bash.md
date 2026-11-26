---
type: lesson
kind: error
root_cause: frontierguard judges an Edit or a Write of frontier.md and not a Bash command that changes the file, and the agent split the box and the closer of one line into two changes where the guard asks for one edit of the whole line
status: clustered
insight: "[[insight-orchestration-frontier-closer-leaves-the-box-open]]"
origin: raw/2026-11-26/1336/ledger.md#L14
sprint: plugin
created: 2026-11-26
tags: [hooks, harness]
---

## Trigger

at the ratification of Case 1064 in session 1336 the agent's Edit of vault/raw/2026-11-26/1336/frontier.md added the closer `· case 1064` to the line C4 and kept its box `[ ]`; frontierguard refused the Edit, and the agent then ticked the box alone by `sed -i` through Bash, which frontierguard did not read, so the line stood `[x]` with no closer until a later Edit added it

## Root cause

frontierguard judges an Edit or a Write of frontier.md and not a Bash command that changes the file, and the agent split the box and the closer of one line into two changes where the guard asks for one edit of the whole line

## History

- 2026-11-26 created · raw/2026-11-26/1336/ledger.md#L14
- 2026-11-26 updated: clustered under insight-orchestration-frontier-closer-leaves-the-box-open (synthesis) · raw/2026-11-26/1336/ledger.md#L14
