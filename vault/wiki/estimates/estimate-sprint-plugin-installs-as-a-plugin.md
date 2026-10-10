---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether the clean branch installs as a Claude Code plugin into an empty project and /hi runs there
method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close
origin: raw/2026-10-10/1713/ledger.md#case-756.6
sprint: plugin
created: 2026-10-10
tags: [sprint, plugin]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, someone installs the clean branch as a Claude Code plugin into an empty project, opens Claude Code there and types `/hi`.

Then:
The plugin installs with no error.
**＋** `/hi` opens a working session in that project.

## History

- 2026-10-10 created · [[decision-case-756.6]]
