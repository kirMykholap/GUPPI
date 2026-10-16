---
type: decision
case: "853"
status: current
create: ["[[estimate-plugin-install-undoes-the-copy-when-uv-sync-fails]]"]
update: ["[[rule-plugin-install]]"]
origin: raw/2026-10-16/0342/ledger.md#case-853
sprint: plugin
created: 2026-10-16
tags: [plugin, harness, render]
---

## Problem

When `uv sync` fails, `/guppi:install` leaves a half-installed project that a second `/guppi:install` refuses, and the agent still sends the person on to `/hi`.

## Recommend

- **What should `/guppi:install` do when `uv sync` fails?**
  - Recommended: (a) undo the copy: show the output of `uv sync`, delete every file it copied and every folder it made, `.guppi/` with its `.venv/` included, say that the install did not finish, tell the person to type `/guppi:install` again, and never mention `/hi`.
  - Answer: agreed, (a).
- **Should the install's `uv sync` also install `pytest` and `ruff`?**
  - Recommended: (a) keep the `dev` group in the install; leaving it out only moves the download to the first hook.
  - Answer: agreed, (a).
- **How should we check that a failed `uv sync` undoes the install?**
  - Recommended: (a) a new Estimate on `rule-plugin-install` for the failure path, read by hand in an empty project offline with an empty cache of `uv`; Case 852 is built again so that the check of the Python environment drops its line on a failed `uv sync` and its offline project.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/0342/ledger.md#case-853
