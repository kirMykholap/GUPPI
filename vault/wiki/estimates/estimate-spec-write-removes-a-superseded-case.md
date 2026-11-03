---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case superseded by a decision line of the reply leaves the plan file and spec.md, with its sub-cases
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k superseded; by hand, a supersedes of a Case of the same session
checked: 2026-10-07
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply whose `LEDGER` block holds a decision line carrying `{supersedes:case N}`, and it has written the Case of that line in the same run.

Then:
The hook removes the section of Case N — its heading, its sections, its `then` and `tasks` blocks, and the sections of its sub-cases — from the plan file.
**＋** Once `raw/<hi date>/<hi HHMM>/spec.md` stands, it removes every section of Case N and of its sub-cases from it too.
**＋** A `{supersedes:case N.M}` removes the section of that sub-case alone while another sub-case of its parent with a decision line is not retired; the parent and those other sub-cases stay.
**＋** When the marks of the session's `raw/<date>/<hi HHMM>/ledger.md` and of the reply retire each sub-case of a parent that has a decision line, judged by `retired_whole` of `.guppi/guppi/prespec.py`, imported, not copied, and the parent holds no decision line of its own that no mark retires, the hook removes the section of that parent too.
**－** A parent with a decision line of its own that no mark retires stays in the plan file and in `raw/<hi date>/<hi HHMM>/spec.md`, though each of its sub-cases is retired.
**＋** A section of Case N under `## Deferred` is removed the same way.
**＋** With `stop_hook_active` set, the hook removes as without it, as `estimate-spec-write-answers-a-refusal` sets it.
**－** A Case N that neither file holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
**－** A line whose own Case the hook refused or did not write removes nothing.

## Result

2026-10-07, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
