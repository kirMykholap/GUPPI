---
type: decision
case: "325.1"
status: archived
create: ["[[estimate-prespec-catches-an-unwrapped-render]]"]
update: ["[[rule-prespec]]"]
origin: raw/2026-09-22/1724/ledger.md#case-325.1
sprint: migration
created: 2026-09-22
tags: [harness, workflow, session]
---

## Context

`own_text` in `guppi/render.py` asks the same of each of the 32 pages with `enforcement: render`: its `## Render` opens with `<!-- slug -->` and closes with `<!-- /slug -->`. A parent `full` page carries one line per child — the opening marker — which `render_full` replaces with the child's text and its markers. Neither `pre-spec` nor `materialize`, `generate` or `lint` looks inside `sections.Render`: to a schema it is free prose. Case 317 wrote the child without markers and the parent with a pair; only `render` refused, at the end of the session, and it refused whole — `plan()` raises before the first write, so every governed file went stale at once. The other half of the same error is never caught: `render_full` sends an unmatched closing line to its `else` branch and copies it into the governed file.
`rule-prespec` stands `built` with six Estimates, one per finding; `rule-lint` stands `built` with the single `estimate-lint-catches` (`passed`, read 2026-09-22), whose Criterion enumerates the classes while the order lives in the docstring of `guppi/lint.py`; the body of `rule-lint` names no class. Case 324 signed the text of both damaged pages but set no guard.

## Problem

An error in the markers survives to the last step of the pipeline, and one kind of it is never caught at all. Two guards are needed in two places: one reads the plan before the Spec is approved, the other reads the pages on disk, by any route, a hand edit included.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-325.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
