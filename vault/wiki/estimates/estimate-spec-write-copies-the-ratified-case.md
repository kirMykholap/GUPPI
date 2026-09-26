---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: The ratified Case enters the plan file and its ratified copy in the words of the stored answer of case-guppi, the then block built from the sub-points
method: uv run pytest tests/test_ratified.py -k write; the live reading by hand, the plan file and its ratified copy after the first ratification of a session
checked: 2026-09-25
origin: raw/2026-09-23/1859/ledger.md#case-387.2
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript for the last earlier reply that shows `## Case N —` whole, and `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N.

Then:
The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `recommend` and `ratification` are not written.
**＋** It writes the same text the same way into the ratified copy `<plan>.ratified.md` beside the plan file.
**＋** A last showing of Case N that differs from the stored answer — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
**＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
**＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item — the one judgment `guppi/materialize.py` lifts by and `guppi/generate.py` applies by — is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` on stderr, and nothing of the Case is written.
**＋** A value that holds a backtick in an outer span not padded on both sides is refused: exit 2 with `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
**＋** No plan file in the event log, no showing of Case N whole, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
**－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).

## Result

2026-09-25, uv run pytest tests/test_ratified.py -k write: 16 passed; by hand, the plan file of session 1654 after the ratification of Case 425: the Case written with its then block built from the sub-points (rename, change) and its tasks block without sub-points, no recommend and no ratification; the ratified copy sparkling-floating-comet.ratified.md beside it holds the twelve Case headings 425–432 with 428.1–428.4

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
