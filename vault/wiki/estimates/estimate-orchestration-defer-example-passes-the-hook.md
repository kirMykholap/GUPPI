---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the example of a short-form defer in orchestration.md passes the Stop hook that writes a defer-only Case into the Spec, so the form the main agent copies stays a form the hook accepts
method: uv run pytest tests/test_orchestration.py -k defer_example, passed and not skipped
checked: 2026-10-05
origin: raw/2026-10-05/1343/ledger.md#case-651.3
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Criterion

When:
`tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

Then:
`vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
**＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
**＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
**＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
**＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `guppi/ratified.py`, and holds no copy of either.
**＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands `actioned`, addressed by case 651.3.
**－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

## Result

2026-10-05, /hi of 1831, uv run pytest tests/test_orchestration.py -rs; 6 passed, none skipped

## History

- 2026-10-05 created · [[decision-case-651.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged defer (case 661.2) · [[decision-case-661.2]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L2
