---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a Case that replaces the Criterion of an Estimate whole, writes no method and keeps one on the page that waits for another session, by the one predicate of guppi/lint.py
method: uv run pytest tests/test_prespec.py -k kept_method
origin: raw/2026-10-07/1804/ledger.md#case-715
sprint: migration
created: 2026-10-07
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads an `update` of an Estimate in the `then` blocks of the plan file that replaces its Criterion whole and carries no `set: {method: …}`, and the `method` of that Estimate's live page.

Then:
When a part of that `method` between two `;` names a later session, the next session, a session after another, the librarian or /hi, and does not name the person, the check gives one line `case N: update <slug>: the method on the page waits for another session — set a method that runs in this session`.
**＋** The judgment is `waits_for_another_session` of `guppi/lint.py`, the same predicate that judges a `method` the plan writes.
**－** An `update` that sets the Estimate `passed` or `failed` by the person's decision gives no such line.
**－** An `update` that names a part of the page alone, such as a `set` of another field or a `replace` pair, gives no such line.
**－** A `method` on the page that waits for no other session, or whose part names the person, gives no such line.

## Result

2026-10-07, uv run pytest tests/test_prespec.py -k kept_method: 2 passed, 198 deselected

## History

- 2026-10-07 created · [[decision-case-715]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L21
