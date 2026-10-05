---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook writes, removes and checks Cases on a reply with stop_hook_active set as on a reply without it, so a Case repeated after a refusal is written at once
method: "uv run pytest tests/test_ratified.py -k answers_a_refusal; by hand at the /hi of a later session: a Case refused at the reply that acknowledges it and written into the plan file at the reply that answers the refusal, read in the plan file and the transcript, recorded in the estimate line"
checked: 2026-10-05
origin: raw/2026-10-05/0311/ledger.md#case-644.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply with `stop_hook_active` set: a reply that answers a refusal of a `Stop` hook, before the person's next message.

Then:
The hook writes, removes and checks Cases as on a reply without `stop_hook_active`.
**＋** A Case N whose decision lines the reply repeats after a refusal, with the cause fixed, is written at that reply into the plan file, and into `raw/<hi date>/<hi HHMM>/spec.md` once it stands.
**＋** A reason to refuse that reply exits 2 as without the flag, unless `estimate-spec-write-tells-each-reason-once` holds it back.
**－** A Case refused at the reply that acknowledges it does not wait for the person's next message to be written.

## Result

2026-10-05, at the /hi of session 1616: uv run pytest -q -rs tests/test_ratified.py -k answers_a_refusal 2 passed, 115 deselected; by hand, transcript f5706873 of session 1343: the Stop hook refused the reply that acknowledged Case 659 at 12:50:01 with "ratified: case 659: no fence tagged then with its defer items"; the reply that answered the refusal (12:50:08) carried the short form with its `then` fence and its LEDGER line, its Stop at 12:50:10 had no hook error, and the plan file mossy-humming-peacock.md holds `## Case 659` at line 650 under `## Deferred`, found there at 12:50:58 with no other Stop after 12:50:10, so it was written at that Stop, before the person's next message at 12:50:53

## History

- 2026-10-05 created · [[decision-case-644.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L6
