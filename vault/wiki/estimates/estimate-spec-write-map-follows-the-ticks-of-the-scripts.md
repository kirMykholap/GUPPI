---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether each script of the librarian's run that ticks a line of a spec.md rebuilds the map of each approved document there that holds one, the ticked line included, and adds no map to a document without one
method: uv run --project .guppi pytest .guppi/tests/test_generate.py .guppi/tests/test_render.py .guppi/tests/test_sprint_close.py -k spec_map
origin: raw/2026-11-27/1402/ledger.md#case-1085.3
sprint: plugin
created: 2026-11-27
tags: [harness, workflow]
---

## Criterion

When:
`tick_read` or `tick_spec` of `.guppi/guppi/generate.py`, `tick_command_lines` of `.guppi/guppi/render.py` or `tick` of `.guppi/guppi/sprint_close.py` ticks a line of a `spec.md`.

Then:
Before the script ends, the box of the line it ticked stands ticked in the map at the head of its document too, where that document holds a map.
**＋** The script writes no map where the document had none.
**－** The script leaves every plan file as it stands.

## Result

2026-11-27, uv run --project .guppi pytest .guppi/tests/test_generate.py .guppi/tests/test_render.py .guppi/tests/test_sprint_close.py -k spec_map, Retro of session 1402: 5 passed; tick_spec, tick_read, tick_command_lines and tick each leave the box of the ticked line ticked in the map of its document, and a spec.md with no map gets none

## History

- 2026-11-27 created · [[decision-case-1085.3]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/1402/ledger.md#L22
