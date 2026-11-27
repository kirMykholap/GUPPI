---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether plugin/assets/GUPPI.png, the first sketch that README.md shows, is a PNG from 800 to 1200 pixels wide and under 1 000 000 bytes
method: "by hand, in Work Mode once the person's export stands at plugin/assets/GUPPI.png: the output of uv run --project .guppi python -c \"import os, struct; p = 'plugin/assets/GUPPI.png'; b = open(p, 'rb').read(24); print(b[:8] == b'\\x89PNG\\r\\n\\x1a\\n', os.path.getsize(p), *struct.unpack('>II', b[16:24]))\", which prints whether the first 8 bytes are the PNG signature, the size in bytes, the width and the height, read against the Criterion; the estimate line keeps the four values"
origin: raw/2026-11-27/1402/ledger.md#case-1086
sprint: plugin
created: 2026-11-27
tags: [readme, github]
once: true
---

## Criterion

When:
The person's new export of the Excalidraw board stands at `plugin/assets/GUPPI.png` in the working tree.

Then:
`plugin/assets/GUPPI.png` holds fewer than 1 000 000 bytes.
**＋** `plugin/assets/GUPPI.png` is a PNG from 800 to 1200 pixels wide.
**－** `README.md` does not change: its picture and its link keep the path `plugin/assets/GUPPI.png`.
**－** No file of `plugin/assets/` enters the clean version that `rule-clean-branch` sets.

## Result

2026-11-27, Work Mode and Retro of session 1402, the method command run as a scratch script with the same code: "True 709414 1000 800" — the PNG signature, 709 414 bytes under 1 000 000, 1000 pixels wide within 800 to 1200, 800 high

## History

- 2026-11-27 created · [[decision-case-1086]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L25
