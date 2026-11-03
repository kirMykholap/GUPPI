---
type: estimate
kind: QA
status: passed
target: "[[rule-language]]"
purpose: Pre-spec finds a name, context or problem of a Case of the plan that holds a letter outside the script of the documentation language of guppi.toml, a Latin letter in a code span excepted, a short form under Deferred included
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k script
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
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

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
