---
type: lesson
kind: error
root_cause: the skill hi runs git branch --show-current and git status --short as shell patterns, and /guppi:install neither runs git init nor tells the person that the project must be a git repository, so an empty project breaks the first /hi
status: new
origin: raw/2026-10-16/0104/ledger.md#L19
sprint: plugin
created: 2026-10-16
tags: [plugin, session, git]
---

## Trigger

in C:\PROJECTS\test the first /hi after /guppi:install stopped on "Shell command failed for pattern "!`git branch --show-current`": fatal: not a git repository"; after git init /hi started /sprint-open

## Root cause

the skill hi runs git branch --show-current and git status --short as shell patterns, and /guppi:install neither runs git init nor tells the person that the project must be a git repository, so an empty project breaks the first /hi

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#L19
