---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a Case whose create or set leaves a page short of what a condition of its schema requires, by one function of .guppi/guppi/lint.py, and leaves alone a Case that does not cause the break
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k condition
origin: raw/2026-10-07/1804/ledger.md#case-714
sprint: migration
created: 2026-10-07
tags: [harness, workflow, schema]
---

## Criterion

When:
`judge` of `.guppi/guppi/prespec.py` — run by `uv run --project .guppi guppi prespec --check <plan> --session <id>`, by the check of a Case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` or an `update` item of the `then` blocks, and the page it names, by the `schema.yaml` of the category of its slug.

Then:
A `create` that leaves its page without a field or section that a condition of the schema requires, or an `update` whose `set` gives the value a condition starts on while neither the page nor the Cases judged hold what it requires, gives one finding that names the Case, the slug, the missing field or section and the condition.
**＋** The judgment of a condition is one function of `.guppi/guppi/lint.py`, which `check_schema` and `.guppi/guppi/prespec.py` both call, and `uv run --project .guppi guppi check` reports what it reported before.
**＋** A field that `.guppi/guppi/generate.py` fills from the item, such as `parent` from `ref`, counts as present, and so does a field or section that an earlier Case of the plan writes on the same page.
**－** An `update` that sets no value a condition starts on gives no such finding, even when the page already breaks a condition.
**－** A category whose schema rule a Case of the session changes is not judged, as for the check of the keys.
**－** In the check of a Case file of `rule-case-check`, a field that only a Case of the session outside the file writes does not count.
**－** A `defer` item is not judged.

## Result

2026-10-07, uv run pytest tests/test_prespec.py tests/test_lint.py -k condition: 7 passed, 283 deselected

## History

- 2026-10-07 created · [[decision-case-714]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L20
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
