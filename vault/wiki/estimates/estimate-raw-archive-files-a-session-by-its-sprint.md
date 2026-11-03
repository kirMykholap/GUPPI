---
type: estimate
kind: QA
status: passed
target: "[[rule-raw-archive]]"
purpose: Whether a done unit of raw/ goes to the archive folder of the sprint its own materialize.yaml records, and to the sprint of sprint.md only when its yaml records none
method: uv run --project .guppi pytest .guppi/tests/test_archive.py -k sprint
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, librarian, sprint]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi archive`, or the close of a sprint by `.guppi/guppi/sprint_close.py`, moves a done unit of `vault/raw/` by the move of `.guppi/guppi/archive.py`, or `.guppi/tests/test_archive.py` runs that move over a made-up vault.

Then:
The unit goes under `vault/archive/<sprint>/`, `<sprint>` being the value of the `sprint` field of its own `materialize.yaml`.
**＋** A unit whose yaml holds no `sprint` field takes the first `## <id>` heading of `vault/wiki/sprint.md`, as before.
**＋** The stdout line of the unit names the folder it went to.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
