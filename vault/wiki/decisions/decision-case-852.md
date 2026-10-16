---
type: decision
case: "852"
status: current
children: ["[[decision-case-852.1]]", "[[decision-case-852.2]]"]
origin: raw/2026-10-16/0342/ledger.md#case-852
sprint: plugin
created: 2026-10-16
tags: [plugin, harness, render]
---

## Problem

When `uv` is missing, `/guppi:install` only says so and stops. The person must find out how to install `uv` alone, though the agent could offer to install it.

## Recommend

- **What should `/guppi:install` do when `uv` is missing?**
  - Recommended: (a) offer to install it: ask, run the install command on a yes, and on a no show the command, say to type `/guppi:install` again after installing `uv`, and stop with nothing written.
  - Answer: agreed, (a).
- **Which command should install `uv`?**
  - Recommended: (a) the official standalone installer for the system, a PowerShell command on Windows and a shell command on macOS and Linux; Work Mode reads the installation page of `uv` and checks the exact commands.
  - Answer: agreed, (a).
- **What should happen right after `uv` is installed?**
  - Recommended: (a) run `uv --version` again; when it passes, go on with the install in the same session, its last message saying to start Claude Code from a new terminal; when it fails, say to open a new terminal, start Claude Code there and type `/guppi:install` again, and stop with nothing written.
  - Answer: agreed, (a).
- **How should we check that this works?**
  - Recommended: (a) a new Estimate on `rule-plugin-install`, read by hand in an empty project with Claude Code started from a terminal that does not find `uv`, once answering no and once yes; and the Criterion of `estimate-guppi-package-is-ready-after-the-install` replaced without the missing-`uv` line.
  - Answer: agreed, (a).
- **Change**
  - Asked: through Case 853, drop from the new Criterion of `estimate-guppi-package-is-ready-after-the-install` the line on a failed `uv sync` and the offline project, since Case 853 checks that failure with its own Estimate.
  - Taken: Case 852.2 drops that line, and its `purpose` and `method` drop the failure and the offline project.

## History

- 2026-10-16 created · raw/2026-10-16/0342/ledger.md#case-852
