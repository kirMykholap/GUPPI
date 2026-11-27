---
type: lesson
kind: knowledge
root_cause: Code Mode gave the same answer and cost about $0.47 against $0.51 at the Opus 5.5 list price, since the tokens it saved were cache reads; it was slower, since its first code read files one by one and hit the 10-minute limit; it runs only in a terminal, not in the VS Code panel or with Remote Control; a script run by one Bash call keeps file text out of the context without it
status: new
source: estimate-sprint-plugin-code-mode-cost-measured; https://code.claude.com/docs/en/code-mode.md
origin: raw/2026-11-27/1402/ledger.md#L4
sprint: plugin
created: 2026-11-27
tags: [harness]
---

## Trigger

the Code Mode trial of case 1079 (Claude Code 2.1.332), read at Plan Mode of session 1402, where the person chose to leave Code Mode out for now

## Root cause

Code Mode gave the same answer and cost about $0.47 against $0.51 at the Opus 5.5 list price, since the tokens it saved were cache reads; it was slower, since its first code read files one by one and hit the 10-minute limit; it runs only in a terminal, not in the VS Code panel or with Remote Control; a script run by one Bash call keeps file text out of the context without it

## History

- 2026-11-27 created · raw/2026-11-27/1402/ledger.md#L4
