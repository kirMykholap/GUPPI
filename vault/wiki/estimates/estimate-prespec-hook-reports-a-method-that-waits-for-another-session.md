---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a method in the plan that waits for a later session, a session of a sprint, the session that closes one, the librarian or a /hi, by one predicate of .guppi/guppi/lint.py, and leaves alone a method that names the person, a part that opens with after and names its event before a colon, the method of an Estimate of a sprint page, and the live pages
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k waits
checked: 2026-10-12
origin: raw/2026-10-05/1831/ledger.md#case-670.4
sprint: migration
created: 2026-10-05
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

Then:
A `method` with a part between two `;` that names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
**＋** The judgment is one predicate in `.guppi/guppi/lint.py`, which `.guppi/guppi/prespec.py` imports.
**＋** Whether the target is a sprint page is judged by one predicate in `.guppi/guppi/ledger.py`, which `.guppi/guppi/prespec.py`, `.guppi/guppi/materialize.py` and `.guppi/guppi/sprint.py` import.
**－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
**－** A part that opens with `after`, or with `by hand, after`, and names its event before a colon, such as `by hand, after a pull request from a second account: the hook's output read against the Criterion`, waits for that event and gives no such line, whatever event it names, a later session or the librarian's run among them; the predicate of that part is one function in `.guppi/guppi/lint.py`. A part with the same words but no colon, or one in which `after` does not open the part, still gives the line.
**－** An Estimate whose target is a sprint page `entity-sprint-<id>` — the `ref` of a `create`, or the `target` that an `update` sets or that the live page holds — gives no such line.
**－** `uv run --project .guppi guppi lint` of `.guppi/guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
**－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

## Result

2026-10-12, uv run pytest tests/test_prespec.py tests/test_lint.py -k waits: 8 passed; a part that opens with after or by hand, after and names its event before a colon is no wait line on a create and an update, the same words without a colon or with after not opening the part still wait; lint does not call the predicate over live pages.

## History

- 2026-10-05 created · [[decision-case-670.4]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L4
- 2026-10-10 updated: the Criterion replaced whole — the predicate catches a session of a sprint and the session that closes one, and an Estimate of a sprint page gives no finding · [[decision-case-772.4]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L41
- 2026-10-12 updated: the Criterion replaced whole — a method part that opens with after and names its event before a colon is no finding · [[decision-case-781.1]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L21
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
