---
type: decision
case: "1075"
status: current
create: ["[[estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close]]"]
update: ["[[entity-sprint-plugin]]"]
supersedes: ["[[decision-case-1021]]", "[[decision-case-1050]]"]
origin: raw/2026-11-26/2333/ledger.md#case-1075
sprint: plugin
created: 2026-11-26
tags: [sprint, workflow]
---

## Problem

The milestone The plugin still lists as open three items whose work is done, and one of its lines says that two pages stay unfinished, though both are built. Its two notes keep it open for good, both of its defers still stand, and it has no merge step before the close.

## Recommend

- **What the Case changes on the milestone The plugin**
  - Recommended: (a) the finished items move to Closed: the plugin that installs, the README and the setup leave the milestone for `## Closed`, the milestone keeps the close line, and both defers are retired.
  - Answer: agreed, (a).
- **A merge step before the close**
  - Recommended: (a) the merge line goes just before the close line, in the form that `/sprint-open` sets.
  - Answer: agreed, (a).
- **Where your wish for more in the README goes**
  - Recommended: (a) a note in the `## Backlog` of the sprint page.
  - Answer: agreed, after the main agent said that Case 1074 takes the wish up in this session and that the note then falls away; Case 1074 adds it to `README.md`, so no note is written.
- **When the sprint closes**
  - Recommended: (a) no set moment: the person takes up the close line in a session of its own when the sprint is done.
  - Answer: agreed, (a).

## History

- 2026-11-27 created · raw/2026-11-26/2333/ledger.md#case-1075
