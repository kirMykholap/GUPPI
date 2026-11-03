---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the clean version holds no file of plugin/assets/, guppi ship --check prints no line on one, and the repository keeps both source pictures of the icon there and no folder guppi-assets/
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k source_pictures
origin: raw/2026-11-03/1825/ledger.md#case-1020
sprint: plugin
created: 2026-11-03
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, from a working tree that holds a picture under `plugin/assets/`.
**＋** `uv run --project .guppi guppi ship --check` judges that working tree.

Then:
The clean version holds no file of `plugin/assets/`, at that path or at any other.
**＋** `uv run --project .guppi guppi ship --check` prints no line on a file of `plugin/assets/`.
**＋** The repository of GUPPI holds `plugin/assets/icon_guppi.png` and `plugin/assets/logo_guppi.png`, and no folder `guppi-assets/`.
**－** What the pictures under `plugin/assets/` show is no part of this promise: neither the build nor `--check` reads them.

## Result

2026-11-03, Retro of session 1825, uv run --project .guppi pytest .guppi/tests/test_ship.py -k source_pictures: 3 passed, 62 deselected; the full uv run --project .guppi guppi test: 1946 passed, 6 skipped, 1 deselected

## History

- 2026-11-03 created · [[decision-case-1020]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/1825/ledger.md#L15
