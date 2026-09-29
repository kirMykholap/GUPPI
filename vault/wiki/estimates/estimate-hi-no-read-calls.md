---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: After /hi the output of every block of the skill is in the first turn's context with no read call
method: "by hand at the /hi of the next session: the first turn's context and the tool calls before it read in the transcript, written into the estimate line"
checked: 2026-09-29
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Criterion

When:
The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

Then:
The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the lines `Pull:`, `Render:`, `Branch:` and `Status:` of `rule-git-context`, the line `Open issues:` of `rule-github-issues`, and the line `Tail:` of `rule-ledger-tail`.
**－** The agent makes no read-tool call to get any of them.

## Result

2026-09-29, by hand at the /hi of session 1134: the first turn held the loaded files of rule-internal-context, then Pull, Render, Branch, Status, Open issues and Tail, in the order of the children of rule-skill-hi; the agent's only tool call before the reply was the Write of frontier.md

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 101.3 added · [[decision-case-101.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L36
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; the hi line left to estimate-event-log-records, the block bookkeeping out; purpose and method set, Context and Method out (case 485.2) · [[decision-case-485.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L44
