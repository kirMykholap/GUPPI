---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work runs guppi style before it stops at a task that opens with stop:, fixes each finding in a file the session changed and writes each other finding into handoff.md
method: "by hand, after the first /work that loads after the librarian's render of .claude/skills/work/SKILL.md from the Render of rule-work-mode and reaches a task that opens with stop:: its run of uv run --project .guppi guppi style before that stop, its fixes and its handoff.md read in the transcript of its session under ~/.claude/projects/ against the Criterion; recorded in the estimate line with the transcript named"
origin: raw/2026-11-25/2003/ledger.md#case-1061
sprint: plugin
created: 2026-11-25
tags: [session, workflow, harness]
---

## Criterion

When:
`/work` of `.claude/skills/work/SKILL.md`, rendered from `rule-work-mode`, reaches a task of the Spec whose text opens with `stop:`.

Then:
Before it stops, the agent runs `uv run --project .guppi guppi style` and fixes each finding in a file that the session changed.
**＋** The agent writes each finding in a file that the session did not change as a line of `raw/<date>/<hi HHMM>/handoff.md`.
**＋** The agent then stops before that task as `vault/wiki/where-to-stop.md` sets it.
**－** A task that does not open with `stop:` gets no style check from this step.

## History

- 2026-11-26 created · [[decision-case-1061]]
