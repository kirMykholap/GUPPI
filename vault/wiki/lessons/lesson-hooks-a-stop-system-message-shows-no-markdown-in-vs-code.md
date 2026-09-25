---
type: lesson
kind: knowledge
root_cause: in the VS Code extension a Stop hook's systemMessage is shown whole but line by line, each line prefixed "Stop says:", with no markdown rendered; a SubagentStop hook's systemMessage is not shown at all, in the CLI or in VS Code, and stands only in the subagent's transcript; a Stop hook's systemMessage does stand in the main transcript as an attachment hook_system_message — so a hook can record what it showed, but a Case cannot be shown that way
status: new
source: probe session e56498c1 (claude-vscode) and 6bb485fc (CLI), scratchpad/probe of session 0051, 2026-09-25
origin: raw/2026-09-25/0051/ledger.md#L16
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
---

## Trigger

the scheme of case 416 would show a checked Case to the person by a systemMessage of a hook

## Root cause

in the VS Code extension a Stop hook's systemMessage is shown whole but line by line, each line prefixed "Stop says:", with no markdown rendered; a SubagentStop hook's systemMessage is not shown at all, in the CLI or in VS Code, and stands only in the subagent's transcript; a Stop hook's systemMessage does stand in the main transcript as an attachment hook_system_message — so a hook can record what it showed, but a Case cannot be shown that way

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#L16
