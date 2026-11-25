---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and runs the index Grep of every other category with its pattern as written, then greps and reads as each finding needs, the code, the tests and the harness files among them, none reaching vault/archive/ and none reported as a broken rule, a count over Decision pages not run again
method: "by hand, after the first /pre-spec that runs once this Criterion is set: the Grep, Glob and Read calls of ask-guppi at that /pre-spec and its list of what it did not check, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript in the estimate line"
checked: 2026-11-25
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
**＋** Those Greps and Reads may cover the code, the tests and the harness files as well as the vault.
**＋** The list of what the agent did not check names no search of the code as a broken rule of `.claude/agents/ask-guppi.md`.
**＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
**－** No search of the code, the tests or the harness files reaches `vault/archive/`, which the agent searches by slug alone.
**－** Whether the folder-walk Grep runs for a Case that adds a file that is no page of the vault is outside this promise: `estimate-prespec-finds-a-reader-of-a-new-files-folder` reads it.
**－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
**－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

## Result

2026-11-25, Retro of session 0605, the agent transcript ~/.claude/projects/c--PROJECTS-GUPPI/16ad52b9-2613-43c4-8115-f092d2d530c2/subagents/agent-afae9ce827f922a5a.jsonl of the ask-guppi of the /pre-spec of this session, the first after Case 1048 set the method: its first four calls are the Greps ^(purpose|deferred_by): over vault/wiki/rules and vault/wiki/entities, ^(root_cause|deferred_by): over vault/wiki/lessons and ^(pattern|deferred_by): over vault/wiki/insights (L16 to L22), as written; later Greps and Reads cover .guppi/guppi, .guppi/tests, .claude, .github and the vault; each search over the repository root carries a glob limited to vault/wiki, .claude or .guppi (L112, L391 to L395, L413, L418, L468), so no search of the code, the tests or the harness files reaches vault/archive/; the one Glob over vault/** (L453) looks for three whole slugs, which its list of what it did not check names as not in the form vault/archive/**/<slug>.md; that list names no search of the code as a broken rule; no count over vault/wiki/decisions/ was run

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
- 2026-11-03 updated: the Criterion replaced whole — the searches a finding needs may cover the code, the tests and the harness files, and none is reported as a broken rule · [[decision-case-1015.1]]
- 2026-11-04 status: pending → failed · raw/2026-11-04/0358/ledger.md#L1
- 2026-11-20 deferred · [[decision-case-1037]]
- 2026-11-25 defer by decision-case-1037 superseded · [[decision-case-1048]]
- 2026-11-25 updated: pending again after the failed reading of session 0358, the Criterion unchanged; read at the /pre-spec of session 0605 · [[decision-case-1048]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0605/ledger.md#L24
