---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: generate ticks, in the Spec beside its yaml, the page line of the Case whose entry it applied
method: pytest tests/test_generate.py with a Spec beside the yaml, plus one reading of this session's spec.md after the librarian's run
checked: 2026-09-18
origin: raw/2026-09-17/1119/ledger.md#case-226.1
sprint: migration
created: 2026-09-17
tags: [harness, workflow, ledger]
---

## Criterion

Given:
A yaml entry carries `case`, `kind` and `slug`; the Spec of the unit lies beside the yaml — `raw/<date>/<HHMM>/spec.md`.
**＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml.
**－** A Rule-class file entry `generate` does not apply — "applied by hand".

When:
`guppi generate` applied an entry `create`, `update`, `delete` or `defer` and marked it `applied`.

Then:
In the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
**＋** Two entries of one kind and slug in one Case tick two lines, in order.
**－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
**－** `estimate`, `lesson` and Rule-class file entries, and an entry with `failed`, tick no line; the lines on code, tests, migrations, `read` and `by hand` are the agent's.

## Result

2026-09-18, uv run pytest tests/test_generate.py tests/test_sprint.py in session 1252: 63 passed; raw/2026-09-17/1119/spec.md after the librarian's run of 2026-09-18: every page line create, update, delete or defer stands [x] — 32 ticked, 0 unticked — and the lines on code, tests, read and by hand untouched by the run

## History

- 2026-09-18 created · [[decision-case-226.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L13
