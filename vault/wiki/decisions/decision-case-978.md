---
type: decision
case: "978"
status: current
create: ["[[estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link]]"]
update: ["[[lesson-ledger-reading-writes-a-bare-wikilink]]"]
origin: raw/2026-11-01/0141/ledger.md#case-978
sprint: plugin
created: 2026-11-01
tags: [sprint, harness, ledger, librarian]
---

## Problem

A bare `[[slug]]` in the `## Root cause` of `lesson-ledger-reading-writes-a-bare-wikilink` names no page, so `guppi check` reports a `ref` finding at each run, and the field `root_cause` holds the same bare form.

## Recommend

- **What the fix changes on the lesson page**
  - Recommended: (b) the section and the field alike, the bare `[[slug]]` put in a code span in both.
  - Answer: agreed, (b).
- **How the fix is checked**
  - Recommended: (a) a new one-time Estimate on `entity-sprint-plugin`, read by hand after the librarian's run.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/0141/ledger.md#case-978
