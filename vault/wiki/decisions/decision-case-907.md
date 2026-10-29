---
type: decision
case: "907"
status: current
defer: ["[[rule-ratification]]"]
origin: raw/2026-10-29/1930/ledger.md#case-907
sprint: plugin
created: 2026-10-29
tags: [session, workflow, ledger, harness]
---

## Context

The person put off the removal of `PLAIN_SPRINTS = ("migration", "plugin")` from `.guppi/guppi/caseid.py` until after the close of sprint `plugin`, with the round of Case 906, which was dropped for this defer. The clean version ships the list with the names of the sprints of GUPPI. Once `plugin` closes, no sprint needs plain ids.

## Problem

No Case of this session removes the fixed list of sprints that keep plain Case ids from the code that the clean version ships.

## Deferred

### [[rule-ratification]]

Remove PLAIN_SPRINTS from .guppi/guppi/caseid.py after sprint plugin closes, so that only an id that already has no sprint part stays plain and the clean version holds no name of a sprint of GUPPI; with it, replace the Criterion sentence of estimate-ratification-case-id-carries-the-sprint that names the list, the test in .guppi/tests/test_caseid.py that expects plugin to get plain ids, and the sentence of the Render of rule-ratification that names the list

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-907
