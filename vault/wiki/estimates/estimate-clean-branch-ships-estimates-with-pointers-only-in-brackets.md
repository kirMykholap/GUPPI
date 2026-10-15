---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether each Estimate that guppi ship takes into the clean version holds each pointer to a case, a decision or a session in a bracket of its own, so that the build prints no line on it
method: "by hand, after the librarian's run of this session: uv run --project .guppi pytest .guppi/tests/test_ship.py -m live, read against the Criterion"
origin: raw/2026-10-15/1959/ledger.md#case-823.1
sprint: plugin
created: 2026-10-15
tags: [ci, plugin]
---

## Criterion

When:
`.guppi/tests/test_ship.py` runs under `uv run --project .guppi pytest -m live` and builds, by `ship` of `.guppi/guppi/ship.py`, the clean version of this repository from its working tree into a temporary folder, with a version the test passes itself.

Then:
No `ship:` line of that build names a page under `vault/wiki/estimates/`.
**＋** Each Estimate of this repository that the build takes holds each pointer to a case, a decision or a session in its `purpose`, its `method` and its `## Criterion` in a bracket of its own at the end of its sentence, as `outside` of `.guppi/guppi/pointers.py` judges it.
**＋** Each such Estimate keeps every pointer it held, with the words that go with it, in that bracket.
**－** The test reads no tag `prod-x.y.z`, and a page with `core: true` stays with `estimate-clean-branch-pages-hold-pointers-only-in-brackets`.
**－** A run of `uv run --project .guppi pytest` without `-m live` leaves the test out, by the settings of `.guppi/pyproject.toml`.

## History

- 2026-10-15 created · [[decision-case-823.1]]
