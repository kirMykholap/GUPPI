---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case of case-guppi under an id, plain or of a sprint, that the store holds from the answer of another agent goes back to it with a free id, and the other agent's entry is kept
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k subagent_clash
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file, `agent_id` of the payload, and `<plan>.checked.json`.

Then:
The hook stores each Case of the file in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
**＋** A top-level Case N of the file, N a plain id or an id of a sprint, is sent back when the store holds Case N, or a sub-case of it, under its id from an answer with another `agent_id`.
**＋** Its message gives `case-guppi` a free id, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
**＋** Each Case of that file is stored apart, under its id joined with its `agent_id`, and the entry of the other agent under the id alone stays as it was.
**＋** The Spec hook, the `Stop` comparison and the comparison of a case file with the store read the entry under the id alone.
**－** An unchanged file whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
**－** An entry with no `agent_id`, such as one held by `uv run --project .guppi guppi caseid --next`, gives no finding of this check, and neither does a file whose `agent_id` is the one of the entry under the id.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
