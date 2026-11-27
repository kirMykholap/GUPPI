---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook writes, removes and checks Cases on a reply with stop_hook_active set as on a reply without it, so a Case repeated after a refusal is written at once
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k answers_a_refusal
checked: 2026-11-28
origin: raw/2026-10-05/0311/ledger.md#case-644.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply with `stop_hook_active` set: a reply that answers a refusal of a `Stop` hook, before the person's next message.

Then:
The hook writes, removes and checks Cases as on a reply without `stop_hook_active`.
**＋** A Case N whose decision lines the reply repeats after a refusal, with the cause fixed, is written at that reply into the Cases file `<plan stem>.cases.md` beside the plan file, and into `raw/<hi date>/<hi HHMM>/spec.md` once it stands.
**＋** A reason to refuse that reply exits 2 as without the flag, unless `estimate-spec-write-tells-each-reason-once` holds it back.
**－** A Case refused at the reply that acknowledges it does not wait for the person's next message to be written.

## Result

2026-11-28, Retro of session 2214, uv run --project .guppi pytest .guppi/tests/test_ratified.py -k answers_a_refusal: 3 passed; against Case 1087.6: a Case repeated on a flagged reply after a refusal is written at that reply into the Cases file and into spec.md

## History

- 2026-10-05 created · [[decision-case-644.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L6
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-28 updated: the Criterion replaced whole — a Case repeated after a refusal is written into the Cases file of the plan · [[decision-case-1087.6]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L35
