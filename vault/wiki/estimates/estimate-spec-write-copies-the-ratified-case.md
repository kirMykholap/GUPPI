---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: The ratified Case enters the plan file in the words of the stored answer of case-guppi, the then block built from the sub-points, each block fenced by its content
method: uv run pytest tests/test_ratified.py -k write; the live reading by hand, the plan file after the first ratification of a session
checked: 2026-09-30
origin: raw/2026-09-23/1859/ledger.md#case-387.2
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N, and the session's transcript for the `SendUserFile` calls on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with at least one of its sections.

Then:
The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `ratification` is not written.
**＋** A sub-case's own `recommend` is written under its heading, and the `context`, `problem` and `recommend` of its parent come from the parent's stored answer.
**＋** Each of the two blocks opens and closes with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least, which `tagged_blocks` of `guppi/materialize.py` reads back whole; the same fence rule holds for the blocks it writes into `raw/<date>/<hi HHMM>/spec.md` once it stands, and for the `then` block of a short-form defer under `## Deferred`.
**＋** No `SendUserFile` call on the file of Case N made after the time the store holds for Case N: exit 2 with the reason on stderr, and nothing of Case N is written.
**＋** A last showing of Case N that differs from the stored answer in a section it shows — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
**＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
**＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item, or a value that holds a backtick in an outer span not padded on both sides, is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` or `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
**＋** No plan file in the event log, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
**－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys.
**－** A reply with no showing of Case N is no refusal when the file of Case N was sent after the store.

## Result

2026-09-30, uv run pytest tests/test_ratified.py -k write: 50 passed; by hand, the plan file after the ratification of Case 547 in session 1736: the heading, context, problem, recommend, given, when and then as the answer held them, a then block built from the sub-points of tasks (the replace pair, change, the fields of the create), a tasks block without sub-points, no ratification

## History

- 2026-09-24 created · [[decision-case-387.2]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L3
- 2026-09-25 updated: the Criterion replaced whole — a value holding a backtick padded by one space, an unpadded one refused (case 402) · [[decision-case-402]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L47
- 2026-09-25 updated: the Criterion replaced whole — the exception for a defer-only Case dropped, the hook writes it (case 421.1) · [[decision-case-421.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1654/ledger.md#L29
- 2026-09-26 updated: the Criterion replaced whole — a sub-point outside the keys item_keys gives its item is refused (case 436.1) · [[decision-case-436.1]]
- 2026-09-26 updated: the Criterion replaced whole — the Case is written from the stored answer of case-guppi, a differing showing refused; the lines of case 436.1 carried (case 437) · [[decision-case-437]]
- 2026-09-26 updated: the Criterion replaced whole — the DIFF skip goes (case 441.8) · [[decision-case-441.8]]
- 2026-09-27 updated: the Criterion replaced whole — the fence of each written block is one longer than the longest fence inside it; the ratified copy no longer named (cases 444.2, 445.2) · [[decision-case-444.2]]
- 2026-09-27 updated: the Criterion replaced whole — a sending of the file after the newest store in place of a showing whole (case 452.3) · [[decision-case-452.3]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L29
- 2026-09-30 updated: the Criterion replaced whole — the Spec holds recommend, a sub-case's own under its heading (case 544.5) · [[decision-case-544.5]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L29
- 2026-09-30 status: passed → passed · raw/2026-09-30/1736/ledger.md#L30
