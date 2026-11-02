---
type: lesson
kind: knowledge
root_cause: Claude Code stores a prompt blocked by a hook as a system warning record with the reason, and the phone app does not show that record, so a refusal of a typed command reaches a person on the phone as silence; a blocked prompt never reaches the agent, so no reply of the agent can carry the reason either
status: new
source: the person's report in session 0254 and the transcript 68effdf4-70dd-447d-bafe-0ca629e82241.jsonl, records of type system, subtype informational, level warning
origin: raw/2026-11-02/0254/ledger.md#L9
sprint: plugin
created: 2026-11-02
tags: [hooks, session]
---

## Trigger

in session 0254 the person typed /hi in permission mode auto from the Claude phone app; the UserPromptSubmit hook guppi event prompt refused it with exit 2 and a reason on stderr, and the person saw nothing, while the VS Code extension shows the same reason

## Root cause

Claude Code stores a prompt blocked by a hook as a system warning record with the reason, and the phone app does not show that record, so a refusal of a typed command reaches a person on the phone as silence; a blocked prompt never reaches the agent, so no reply of the agent can carry the reason either

## History

- 2026-11-02 created · raw/2026-11-02/0254/ledger.md#L9
