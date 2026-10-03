---
type: estimate
kind: QA
status: pending
target: "[[rule-lint]]"
purpose: Whether lint and pre-spec report a method that ties its reading by hand to the first moment after the render or after the change, by one predicate, and leave a method that names the kind of its moment
method: uv run pytest tests/test_lint.py tests/test_prespec.py -k moment; the make lint of a later session, no moment finding on wiki/estimates/
origin: raw/2026-10-03/0317/ledger.md#case-613.1
sprint: migration
created: 2026-10-03
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` reads the `method` field of each live Estimate under `vault/wiki/estimates/`.
**＋** Or `uv run guppi prespec --check <plan> --session <id>` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

Then:
A `method` that holds `by hand` and names the first of something after the render or after the change, with no `;` between the two, is one lint finding of the class `moment`.
**＋** The same `method` in the plan gives one line `case N: <create|update> <slug>: method ties its reading by hand to the first moment after the render or the change`, which goes on to say that the method names the kind of its moment.
**＋** Both sides judge by one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
**－** A `method` that names the kind of its moment, with no word "first", gets no such finding.
**－** A `method` that names the first of an event without "after the render" or "after the change", such as the first close of a sprint, gets no such finding.
**－** A `method` without `by hand` gets no such finding.
**－** The finding does not replace the `method` finding of a `method` that names no form.

## History

- 2026-10-03 created · [[decision-case-613.1]]
