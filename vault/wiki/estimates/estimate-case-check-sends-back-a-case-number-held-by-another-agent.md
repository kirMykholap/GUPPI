---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case of case-guppi under an id, plain or of a sprint, that the store holds from the answer of another agent goes back to it with a free id, and the other agent's entry is kept
method: uv run pytest tests/test_casecheck.py -k subagent_clash
checked: 2026-10-13
origin: raw/2026-10-03/0115/ledger.md#case-610.2
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, `agent_id` of the payload, and `<plan>.checked.json`.

Then:
The hook stores each Case of the file in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
**＋** A top-level Case N of the file, N a plain id or an id of a sprint, is sent back when the store holds Case N, or a sub-case of it, under its id from an answer with another `agent_id`.
**＋** Its message gives `case-guppi` a free id, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
**＋** Each Case of that file is stored apart, under its id joined with its `agent_id`, and the entry of the other agent under the id alone stays as it was.
**＋** The Spec hook, the `Stop` comparison and the comparison of a case file with the store read the entry under the id alone.
**－** An unchanged file whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
**－** An entry with no `agent_id`, stored before the change or held by `uv run guppi caseid --next`, gives no finding of this check, and neither does a file whose `agent_id` is the one of the entry under the id.

## Result

2026-10-13, uv run pytest tests/test_casecheck.py -k subagent_clash: 5 passed — Case kir-plugin-12 held by another agent is sent back as kir-plugin-13; an id held by guppi caseid --next with no agent_id gives no finding

## History

- 2026-10-03 created · [[decision-case-610.2]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 updated: the method selects -k subagent_clash, so that the tests of session_clash are not run (case 632.8) · [[decision-case-632.8]]
- 2026-10-05 updated: the method is pytest alone; the live send-back is no longer waited for (case 637.1) · [[decision-case-637.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L5
- 2026-10-05 updated: the Criterion replaced whole — the Cases are read from the file case-guppi wrote, and no hook writes the file from the entry (case 645.9) · [[decision-case-645.9]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L6
- 2026-10-13 updated: the Criterion replaced whole — an id of a sprint is judged as a plain one, and an id held by guppi caseid --next gives no finding (case 788.7) · [[decision-case-788.7]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L53
