---
type: decision
case: "1007"
status: current
defer: ["[[estimate-retro-loads-on-a-red-command]]"]
origin: raw/2026-11-02/2035/ledger.md#case-1007
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness]
---

## Context

The person put off C5 of the Frontier of session 2035, as the brief of session 1548 proposed. `estimate-retro-loads-on-a-red-command` stands `pending` with target `rule-retro`. The render its `method` names has run: lines 7 and 9 of `.claude/skills/retro/SKILL.md` hold `guppi test --exit-zero` and `guppi style --exit-zero`. Its reading waits for the first load of `/retro` that a transcript can show. Session 1548 loaded `/retro` in the VS Code extension, which handed the `!` commands to the agent as instructions. Session 2035 also runs in the VS Code extension.

## Problem

No Case of this session sets when or in which client the first load of `/retro` after that render is read.

## Deferred

### [[estimate-retro-loads-on-a-red-command]]

Whether /retro loads while guppi test or guppi style finds something, its lines Tests and Style running both commands with --exit-zero; waits for the first load of /retro in the Claude Code CLI; put off at /hi of session 2035

## History

- 2026-11-02 created · raw/2026-11-02/2035/ledger.md#case-1007
