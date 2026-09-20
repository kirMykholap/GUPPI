---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: generate ticks, in the Spec beside its yaml, the page line of the Case whose entry it applied
method: pytest tests/test_generate.py with a Spec beside the yaml, plus one reading of this session's spec.md after the librarian's run
checked: 2026-09-20
origin: raw/2026-09-17/1119/ledger.md#case-226.1
sprint: migration
created: 2026-09-17
tags: [harness, workflow, ledger]
---

## Criterion

Given:
A yaml entry of kind `estimate` carries `slug`, `status`, `result` and no `case`; a `create` entry with `folded` carries the reading of the same session.
**＋** The Spec of the unit lies beside the yaml — `raw/<date>/<HHMM>/spec.md`; the Specs of the other sessions are the `spec.md` of their folders under `raw/`.
**＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
**＋** A reading line of the Spec is `- [ ] read `<slug>`` with text after it, in any Case.
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml and a second Spec in another session folder.
**－** A Rule-class file entry `generate` does not apply — "applied by hand".

When:
`guppi generate` applied an entry and marked it `applied`.

Then:
For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
**＋** Two entries of one kind and slug in one Case tick two lines, in order.
**＋** For an `estimate` entry, and for a `create` entry with `folded`, the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry.
**＋** A `create` entry with `folded` ticks both lines: the page line and the reading line.
**－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
**－** `lesson` and Rule-class file entries, and an entry marked `failed`, tick no line; the lines on code, tests, migrations and `by hand` are the agent's.
**－** A Spec under `vault/archive/` is not read.

## Result

2026-09-20, `uv run pytest -q tests/test_generate.py` 67 green, six new — a reading ticks the first unticked read line of its slug, two readings two lines in order, a create with a folded reading ticks the page line and the read line, another session's Spec oldest first with the archive untouched, nothing found applied without a word, a lesson ticks nothing; live — the librarian's run of this session on the read lines W1–W3 of Spec 0958 and lines 56 and 829 of Spec 1308, read in the next

## History

- 2026-09-18 created · [[decision-case-226.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L13
- 2026-09-20 updated: the Criterion replaced whole — an estimate entry and a create with a folded reading tick the read line, across the Specs of raw/ (case 270.1) · [[decision-case-270.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L53
