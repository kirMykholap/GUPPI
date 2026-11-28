---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook writes a decision line while no sprint is open where guppi.toml holds setup_done = false, refuses it as before otherwise, and still refuses a taken sprint id
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k setup
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [ledger, plugin]
core: true
---

## Criterion

When:
The `Stop` hook of `rule-ledger-write`, `.guppi/guppi/ledger.py`, reads a fresh decision line other than a `defer` while no sprint page is live and no `create` of a sprint page stands in the session's ledger or in the same `Stop`, or `.guppi/tests/test_ledger.py` runs it over a made-up project.

Then:
Where `guppi.toml` holds `setup_done = false`, by `setup_pending` of `.guppi/guppi/config.py`, the hook writes the line.
**＋** Where `guppi.toml` holds anything else or is missing, the hook refuses the line as before, with its stderr line that names the opening of the next sprint.
**－** A `create` of a sprint page whose id a live or archived page holds is refused as before, whatever `guppi.toml` holds.

## Result

2026-11-03, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
