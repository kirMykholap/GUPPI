---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether the hook on /hi tells the agent to start /sprint-open when sprint.md marks the last sprint closed, and prints nothing otherwise
method: uv run pytest tests/test_sprint.py -k hi
origin: raw/2026-10-08/2352/ledger.md#case-743.7
sprint: migration
created: 2026-10-08
tags: [sprint, hooks, harness]
---

## Criterion

When:
The person types a prompt, and the `UserPromptSubmit` hook `uv run guppi sprint --hi` of `guppi/sprint.py` reads its payload and `vault/wiki/sprint.md`, or `tests/test_sprint.py` runs it over a made-up vault.

Then:
When the prompt is `/hi`, by `is_hi_prompt` of `guppi/event.py`, and the first `## ` heading of `vault/wiki/sprint.md` carries the closed mark, the hook prints into the agent's context one line that names the closed sprint and tells the agent to start the skill of `rule-skill-sprint-open` before the Frontier.
**＋** The hook judges the mark by the function of `guppi/sprint.py` that writes it.
**＋** The hook exits 0 in every case, and an error of its own is one line on stderr.
**－** Any other prompt, and a `/hi` while the heading carries no mark, print nothing.
**－** The hook writes no file.

## Result

2026-10-09, uv run pytest tests/test_sprint.py -k hi; 7 passed: /hi with a closed heading prints the line, an open heading, another prompt and no file print nothing, each exit 0

## History

- 2026-10-09 created · [[decision-case-743.7]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L35
