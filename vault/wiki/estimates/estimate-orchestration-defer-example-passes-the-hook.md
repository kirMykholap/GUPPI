---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the example of a short-form defer in orchestration.md passes the Stop hook that writes a short put-off into the Spec, so the form the main agent copies stays a form the hook accepts
method: uv run --project .guppi pytest .guppi/tests/test_orchestration.py -k defer_example, passed and not skipped
checked: 2026-10-17
origin: raw/2026-10-05/1343/ledger.md#case-651.3
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Criterion

When:
`.guppi/tests/test_orchestration.py` runs under `uv run --project .guppi pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `.guppi/guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a short put-off, a Case of `defer` lines that the reply shows in the short form, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

Then:
`vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
**＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
**＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
**＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
**＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `.guppi/guppi/ratified.py`, and holds no copy of either.
**－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, both tests of `.guppi/tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

## Result

2026-10-17, Retro of session 1805: uv run --project .guppi pytest .guppi/tests/test_orchestration.py -k defer_example 2 passed, none skipped, over the defer block of vault/wiki/orchestration.md and write_defers of .guppi/guppi/ratified.py after the change of Case 879

## History

- 2026-10-05 created · [[decision-case-651.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged defer (case 661.2) · [[decision-case-661.2]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L2
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — its pointer stands in a bracket, and the insight stands archived · [[decision-case-823.4]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L68
- 2026-10-17 updated: the Criterion replaced whole — the line on an Insight of the repository of GUPPI dropped; the hook runs over a short put-off, the term of case 879.1 · [[decision-case-880.10]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L67
