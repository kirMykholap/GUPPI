---
type: estimate
kind: QA
status: passed
target: "[[rule-raw-archive]]"
purpose: Whether a done unit of raw/ goes to the archive folder of the sprint its own materialize.yaml records, and to the sprint of sprint.md only when its yaml records none
method: uv run --project .guppi pytest .guppi/tests/test_archive.py -k sprint
origin: raw/2026-10-08/2352/ledger.md#case-743.2
sprint: migration
created: 2026-10-08
tags: [harness, librarian, sprint]
---

## Criterion

When:
`uv run --project .guppi guppi archive`, or the close of a sprint by `.guppi/guppi/sprint_close.py`, moves a done unit of `vault/raw/` by the move of `.guppi/guppi/archive.py`, or `.guppi/tests/test_archive.py` runs that move over a made-up vault.

Then:
The unit goes under `vault/archive/<sprint>/`, `<sprint>` being the value of the `sprint` field of its own `materialize.yaml`.
**＋** A unit whose yaml holds no `sprint` field takes the first `## <id>` heading of `vault/wiki/sprint.md`, as before.
**＋** The stdout line of the unit names the folder it went to.

## Result

2026-10-09, uv run pytest tests/test_archive.py -k sprint; 2 passed: a unit whose yaml holds sprint a goes under vault/archive/a/ while sprint.md names b, a unit with no sprint field goes under b

## History

- 2026-10-09 created · [[decision-case-743.2]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L30
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
