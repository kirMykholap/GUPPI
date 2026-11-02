---
type: lesson
kind: knowledge
root_cause: the VS Code extension does not run the ! commands of a skill at its load but hands them to the agent to run, so a red command does not stop the skill there, while the CLI runs them and refuses the skill on a non-zero exit; a reading of how a skill loads holds only for the client it was taken in
status: new
source: the loads of /work and /retro in session 1337, run in the VS Code extension of Claude Code, transcript 561dc30b under ~/.claude/projects/c--PROJECTS-GUPPI/
origin: raw/2026-11-02/1337/ledger.md#L21
sprint: plugin
created: 2026-11-02
tags: [harness, workflow]
---

## Trigger

in session 1337, run in the VS Code extension, /work and /retro loaded while guppi check exited 1, and each skill text came with a first line "Run these N commands first, exactly as written" and placeholders such as "[output of command 2, uv run --project .guppi guppi check]" in place of its ! lines, while in the CLI of the trial session 1429 the same /work was refused

## Root cause

the VS Code extension does not run the ! commands of a skill at its load but hands them to the agent to run, so a red command does not stop the skill there, while the CLI runs them and refuses the skill on a non-zero exit; a reading of how a skill loads holds only for the client it was taken in

## History

- 2026-11-02 created · raw/2026-11-02/1337/ledger.md#L21
