---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading across the Specs of raw/ — never a line of a later or a superseded Case
method: pytest tests/test_generate.py with a Spec beside the yaml, plus one reading of this session's spec.md after the librarian's run
checked: 2026-09-21
origin: raw/2026-09-17/1119/ledger.md#case-226.1
sprint: migration
created: 2026-09-17
tags: [harness, workflow, ledger]
---

## Criterion

Given:
A yaml entry of kind `estimate` carries `slug`, `status`, `result`, `line` and no `case`; a decision entry carries `case` and `line`, the number of its line in the ledger.
**＋** A line `{supersedes:case N}` marks every entry of Case N `superseded_by`, in the yaml of any session under `raw/` (130.2, 175); `generate` neither applies them nor ticks their page lines (151, 200.2).
**＋** The lines of a superseded Case are not counted at Retro — its work stands under the superseding Case (282).
**＋** The Spec of a session lies beside its `materialize.yaml` — `raw/<date>/<HHMM>/spec.md`; the Specs of the other sessions are the `spec.md` of their folders under `raw/`.
**＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
**＋** A reading line of the Spec is `- [ ] read `<slug>`` with text after it, in any Case.
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml and a second Spec with a yaml of its own in another session folder.
**－** A Rule-class file entry `generate` does not apply — "applied by hand".

When:
`guppi generate` applied an entry and marked it `applied`.

Then:
For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
**＋** Two entries of one kind and slug in one Case tick two lines, in order.
**＋** For an `estimate` entry, and for a `create` entry with `folded`, the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry.
**＋** In the Spec beside the yaml, a `read` line in the section of a Case whose first decision entry of the yaml carries a `line` greater than the `line` of the `estimate` entry is not the reading's line — the Case was ratified after it; the search goes on to the next line, then to the other sessions.
**＋** In any Spec, a `read` line in the section of a Case whose entries in the yaml of that session are marked `superseded_by` is not the reading's line — its work stands under the superseding Case; the search goes on. For the Spec beside the yaml the marks are the run's entries; for the Spec of another session its `materialize.yaml` beside it, read for the marks alone; no yaml beside it — nothing is skipped there.
**＋** A `create` entry with `folded` ticks both lines: the page line and the reading line; its Case is the reading's Case, the filter of 280 does not apply to it; the filter by `superseded_by` does.
**－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
**－** `lesson` and Rule-class file entries, and an entry marked `failed`, tick no line; the lines on code, tests, migrations and `by hand` are the agent's.
**－** A Spec under `vault/archive/` is not read; the Specs of the other sessions are not filtered by `line`.

## Result

2026-09-21, uv run pytest tests/test_generate.py: 74 green; live — Spec 1315 after the librarian's run: line 311, the read line of estimate-materialize-assembles under 296, is [x]; line 72, the read line of the same slug under 291.1, superseded by 296 in the same yaml, is [ ] — the filter by superseded_by

## History

- 2026-09-18 created · [[decision-case-226.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L13
- 2026-09-20 updated: the Criterion replaced whole — an estimate entry and a create with a folded reading tick the read line, across the Specs of raw/ (case 270.1) · [[decision-case-270.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L53
- 2026-09-20 updated: the Criterion replaced whole — the read line of a later Case of the same unit is skipped by the ledger line numbers (case 280) · [[decision-case-280]]
- 2026-09-21 status: pending → passed · raw/2026-09-20/2106/ledger.md#L2
- 2026-09-21 updated: the Criterion replaced whole — the read line of a superseded Case is skipped by the marks of the yaml beside the Spec (case 286) · [[decision-case-286]]
- 2026-09-21 updated: the purpose by the Criterion of 286 (case 290.3) · [[decision-case-290.3]]
- 2026-09-21 updated: the Criterion of 286 restored whole, replaced by the purpose update of 290.3 (case 291.2) · [[decision-case-291.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L5
