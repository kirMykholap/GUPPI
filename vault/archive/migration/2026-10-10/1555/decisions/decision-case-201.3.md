---
type: decision
case: "201.3"
status: archived
create: ["[[estimate-generate-fails-alone]]"]
origin: raw/2026-09-16/1955/ledger.md#case-201.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
---

## Context

`rule-page-generation` is a Leaf, `enforcement: check`, its code `guppi/generate.py`, its tests `tests/test_generate.py`. The page carries `## Purpose` and a long `## How it works`; two Estimates: `estimate-generate-writes` — a head plus ten `### case N` blocks (101.1, 104.1–104.3, 105.3, 142.2, 151, 166.2, 166.3, 172) — and `estimate-generate-walks-dates` — a head plus block 103.3; both `passed`. The replacement of a Criterion whole already works through `sections` (194.1), but the code still applies `criterion_block` and `remove_criterion`, writes no `checked`, and the key order of an Estimate does not know `purpose`, `method`, `checked`; the Decision page still gets `## Given` and a `## Criterion` list of `[[estimate-x]] § case N`, which died with the blocks (point 10 of the model of 182, deferred here by 193). Decision 191 deferred the page with the text: generate without blocks and `remove_criterion`, the Criterion whole, the fields `purpose`, `method`, `checked`, the recut of both Estimates; the change of 186.1 (`## Deferred`) stands ratified. The vault was asked for the slugs: `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone`, `estimate-generate-cascades` are free in the vault and in the archive (the archive holds seven other `estimate-generate-*`, among them `-rejects-shape-alone` and `-logs-per-entry`, folded into `-writes` by 53.2). The Case touches both Estimate pages and creates three.

## Problem

`estimate-generate-writes` is ten deltas without a whole: what generate promises now is written nowhere, and lint finds a `[[slug]]` in its body that no page carries. The code keeps two paths of the old model that materialize no longer produces, and writes no `checked`, although the schema (193) and the reading line (199) already carry the date. The Decision page writes a Criterion list that points at nothing after a recut. The question: how to recut the two Estimates into promises that read whole, and take the old model out of the code without losing one signed line.

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-201.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
