---
type: lesson
kind: knowledge
root_cause: a SubagentStop hook matched by agent type gets agent_id, agent_type, agent_transcript_path, the raw last_assistant_message and stop_hook_active; its exit 2 hands its stderr to the subagent as "Stop hook feedback" and the subagent answers again, the second call with stop_hook_active true — in the CLI and in VS Code alike; a hook in Python on Windows must read stdin as utf-8, or Cyrillic in the payload comes out garbled
status: new
source: probe session e56498c1 (claude-vscode) and 6bb485fc (CLI), scratchpad/probe of session 0051, 2026-09-25
origin: raw/2026-09-25/0051/ledger.md#L17
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
---

## Trigger

the scheme of case 416 checks the Case of case-guppi on SubagentStop before the main agent gets it

## Root cause

a SubagentStop hook matched by agent type gets agent_id, agent_type, agent_transcript_path, the raw last_assistant_message and stop_hook_active; its exit 2 hands its stderr to the subagent as "Stop hook feedback" and the subagent answers again, the second call with stop_hook_active true — in the CLI and in VS Code alike; a hook in Python on Windows must read stdin as utf-8, or Cyrillic in the payload comes out garbled

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#L17
