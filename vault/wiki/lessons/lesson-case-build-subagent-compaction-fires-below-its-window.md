---
type: lesson
kind: knowledge
root_cause: Claude Code compacts a subagent at about 72–75k preTokens of a 100000 window, keeps the transcript lines before each compact_boundary, still fires SubagentStop for it afterwards, and restores recently read files such as an interim file after a compaction; its PreCompact and PostCompact hooks fire with no agent_type and no agent_id and the main session's transcript_path, and each compaction runs a summarizer that fires SubagentStop with an empty agent_type and its own agent_id, so a hook cannot tell from those events alone which subagent compacted.
status: new
source: claude -p 2.1.301, test folder scratchpad/compact-test of session 1907, transcript agent-a12be5ab8317687d5.jsonl and log.txt
origin: raw/2026-10-28/1907/ledger.md#L20
sprint: plugin
created: 2026-10-28
tags: [case-build, hooks]
---

## Trigger

the test of Case 895 ran a subagent with autoCompactWindow 100000 past that size.

## Root cause

Claude Code compacts a subagent at about 72–75k preTokens of a 100000 window, keeps the transcript lines before each compact_boundary, still fires SubagentStop for it afterwards, and restores recently read files such as an interim file after a compaction; its PreCompact and PostCompact hooks fire with no agent_type and no agent_id and the main session's transcript_path, and each compaction runs a summarizer that fires SubagentStop with an empty agent_type and its own agent_id, so a hook cannot tell from those events alone which subagent compacted.

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#L20
