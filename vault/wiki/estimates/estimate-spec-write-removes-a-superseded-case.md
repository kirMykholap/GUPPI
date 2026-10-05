---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case superseded by a decision line of the reply leaves the plan file and spec.md, with its sub-cases
method: uv run pytest tests/test_ratified.py -k superseded; by hand, a supersedes of a Case of the same session
checked: 2026-10-05
origin: raw/2026-09-26/1745/ledger.md#case-441.7
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds a decision line carrying `{supersedes:case N}`, and it has written the Case of that line in the same run.

Then:
The hook removes the section of Case N — its heading, its sections, its `then` and `tasks` blocks, and the sections of its sub-cases — from the plan file.
**＋** Once `raw/<hi date>/<hi HHMM>/spec.md` stands, it removes every section of Case N and of its sub-cases from it too.
**＋** A `{supersedes:case N.M}` removes the section of that sub-case alone; its parent and its other sub-cases stay.
**＋** A section of Case N under `## Deferred` is removed the same way.
**＋** With `stop_hook_active` set, the hook removes as without it, as `estimate-spec-write-answers-a-refusal` sets it.
**－** A Case N that neither file holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
**－** A line whose own Case the hook refused or did not write removes nothing.

## Result

2026-10-05, by hand at the Work readings of session 1343: uv run pytest -q tests/test_ratified.py -k superseded 7 passed; the plan held `## Case 653`, `### Case 653.1` and `### Case 653.2` at 15:25:20; after the reply of Case 658 with {supersedes:case 653} the heading listing at 15:48:46 holds `## Case 658` and no heading of 653, 653.1 or 653.2; after Case 659 with {supersedes:case 658}{supersedes:case 653}{supersedes:case 653.1}{supersedes:case 653.2} the plan holds `## Case 659` and no `## Case 658`; marks on Cases the plan no longer held, and {supersedes:case 649} of session 0311 on Case 655, gave no refusal; not exercised: the removal from spec.md and a sub-case mark whose parent stands

## History

- 2026-09-26 created · [[decision-case-441.7]]
- 2026-09-27 updated: the Criterion replaced whole — no ratified copy to remove it from (case 445.3) · [[decision-case-445.3]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L32
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-05 updated: the Criterion replaced whole — with stop_hook_active set the hook removes a superseded Case as without it (case 644.6) · [[decision-case-644.6]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L35
