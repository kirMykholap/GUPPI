---
type: decision
case: "957"
status: archived
defer: ["[[insight-plugin-cli-withholds-approval-of-a-long-plan]]"]
superseded_by: ["[[decision-case-987.1]]"]
origin: raw/2026-10-31/0431/ledger.md#case-957
sprint: plugin
created: 2026-10-31
tags: [plugin, harness]
---

## Context

The by-hand test of session 0128 showed that the Claude Code CLI withholds the approval of a long plan in any terminal, the terminal of VS Code included, with no GUPPI in the folder, while the Claude Code extension of VS Code approves it. The person judged it a bug of Claude Code, which has been reported to Anthropic, and put off any fix in GUPPI at /hi of session 0431: the person works in the extension, and only users of the plugin who approve a Spec in the CLI meet the fault.

## Problem

No Case of this session decides how GUPPI lets a long Spec be approved in the Claude Code CLI.

## Deferred

### [[insight-plugin-cli-withholds-approval-of-a-long-plan]]

Wait for Claude Code to fix the approval of a long plan in the CLI, a bug reported to Anthropic; read it again before the plugin ships, and name the limit in README.md for the users of the plugin

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-957
- 2026-11-01 superseded by decision-case-987.1 · [[decision-case-987.1]]
- 2026-11-01 archived · superseded
- 2026-11-01 archived · cleanup
