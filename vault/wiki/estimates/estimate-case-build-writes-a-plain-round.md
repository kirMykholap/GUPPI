---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a quotation in the Context as a blockquote, a number only beside a quotation of what it points to, and an unknown term explained
method: "by hand, in a session after the render: one first round and one later round of case-guppi read in the chat against the Criterion"
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

Then:
The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
**＋** A list in the `**Context:**` stands one item per line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a list.
**＋** A quotation in the `**Context:**` stands as a blockquote on its own line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a quotation.
**＋** The instructions of `case-guppi` point each question, and each list and each quotation of the Context, to `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
**＋** The round says what it rests on in plain words and uses no number where plain words are enough.
**＋** A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in any line of the round, the `➡️` line included, only beside a short quotation of the words it points to, as the source of that quotation.
**＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
**－** A page name in a code span is no such reference: it stays where the question is about that page.
**－** The shape of a question, what counts as a list, and the form of a quotation in a question are read by `estimate-skill-grill-me-asks-in-rounds`, not here.
**－** The `context`, `problem` and `recommend` of a Case keep their numbers as `rule-case-protocol` allows: this promise is about a round only.

## Result

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
