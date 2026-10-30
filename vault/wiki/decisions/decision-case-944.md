---
type: decision
case: "944"
status: current
update: ["[[rule-close]]", "[[estimate-close-reports-the-run]]", "[[rule-documentation]]"]
origin: raw/2026-10-30/2345/ledger.md#case-944
sprint: plugin
created: 2026-10-30
tags: [harness, workflow, git, librarian, session, render]
---

## Problem

The Estimate of the librarian's report can be read only by the person, from a text shown once in the chat of an earlier session, so the agent cannot check it by itself.

## Recommend

- **How the agent reads the report**
  - Recommended: (a) the librarian writes the report into `report.md` in the session folder before its commit and returns the same text.
  - Answer: agreed, (a).
- **What happens to the promise and to today's passed reading**
  - Recommended: (a) one Estimate: its Criterion replaced whole with the file, its `purpose` and `method` set anew, its status `pending`.
  - Answer: agreed, (a).
- **What the Estimate promises about the text the librarian sends back**
  - Recommended: (a) the Estimate promises the file and its content only; the frame still tells the librarian to return the text of the file unchanged.
  - Answer: agreed, (a).
- **Change**
  - Asked: after a finding of `/pre-spec`, the person chose that a run that stops at step 1 of the frame, when `guppi materialize` exits 1, writes no `report.md` and returns its report as text, as today; the Criterion does not change.
  - Taken: an `update` of `rule-documentation` rewrites step 1 of its Render so; `context` says why the line on the scripts as the only way to write stands.

## History

- 2026-10-31 created · raw/2026-10-30/2345/ledger.md#case-944
