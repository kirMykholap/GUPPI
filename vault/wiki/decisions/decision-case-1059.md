---
type: decision
case: "1059"
status: current
create: ["[[estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine]]"]
origin: raw/2026-11-25/2003/ledger.md#case-1059
sprint: plugin
created: 2026-11-25
tags: [sprint, plugin]
---

## Problem

The build line of `.guppi/pyproject.toml` allows only the 0.11 build tool of uv, so every uv from 0.12 on warns at `uv sync` and builds with a downloaded 0.11 build tool instead of its own.

## Recommend

- **Which bound `.guppi/pyproject.toml` sets for `uv_build`**
  - Recommended: (a) widen the range to 0.11 up to, but not including, 0.14.
  - Answer: agreed, (a).
- **How the widened range is checked**
  - Recommended: (b) a one-time reading on the sprint page, `once: true`, of the output of `uv sync` in Work Mode.
  - Answer: agreed, (b).

## History

- 2026-11-26 created · raw/2026-11-25/2003/ledger.md#case-1059
