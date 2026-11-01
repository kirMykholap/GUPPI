---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and runs the index Grep of every other category with its pattern as written, then greps and reads as each finding needs, a count over Decision pages not run again
method: "by hand, after the first /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md rendered from the Render of rule-ask that runs every category whatever the question: the Grep, Glob and Read calls of ask-guppi at that /pre-spec, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript in the estimate line"
checked: 2026-11-01
origin: raw/2026-10-04/2041/ledger.md#case-633.2
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs, whatever the question, the Grep `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, each with its pattern as the recipe writes it and no word added.
**＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
**＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
**－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
**－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

## Result

2026-11-01, Work Mode of session 0141, the ask-guppi transcript of the pre-spec of session 2307, ~/.claude/projects/c--PROJECTS-GUPPI/8d8876d7-f627-4f65-95f7-cb7b7172cd46/subagents/agent-a5ddd2830f464981b.jsonl, rendered at 6ccb92a0 before the run: L15 Grep ^(purpose|deferred_by): over vault/wiki/rules, L17 the same over entities, L19 ^(root_cause|deferred_by): over lessons, L21 ^(pattern|deferred_by): over insights, each pattern as written and no call before L21; about 70 further Greps and Reads as findings needed, among them the counts of the contexts of Cases 972 and 975 at L155 and L238, run over vault/wiki, where the hook of rule-search-leaves-out-decisions leaves out the decisions folder; no call under vault/wiki/decisions/

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
- 2026-10-31 updated: the Criterion replaced whole — at /pre-spec too the agent runs the index Grep of every category with its pattern as written · [[decision-case-970.3]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/0141/ledger.md#L16
