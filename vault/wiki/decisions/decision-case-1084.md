---
type: decision
case: "1084"
status: current
update: ["[[rule-work-mode]]", "[[estimate-work-mode-runs-the-style-check-before-a-stop]]"]
origin: raw/2026-11-27/1402/ledger.md#case-1084
sprint: plugin
created: 2026-11-27
tags: [session, workflow, harness, render]
---

## Problem

`/work` skipped the style check before a `stop:` task when it judged that the run was not needed, and the Estimate of that step failed.

## Recommend

- **How the skipped style check gets fixed**
  - Recommended: (a) say it plainly in the skill: before each `stop:` task, every time, also when an earlier run was clean and no file changed since then; the Estimate keeps its promise word for word and is read again at the next `/work`.
  - Answer: agreed, (a).

## History

- 2026-11-27 created · raw/2026-11-27/1402/ledger.md#case-1084
