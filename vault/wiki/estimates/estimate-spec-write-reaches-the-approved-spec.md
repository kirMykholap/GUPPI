---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case ratified after the approval reaches spec.md from its stored answer, every section of it replaced or the Case placed, the ticks of its unchanged task lines kept
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k approved_spec
checked: 2026-11-28
origin: raw/2026-09-26/1745/ledger.md#case-441.6
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` has written a ratified Case N from the text stored under it into the Cases file `<plan stem>.cases.md` beside the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

Then:
The hook writes the same stored text of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
**＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
**＋** A task line whose text stood in a replaced section keeps the box it had there.
**＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the Cases file, come from the text stored under the parent, never from the reply.
**＋** With `stop_hook_active` set, the hook writes into `spec.md` as without it, as `estimate-spec-write-answers-a-refusal` sets it.
**－** Nothing written into `spec.md` is translated or refused for its language.
**－** A refusal that writes nothing of Case N into the Cases file writes nothing of it into `spec.md`.

## Result

2026-11-28, Retro of session 2214, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k approved_spec: 10 passed; against Case 1087.4: a Case written into the Cases file reaches spec.md with the boxes of its unchanged task lines kept, the plan file holds no section of it, and a refused showing writes it into neither file

## History

- 2026-09-26 created · [[decision-case-441.6]]
- 2026-09-30 updated: the Criterion replaced whole — spec.md holds recommend, the parent's from its stored answer (case 544.10) · [[decision-case-544.10]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-630]]
- 2026-10-05 updated: the Criterion replaced whole — the text stored under Case N in place of its stored answer; with stop_hook_active set the hook writes into spec.md as without it (case 644.5) · [[decision-case-644.5]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.7]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-28 updated: the Criterion replaced whole — the Case reaches spec.md beside the Cases file of the plan · [[decision-case-1087.4]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L33
