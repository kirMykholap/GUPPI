---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: After /hi the output of every block of the skill is in the first turn's context with no read call
method: "by hand, after a /hi: the first turn's context and the tool calls before it read in the transcript, and the allowed-tools of .claude/skills/hi/SKILL.md, written into the estimate line"
checked: 2026-10-16
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness]
core: true
---

## Criterion

When:
The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

Then:
The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the line `Render:` and the output of `uv run --project .guppi guppi gitstate` under the line `Branch:` of `rule-git-context`, and the line `Tail:` of `rule-ledger-tail`.
**＋** The `allowed-tools` of the skill names `uv run --project .guppi guppi render --sync`, `uv run --project .guppi guppi gitstate` and `uv run --project .guppi guppi tail`, and neither `git pull`, `git init` nor `gh`.
**－** The agent makes no read-tool call to get any of them.

## Result

2026-10-16, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
