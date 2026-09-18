---
type: decision
case: "235"
status: current
update: ["[[rule-render-harness]]", "[[estimate-render-harness-ticks-the-spec]]"]
origin: raw/2026-09-18/1252/ledger.md#case-235
sprint: migration
created: 2026-09-18
tags: [harness, render]
---

## Context

`rule-render-harness` (`draft`) governs `guppi/render.py`: the plain `guppi render` writes the governed files and, on exit 0, ticks the render lines in the `spec.md` of every unit under `raw/` whose yaml is applied whole (case 226.2). A render line of the Spec has the form `- [ ] `uv run guppi render`: `<file>`` — the command in the first code span. Today `RENDER_LINE` matches any unticked line that holds `guppi render` in a code span anywhere. The reading line `- [ ] read `estimate-render-harness-ticks-the-spec`: pytest, plus the `guppi render` lines …` of the 1119 Spec matched it and stands `[x]` without a reading taken; the brief named it in Flags. The Case touches one Estimate, `estimate-render-harness-ticks-the-spec` (`pending`); it does not touch `estimate-render-harness-reproduces` or `estimate-render-sync-reports`.

## Problem

The Criterion of 226.2 says "a line holding `guppi render` in a code span" and the code does exactly that, so a reading line that names the command is ticked as a render done. The tick is false: the reading is not taken, and Retro does not count it.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-235
