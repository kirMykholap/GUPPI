---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi lets a fact its prompt states besides the person's words into a Case only after it reads it at its source, and keeps out a fact it cannot read there
method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
origin: raw/2026-10-06/0104/ledger.md#case-690.1
sprint: migration
created: 2026-10-06
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case, and the prompt of its call or a later message states a fact besides the person's words: a count, or what a page, a file or a reply says.

Then:
The fact enters the Case only after `case-guppi` reads it at its source.
**＋** A fact that `case-guppi` cannot read at its source stays out of the Case.
**－** The person's words enter `recommend` as the person's answer, with no source to read.

## Result

2026-10-06, Retro, the new text of rule-case-build in the Spec (case 690.1): a fact the prompt or a message states besides the person's words enters the Case only after case-guppi reads it at its source, and one it cannot read stays out; its anchor stands once in the page

## History

- 2026-10-06 created · [[decision-case-690.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L45
