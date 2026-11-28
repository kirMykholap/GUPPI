---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether each script of the librarian's run that ticks a line of a spec.md rebuilds the map of each approved document there that holds one, the ticked line included, and adds no map to a document without one
method: uv run --project .guppi pytest .guppi/tests/test_generate.py .guppi/tests/test_render.py .guppi/tests/test_sprint_close.py -k spec_map
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [harness, workflow]
core: true
---

## Criterion

When:
`tick_read` or `tick_spec` of `.guppi/guppi/generate.py`, `tick_command_lines` of `.guppi/guppi/render.py` or `tick` of `.guppi/guppi/sprint_close.py` ticks a line of a `spec.md`.

Then:
Before the script ends, the box of the line it ticked stands ticked in the map at the head of its document too, where that document holds a map.
**＋** The script writes no map where the document had none.
**－** The script leaves every plan file as it stands.

## Result

2026-11-27, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
