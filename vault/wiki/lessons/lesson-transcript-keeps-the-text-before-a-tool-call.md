---
type: lesson
kind: knowledge
root_cause: the transcript keeps the text before a tool call and transcript_texts collects it since case 55.2, so a block followed by a tool call reaches the ledger at the next Stop of the session; the claim "never kept" was measured on one turn (109) and the loss of 222 was a check of ledger.md before the turn's Stop had fired
status: new
source: ~/.claude/projects/c--PROJECTS-GUPPI/cf5992b5-9102-4632-9a42-7a37b684ffe5.jsonl
origin: raw/2026-09-17/1119/ledger.md#L6
sprint: migration
created: 2026-09-17
tags: [ledger, hooks, harness]
---

## Trigger

the LEDGER block of case 222 stood in a text followed by a ToolSearch call in the same turn and the agent called it lost before the turn ended; the transcript of session 2238 (Claude Code 2.1.272) holds that text and 18 others followed by a tool call, and the Stop hook wrote its lines at 01:25:46, at the end of the same turn; the blocks of case 117 (2.1.270, written 13 seconds later) and case 101 (2.1.269, written at the next Stop 22 minutes later) show the same; only the block of case 109 (2.1.269) is absent from its transcript and unexplained

## Root cause

the transcript keeps the text before a tool call and transcript_texts collects it since case 55.2, so a block followed by a tool call reaches the ledger at the next Stop of the session; the claim "never kept" was measured on one turn (109) and the loss of 222 was a check of ledger.md before the turn's Stop had fired

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#L6
