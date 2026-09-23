---
type: lesson
kind: knowledge
root_cause: generate applies a replace pair to the text of one section at a time, the section's heading outside it, so an anchor that crosses a section heading never matches; the Case schema does not say so
status: clustered
source: guppi/generate.py replace_once
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-09-23/1355/ledger.md#L36
sprint: migration
created: 2026-09-23
tags: [harness, workflow]
---

## Trigger

the first pair of Case 381 opened its old with the heading ## Milestones and ended inside the section; guppi prespec --check reported the anchor not in the page

## Root cause

generate applies a replace pair to the text of one section at a time, the section's heading outside it, so an anchor that crosses a section heading never matches; the Case schema does not say so

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#L36
- 2026-09-23 updated: clustered into insight-workflow-case-schema-silent-on-what-the-scripts-accept by the librarian's synthesis · raw/2026-09-23/1355/ledger.md#L36
