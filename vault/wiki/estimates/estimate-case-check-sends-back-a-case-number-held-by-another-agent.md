---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case of case-guppi under a number that the store holds from the answer of another agent goes back to it with a new number, and the other agent's entry is kept
method: uv run pytest tests/test_casecheck.py -k clash, then by hand an answer of case-guppi the hook sends back for this reason
origin: raw/2026-10-03/0115/ledger.md#case-610.2
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, `agent_id` of the payload, and `<plan>.checked.json` beside the plan file.

Then:
The hook stores each Case of an answer in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
**＋** A top-level Case N of the answer is sent back when the store holds Case N, or a sub-case of it, under its number from an answer with another `agent_id`.
**＋** Its message gives `case-guppi` a free number, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
**＋** Each Case of that answer is stored apart, under its number joined with its `agent_id`, and the entry of the other agent under the number alone stays as it was.
**＋** The Spec hook, the `Stop` comparison and the writing of the file of a Case read the entry under the number alone.
**－** An unchanged answer whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
**－** An entry with no `agent_id`, stored before the change, gives no finding of this check, and neither does an answer whose `agent_id` is the one of the entry under the number.

## History

- 2026-10-03 created · [[decision-case-610.2]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
