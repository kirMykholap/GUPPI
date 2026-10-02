---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: An answer of case-guppi whose name, context or problem holds a letter outside the script of the documentation language, a Latin letter in a code span excepted, is a finding of the check, and no file of the Case is written while it stands
method: uv run pytest tests/test_casecheck.py -k script
checked: 2026-10-02
origin: raw/2026-09-30/0248/ledger.md#case-537
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the answer and `guppi.toml`.

Then:
A name, `context` or `problem` of a Case of the answer that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` answers again.
**＋** While such a finding stands, no `raw/<date>/<hi HHMM>/cases/case-<N>.md` is written for the answer.
**＋** An answer whose names, contexts and problems hold no such letter gets no finding from this check.
**＋** A Latin slug or path in a code span of an answer is no finding, whatever the documentation language.
**＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
**＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
**－** An answer whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged answer is not sent back twice, and no file is written for it.
**－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

## Result

2026-10-02, uv run pytest tests/test_casecheck.py -k script: 9 passed

## History

- 2026-09-30 created · [[decision-case-537]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1306/ledger.md#L43
- 2026-10-02 updated: the Criterion replaced whole — a Latin letter in a code span is no finding, any other letter there is judged as in prose (case 589.2) · [[decision-case-589.2]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L36
