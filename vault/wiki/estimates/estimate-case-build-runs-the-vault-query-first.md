---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi makes the Grep of the rules of its vault query its first Grep of vault/wiki/ once it sees that its Case proposes a create without a ref
method: "by hand, after the first build of case-guppi on the Render of rule-case-build that holds the sentence on when the vault query runs, whose Case proposes a create without a ref: the Grep, Glob and Read calls of that build, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript and the line numbers in the estimate line"
origin: raw/2026-10-31/1831/ledger.md#case-970.1
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that proposes a `create` without a `ref`.

Then:
Where the item asks for a new page, the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` of the vault query of `.claude/agents/ask-guppi.md` is the first Grep of `vault/wiki/` in the build.
**＋** Where the person chooses the new page in a round, that Grep is the first Grep of `vault/wiki/` after the answer to that round.
**－** A Glob or a Read of a page the item names may come before that Grep.

## History

- 2026-10-31 created · [[decision-case-970.1]]
