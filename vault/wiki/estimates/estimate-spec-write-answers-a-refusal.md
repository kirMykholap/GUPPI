---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook writes, removes and checks Cases on a reply with stop_hook_active set as on a reply without it, so a Case repeated after a refusal is written at once
method: "uv run --project .guppi pytest .guppi/tests/test_ratified.py -k answers_a_refusal; by hand at the /hi of a later session: a Case refused at the reply that acknowledges it and written into the plan file at the reply that answers the refusal, read in the plan file and the transcript, recorded in the estimate line"
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply with `stop_hook_active` set: a reply that answers a refusal of a `Stop` hook, before the person's next message.

Then:
The hook writes, removes and checks Cases as on a reply without `stop_hook_active`.
**＋** A Case N whose decision lines the reply repeats after a refusal, with the cause fixed, is written at that reply into the plan file, and into `raw/<hi date>/<hi HHMM>/spec.md` once it stands.
**＋** A reason to refuse that reply exits 2 as without the flag, unless `estimate-spec-write-tells-each-reason-once` holds it back.
**－** A Case refused at the reply that acknowledges it does not wait for the person's next message to be written.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
