---
type: lesson
kind: knowledge
root_cause: a PreToolUse hook on Read that prints hookSpecificOutput.updatedInput with a limit and no permissionDecision changes the call in the main agent and in a subagent alike; PostToolUse then receives the changed tool_input, limit included, and its additionalContext reaches the agent; an Edit of the file after the cut Read succeeds
status: new
source: live probe of session 1228 in the scratchpad, Claude Code 2.1.282
origin: raw/2026-09-25/1228/ledger.md#L37
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
---

## Trigger

Case 420.1 needed a hook to cut the History of a vault page from a Read

## Root cause

a PreToolUse hook on Read that prints hookSpecificOutput.updatedInput with a limit and no permissionDecision changes the call in the main agent and in a subagent alike; PostToolUse then receives the changed tool_input, limit included, and its additionalContext reaches the agent; an Edit of the file after the cut Read succeeds

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#L37
