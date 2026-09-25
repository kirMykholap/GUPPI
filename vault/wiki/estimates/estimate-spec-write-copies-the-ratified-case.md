---
type: estimate
kind: QA
status: pending
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
**＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
**＋** A value that holds a backtick in an outer span not padded on both sides is refused: exit 2 with `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
**＋** `recommend` and `ratification` are not written.
**＋** When the last showing of Case N is a `DIFF` block, not the Case whole, the hook writes nothing for it.
**＋** No plan file in the event log, no showing of Case N, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.

## Result

2026-09-24, `uv run pytest tests/test_ratified.py`: 18 passed, with the code of Case 402 — an unpadded value holding a backtick refused with its reason, a padded one read, the fixture `SHOWING` padded

## History

- 2026-09-24 created · [[decision-case-387.2]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L3
- 2026-09-25 updated: the Criterion replaced whole — a value holding a backtick padded by one space, an unpadded one refused (case 402) · [[decision-case-402]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L47
- 2026-09-25 updated: the Criterion replaced whole — the exception for a defer-only Case dropped, the hook writes it (case 421.1) · [[decision-case-421.1]]
