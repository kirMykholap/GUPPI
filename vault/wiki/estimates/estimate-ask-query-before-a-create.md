---
type: estimate
kind: QA
status: pending
target: "[[rule-ask]]"
purpose: Whether the vault query that case-guppi runs before a create without a ref, by the recipe of ask-guppi, opens with the rules and runs the index Grep of every other category with its pattern as written, finds an existing page by meaning in either language, and names the rule a proposal crosses and the state of a named slug
method: "by hand, after the first build of case-guppi whose Case proposes a create without a ref and that runs on .claude/agents/ask-guppi.md rendered from the Render of rule-ask that runs every category whatever the question: the Grep, Glob and Read calls of that build, read in its agent transcript under ~/.claude/projects/ against the Criterion, and the context of its case file read with them, the transcript and the line numbers in the estimate line"
checked: 2026-10-31
origin: raw/2026-10-04/0112/ledger.md#case-626.2
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The query opens with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs, whatever the question, the Grep `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`.
**＋** Each of those four Greps takes its pattern as the recipe writes it, with no word added.
**＋** A page that already holds the thing is found by meaning, whether the person's words name it in the language of the chat or in the language of the repository, and the `context` of the Case names its slug.
**＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
**＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
**＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
**－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.
**－** Where the query stands among the other searches of the build is outside this promise: `estimate-case-build-runs-the-vault-query-first` reads it.

## Result

2026-10-31, Retro of session 0431, the builds of Case 787.1 (~/.claude/projects/c--PROJECTS-GUPPI/d346cd66-267a-40ee-9b8a-c61a4f83fe58/subagents/agent-aa05b9b111196ecd1.jsonl) and Case 804.6 (c3e1bea8-7bfa-4b46-9a71-75671681caf3/subagents/agent-a673fbf70b192fe38.jsonl) with vault/archive/plugin/2026-10-12/2349/raw/cases/case-787.md and vault/archive/plugin/2026-10-13/1753/raw/cases/case-804.md, on the text of ask-guppi.md of commits 279c853d and acf719df: in 787.1 four Greps of vault/wiki came before the rules Grep ^(purpose|deferred_by): (lines 51, 58, 82, 83, the rules Grep at line 84), and the lessons and insights Greps matched words; in 804.6 three vault searches came before it (lines 108, 157, 217) and no lessons or insights Grep ran; both found the near pages, named the crossing rules, checked the slug by a Glob over vault/archive/, opened no archived page and searched the archive by no meaning

## History

- 2026-10-04 created · [[decision-case-626.2]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.8]]
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end, and the method waits for the event it names · [[decision-case-823.1]]
- 2026-10-30 updated: the Criterion replaced whole — the languages are named by their role · [[decision-case-920.2]]
- 2026-10-31 updated: the method reads the builds of Cases 787 and 804 in their transcripts and case files, the Criterion written back unchanged · [[decision-case-961.4]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L44
- 2026-10-31 updated: the Criterion replaced whole — the query opens with the rules and runs every other index Grep with its pattern as written; the moment in the build is read by estimate-case-build-runs-the-vault-query-first · [[decision-case-970.2]]
