---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook writes nothing of a ratified Case whose file under cases/ differs from the text the store holds for it
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k changed_file
checked: 2026-10-05
origin: raw/2026-10-05/0311/ledger.md#case-645.5
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, and reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

Then:
The hook compares the Cases of that file with the entries of the store under their ids, by the one function of `.guppi/guppi/casecheck.py` that the `Stop` check of a showing runs.
**＋** A Case of the file that differs from its entry, or that the store does not hold: exit 2 with the reason on stderr, and nothing of Case N is written into the plan file or into `raw/<date>/<hi HHMM>/spec.md`.
**＋** With `stop_hook_active` set, the hook compares and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
**－** A defer-only Case has no file and is not compared.

## Result

2026-10-05, at the /hi of session 1343: uv run pytest -q tests/test_ratified.py -k changed_file 2 passed, 104 deselected

## History

- 2026-10-05 created · [[decision-case-645.5]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L3
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
