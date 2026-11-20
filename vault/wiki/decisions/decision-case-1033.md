---
type: decision
case: "1033"
status: current
create: ["[[estimate-guppi-package-keeps-python-caches-out-of-git]]"]
update: ["[[rule-guppi-package]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1033
sprint: plugin
created: 2026-11-04
tags: [git, plugin, harness]
---

## Problem

A project that installs GUPPI gets no ignore line for the Python caches under `.guppi/`, so after the first run of the tests git lists them as untracked, and the gate refuses `/handoff` until someone ignores them by hand.

## Recommend

- Recommended: add `__pycache__/` to `.guppi/.gitignore`, which the clean version and the install copy as it stands, describe it in `rule-guppi-package` and check it with a new Estimate on that page.
- Answer: ratified as built

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1033
