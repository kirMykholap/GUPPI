---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether /retro, called by the agent at the end of /work in the Claude Code CLI, loads whatever guppi test and guppi style find, its lines Tests and Style each ending with the line that names the exit code
method: "by hand, after a call of /retro by the agent at the end of /work in the Claude Code CLI: the transcript of that session under ~/.claude/projects/ read against the Criterion, the skill loaded and its lines Tests and Style each ending with the line exit code: <n>, recorded in the estimate line with the transcript named"
origin: raw/2026-11-26/2333/ledger.md#case-1072.2
sprint: plugin
created: 2026-11-26
tags: [sprint, session, harness]
once: true
---

## Criterion

When:
In the Claude Code CLI, the agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`.

Then:
The skill loads, whatever `uv run --project .guppi guppi test` and `uv run --project .guppi guppi style` find.
**＋** Its lines Tests and Style each come back with the output of its command and a last line `exit code: <n>`, and the agent takes each failing test and each style finding from them.

## History

- 2026-11-27 created · [[decision-case-1072.2]]
