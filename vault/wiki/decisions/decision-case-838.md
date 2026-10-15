---
type: decision
case: "838"
status: current
defer: ["[[rule-lint]]"]
origin: raw/2026-10-15/1959/ledger.md#case-838
sprint: plugin
created: 2026-10-15
tags: [harness, workflow]
---

## Context

The person put off the items left open at the close of Plan Mode of session 1959. `guppi lint` reads the words "make with the targets …" of a `method` as the Makefile target `with` (`.guppi/guppi/lint.py`, the `MAKE_TARGET` match).

## Problem

No Case of this session fixes how `guppi lint` reads a make target in a `method`.

## Deferred

### [[rule-lint]]

guppi lint reads make with the targets in a method as the target with; put off at the close of Plan Mode of session 1959

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#case-838
