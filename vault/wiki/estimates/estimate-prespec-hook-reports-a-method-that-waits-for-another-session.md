---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a method in the plan that waits for a later session, a session of a sprint, the session that closes one, the librarian or a /hi, by one predicate of guppi/lint.py, and leaves alone a method that names the person, the method of an Estimate of a sprint page, and the live pages
method: uv run pytest tests/test_prespec.py tests/test_lint.py -k waits
checked: 2026-10-10
origin: raw/2026-10-05/1831/ledger.md#case-670.4
sprint: migration
created: 2026-10-05
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

Then:
A `method` with a part between two `;` that names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
**＋** The judgment is one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
**＋** Whether the target is a sprint page is judged by one predicate in `guppi/ledger.py`, which `guppi/prespec.py`, `guppi/materialize.py`, `guppi/sprint.py` and `guppi/sprint_close.py` import.
**－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
**－** An Estimate whose target is a sprint page `entity-sprint-<id>` — the `ref` of a `create`, or the `target` that an `update` sets or that the live page holds — gives no such line.
**－** `uv run guppi lint` of `guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
**－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

## Result

2026-10-10, uv run pytest tests/test_prespec.py tests/test_lint.py -k waits: 5 passed — a session of a sprint and the session that closes one are caught; an Estimate of a sprint page, by create ref or update target, gives no line, the same method on a rule does

## History

- 2026-10-05 created · [[decision-case-670.4]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L4
- 2026-10-10 updated: the Criterion replaced whole — the predicate catches a session of a sprint and the session that closes one, and an Estimate of a sprint page gives no finding · [[decision-case-772.4]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L41
