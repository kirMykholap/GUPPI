---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes setup_done = false into the Render of rule-guppi-config of the clean version, whether the working tree holds the key or not, every other line kept, and whether setup_pending of config.py takes the setup as not done only on setup_done = false
method: uv run --project .guppi pytest .guppi/tests/test_config.py .guppi/tests/test_ship.py -k setup
origin: raw/2026-11-03/0316/ledger.md#case-1017.1
sprint: plugin
created: 2026-11-03
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` builds the clean version from a working tree whose Render of `rule-guppi-config` holds the line `setup_done = true`, or no line of the key `setup_done`.
**＋** A hook reads `guppi.toml` by `setup_pending` of `.guppi/guppi/config.py`, or `.guppi/tests/test_config.py` and `.guppi/tests/test_ship.py` run it over a made-up project.

Then:
The copy of `rule-guppi-config` in the clean version holds `setup_done = false` in place of each line of that key, or as a line added before the closing marker line of its Render where no line of the key stands, and every other line of its Render as the working tree holds it.
**＋** A `guppi.toml` written from the Render of that copy makes `setup_pending` answer that the setup is not done.
**＋** `setup_pending` answers that the setup is not done only where `guppi.toml` holds `setup_done = false`.
**－** A missing `guppi.toml`, a text that does not parse, a missing key `setup_done` and any other value of it count as the setup done.
**－** The key does not stop the render, and `guppi.toml` of the working tree stays out of the clean version.

## Result

2026-11-03, uv run --project .guppi pytest .guppi/tests/test_config.py .guppi/tests/test_ship.py -k setup at Retro of session 0316; 10 passed: setup_pending is True only on setup_done = false, and the copy of rule-guppi-config holds setup_done = false whether the working tree holds setup_done = true or no line of the key

## History

- 2026-11-03 created · [[decision-case-1017.1]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/0316/ledger.md#L28
