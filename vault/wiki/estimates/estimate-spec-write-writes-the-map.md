---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Stop hook opens the plan file, under its title line, with a map of its Cases rebuilt at each write or removal — a table, a Mermaid diagram and an entry per Case whose task lines stand indented after a box taken from spec.md once it stands, with their signs and the words of the Case — that no reader of the Cases reads and no Case placed after the approval enters, and whether --map prints the same map
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k map
checked: 2026-11-27
origin: raw/2026-11-27/0947/ledger.md#case-1078.1
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` of `.guppi/guppi/ratified.py` writes, places or removes a Case in the plan file of the session.
**＋** Or `uv run --project .guppi guppi ratified --map <file> --session <stamp>` runs on a file that holds Cases.

Then:
Right under its title line, the plan file holds a map of the Cases it holds, rebuilt from them at each such run.
**＋** The map opens with a table of one row per top-level Case: its id, its name, and the number of open `stop:` lines and of open `read` lines of the Case and its sub-cases.
**＋** A Mermaid diagram follows, with one node per Case and sub-case in the order of the plan, an edge from each top-level Case to the next and from a parent to each of its sub-cases, and ⛔ on the node of a Case that holds an open `stop:` line.
**＋** Then each Case and sub-case has an entry: 🧩 with its id, its name and the path of its case file, and under it, indented, each line of its `tasks` block without its sub-points after a box: `[x]` for a ticked line, `[ ] ⛔` for an open `stop:` line, `[ ] 🔍` for an open `read` line, and `[ ]` for any other open line.
**＋** Once `raw/<date>/<hi HHMM>/spec.md` stands, each box of the map is the box of the task line with the same text in the same Case in `spec.md`.
**＋** A `create`, `update`, `delete` or `defer` line carries the `purpose`, the `change` or the `impact` of its item, and a `read` line carries the `purpose` of the `create` of the same Estimate in the Case.
**＋** The Cases under `## Deferred` stand in the map by id and name.
**＋** `--map` prints the same map of the Cases of `<file>`, its boxes taken in the same way, reads no payload and writes no file.
**－** No line of the map starts with a box at its first character, with a Case heading or with `# `, and no line of it is `## Deferred`, so `split_cases` of `.guppi/guppi/materialize.py`, the tickers and `place` of `.guppi/guppi/ratified.py` read the plan file and `spec.md` as before, and a Case placed after the approval goes before the `## Deferred` of its document, never into the map.
**－** A box ticked in the map alone ticks no task, and the next rebuild writes it back from its task line.

## Result

2026-11-27, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k map, Retro of session 1402: 19 passed; the tests assert the boxes [x], [ ] ⛔, [ ] 🔍 and [ ] of the indented task lines with no ✅, the boxes taken from the same Case of spec.md, a box ticked in the map alone written back at the next rebuild, the table, the Mermaid diagram, the Deferred line, --map printing the same map and no line of the map that TASK_LINE matches

## History

- 2026-11-27 created · [[decision-case-1078.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L31
- 2026-11-27 updated: the Criterion replaced whole — each task line of the map stands after a box taken from spec.md · [[decision-case-1085.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L20
