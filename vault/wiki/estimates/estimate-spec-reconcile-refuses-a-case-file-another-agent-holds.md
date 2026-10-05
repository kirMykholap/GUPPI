---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-reconcile]]"
purpose: Whether the first call of case-guppi on the file of a Case holds its number in the store, and a call of another case-guppi on that file is refused with a free number
method: uv run pytest tests/test_ratified.py -k number_held; by hand in a session after the work, the entry of the store that the first Write of a live case-guppi wrote, holding its agent_id
origin: raw/2026-10-05/1343/ledger.md#case-650.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
`case-guppi` calls `Edit`, `Write` or `MultiEdit` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the agent type and the `agent_id` of the call from the hook input, and `<plan>.checked.json` beside the plan file of the session.

Then:
The call is refused when `<plan>.checked.json` holds Case N, or a sub-case of it, under its number alone with an `agent_id` other than the one of the call: exit 2 with the reason on stderr, and the call does not run.
**＋** The reason names the file and a free number, and tells `case-guppi` to build its Case under that number.
**＋** The holder is judged by `clashes` and the free number is counted by `new_number` of `guppi/casecheck.py`, the judgments that the check of `rule-case-check` runs.
**＋** A call that passes while `<plan>.checked.json` holds no entry under N alone writes there, under N, an entry with the `agent_id` of the call and the time, and no text, so the number is held before the agent stops.
**＋** A refusal writes one line of the refusal to the day's event log.
**－** A call whose `agent_id` is the one of the entry under N, and an entry with no `agent_id`, are not refused by this check.
**－** A call with no `agent_id`, a file whose name gives no number, and a session with no plan file are not judged by this check, and nothing is written into `<plan>.checked.json`.
**－** An error of the guard while it finds the plan file or reads or writes `<plan>.checked.json` lets the call run: exit 0 with one line on stderr, as `estimate-spec-write-exits-2-on-an-error` sets it for the guard.

## History

- 2026-10-05 created · [[decision-case-650.1]]
