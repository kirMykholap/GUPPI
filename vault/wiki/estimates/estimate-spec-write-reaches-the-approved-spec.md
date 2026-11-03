---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: A Case ratified after the approval reaches spec.md from its stored answer, every section of it replaced or the Case placed, the ticks of its unchanged task lines kept
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k approved_spec; by hand, a Case ratified in Work Mode
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` has written a ratified Case N from the text stored under it into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

Then:
The hook writes the same stored text of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
**＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
**＋** A task line whose text stood in a replaced section keeps the box it had there.
**＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the text stored under the parent, never from the reply.
**＋** With `stop_hook_active` set, the hook writes into `spec.md` as without it, as `estimate-spec-write-answers-a-refusal` sets it.
**－** Nothing written into `spec.md` is translated or refused for its language.
**－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
