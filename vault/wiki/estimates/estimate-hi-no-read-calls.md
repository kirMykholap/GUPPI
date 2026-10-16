---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: After /hi the output of every block of the skill is in the first turn's context with no read call
method: "by hand, after a /hi: the first turn's context and the tool calls before it read in the transcript, and the allowed-tools of .claude/skills/hi/SKILL.md, written into the estimate line"
checked: 2026-10-16
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Criterion

When:
The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

Then:
The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the line `Render:` and the output of `uv run --project .guppi guppi gitstate` under the line `Branch:` of `rule-git-context`, and the line `Tail:` of `rule-ledger-tail`.
**＋** The `allowed-tools` of the skill names `uv run --project .guppi guppi render --sync`, `uv run --project .guppi guppi gitstate` and `uv run --project .guppi guppi tail`, and neither `git pull`, `git init` nor `gh`.
**－** The agent makes no read-tool call to get any of them.

## Result

2026-10-16, /hi of session 1712, the first turn's context and .claude/skills/hi/SKILL.md: the context holds the text of sprint.md, backlog.md, brief.md, orchestration.md, where-to-stop.md, ratification.md and glossary.md, then Render:, Branch: with the output of guppi gitstate (the branch plugin and Status:), and Tail:, in the order of the blocks of the skill; allowed-tools names uv run --project .guppi guppi render --sync, uv run --project .guppi guppi gitstate and uv run --project .guppi guppi tail, and no git pull, git init or gh; the agent's first tool calls were Reads of four Estimate pages, and it made no read-tool call for any block

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 101.3 added · [[decision-case-101.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L36
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; the hi line left to estimate-event-log-records, the block bookkeeping out; purpose and method set, Context and Method out (case 485.2) · [[decision-case-485.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L44
- 2026-09-30 updated: the Criterion replaced whole — no Pull and no Open issues line; allowed-tools names neither git pull nor gh (case 528.3) · [[decision-case-528.3]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L2
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-16 updated: the Criterion replaced whole — allowed-tools names guppi gitstate in place of the two git commands · [[decision-case-851.2]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/1712/ledger.md#L1
- 2026-10-17 updated: the method waits for a /hi, with no past moment · [[decision-case-875]]
