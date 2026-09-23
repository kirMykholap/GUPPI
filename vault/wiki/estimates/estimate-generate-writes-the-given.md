---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: A decision page carries the given of its Case, so the frame survives the Criterion that no longer holds it
method: pytest tests/test_generate.py on a temp vault
origin: raw/2026-09-23/1355/ledger.md#case-378.3
sprint: migration
created: 2026-09-23
tags: [harness, workflow, librarian]
---

## Criterion

When:
`guppi generate` writes the decision page of a Case whose `case_text` in the yaml carries `given`.

Then:
The body of the page is `## Context`, `## Problem`, `## Given`, `## Deferred` on a Case with a defer, and `## History`; `## Given` is the Case's `given`, verbatim.
**－** A Case without `given` (defer-only) has no `## Given`.
**－** The decision pages already in the vault are not rewritten.

## Result

2026-09-23, uv run pytest tests/test_generate.py -k "decision_page_carries_the_given or case_without_given or supersedes_marks_the_earlier": 3 passed — the decision page body is Context, Problem, Given, History, the Given verbatim; a Case without given has no ## Given; no ## When, no ## Criterion

## History

- 2026-09-23 created · [[decision-case-378.3]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L40
