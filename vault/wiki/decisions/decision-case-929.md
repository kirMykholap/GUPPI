---
type: decision
case: "929"
status: current
update: ["[[rule-guppi-config]]", "[[rule-guppi-package]]", "[[estimate-guppi-config-runs-the-test-and-style-commands]]"]
supersedes: ["[[decision-case-834]]", "[[decision-case-848]]"]
origin: raw/2026-10-30/1713/ledger.md#case-929
sprint: plugin
created: 2026-10-30
tags: [harness, render, plugin, tests]
---

## Problem

In a project that installs GUPPI, `guppi test` runs pytest from the root of the project with no folder, so pytest never reads `.guppi/pyproject.toml` and never collects `.guppi/tests/`; two defers of `rule-guppi-package` still wait on this.

## Recommend

- **What this Case changes**
  - Recommended: (a) the key `test` of `guppi.toml` becomes `uv run --project .guppi pytest -q .guppi/tests`; the root `pyproject.toml` and `uv.lock` of the repository of GUPPI stay for a later Case; both defers close, the second with the answer that the root file keeps its pytest settings until then.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-30/1713/ledger.md#case-929
