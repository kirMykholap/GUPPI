---
type: estimate
kind: QA
status: passed
target: "[[rule-cleanup]]"
purpose: Whether guppi cleanup moves an archived page under the sprint that the materialize.yaml of the session of its run records, and under the sprint of sprint.md only when that yaml or its field is missing
method: uv run --project .guppi pytest .guppi/tests/test_cleanup.py -k sprint
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, librarian, sprint]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi cleanup` of `.guppi/guppi/cleanup.py` moves a live page with `status: archived` under `vault/archive/`, or `.guppi/tests/test_cleanup.py` runs that move over a made-up vault.

Then:
The page goes under `vault/archive/<sprint>/`, `<sprint>` being the value of the `sprint` field of the `vault/raw/<date>/<HHMM>/materialize.yaml` of the session of the run.
**＋** A run whose session has no `materialize.yaml`, or whose yaml holds no `sprint` field, or a run with no session folder, takes the first `## <id>` heading of `vault/wiki/sprint.md`, as before.
**－** The date and session folders under the sprint folder, the History and `log.md` lines and the rest of the move do not change.

## Result

2026-10-10, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
