---
type: lesson
kind: knowledge
root_cause: the suite and the formatter read the whole tree, so an agent's half-written edit is a failure in every other agent's run; a measurement taken while another agent is writing measures the other agent; the suite is run once, by the main agent, after every subagent has returned, and a subagent's mid-flight red is not a finding
status: new
origin: raw/2026-09-12/ledger.md#L105
sprint: migration
created: 2026-09-12
tags: [harness, tests, workflow]
---

## Trigger

four subagents worked the same working tree at once, each on its own files; each reported make test and make style red in the middle of its run on files it had not touched, and green once every agent had returned; the final suite was 211 green

## Root cause

the suite and the formatter read the whole tree, so an agent's half-written edit is a failure in every other agent's run; a measurement taken while another agent is writing measures the other agent; the suite is run once, by the main agent, after every subagent has returned, and a subagent's mid-flight red is not a finding

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L105
