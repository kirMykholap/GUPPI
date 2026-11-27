---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Stop hook opens the plan file, under its title line, with a map of its Cases rebuilt at each write or removal — a table, a Mermaid diagram and an entry per Case whose lines take their words from the Case, with their signs — that no reader of the Cases reads and no Case placed after the approval enters, and whether --map prints the same map
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k map
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
**＋** Then each Case and sub-case has an entry: 🧩 with its id and its name, the path of its case file, and each line of its `tasks` block without its box and sub-points, with ✅ before a ticked line, ⛔ before an open `stop:` line and 🔍 before an open `read` line.
**＋** A `create`, `update`, `delete` or `defer` line carries the `purpose`, the `change` or the `impact` of its item, and a `read` line carries the `purpose` of the `create` of the same Estimate in the Case.
**＋** The Cases under `## Deferred` stand in the map by id and name.
**＋** `--map` prints the same map of the Cases of `<file>`, reads no payload and writes no file.
**－** No line of the map opens with a box, with a Case heading or with `# `, and no line of it is `## Deferred`, so `split_cases` of `.guppi/guppi/materialize.py`, the tickers and `place` of `.guppi/guppi/ratified.py` read the plan file and `spec.md` as before, and a Case placed after the approval goes before the `## Deferred` of its document, never into the map.

## Result

2026-11-27, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k map: 9 passed (table, Mermaid diagram, entries with ✅ ⛔ 🔍 and the words of each item, a ticked read line with ✅ and no 🔍, no line opening with a box, a heading or ## Deferred, split_cases as before, the map rebuilt after a write and after a removal, --map printing the same map and writing nothing, test_approved_spec_places_a_case_after_the_map); the full guppi test 2043 passed, 6 skipped, 2 deselected

## History

- 2026-11-27 created · [[decision-case-1078.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L31
