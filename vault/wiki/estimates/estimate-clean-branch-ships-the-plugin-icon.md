---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the clean version holds the icon .guppi/icon.png as it stands, a PNG of 512 by 512 pixels, whose manifest names it in the field icon, and whether guppi ship and its --check print no line on it
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k icon
origin: raw/2026-11-03/0316/ledger.md#case-1016
sprint: plugin
created: 2026-11-03
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, from a working tree that holds `.guppi/icon.png` and `plugin/plugin.json`.
**＋** `uv run --project .guppi guppi ship --check` judges that working tree.

Then:
The clean version holds `.guppi/icon.png`, byte for byte the file of the working tree.
**＋** Its manifest, copied from `plugin/plugin.json`, carries the field `icon`, whose value is the path of `.guppi/icon.png` from the root of the plugin.
**＋** `.guppi/icon.png` of the working tree is a PNG image of 512 by 512 pixels.
**＋** Neither the build nor `uv run --project .guppi guppi ship --check` prints a line on `.guppi/icon.png`.
**－** What `claude plugin validate` notes on the field `icon` of `plugin/plugin.json`, and how Anthropic's directory shows the picture, are no part of this promise.

## Result

2026-11-03, uv run --project .guppi pytest .guppi/tests/test_ship.py -k icon at Retro of session 0316; 3 passed: the copy holds .guppi/icon.png byte for byte with no line, --check prints no line on it, and the live .guppi/icon.png is a PNG of 512 by 512 named by the field icon of plugin/plugin.json

## History

- 2026-11-03 created · [[decision-case-1016]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/0316/ledger.md#L27
