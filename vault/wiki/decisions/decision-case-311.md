---
type: decision
case: "311"
status: current
update: ["[[estimate-harness-pipeline]]"]
origin: raw/2026-09-22/1121/ledger.md#case-311
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Context

The Criterion of `estimate-harness-pipeline` describes `make lint` as four steps — `render --check`, `sprint --check`, `glossary --check`, `guppi lint` (306.5 added the third) — but its `then` line still says "exits 0 … by its first two steps": the promise counts the steps by the shape before 306. The sense of the line: the file checks pass clean, and `guppi lint` with its findings is read by its own Estimates. The page is `pending`; the Purpose of `rule-harness` names the four steps in order; W5 reads the Estimate by hand after the librarian's run.

## Problem

One line of the Criterion counts the wrong number of steps; a reading by it either fails by the letter or passes against it.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-311
