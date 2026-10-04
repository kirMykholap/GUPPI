---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: A Case ratified after the approval reaches spec.md from its stored answer, every section of it replaced or the Case placed, the ticks of its unchanged task lines kept
method: uv run pytest tests/test_ratified.py -k approved_spec; by hand, a Case ratified in Work Mode
origin: raw/2026-09-26/1745/ledger.md#case-441.6
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` has written a ratified Case N from its stored answer into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

Then:
The hook writes the same stored answer of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
**＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
**＋** A task line whose text stood in a replaced section keeps the box it had there.
**＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the parent's stored answer, never from the reply.
**－** Nothing written into `spec.md` is translated or refused for its language.
**－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.
**－** On the re-fire (`stop_hook_active`) nothing is written: exit 0.

## History

- 2026-09-26 created · [[decision-case-441.6]]
- 2026-09-30 updated: the Criterion replaced whole — spec.md holds recommend, the parent's from its stored answer (case 544.10) · [[decision-case-544.10]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-630]]
