---
type: lesson
kind: error
root_cause: case-guppi wrote what a step does and changed one step of a Render from the step it was looking at, without reading the other skill that does the same step or the next step of the Render that reads the list the change alters
status: archived
insight: "[[insight-case-build-changes-a-step-without-reading-its-readers]]"
origin: raw/2026-10-29/1930/ledger.md#L26
sprint: plugin
created: 2026-10-29
tags: [case-build, prespec]
---

## Trigger

/pre-spec of session 1930 found that Case 903.2 named only /box as the step that shows the librarian's report, though /handoff shows it in every session that /box does not run, and that Case 905 left step 5 of the Render of rule-plugin-install checking .claude/settings.json, which its own new step 4 no longer copies; the person had ratified both before the findings

## Root cause

case-guppi wrote what a step does and changed one step of a Render from the step it was looking at, without reading the other skill that does the same step or the next step of the Render that reads the list the change alters

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#L26
- 2026-10-29 updated: clustered under insight-case-build-changes-a-step-without-reading-its-readers (synthesis) · raw/2026-10-29/1930/ledger.md#L26
- 2026-10-30 archived · insight actioned
- 2026-10-30 archived · cleanup
