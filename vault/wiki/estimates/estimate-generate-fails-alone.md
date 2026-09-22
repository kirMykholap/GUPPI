---
type: estimate
kind: QA
status: failed
target: "[[rule-page-generation]]"
purpose: One bad entry never stops the run; every entry carries its mark
method: pytest tests/test_generate.py, the tests of the failed, skipped and marked entries
checked: 2026-09-23
origin: raw/2026-09-16/1955/ledger.md#case-201.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
---

## Criterion

Given:
`guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
**＋** An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
**＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `materialize`, `cleanup` and `lint` do not change here.

When:
`guppi generate` meets an entry it cannot apply, or one already handled.

Then:
An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
**＋** An `update` with `sections.Criterion` on an Estimate page without a `method` field, whose `set` carries no `method`, fails the same way: `generate: <slug>: a recut without method (case 211)`; a page with the field takes the Criterion as before (case 211.2).
**＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
**＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
**＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
**＋** An `update` with no content prints `an update with no content in the Spec; applied by hand` and is marked applied.
**－** The failure of one entry changes no other page: `log.md` after it is level with the pages.

## Result

2026-09-23, uv run pytest tests/test_generate.py: 85 passed, 23 selected by -k "fail or skip or mark or superseded or rerun or stale"; but the Criterion's line "An update with no content prints `an update with no content in the Spec; applied by hand`" does not hold: guppi/generate.py:763 prints "an update with no content in the Spec; nothing applied" (the words since case 320), and no test asserts the message — the Criterion is stale, not the code

## History

- 2026-09-16 created · [[decision-case-201.3]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L29
- 2026-09-17 updated: one line in the Criterion — a recut without method fails alone (case 211.2) · [[decision-case-211.2]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L50
- 2026-09-21 updated: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295) · [[decision-case-295]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L4
- 2026-09-22 updated: no Rule-class branch in generate (case 320) · [[decision-case-320]]
- 2026-09-23 status: pending → failed · raw/2026-09-23/0034/ledger.md#L58
