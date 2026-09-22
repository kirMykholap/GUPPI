---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: The rules of every live Entity are the live rules whose applies_to names it, recomputed by the cascade of generate on every run
method: pytest tests/test_generate.py on a temp vault; the live reading the librarian's run of this session — entity-sprint carries rules [rule-sprint]
origin: raw/2026-09-22/0014/ledger.md#case-305.3
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian]
---

## Criterion

Given:
The cascade of `generate`, after the entries are applied, recomputes on the live pages the status of every Entity and Rule and the `severity` of every Insight.
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault.

When:
`guppi generate` reaches the cascade.

Then:
The `rules` of every live Entity is the slugs of the live rules whose `applies_to` names it, in slug order; the field is written when the list is not empty or the field already stands; a change is a History line `rules: [...] · cascade`; an empty list on a page without the field writes no field.
**＋** A rule with `applies_to` on a slug with no live page: the entry applies and the field stands; the cascade skips it; lint names it (305.5).
**－** An archived rule gives no edge; `applies_to` is never computed — it comes from the Case alone.

## Result

2026-09-22, uv run pytest tests/test_generate.py, 77 passed: the cascade writes rules on an Entity from the applies_to of the live rules in slug order as wikilinks with a History line, recounts a stale list to [], writes no field where no rule points and the field is absent, never computes applies_to, and counts no archived rule; the live leg, the librarian's run with entity-sprint carrying rules [rule-sprint], not taken

## History

- 2026-09-22 created · [[decision-case-305.3]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L59
