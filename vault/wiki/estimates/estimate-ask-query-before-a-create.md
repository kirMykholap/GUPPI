---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether the vault query that case-guppi runs before a create without a ref, by the recipe of ask-guppi, starts with the rules, finds an existing page by meaning in either language, and names the rule a proposal crosses and the state of a named slug
method: "by hand at the /hi of a later session: the transcript of a case-guppi that built a Case with a create without a ref after the render of .claude/agents/ask-guppi.md by case 626.1, its Grep and Glob calls and the context of its Case read against the Criterion, recorded in the estimate line"
checked: 2026-10-05
origin: raw/2026-10-04/0112/ledger.md#case-626.2
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
**＋** A page that already holds the thing is found by meaning, whether the person's words name it in Russian or in English, and the `context` of the Case names its slug.
**＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
**＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
**＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
**－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

## Result

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.

## History

- 2026-10-04 created · [[decision-case-626.2]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.8]]
