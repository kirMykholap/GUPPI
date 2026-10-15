---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case of case-guppi whose name, context or problem holds a letter outside the script of the documentation language, a Latin letter in a code span excepted, is a finding of the check, and the Case is not shown or written into the Spec while it stands
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k script
checked: 2026-10-05
origin: raw/2026-09-30/0248/ledger.md#case-537
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file and `guppi.toml`.

Then:
A name, `context` or `problem` of a Case of the file that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` fixes the file.
**＋** While such a finding stands, the store holds the Case with it, so the `Stop` check refuses its showing and the Spec hook writes nothing of it.
**＋** A file whose names, contexts and problems hold no such letter gets no finding from this check.
**＋** A Latin slug or path in a code span is no finding, whatever the documentation language.
**＋** A `guppi.toml` that is missing, or that names a code the table of `.guppi/guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
**＋** The hook runs `check_untranslated` of `.guppi/guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
**－** A file whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged file is not sent back twice.
**－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

## Result

2026-10-05, at the /hi of session 1343: uv run pytest -q tests/test_casecheck.py -k script 10 passed, 125 deselected

## History

- 2026-09-30 created · [[decision-case-537]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1306/ledger.md#L43
- 2026-10-02 updated: the Criterion replaced whole — a Latin letter in a code span is no finding, any other letter there is judged as in prose (case 589.2) · [[decision-case-589.2]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L36
- 2026-10-05 updated: the Criterion replaced whole — the check reads the file case-guppi wrote, and a finding holds the Case back from the showing and the Spec instead of keeping a file unwritten; the purpose follows (case 645.7) · [[decision-case-645.7]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L5
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
