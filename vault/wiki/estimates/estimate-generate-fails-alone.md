---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: One bad entry never stops the run; every entry carries its mark
method: pytest .guppi/tests/test_generate.py, the tests of the failed, skipped and marked entries
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger, tests]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi generate` meets an entry of `materialize.yaml` it cannot apply, or one already handled.

Then:
An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
**＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
**＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
**＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
**＋** An `update` with no content prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, changes no page and is marked applied.
**＋** A `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` marked `applied` is marked `applied`, loses a stale `failed` mark, changes no page, appends nothing to `vault/wiki/log.md` and prints `generate: <slug>: line N repeats line M of case C; nothing applied` on stdout, whichever of the two lines stands first in the ledger.
**－** The failure of one entry changes no other page: `vault/wiki/log.md` after it is level with the pages.
**－** An `update` with `sections.Criterion` on an Estimate page does not fail for want of a `method` field.
**－** An `estimate` or a `lesson` entry is never taken for a repeat: it carries no `case`.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
