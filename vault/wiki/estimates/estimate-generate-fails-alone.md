---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: One bad entry never stops the run; every entry carries its mark
method: pytest tests/test_generate.py, the tests of the failed, skipped and marked entries
origin: raw/2026-09-16/1955/ledger.md#case-201.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
---

## Criterion

Given:
`guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
**＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
**＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `materialize`, `cleanup` and `lint` do not change here.

When:
`guppi generate` meets an entry it cannot apply, or one already handled.

Then:
An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
**＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
**＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
**＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
**＋** A Rule-class file entry prints `a Rule-class file, applied by hand` and is marked applied; an `update` with no content prints `an update with no content in the Spec; applied by hand` and is marked applied.
**－** The failure of one entry changes no other page: `log.md` after it is level with the pages.

## Result

2026-09-16, `pytest tests/test_generate.py`: 46 green — a failing entry is on stderr, marked failed and skipped, the rest apply, exit 1; applied marks, a stale failed dropped, a rerun silent; an entry materialize could not lift and one with superseded_by skipped as before

## History

- 2026-09-16 created · [[decision-case-201.3]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L29
