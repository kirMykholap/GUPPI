---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook exits 2 with the error on stderr when its Stop run raises after reading the payload, once a stretch for the same error, exits 0 and prints nothing with stop_hook_active set and a transcript it cannot read, and exits 0 on an error while reading the payload and in the guard
method: uv run pytest tests/test_ratified.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-05
origin: raw/2026-09-30/2042/ledger.md#case-554
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` fires, and an exception rises in `guppi/ratified.py` after the hook has read the payload: while it reads the transcript, the store, the plan file or `spec.md`, or while it writes, removes or checks a Case.

Then:
The hook exits 2. Its stderr holds `ratified: not done: <error>` and the advice to repeat the ledger lines once the cause is fixed, so the agent sees the error at the end of that reply.
**＋** The reply that repeats the ledger lines writes a Case that the error left unwritten.
**＋** A Case written before the error stays written, and the repeat replaces its section.
**＋** The error line is told once a stretch, as `estimate-spec-write-tells-each-reason-once` sets it for every reason of the hook.
**－** When `stop_hook_active` is set and the hook cannot read the transcript, so it cannot tell whether a refusal of its own stands, it exits 0 and prints nothing, so it cannot loop.
**－** An error while the hook reads the payload exits 0 with the error on stderr. The hook cannot read its refusals at that point, and exit 2 could loop.
**－** The guard `uv run guppi ratified --guard` keeps exit 0 with its line on stderr on its own error.
**－** A refusal of the hook with no error keeps its own reason on stderr and its own exit.

## Result

2026-10-05, at the /hi of session 1343: uv run pytest -q tests/test_ratified.py 106 passed

## History

- 2026-09-30 created · [[decision-case-554]]
- 2026-10-01 status: pending → passed · raw/2026-09-30/2356/ledger.md#L43
- 2026-10-05 updated: the Criterion replaced whole — an error is told once a stretch, judged by the hook's own refusals in the transcript, and with stop_hook_active set and a transcript it cannot read the hook exits 0 silent; the purpose follows (case 644.7) · [[decision-case-644.7]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L1
