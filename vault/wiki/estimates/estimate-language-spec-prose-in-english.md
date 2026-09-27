---
type: estimate
kind: QA
status: passed
target: "[[rule-language]]"
purpose: Pre-spec finds a name, context or problem of a Case of the plan that holds a Cyrillic letter, a short form under Deferred included
method: uv run pytest tests/test_prespec.py -k cyrillic
checked: 2026-09-27
origin: raw/2026-09-26/2300/ledger.md#case-445.4
sprint: migration
created: 2026-09-26
tags: [harness, workflow]
---

## Criterion

When:
`guppi prespec --check <plan>` runs at `/pre-spec` and reads the plan file.

Then:
A name, `context` or `problem` of a Case of the plan that holds a Cyrillic letter: one finding naming the Case and the part.
**＋** A short-form Case under `## Deferred` is read the same way.
**＋** A plan whose names, contexts and problems hold no Cyrillic letter gives no finding of this check.
**－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.
**－** The plan is compared with no other file: no ratified copy is read.

## Result

2026-09-27, uv run pytest tests/test_prespec.py -k cyrillic: 4 passed; live, session 1819: prespec --check reported "case 458: its context still holds Cyrillic"

## History

- 2026-09-27 created · [[decision-case-445.4]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L33
