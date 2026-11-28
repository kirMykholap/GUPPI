---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and runs the index Grep of every other category with its pattern as written, then greps and reads as each finding needs, the code, the tests and the harness files among them, none reaching vault/archive/ and none reported as a broken rule, a count over Decision pages not run again
method: "by hand, after the first /pre-spec that runs once this Criterion is set: the Grep, Glob and Read calls of ask-guppi at that /pre-spec and its list of what it did not check, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript in the estimate line"
checked: 2026-11-25
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness]
core: true
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

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
