---
type: lesson
kind: error
root_cause: each hook command of rule-hook-registry names `uv run --project .guppi`, a path relative to the working folder of the shell, which a cd in a Bash call moves for every later hook, and uv exits 2, which Claude Code reads as a refusal
status: new
origin: raw/2026-11-04/0358/ledger.md#L33
sprint: plugin
created: 2026-11-04
tags: [hooks, plugin]
---

## Trigger

2026-11-04, the Retro of the trial session in C:/PROJECTS/guppi-trial-0358/no-git (transcript 2b6bed0c, L733 to L900): a Bash call ran `cd vault/wiki/estimates && ...`, the shell stayed there, and every PreToolUse and Stop hook failed with "Project directory `.guppi` does not exist ... Failed to spawn: `guppi`", refusing every tool call and every reply until the person pressed Esc; in session 0358 a Bash call of the main agent moved the shell into vault/wiki/estimates the same way

## Root cause

each hook command of rule-hook-registry names `uv run --project .guppi`, a path relative to the working folder of the shell, which a cd in a Bash call moves for every later hook, and uv exits 2, which Claude Code reads as a refusal

## History

- 2026-11-04 created · raw/2026-11-04/0358/ledger.md#L33
