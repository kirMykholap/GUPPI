---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a quotation in the Context as a blockquote, a number only beside a quotation of what it points to, and an unknown term explained
method: "by hand, in a session after the render: one first round and one later round of case-guppi read in the chat against the Criterion"
checked: 2026-09-30
origin: raw/2026-09-28/1318/ledger.md#case-477.1
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
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

2026-09-30, by hand, the first rounds of case-guppi on Cases 547 to 550 and the later rounds on 548 (Q4), 549 (Q3) and 550, read in the chat of session 1736: each Context gives the mechanism in plain words with an example, quotations stand as blockquotes on their own lines, terms are explained where they first stand, no number stands alone but beside a quotation; but the sentence on what the round decides runs a series of parallel clauses inside one sentence on Case 548 (how to fix the test, whether to drop the skips, whether to fix the method line) and Case 550 (what happens to the pages, whether the code gets a limit, whether the schema text states the old shape), and the Context of Case 547 names five examples of closed lines in one sentence, against the list rule of .claude/skills/grill-me/SKILL.md

## History

- 2026-09-28 created · [[decision-case-477.1]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/2000/ledger.md#L25
- 2026-09-29 updated: the Criterion replaced whole — the instructions point to the question shape of the grill-me template, read by estimate-skill-grill-me-asks-in-rounds; this promise keeps the Context, the case numbers and the terms (case 501.2) · [[decision-case-501.2]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1134/ledger.md#L39
- 2026-09-29 updated: the Criterion replaced whole — a list in the Context one item per line; a number in any line of a round only beside a quotation of what it points to (case 512, supersedes 511.2) · [[decision-case-512]]
- 2026-09-29 updated: the Criterion replaced whole — a quotation in the Context stands as the grill-me template sets it (case 524.2) · [[decision-case-524.2]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/0248/ledger.md#L36
- 2026-09-30 status: failed → failed · raw/2026-09-30/1736/ledger.md#L19
- 2026-10-01 deferred · [[decision-case-563]]
- 2026-10-01 deferred · [[decision-case-572]]
