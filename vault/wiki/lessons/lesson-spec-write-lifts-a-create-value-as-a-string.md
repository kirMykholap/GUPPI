---
type: lesson
kind: error
root_cause: put of .guppi/guppi/ratified.py parses a value as YAML only under set or when it starts with [ or {, so every other value of a create, a fenced block or a code span, reaches the Spec as a string, and case-schema.md gives no form for a boolean in a create
status: new
origin: raw/2026-10-31/0431/ledger.md#L50
sprint: plugin
created: 2026-10-31
tags: [harness, schema]
---

## Trigger

the case file of Case 956.1 wrote the core of a create as a fenced true, and the hook of rule-spec-write wrote it into spec.md and the plan file as core: 'true', a string that would have given the new Rule no core: true; /pre-spec printed no finding, and Case 965 in Work Mode set core by an update with set

## Root cause

put of .guppi/guppi/ratified.py parses a value as YAML only under set or when it starts with [ or {, so every other value of a create, a fenced block or a code span, reaches the Spec as a string, and case-schema.md gives no form for a boolean in a create

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#L50
