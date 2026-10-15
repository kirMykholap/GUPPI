---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case superseded by a decision line of the reply leaves the plan file and spec.md, with its sub-cases
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k superseded; by hand, a supersedes of a Case of the same session
checked: 2026-10-07
origin: raw/2026-09-26/1745/ledger.md#case-441.7
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow]
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

2026-10-07, Retro of session 2114: uv run pytest tests/test_ratified.py -k superseded 10 passed — a Case and its sub-cases leave the plan and spec.md, a sub-case leaves alone while another with a decision line stands, the last sub-case retired by the ledger and the reply takes its parent out of the plan and spec.md, a parent with a create line of its own stays, a section under Deferred leaves, a flagged reply removes, a refused Case removes nothing; not exercised by hand: no supersedes of a Case of the same session occurred in this session

## History

- 2026-09-26 created · [[decision-case-441.7]]
- 2026-09-27 updated: the Criterion replaced whole — no ratified copy to remove it from (case 445.3) · [[decision-case-445.3]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L32
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-05 updated: the Criterion replaced whole — with stop_hook_active set the hook removes a superseded Case as without it (case 644.6) · [[decision-case-644.6]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L35
- 2026-10-07 updated: the Criterion replaced whole — a parent whose every sub-case is retired leaves the plan and spec.md (case 722.2) · [[decision-case-722.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/2114/ledger.md#L20
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
