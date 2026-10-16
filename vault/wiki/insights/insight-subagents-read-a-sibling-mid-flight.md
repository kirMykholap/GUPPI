---
type: insight
pattern: agents that work at once read files that another agent of the same run is still writing, so what one agent reads or measures is the other agent's half-done state, not its result
status: open
children: ["[[lesson-subagents-parallel-on-one-tree-red-mid-flight]]", "[[lesson-case-build-reads-a-sibling-case-file-mid-rebuild]]"]
severity: 2
origin: raw/2026-10-16/0104/ledger.md#L21
sprint: plugin
created: 2026-10-16
tags: [harness, tests, workflow, case-build, prespec]
---

## Pattern

Two lessons, one cause. In session I of 2026-09-12 four subagents worked one tree at once, and each saw make test and make style red mid-run on files it had not touched, green once every agent had returned. In session 0104 Cases sent back in one message were built again in parallel, and the case-guppi of Case 843 read case-846.md before the rebuild of Case 846 ended, so Case 843 kept an Other Case line that the finished case-846.md already answered. In both, an agent read what a sibling agent was still writing and took it for the sibling's result.

## Proposal

One sentence in rule-case-build that Cases sent back in one message are built again with no read of a sibling's case file, and that the main agent checks the cross-references between the rebuilt Cases once every case-guppi has answered, as the suite is run once after every subagent has returned. A suggestion, not a decision.

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#L21
