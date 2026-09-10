---
type: insight
pattern: The moment Claude Code reads an agent definition is not established; two sessions rendered an agent and got opposite results, and no measurement separates them.
status: open
children: [lesson-agents-loaded-at-session-start, lesson-agents-visible-in-session]
severity: 2
origin: raw/2026-09-10/ledger.md#L80
sprint: migration
created: 2026-09-10
tags: [harness, hooks]
---

## Pattern

Two lessons make opposite claims about the same mechanism.

Session D (`lesson-agents-loaded-at-session-start`) rendered `.claude/agents/ask-guppi.md` and dispatched it three times in the same session; every call failed with "Agent type not found".

Session E (`lesson-agents-visible-in-session`) rendered `.claude/agents/librarian-guppi.md` at about 10:40 and the Agent tool listed it at 10:52, in the same session, without a restart.

The difference between the two sessions was not measured. Until it is, the rule "an agent is usable only from the next session" rests on one reading and its counter-example rests on one reading.

## Proposal

A suggestion, not a decision. Take one reading that separates the two: render a throwaway agent mid-session, dispatch it at once, record the result and the session state (whether the file is new or replaced, whether a compaction happened, the client version). Write it as an Estimate on the Rule that renders agents. Until that reading exists, plan as if a rendered agent were unusable in the session that creates it, and treat a successful same-session dispatch as a bonus, not as a guarantee.

## Children

- [[lesson-agents-loaded-at-session-start]]
- [[lesson-agents-visible-in-session]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L80
