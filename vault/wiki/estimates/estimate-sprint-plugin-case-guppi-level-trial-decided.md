---
type: estimate
kind: Research
status: pending
target: "[[entity-sprint-plugin]]"
purpose: What the levels of the dispatch of case-guppi saved in time and tokens per Case, whether the builds got worse, and whether the person keeps them
method: "by hand, in the session that closes the sprint plugin: the output of guppi agents over the transcripts of the Criterion and the findings of ask-guppi in those transcripts read against the Criterion, the numbers and the person's answer in the estimate line"
origin: raw/2026-11-04/0807/ledger.md#case-1029.4
sprint: plugin
created: 2026-11-04
tags: [sprint, workflow]
once: true
---

## Criterion

When:
The session that closes the sprint `plugin` runs `uv run --project .guppi guppi agents <transcript>` of `.guppi/guppi/agents.py` over `~/.claude/projects/c--PROJECTS-GUPPI/f7321efe-eca6-49ea-9ba1-c44aec197fd9.jsonl`, over the main transcripts under `~/.claude/projects/C--PROJECTS-guppi-trial-0358-*/`, and over the transcript of each session of the sprint after it.

Then:
Determine how much time and how many tokens per Case the levels of `rule-orchestration` saved against those transcripts.
**＋** Determine whether the findings of `.claude/agents/ask-guppi.md` and the changes the person asked per Case grew.
**＋** The person answers whether the levels stay, go, or stay on trial, and whether the setup Case and the opening Case need the full build and the audit.
**－** The session that closes the sprint carries out no such answer: a Case of a later session does.

## History

- 2026-11-20 created · [[decision-case-1029.4]]
