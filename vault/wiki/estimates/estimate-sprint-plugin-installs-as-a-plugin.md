---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether the clean version, written into a local folder by guppi ship --allow-draft, installs as a Claude Code plugin into an empty project, /guppi:install copies GUPPI there, and /hi runs there
method: "by hand, in a session of the sprint plugin before its close: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue in an empty project by /plugin marketplace add, guppi installed from it by /plugin install guppi@guppi-marketplace, /guppi:install typed, Claude Code reopened there and /hi typed, read against the Criterion"
origin: raw/2026-10-10/1713/ledger.md#case-756.6
sprint: plugin
created: 2026-10-10
tags: [sprint, plugin]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, someone writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it.
**＋** In an empty project, that person adds the folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install`, as `rule-plugin-install` sets it.
**＋** That person then reopens Claude Code in the project and types `/hi`.

Then:
The catalogue adds with no error.
**＋** The plugin installs with no error.
**＋** `/guppi:install` copies GUPPI into the project with no error.
**＋** `/hi` opens a working session in that project.

## History

- 2026-10-10 created · [[decision-case-756.6]]
- 2026-10-10 updated: the reading waits for the milestone The plugin of entity-sprint-plugin; no clean branch exists to install before it · [[decision-case-768]]
- 2026-10-15 updated: the Criterion replaced whole — the install is read from a local copy that guppi ship --allow-draft writes, and /guppi:install copies GUPPI into the empty project before /hi runs there · [[decision-case-818.2]]
