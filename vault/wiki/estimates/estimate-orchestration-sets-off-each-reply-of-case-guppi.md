---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each reply of case-guppi that the main agent shows — a round, a Fact answer or a built Case — stands between two horizontal rules, with the agent's own text after the second
method: "by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-09/2049/ledger.md#case-751.1
sprint: migration
created: 2026-10-09
tags: [session, workflow]
---

## Criterion

When:
The main agent shows in the chat a reply of `case-guppi` — a round of questions, a `**Fact:**` answer it passes on, or a built Case with its list and its `ratification` — with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
A horizontal rule stands on its own line before the reply of `case-guppi`.
**＋** A second horizontal rule stands after the reply; the main agent's own text follows it, or, in a batch, the next reply of `case-guppi`, for which that rule is the rule before it.
**＋** Each rule is the line `---` alone, with a blank line after it, and with a blank line before it unless it opens the reply, so that Markdown does not read the line above it as the underline of a heading.
**－** A `**Waiting:**` line, the acknowledging reply and a Case in the short form are no reply of `case-guppi` and get no such rules.

## Result

2026-10-09, Retro, by hand: the new Render sentence of rule-orchestration in raw/2026-10-09/2049/spec.md (case 751.1) read against the Criterion; it sets a rule before and after each round, Fact answer and built Case, the agent's own text or the next reply of a batch after the second, the line `---` with a blank line after it and before it unless it opens the reply, and no rules for a Waiting line, the acknowledging reply or a short-form Case; its replace anchor stands once on the page

## History

- 2026-10-09 created · [[decision-case-751.1]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/2049/ledger.md#L14
