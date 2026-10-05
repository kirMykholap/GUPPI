---
type: estimate
kind: QA
status: pending
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, a count over Decision pages not run again
method: "by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md, read in its agent transcript against the Criterion, recorded in the estimate line"
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
**－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
**－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

## Result

2026-10-05, by hand at the /hi of session 1616: the Grep, Glob and Read calls of the three ask-guppi runs at the /pre-spec of session 0311 (transcript 6d53e05d; a055d35695650c13f 46 calls, af56f988c579ddc06 46, af7cde916f5b24293 47): each starts with the Grep `^(purpose|deferred_by):` over vault/wiki/rules/ (call 1); af56f988c579ddc06 then read the plan and grepped lessons/, insights/ and entities/ (calls 4–6) before any other search; a055d35695650c13f read rule-spec-write.md (call 4) before its Greps of lessons/ and insights/ (calls 5–6), and af7cde916f5b24293 read rule-case-protocol.md and case-schema.md (calls 4–5) before its Grep of insights/ (call 6), so in two runs a Read came between the rules Grep and the Greps of the other categories; no context of Cases 644–646 states a count whose search covers decisions/ (each count there carries `!**/decisions/**`), so none was run again; the later Greps and Reads followed findings

## History

- 2026-10-04 created · [[decision-case-633.2]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/0109/ledger.md#L9
- 2026-10-05 updated: the method names the render of .claude/rules/search-leaves-out-decisions.md by case 640; the Criterion stands · [[decision-case-640]]
- 2026-10-05 deferred · [[decision-case-649]]
- 2026-10-05 updated: the Criterion replaced whole — the clause on Decision pages left to estimate-search-leaves-out-decisions-in-every-agent; purpose and method set anew (case 655) · [[decision-case-655]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1616/ledger.md#L4
- 2026-10-05 updated: the Criterion replaced whole — the Greps over a folder that holds the Decision pages are left to estimate-search-leaves-out-decisions-by-the-grep-hook, the Reads and the Greps inside it to estimate-search-leaves-out-decisions-in-every-agent (case 664.3) · [[decision-case-664.3]]
