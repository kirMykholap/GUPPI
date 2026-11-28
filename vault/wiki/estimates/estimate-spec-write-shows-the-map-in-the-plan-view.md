---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the plan view of the VS Code extension of Claude Code shows the map at the head of the plan file with its table drawn as a table, its Mermaid diagram drawn as a picture and its signs before the lines they mark, as the person confirms
method: "by hand, after the exit of Plan Mode in the VS Code extension of the next session whose plan file holds a ratified Case: the person's answer on the map as the plan view of the VS Code extension showed it; the estimate line keeps the person's answer"
checked: 2026-11-27
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The VS Code extension of Claude Code shows at `ExitPlanMode` the plan file of a session whose plan holds a ratified Case, after the `Stop` hook of `rule-spec-write` wrote the map.

Then:
The table of the map stands above the Cases, drawn as a table.
**＋** The Mermaid diagram stands drawn as a picture.
**＋** The signs stand before the lines they mark.
**＋** The person says that the map shows the plan in a way that is easy to read.

## Result

2026-11-27, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
