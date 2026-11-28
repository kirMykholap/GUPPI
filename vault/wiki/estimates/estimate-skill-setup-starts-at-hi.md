---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-setup]]"
purpose: Whether the hook on /hi tells the agent to start /setup before /sprint-open when sprint.md marks the last sprint closed and guppi.toml holds setup_done = false, and prints no setup line otherwise
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k setup
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [hooks, harness, plugin]
core: true
---

## Criterion

When:
The person types a prompt, and the `UserPromptSubmit` hook `uv run --project .guppi guppi sprint --hi` of `.guppi/guppi/sprint.py` reads its payload, `vault/wiki/sprint.md` and `guppi.toml`, or `.guppi/tests/test_sprint.py` runs it over a made-up project.

Then:
When the prompt is `/hi`, the first `## ` heading of `vault/wiki/sprint.md` carries the closed mark and `guppi.toml` holds `setup_done = false`, by `setup_pending` of `.guppi/guppi/config.py`, the hook prints, before its line on the closed sprint, one line that tells the agent to start the skill `/setup` of `rule-skill-setup` before `/sprint-open` and before the Frontier.
**－** An open heading, a `guppi.toml` that does not hold `setup_done = false`, a missing file and any other prompt print no setup line.
**－** The hook exits 0 in every case and writes no file.

## Result

2026-11-03, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
