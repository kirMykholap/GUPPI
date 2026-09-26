---
type: lesson
kind: knowledge
root_cause: in Claude Code 2.1.282 a subagent can hand its report to the main agent through the SubagentHandback tool call and then end with a text of its own; case-guppi handed the Case back that way and ended with a short summary, and guppi casecheck --subagent reads only last_assistant_message, so it found no Case heading, took the answer for a question and stored nothing; asked again to end with the Case as its text, case-guppi wrote it, called the handback, wrote it once more, and the check stored it with no finding
status: new
source: transcript subagents/agent-ae6c9dbed8844dfb3.jsonl of session af4c2d33, Claude Code 2.1.282 (claude-vscode), 2026-09-26
origin: raw/2026-09-26/1337/ledger.md#L2
sprint: migration
created: 2026-09-26
tags: [hooks, harness]
---

## Trigger

the first showing of Case 433 was refused on Stop with "case 433: not built and checked by case-guppi", though case-guppi had built it; no checked.json stood beside the plan file

## Root cause

in Claude Code 2.1.282 a subagent can hand its report to the main agent through the SubagentHandback tool call and then end with a text of its own; case-guppi handed the Case back that way and ended with a short summary, and guppi casecheck --subagent reads only last_assistant_message, so it found no Case heading, took the answer for a question and stored nothing; asked again to end with the Case as its text, case-guppi wrote it, called the handback, wrote it once more, and the check stored it with no finding

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#L2
