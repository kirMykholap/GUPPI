---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: Whether VS Code draws the boxes of the map of the plan file as checkboxes at the exit of Plan Mode, and shows a box ticked once Work Mode ticks its task line in spec.md, as the person confirms
method: "by hand, after the exit of Plan Mode and the first tick of Work Mode in the VS Code extension of the next session whose plan file holds a ratified Case: the person's answer on the boxes of the map as VS Code showed the plan file at the exit and after that tick; the estimate line keeps the person's answer"
origin: raw/2026-11-27/1402/ledger.md#case-1085.4
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
The VS Code extension of Claude Code shows the plan file at `ExitPlanMode`, after the `Stop` hook of `rule-spec-write` wrote its map with boxes.
**＋** Then, in Work Mode of the same session, the agent ticks a task line of `raw/<date>/<hi HHMM>/spec.md`, and the person looks at the plan file in VS Code.

Then:
The boxes of the map stand drawn as checkboxes.
**＋** After the tick, the plan file in VS Code shows the box of that line ticked.
**＋** The person says that the boxes show the progress of the plan in the way they want.

## History

- 2026-11-27 created · [[decision-case-1085.4]]
