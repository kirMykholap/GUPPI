---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether the summary of case-guppi names, under the item of its Case, each stop task that waits for a file, data or an action of the person, with what the person gives and the path of a file, and names no stop that waits only for the word before a command
method: "by hand at Retro of the session that changes it: the new Render of rule-case-build in the Spec, read against the Criterion, recorded in the estimate line"
origin: raw/2026-11-27/0947/ledger.md#case-1077.1
sprint: plugin
created: 2026-11-27
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi` answers with the summary of a Case whose `tasks` hold a task that opens with `stop:`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

Then:
Where the task waits for a file, data or an action of the person, the summary holds a line `**From the person:**` under the item of the Case or sub-case of that task.
**＋** The line names what the person gives, and for a file the path where the file is to stand.
**＋** Two such tasks give two lines.
**－** A `stop:` task that waits only for the person's word before a command runs, such as a push or a merge, gets no such line.

## Result

2026-11-27, Retro of session 0947, the new Render of rule-case-build in vault/raw/2026-11-27/0947/spec.md (Case 1077.1, its replace pair) read against the Criterion: for each task of a Case or sub-case that opens with stop: and waits for a file, data or an action of the person, a line **From the person:** under its item after the fence, naming what the person gives and the path of a file; one line per such task; a stop: task that waits only for the word before a command, such as a push or a merge, gets none

## History

- 2026-11-27 created · [[decision-case-1077.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L27
