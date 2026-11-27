---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the plan view of the VS Code extension of Claude Code shows the map at the head of the plan file with its table drawn as a table, its Mermaid diagram drawn as a picture and its signs before the lines they mark, as the person confirms
method: "by hand, after the exit of Plan Mode in the VS Code extension of the next session whose plan file holds a ratified Case: the person's answer on the map as the plan view of the VS Code extension showed it; the estimate line keeps the person's answer"
checked: 2026-11-27
origin: raw/2026-11-27/0947/ledger.md#case-1078.2
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow]
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

2026-11-27, at the /hi of session 2214, the person's answer: at the exit of Plan Mode of session 1402 the plan view in VS Code showed the table, the Mermaid diagram and the signs of the map of the Cases as wanted ("выглядело нормально"); the text judged: the plan file C:\Users\kir\.claude\plans\generic-swimming-parnas-of-ee662ed3-a713-4708-a454-42866d7e862b.md, its copy vault/raw/2026-11-27/1402/spec.md at commit 34ba4b8d, section Map of the Cases

## History

- 2026-11-27 created · [[decision-case-1078.2]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L5
