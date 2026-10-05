---
type: estimate
kind: QA
status: pending
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, each of their Greps over vault/wiki/ or a folder that holds it leaves out the Decision pages with !**/decisions/**, and the text of a Decision page reaches them only by a Read of its path for a reason their frame names
method: "by hand at the /hi of a later session: the transcripts of the main agent and of each ask-guppi and case-guppi of a session after the render of .claude/rules/search-leaves-out-decisions.md by case 640, whether the file stands in each context and each Grep, Glob and Read call, read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-05/0109/ledger.md#case-640
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session]
---

## Criterion

When:
A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Grep, Glob or Read.

Then:
`.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
**＋** Each Grep whose path is `vault/wiki/` or a folder that holds it carries `!**/decisions/**` in its glob, alone or after another filter, and prints no line of a page under `vault/wiki/decisions/`.
**＋** The text of a Decision page reaches one of these agents only by a Read of its path, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi`, and for no reason in the main agent.
**－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
**－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

## History

- 2026-10-05 created · [[decision-case-640]]
