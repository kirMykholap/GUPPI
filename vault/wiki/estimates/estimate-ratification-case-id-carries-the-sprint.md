---
type: estimate
kind: QA
status: passed
target: "[[rule-ratification]]"
purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next prints and holds the next id of the open sprint, which the main agent uses
method: "uv run pytest tests/test_caseid.py; by hand at the Retro of this session: the new Renders of rule-ratification and rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion"
origin: raw/2026-10-12/2349/ledger.md#case-788.2
sprint: plugin
created: 2026-10-12
tags: [ledger, harness, session]
---

## Criterion

When:
`guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
**＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next` before it dispatches a new top-level Case.

Then:
A Case id of a sprint opened after this Case is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
**＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
**＋** The sprints `migration` and `plugin`, opened before this Case, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
**＋** `uv run guppi caseid --next` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md`, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
**＋** It holds the id it prints in `<plan>.checked.json`, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
**＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
**－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.

## Result

2026-10-13, uv run pytest tests/test_caseid.py: 20 passed — parse_line, top_case, case_file, case_number, held_number, check_origin, DEFERRED_LINE and case_key read kir-plugin-12.1 and 785.1 alike, and guppi caseid --next prints and holds two ids for a new sprint, a session that creates a sprint page and the sprint plugin; Retro by hand: the Renders of rule-ratification and rule-orchestration in spec.md state the form and the dispatch by guppi caseid --next

## History

- 2026-10-13 created · [[decision-case-788.2]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L48
