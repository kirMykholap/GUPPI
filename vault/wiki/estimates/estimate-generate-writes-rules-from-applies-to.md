---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: The rules of every live Entity are the live rules whose applies_to names it, recomputed by the cascade of generate on every run
method: "pytest .guppi/tests/test_generate.py on a temp vault; by hand, after a run of guppi generate: the rules of each live Entity read against the applies_to of the live rules"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian]
core: true
---

## Criterion

When:
`guppi generate` has applied the entries of a yaml and runs the cascade over the live pages of `vault/wiki/`.

Then:
The `rules` of every live Entity is the slugs of the live rules whose `applies_to` names it, in slug order; the field is written when the list is not empty or the field already stands; a change is a History line `rules: [...] · cascade`; an empty list on a page without the field writes no field.
**＋** A rule with `applies_to` on a slug with no live page: the entry applies and the field stands; the cascade skips it; `guppi lint` names it.
**－** An archived rule gives no edge; `applies_to` is never computed — it comes from the Case alone.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
