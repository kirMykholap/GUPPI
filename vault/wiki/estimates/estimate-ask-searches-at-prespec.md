---
type: estimate
kind: QA
status: failed
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, and leaves vault/wiki/decisions/ out of every search but the two reasons its frame names, a count over Decision pages not run again
method: "by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.2 and of .claude/rules/search-leaves-out-decisions.md by case 640, read in its agent transcript against the Criterion, recorded in the estimate line"
checked: 2026-10-05
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

## Result

2026-10-05, at the /hi of session 0109, by hand: the Grep, Glob and Read calls of the two ask-guppi runs at the /pre-spec of session 2245 (transcript 7086b96c, agent aab5addf1e347ccb8 with 32 calls, agent a390781c7f1241c18 with 57), after the render of .claude/agents/ask-guppi.md by case 633.2 in commit 3b31fb80: both start with the Grep `^(purpose|deferred_by):` over vault/wiki/rules/, then the Grep of insights/ (both) and of lessons/ (636), then Greps and Reads as a finding needs; neither ran again a count of a context whose search covers decisions/; but call 16 of a390781c7f1241c18, a Grep of the seven Estimate slugs over vault/wiki with the glob `!decisions/**`, printed 29 lines of files under vault/wiki/decisions/, decision-case-12.md and decision-case-16.1.md among them — the glob did not keep the folder out — for neither reason the frame names; the agent reported it under What I did not check; no call of aab5addf1e347ccb8 printed a line of a Decision page

## History

- 2026-10-04 created · [[decision-case-633.2]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/0109/ledger.md#L9
- 2026-10-05 updated: the method names the render of .claude/rules/search-leaves-out-decisions.md by case 640; the Criterion stands · [[decision-case-640]]
- 2026-10-05 deferred · [[decision-case-649]]
