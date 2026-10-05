---
type: estimate
kind: QA
status: passed
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

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page failed: 2026-10-05, /hi of 1831, the ask-guppi transcripts of the /pre-spec of 1616 (6360af9f, 17:39) and 1343 (f5706873, 15:25), after the render of ask-guppi.md at 03:09; every run opened with the Grep ^(purpose|deferred_by): over vault/wiki/rules/; in 1616 the run on 664 Read rule pages and Estimates and ran no Grep of lessons, insights or entities, the run on 661 grepped insights alone; in 1343 the runs on 650, 651, 652, 653 and 656 ran Reads of rule and estimate pages before their last category Grep

## History

- 2026-10-04 created · [[decision-case-633.2]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/0109/ledger.md#L9
- 2026-10-05 updated: the method names the render of .claude/rules/search-leaves-out-decisions.md by case 640; the Criterion stands · [[decision-case-640]]
- 2026-10-05 deferred · [[decision-case-649]]
- 2026-10-05 updated: the Criterion replaced whole — the clause on Decision pages left to estimate-search-leaves-out-decisions-in-every-agent; purpose and method set anew (case 655) · [[decision-case-655]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1616/ledger.md#L4
- 2026-10-05 updated: the Criterion replaced whole — the Greps over a folder that holds the Decision pages are left to estimate-search-leaves-out-decisions-by-the-grep-hook, the Reads and the Greps inside it to estimate-search-leaves-out-decisions-in-every-agent (case 664.3) · [[decision-case-664.3]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1831/ledger.md#L8
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.15]]
