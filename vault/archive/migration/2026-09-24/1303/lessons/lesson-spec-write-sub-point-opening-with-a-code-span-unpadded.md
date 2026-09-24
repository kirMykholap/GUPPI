---
type: lesson
kind: error
root_cause: the value opened with a code span of its own, and the agent wrapped it in two backticks with no space, so the parser read three opening backticks against two closing; a value that opens or closes with a backtick needs its outer span padded by one space on each side
status: archived
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-09-24/1303/ledger.md#L15
sprint: migration
created: 2026-09-24
tags: [hooks, workflow]
---

## Trigger

the Stop hook of rule-spec-write refused Case 392.1 after its ratification in session 1303 — `sections.How it works`: the value is not one code span; 392.2 and the parent were written, 392.1 was not

## Root cause

the value opened with a code span of its own, and the agent wrapped it in two backticks with no space, so the parser read three opening backticks against two closing; a value that opens or closes with a backtick needs its outer span padded by one space on each side

## History

- 2026-09-24 created · raw/2026-09-24/1303/ledger.md#L15
- 2026-09-24 updated: clustered into insight-workflow-case-schema-silent-on-what-the-scripts-accept by the librarian's synthesis · raw/2026-09-24/1303/ledger.md#L15
- 2026-09-24 archived · insight actioned
- 2026-09-24 archived · cleanup
