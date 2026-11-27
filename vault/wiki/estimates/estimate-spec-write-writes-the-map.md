---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the plan file holds only its title line and a map of the Cases of the plan, cut from the plan file and its Cases file by plan_cases_text and rebuilt at each write or removal — a line that names the Cases file, a table, a Mermaid diagram and an entry per Case whose task lines stand indented after a box taken from spec.md once it stands, with their signs and the words of the Case — that no reader of the Cases reads and no Case placed after the approval enters, and whether --map prints the same map
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k map
checked: 2026-11-28
origin: raw/2026-11-27/0947/ledger.md#case-1078.1
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` of `.guppi/guppi/ratified.py` writes, places or removes a Case in the Cases file `<plan stem>.cases.md` beside the plan file of the session.
**＋** Or `uv run --project .guppi guppi ratified --map <file> --session <stamp>` runs on a file that holds Cases or stands beside a Cases file that holds them.

Then:
Right under its title line, the plan file holds a map of the Cases of the plan, read from the plan file and then its Cases file by `plan_cases_text` of `.guppi/guppi/ledger.py`, and rebuilt from them at each such run.
**＋** Below the map the plan file holds no Case heading and no `## Deferred`: each Case and each defer of the plan stands in its Cases file.
**＋** The map opens with a line that names the Cases file and says that each box copies the box of its task line there and is no task of its own; then a table of one row per top-level Case: its id, its name, and the number of open `stop:` lines and of open `read` lines of the Case and its sub-cases.
**＋** A Mermaid diagram follows, with one node per Case and sub-case in the order of the plan, an edge from each top-level Case to the next and from a parent to each of its sub-cases, and ⛔ on the node of a Case that holds an open `stop:` line.
**＋** Then each Case and sub-case has an entry: 🧩 with its id, its name and the path of its case file, and under it, indented, each line of its `tasks` block without its sub-points after a box — `[x]` for a ticked line, `[ ] ⛔` for an open `stop:` line, `[ ] 🔍` for an open `read` line, and `[ ]` for any other open line — a `create`, `update`, `delete` or `defer` line with the `purpose`, the `change` or the `impact` of its item, and a `read` line with the `purpose` of the `create` of the same Estimate; the Cases under `## Deferred` stand in the map by id and name.
**＋** Once `raw/<date>/<hi HHMM>/spec.md` stands, each box of the map is the box of the task line with the same text in the same Case in `spec.md`.
**＋** `--map` prints the same map of the Cases of `<file>` and of the Cases file beside it, its boxes taken in the same way, reads no payload and writes no file.
**－** No line of the map starts with a box at its first character, with a Case heading or with `# `, and no line of it is `## Deferred`, so `split_cases` of `.guppi/guppi/materialize.py`, the tickers and `place` of `.guppi/guppi/ratified.py` read the plan file, its Cases file and `spec.md` as before, and a Case placed after the approval goes before the `## Deferred` of its document, never into the map; a box ticked in the map alone ticks no task, and the next rebuild writes it back from its task line.
**－** A plan file that holds Cases of its own, written before its Cases file stood, keeps them, and the map takes them with the Cases of the Cases file.

## Result

2026-11-28, Retro of session 2214, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k map: 21 passed; against the when and then of Case 1087.1: the plan file holds its title line and the map alone, the map cut from the Cases file by plan_cases_text and opened by the line that names `plan.cases.md`, a plan file with Cases of its own keeps them and the map takes them, --map prints the same map from the Cases file and writes nothing

## History

- 2026-11-27 created · [[decision-case-1078.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L31
- 2026-11-27 updated: the Criterion replaced whole — each task line of the map stands after a box taken from spec.md · [[decision-case-1085.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L20
- 2026-11-28 updated: the Criterion replaced whole — the plan file holds no Case, and the map is cut from the plan file and the Cases file beside it · [[decision-case-1087.1]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L30
