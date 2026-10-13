---
type: lesson
kind: error
root_cause: case-guppi recommended all three checks as required without reading what make lint prints at the Baseline of the session or rule-lint, which calls lint a signal and not a gate
status: archived
insight: "[[insight-case-build-recommends-without-reading-the-governing-rule]]"
origin: raw/2026-10-12/2349/ledger.md#L57
sprint: plugin
created: 2026-10-12
tags: [case-build, ci, github]
---

## Trigger

Case 787 made style, test and lint required checks on main; in Work Mode the first CI run showed lint red on the 8 lines of the Baseline, so no outside pull request could merge, and Case 794 had to replace 787.1

## Root cause

case-guppi recommended all three checks as required without reading what make lint prints at the Baseline of the session or rule-lint, which calls lint a signal and not a gate

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#L57
- 2026-10-13 updated: clustered under insight-case-build-recommends-without-reading-the-governing-rule (synthesis) · raw/2026-10-12/2349/ledger.md#L57
- 2026-10-13 archived · insight actioned
- 2026-10-13 archived · cleanup
