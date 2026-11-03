---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook writes a decision line while no sprint is open where guppi.toml holds setup_done = false, refuses it as before otherwise, and still refuses a taken sprint id
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k setup
origin: raw/2026-11-03/0316/ledger.md#case-1017.2
sprint: plugin
created: 2026-11-03
tags: [ledger, plugin]
---

## Criterion

When:
The `Stop` hook of `rule-ledger-write`, `.guppi/guppi/ledger.py`, reads a fresh decision line other than a `defer` while no sprint page is live and no `create` of a sprint page stands in the session's ledger or in the same `Stop`, or `.guppi/tests/test_ledger.py` runs it over a made-up project.

Then:
Where `guppi.toml` holds `setup_done = false`, by `setup_pending` of `.guppi/guppi/config.py`, the hook writes the line.
**＋** Where `guppi.toml` holds anything else or is missing, the hook refuses the line as before, with its stderr line that names the opening of the next sprint.
**－** A `create` of a sprint page whose id a live or archived page holds is refused as before, whatever `guppi.toml` holds.

## Result

2026-11-03, uv run --project .guppi pytest .guppi/tests/test_ledger.py -k setup at Retro of session 0316; 4 passed: with no live sprint page a decision line is written on setup_done = false, refused on setup_done = true or no key, and a taken sprint id is refused on setup_done = false; the run -k sprint collects none of them

## History

- 2026-11-03 created · [[decision-case-1017.2]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/0316/ledger.md#L29
