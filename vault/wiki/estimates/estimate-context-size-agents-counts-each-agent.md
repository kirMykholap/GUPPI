---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: Whether guppi agents prints from a transcript one line for the main agent and one for each agent of the session, with its effort, model, calls, tokens, runs and seconds
method: uv run --project .guppi pytest .guppi/tests/test_agents.py
origin: raw/2026-11-04/0807/ledger.md#case-1029.3
sprint: plugin
created: 2026-11-04
tags: [hooks, harness, session]
---

## Criterion

When:
`uv run --project .guppi guppi agents <transcript>` of `.guppi/guppi/agents.py` runs on the path of a session transcript under `~/.claude/projects/`.

Then:
It prints one line for the main agent and one line for each file `subagents/agent-<id>.jsonl` in the folder named after the transcript.
**＋** The line of the main agent gives its calls, the sum of `call_size` over them, its tool calls, and the seconds from the first record of the transcript to the last.
**＋** The line of an agent gives its type and description from `agent-<id>.meta.json`, the `effort` that its Agent call passed or `-`, the model of its calls, its calls, the sum of `call_size`, the `call_size` of its last call, and its tool calls.
**＋** The line of an agent also gives its runs and seconds, from the `duration_ms` of each notification of a finished run, each notification counted once, or `-` where the transcript holds none.
**－** It writes no file.
**－** A transcript it cannot read gives one line on stderr and exit 1.
**－** An agent with no `.meta.json` prints as `unknown`.

## Result

2026-11-20, uv run --project .guppi pytest .guppi/tests/test_agents.py; 5 passed: one line for the main agent and one per agent with effort, model, calls, tokens, last, tools, runs and seconds, a message in several records one call, a repeated notice counted once, an agent with no meta file `unknown`, an unreadable transcript one stderr line and exit 1, no file written

## History

- 2026-11-20 created · [[decision-case-1029.3]]
- 2026-11-20 status: pending → passed · raw/2026-11-04/0807/ledger.md#L45
