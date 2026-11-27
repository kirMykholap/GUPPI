---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether Claude Code runs an Edit of a file that a command rewrote after the last Edit of the agent, with no new Read asked for, as the hook of rule-spec-write rewrites spec.md between two ticks of Work Mode
method: "by hand, in the Work Mode of this session: the agent writes a scratch file of three lines outside the repository, changes its first line by Edit, rewrites its second line by uv run --project .guppi python -c, and changes its third line by Edit with no Read between; what the second Edit gave back, in the transcript of the session under ~/.claude/projects/, read against the Criterion; the estimate line keeps those words"
origin: raw/2026-11-27/1402/ledger.md#case-1085.9
sprint: plugin
created: 2026-11-27
tags: [hooks, harness]
once: true
---

## Criterion

When:
In Work Mode, the agent changes a scratch file outside the repository by `Edit`, a command outside the tool then rewrites one line of that file, and the agent changes another line of the file by `Edit` with no `Read` between.

Then:
Claude Code runs the second `Edit` and writes its change.
**－** Claude Code does not ask for a new `Read` of the file before that `Edit`.

## Result

2026-11-27, Work Mode of session 1402, transcript of session ee662ed3 under ~/.claude/projects/c--PROJECTS-GUPPI/: a scratch file of three lines written, its first line changed by Edit, its second rewritten by uv run --project .guppi python -c, its third changed by Edit with no Read between; the second Edit ran and gave back "has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)"; the file then held all three changes; no new Read was asked for

## History

- 2026-11-27 created · [[decision-case-1085.9]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L24
