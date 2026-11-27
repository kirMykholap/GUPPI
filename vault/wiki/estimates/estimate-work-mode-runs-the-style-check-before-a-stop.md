---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work runs guppi style before it stops at a task that opens with stop:, fixes each finding in a file the session changed and writes each other finding into handoff.md
method: "by hand, after the first /work that loads after the librarian's render of .claude/skills/work/SKILL.md from the Render of rule-work-mode and reaches a task that opens with stop:: its run of uv run --project .guppi guppi style before that stop, its fixes and its handoff.md read in the transcript of its session under ~/.claude/projects/ against the Criterion; recorded in the estimate line with the transcript named"
checked: 2026-11-27
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

## Result

2026-11-27, transcript ~/.claude/projects/c--PROJECTS-GUPPI/0446e3f0-7eab-44a6-9f97-c7bed477194a.jsonl of session 0947, its /work after the render of commit 4bc899cf, read against the Criterion: /work reached four stop: tasks, lines 505, 671, 674 and 715 of vault/raw/2026-11-27/0947/spec.md. Before the stop reply on lines 505 and 671 it ran guppi style, which found 1 lint error and 1 unformatted file in .guppi/guppi/ratified.py, a file the session changed; it fixed them by Edit and ran it again: "All checks passed!". Before the stop on line 674 it ran guppi style: "All checks passed!". Before the stop on line 715 it ran no guppi style: no call stands between the stop reply on line 674 and the one on line 715, and between them it edited only spec.md and frontier.md of the session. No finding stood in a file the session did not change, so handoff.md got no such line. The step ran before three of the four stops and not before the fourth.

## History

- 2026-11-26 created · [[decision-case-1061]]
- 2026-11-27 status: pending → failed · raw/2026-11-27/1402/ledger.md#L1
- 2026-11-27 updated: the Criterion written back word for word, to be read again after the skill says the check runs before each stop · [[decision-case-1084]]
