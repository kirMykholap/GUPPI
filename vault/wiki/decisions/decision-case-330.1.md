---
type: decision
case: "330.1"
status: current
update: ["[[estimate-lint-catches]]", "[[rule-lint]]", "[[estimate-plan-mode-names-its-estimates]]"]
origin: raw/2026-09-22/1724/ledger.md#case-330.1
sprint: migration
created: 2026-09-22
tags: [harness, workflow, session]
---

## Context

`is_reading` in lint is `"by hand" in method or "reading" in method`: two spellings of one thing, by substring. An agent writing a `create` guesses which word to put there, because neither the schema of an Estimate nor the rule page names the set of forms: the description of the field `method` in `rule-estimates-schema` says "the test command; or where and when it is read by hand; or, for Research, what is measured" — an example, not a list, and with no obligation in it. The field is marked `optional`, and not by accident: the pages before case 193 carry none. Of the 75 live Estimates with a `method`, the word `reading` stands in 51 but carries the classification in exactly one — `estimate-plan-mode-names-its-estimates`; in the others `pytest` stands beside it and the classification goes by that.
`rule-lint` stands `built`, its single Estimate `estimate-lint-catches` enumerates the classes in its Criterion and is already changed in this session by case 325.2 — in another place, the anchors do not overlap. `rule-estimates-schema` renders `vault/wiki/estimates/schema.yaml`, the file the agent reads before a `create`.

## Problem

Two spellings of one notion force a guess, and the guess is needed because the set of forms is nowhere written as a set. The guard meanwhile stands at the end of the pipeline: lint speaks of an unhappy `method` in the librarian's run, a session later.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-330.1
