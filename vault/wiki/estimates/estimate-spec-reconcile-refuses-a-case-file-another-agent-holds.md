---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-reconcile]]"
purpose: Whether the first call of case-guppi on the file of a Case, its name in either form of the id, holds its id in the store, and a call of another case-guppi on that file is refused with a free id
method: uv run pytest tests/test_ratified.py -k number_held
checked: 2026-10-13
origin: raw/2026-10-05/1343/ledger.md#case-650.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
`case-guppi` calls `Edit`, `Write` or `MultiEdit` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the agent type and the `agent_id` of the call from the hook input, and `<plan>.checked.json` beside the plan file of the session.

Then:
The guard reads the id N from the file name by `case_number` of `guppi/casecheck.py`, a plain id such as `785` or an id of a sprint such as `kir-plugin-12` alike.
**＋** The call is refused when `<plan>.checked.json` holds Case N, or a sub-case of it, under its id alone with an `agent_id` other than the one of the call: exit 2 with the reason on stderr, and the call does not run.
**＋** The reason names the file and a free id, and tells `case-guppi` to build its Case under that id.
**＋** The holder is judged by `clashes` and the free id is counted by `new_number` of `guppi/casecheck.py`, the judgments that the check of `rule-case-check` runs.
**＋** A call that passes while `<plan>.checked.json` holds no entry under N alone writes there, under N, an entry with the `agent_id` of the call and the time, and no text, so the id is held before the agent stops.
**＋** A refusal writes one line of the refusal to the day's event log.
**－** A call whose `agent_id` is the one of the entry under N, and an entry with no `agent_id`, are not refused by this check.
**－** A call with no `agent_id`, a file whose name gives no id, and a session with no plan file are not judged by this check, and nothing is written into `<plan>.checked.json`.
**－** An error of the guard while it finds the plan file or reads or writes `<plan>.checked.json` lets the call run: exit 0 with one line on stderr, as `estimate-spec-write-exits-2-on-an-error` sets it for the guard.

## Result

2026-10-13, uv run pytest tests/test_ratified.py -k number_held: 13 passed — a file case-kir-plugin-12.md held by another agent is refused with case kir-plugin-13, the same agent passes

## History

- 2026-10-05 created · [[decision-case-650.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L7
- 2026-10-13 updated: the Criterion replaced whole — the guard reads a file name in either form of the id and names a free id (case 788.6) · [[decision-case-788.6]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L52
