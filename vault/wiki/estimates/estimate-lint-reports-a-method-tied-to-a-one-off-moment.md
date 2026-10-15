---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: Whether lint and pre-spec report a method that ties its reading by hand to the first moment after the render or after the change, by one predicate, and leave a method that names the kind of its moment
method: uv run --project .guppi pytest .guppi/tests/test_lint.py .guppi/tests/test_prespec.py -k moment; the uv run --project .guppi guppi check of a later session, no moment finding on wiki/estimates/
checked: 2026-10-03
origin: raw/2026-10-03/0317/ledger.md#case-613.1
sprint: migration
created: 2026-10-03
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the `method` field of each live Estimate under `vault/wiki/estimates/`.
**＋** Or `uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

Then:
A `method` that holds `by hand` and names the first of something after the render or after the change, with no `;` between the two, is one lint finding of the class `moment`.
**＋** The same `method` in the plan gives one line `case N: <create|update> <slug>: method ties its reading by hand to the first moment after the render or the change`, which goes on to say that the method names the kind of its moment.
**＋** Both sides judge by one predicate in `.guppi/guppi/lint.py`, which `.guppi/guppi/prespec.py` imports.
**－** A `method` that names the kind of its moment, with no word "first", gets no such finding.
**－** A `method` that names the first of an event without "after the render" or "after the change", such as the first close of a sprint, gets no such finding.
**－** A `method` without `by hand` gets no such finding.
**－** The finding does not replace the `method` finding of a `method` that names no form.

## Result

2026-10-03, at the /hi of session 1341: `uv run pytest tests/test_lint.py tests/test_prespec.py -k moment` 5 passed, 264 deselected; `make lint` exit 2, 48 lines (5 deferred, 41 unread: pending, 1 unread: failed, the make error line), no finding of the class moment on wiki/estimates/ — the one line with the word is the unread line of this Estimate; guppi/prespec.py imports `tied_to_a_one_off_moment` from guppi/lint.py

## History

- 2026-10-03 created · [[decision-case-613.1]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1341/ledger.md#L1
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
