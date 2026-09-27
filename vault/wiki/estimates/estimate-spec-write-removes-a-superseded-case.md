---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case superseded by a decision line of the reply leaves the plan file and spec.md, with its sub-cases
method: uv run pytest tests/test_ratified.py -k superseded; by hand, the first supersedes of a Case of the same session after the change
checked: 2026-09-27
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
**－** A Case N that neither file holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
**－** A line whose own Case the hook refused or did not write removes nothing.
**－** On the re-fire (`stop_hook_active`) nothing is removed: exit 0.

## Result

2026-09-27, uv run pytest tests/test_ratified.py -k superseded: 5 passed; by hand, session 1819: after the ratification of Case 460.5 with {supersedes:case 460.2}, the heading and sections of Case 460.2 were gone from the plan file and 460.5 stood whole

## History

- 2026-09-26 created · [[decision-case-441.7]]
- 2026-09-27 updated: the Criterion replaced whole — no ratified copy to remove it from (case 445.3) · [[decision-case-445.3]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L32
