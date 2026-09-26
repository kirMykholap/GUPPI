---
type: lesson
kind: knowledge
root_cause: "in Claude Code 2.1.282 the SubagentStop payload carries agent_transcript_path, agent_id, agent_type, last_assistant_message and stop_hook_active; a subagent is told that only a SubagentHandback call reaches its caller; when it ends with text and no handback, SubagentStop fires with stop_hook_active false and last_assistant_message that text, then the harness sends it \"[handback-send-enforce] Your report has not been delivered\", it calls SubagentHandback, the harness may send \"[Your previous response had no visible output…]\", it writes a text again, and SubagentStop fires a second time with stop_hook_active true though no hook exited 2; these harness messages stand in the subagent transcript as user messages, and a SendMessage arrives as a user message \"The coordinator sent a message while you were working: …\""
status: new
source: "probe of session af4c2d33, Claude Code 2.1.282 (claude-vscode), 2026-09-26: a SubagentStop payload dump in guppi/casecheck.py and the transcripts subagents/agent-a47709debf3034a82.jsonl and agent-ae6c9dbed8844dfb3.jsonl"
origin: raw/2026-09-26/1337/ledger.md#L19
sprint: migration
created: 2026-09-26
tags: [hooks, harness]
---

## Trigger

W28 checked on a live payload that SubagentStop carries agent_transcript_path before the code of Case 434

## Root cause

in Claude Code 2.1.282 the SubagentStop payload carries agent_transcript_path, agent_id, agent_type, last_assistant_message and stop_hook_active; a subagent is told that only a SubagentHandback call reaches its caller; when it ends with text and no handback, SubagentStop fires with stop_hook_active false and last_assistant_message that text, then the harness sends it "[handback-send-enforce] Your report has not been delivered", it calls SubagentHandback, the harness may send "[Your previous response had no visible output…]", it writes a text again, and SubagentStop fires a second time with stop_hook_active true though no hook exited 2; these harness messages stand in the subagent transcript as user messages, and a SendMessage arrives as a user message "The coordinator sent a message while you were working: …"

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#L19
