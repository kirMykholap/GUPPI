---
type: estimate
kind: QA
status: pending
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, and leaves vault/wiki/decisions/ out of every search but the two reasons its frame names, a count over Decision pages not run again
method: "by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.2, read in its agent transcript against the Criterion, recorded in the estimate line"
origin: raw/2026-10-04/2041/ledger.md#case-633.2
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
**＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
**＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
**－** No Grep or Read of the agent reaches `vault/wiki/decisions/`, except for the `## Problem` of a Decision that a `deferred_by` names and a Decision reached through a page's `origin` when the question asks why something was decided.

## History

- 2026-10-04 created · [[decision-case-633.2]]
