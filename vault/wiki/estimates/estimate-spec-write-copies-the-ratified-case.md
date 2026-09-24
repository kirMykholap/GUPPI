---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: The ratified Case enters the plan file and its ratified copy in the words of the chat, the then block built from the sub-points
method: uv run pytest tests/test_ratified.py -k write; the live reading by hand, the plan file and its ratified copy after the first ratification of a session
checked: 2026-09-24
origin: raw/2026-09-23/1859/ledger.md#case-387.2
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript and finds the last earlier reply that shows `## Case N —` whole.

Then:
The hook writes that Case into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as they stand in the chat; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points.
**＋** It writes the same text the same way into the ratified copy `<plan>.ratified.md` beside the plan file.
**＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span or a fenced block under the sub-point.
**＋** `recommend` and `ratification` are not written.
**＋** When the last showing of Case N is a `DIFF` block, not the Case whole, the hook writes nothing for it.
**＋** No plan file in the event log, no showing of Case N, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
**－** A Case whose lines are all `defer` is not written by the hook: the agent appends it under `## Deferred`, as before.

## Result

2026-09-24, uv run pytest tests/test_ratified.py -k write: 9 passed; live in session 1303: after the acknowledging reply of Case 390 the Stop hook wrote Case 390 into the plan file and its ratified copy — the heading, context, problem, given, when and then as in the chat, a then block built from the sub-points (replace old/new, set, change), a tasks block without the sub-points, no recommend and no ratification; the two files equal below their title lines

## History

- 2026-09-24 created · [[decision-case-387.2]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L3
