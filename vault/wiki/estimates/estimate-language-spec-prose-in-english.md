---
type: estimate
kind: QA
status: passed
target: "[[rule-language]]"
purpose: Pre-spec finds a name, context or problem of a Case of the plan that holds a letter outside the script of the documentation language of guppi.toml, a Latin letter in a code span excepted, a short form under Deferred included
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k script
checked: 2026-10-02
origin: raw/2026-09-26/2300/ledger.md#case-445.4
sprint: migration
created: 2026-09-26
tags: [harness, workflow]
---

## Criterion

When:
`guppi prespec --check <plan>` runs at `/pre-spec`, and reads the plan file and `guppi.toml`.

Then:
A name, `context` or `problem` of a Case of the plan that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, gives one finding naming the Case, the part and the language.
**＋** A Latin slug, path or field name in a code span gives no finding, whatever the documentation language.
**＋** A short-form Case under `## Deferred` is read the same way.
**＋** A plan whose names, contexts and problems hold no letter outside that script gives no finding of this check.
**＋** A `guppi.toml` that is missing, or that names a code the table of `.guppi/guppi/config.py` does not hold, gives one finding that names `guppi.toml`, and no Case is read by this check.
**＋** The judgment of a letter's script lives in `.guppi/guppi/config.py`, and `.guppi/guppi/ratified.py` imports it.
**＋** `.guppi/guppi/config.py` reads a code span by `CODE_SPAN` of `.guppi/guppi/lint.py`, and holds no pattern of its own.
**－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.
**－** The plan is compared with no other file: no ratified copy is read.

## Result

2026-10-02, uv run pytest tests/test_prespec.py -k script: 9 passed

## History

- 2026-09-27 created · [[decision-case-445.4]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L33
- 2026-09-28 updated: the Criterion replaced whole — a letter outside the script of documentation_lang, read from guppi.toml, not a Cyrillic letter (case 476.3) · [[decision-case-476.3]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L19
- 2026-10-02 updated: the Criterion replaced whole — a Latin letter in a code span gives no finding, any other letter there is judged as in prose (case 589.1) · [[decision-case-589.1]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L35
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
