---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a Case that replaces the Criterion of an Estimate whole, writes no method and keeps one on the page that waits for another session, by the one predicate of .guppi/guppi/lint.py, but for an Estimate of a sprint page and a method part that opens with after and names its event before a colon
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k kept_method
checked: 2026-10-12
origin: raw/2026-10-07/1804/ledger.md#case-715
sprint: migration
created: 2026-10-07
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py` reads an `update` of an Estimate in the `then` blocks of the plan file that replaces its Criterion whole and carries no `set: {method: …}`, and the `method` of that Estimate's live page.

Then:
When a part of that `method` between two `;` names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or /hi, and does not name the person, the check gives one line `case N: update <slug>: the method on the page waits for another session — set a method that runs in this session`.
**＋** The judgment is `waits_for_another_session` of `.guppi/guppi/lint.py`, the same predicate that judges a `method` the plan writes.
**－** A part of that `method` that opens with `after`, or with `by hand, after`, and names its event before a colon waits for that event and gives no such line.
**－** An Estimate whose live page holds a sprint page `entity-sprint-<id>` as its `target`, by the predicate of `.guppi/guppi/ledger.py`, gives no such line.
**－** An `update` that sets the Estimate `passed` or `failed` by the person's decision gives no such line.
**－** An `update` that names a part of the page alone, such as a `set` of another field or a `replace` pair, gives no such line.
**－** A `method` on the page that waits for no other session, or whose part names the person, gives no such line.

## Result

2026-10-12, uv run pytest tests/test_prespec.py -k kept_method: 4 passed; a live method by hand, after a pull request from a second account: the output read gives no kept-method line, by hand after the librarian's run still gives it.

## History

- 2026-10-07 created · [[decision-case-715]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L21
- 2026-10-10 updated: the Criterion replaced whole — a kept method of an Estimate of a sprint page gives no finding, and the predicate names a session of a sprint and the session that closes one · [[decision-case-772.5]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L42
- 2026-10-12 updated: the Criterion replaced whole — a kept method part that waits for an event it names is no finding · [[decision-case-781.2]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L22
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
