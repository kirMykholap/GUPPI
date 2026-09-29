---
type: lesson
kind: error
root_cause: the frame of case-guppi does not say that a Case shown again after its ratification keeps the ids of the ledger lines it already wrote.
status: clustered
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-09-29/1432/ledger.md#L35
sprint: migration
created: 2026-09-29
tags: [harness, workflow]
---

## Trigger

rebuilt after /pre-spec, Case 510 came back as sub-cases 510.1 and 510.2, though its first ratification had written decision[case 510] into the ledger; that line would have had no item under its own Case, and the main agent asked for one Case with two items.

## Root cause

the frame of case-guppi does not say that a Case shown again after its ratification keeps the ids of the ledger lines it already wrote.

## History

- 2026-09-29 created · raw/2026-09-29/1432/ledger.md#L35
- 2026-09-29 updated: clustered under insight-workflow-case-schema-silent-on-what-the-scripts-accept (synthesis) · raw/2026-09-29/1432/ledger.md#L35
