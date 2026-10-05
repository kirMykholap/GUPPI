---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook writes nothing of a ratified Case whose file under cases/ differs from the text the store holds for it
method: uv run pytest tests/test_ratified.py -k changed_file
origin: raw/2026-10-05/0311/ledger.md#case-645.5
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, and reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

Then:
The hook compares the Cases of that file with the entries of the store under their ids, by the one function of `guppi/casecheck.py` that the `Stop` check of a showing runs.
**＋** A Case of the file that differs from its entry, or that the store does not hold: exit 2 with the reason on stderr, and nothing of Case N is written into the plan file or into `raw/<date>/<hi HHMM>/spec.md`.
**＋** With `stop_hook_active` set, the hook compares and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
**－** A defer-only Case has no file and is not compared.

## History

- 2026-10-05 created · [[decision-case-645.5]]
