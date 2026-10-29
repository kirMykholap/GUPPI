---
type: decision
case: "912"
status: current
children: ["[[decision-case-912.1]]", "[[decision-case-912.2]]"]
origin: raw/2026-10-29/1930/ledger.md#case-912
sprint: plugin
created: 2026-10-29
tags: [plugin, hooks, harness, render]
---

## Problem

The hooks of the copied settings run inside the install session itself: they build `.guppi/.venv/` before `uv sync`, and they fail at each command after a rollback.

## Recommend

- **How the install keeps the copied hooks from running**
  - Recommended: (a) copy `.claude/settings.json` last, after `uv sync` passes.
  - Answer: agreed, (a).
- **Which Estimate checks the fix**
  - Recommended: (a) a new Estimate `estimate-plugin-install-runs-no-hook-before-uv-sync` on `rule-plugin-install`.
  - Answer: agreed, (a).
- **When the new check is read**
  - Recommended: (a) by hand, after the librarian's run, like the other install Estimates: one install where `uv sync` passes and one offline.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, a pair on step 5 of the Render, so that it checks only the files that step 4 copied.
  - Taken: Case 912.1 gains that pair.
- **Change**
  - Asked: at `/pre-spec`, the Case also replaces the Criterion of `estimate-guppi-package-is-ready-after-the-install`, so that it says the install copies every file but `.claude/settings.json` before `uv sync`; the Estimate goes `pending` and is read in the same installs by hand as the new Estimate.
  - Taken: Case 912.2, under the new number 912 with sub-cases, which retires Case 905.

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-912
