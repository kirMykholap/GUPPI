---
type: estimate
kind: QA
status: passed
target: "[[rule-ratification]]"
purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next --session <stamp> prints and holds the next id of the open sprint, which the main agent uses, and prints no id without --session or without the plan file of the session
method: "uv run pytest tests/test_caseid.py; by hand at the Retro of this session: the new Renders of rule-ratification and rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion"
checked: 2026-10-14
origin: raw/2026-10-12/2349/ledger.md#case-788.2
sprint: plugin
created: 2026-10-12
tags: [ledger, harness, session]
---

## Criterion

When:
`guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
**＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
**＋** Or `uv run guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

Then:
A Case id of a sprint opened after case 788.2 is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
**＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
**＋** The sprints `migration` and `plugin`, opened before case 788.2, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
**＋** The main agent creates the plan file of its session with its title line before its first run of the command.
**＋** `uv run guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
**＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
**＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
**－** Without `--session` the command prints no id: it prints its usage error and exits 2.
**－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
**－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.

## Result

2026-10-14, session 0232, uv run pytest tests/test_caseid.py tests/test_casecheck.py: 252 passed, with two new tests — guppi caseid --next without --session exits 2 with its usage error and prints no id, and with --session and no plan file of that session (the stamp of the session, and an unknown stamp) it exits 1, prints no id, prints one line naming the session on stderr and writes no store; the new Renders in spec.md of session 0232: orchestration.md gives `uv run guppi caseid --next --session <stamp>` for a new top-level Case and the plan file before its first run, ratification.md gives the same command, that it holds the id in the store of the session's plan file, and that it prints no id without --session or without that plan file

## History

- 2026-10-13 created · [[decision-case-788.2]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L48
- 2026-10-14 updated: the Criterion replaced whole — guppi caseid --next takes --session with the stamp of the hi: line, and prints no id without it or without the plan file of the session · [[decision-case-812.1]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0232/ledger.md#L12
