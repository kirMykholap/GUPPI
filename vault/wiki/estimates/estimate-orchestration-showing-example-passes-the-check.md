---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: Whether the example of a showing in orchestration.md passes the Stop check of a reply that shows a Case, so the form the main agent copies stays a form the check accepts
method: uv run pytest tests/test_orchestration.py -k showing_example, passed and not skipped
checked: 2026-10-05
origin: raw/2026-10-05/1343/ledger.md#case-651.2
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Criterion

When:
`tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

Then:
`vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
**＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
**＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the `Stop` check of `rule-case-check`, which is the source of the limits; it lists no other limit.
**＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
**＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
**＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
**－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

## Result

2026-10-05, at the /hi of session 1616: uv run pytest -q -rs tests/test_orchestration.py -k showing_example 2 passed, 2 deselected, none skipped

## History

- 2026-10-05 created · [[decision-case-651.2]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L1
- 2026-10-05 updated: the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged showing (case 661.1) · [[decision-case-661.1]]
