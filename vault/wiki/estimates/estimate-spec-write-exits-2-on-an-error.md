---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook exits 2 with the error on stderr when its Stop run raises after reading the payload, and exits 0 on an error while reading the payload, on the re-fire and in the guard
method: uv run pytest tests/test_ratified.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-01
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
**＋** A Case of the reply that was not written when the error rose is written at the reply that repeats its ledger lines.
**＋** A Case written before the error stays written, and the repeat replaces its section.
**－** An error while the hook reads the payload exits 0 with the error on stderr. The hook cannot tell a re-fire at that point, and exit 2 could loop.
**－** With `stop_hook_active` (the re-fire after a block), the hook exits 0 and writes nothing, so it cannot loop.
**－** The guard `uv run guppi ratified --guard` keeps exit 0 with its line on stderr on its own error.
**－** A refusal of the hook with no error keeps its own reason on stderr and its own exit.

## Result

2026-10-01, uv run pytest tests/test_ratified.py: 89 passed (-k error: 4 passed)

## History

- 2026-09-30 created · [[decision-case-554]]
- 2026-10-01 status: pending → passed · raw/2026-09-30/2356/ledger.md#L43
