---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case ratified after the approval reaches spec.md from its stored answer, every section of it replaced or the Case placed, the ticks of its unchanged task lines kept
method: uv run pytest tests/test_ratified.py -k approved_spec; by hand, a Case ratified in Work Mode
checked: 2026-10-05
origin: raw/2026-09-26/1745/ledger.md#case-441.6
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` has written a ratified Case N from the text stored under it into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

Then:
The hook writes the same stored text of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
**＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
**＋** A task line whose text stood in a replaced section keeps the box it had there.
**＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the text stored under the parent, never from the reply.
**＋** With `stop_hook_active` set, the hook writes into `spec.md` as without it, as `estimate-spec-write-answers-a-refusal` sets it.
**－** Nothing written into `spec.md` is translated or refused for its language.
**－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.

## Result

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.

## History

- 2026-09-26 created · [[decision-case-441.6]]
- 2026-09-30 updated: the Criterion replaced whole — spec.md holds recommend, the parent's from its stored answer (case 544.10) · [[decision-case-544.10]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-630]]
- 2026-10-05 updated: the Criterion replaced whole — the text stored under Case N in place of its stored answer; with stop_hook_active set the hook writes into spec.md as without it (case 644.5) · [[decision-case-644.5]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.7]]
