---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: One bad entry never stops the run; every entry carries its mark
method: pytest tests/test_generate.py, the tests of the failed, skipped and marked entries
checked: 2026-09-24
origin: raw/2026-09-16/1955/ledger.md#case-201.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
---

## Criterion

When:
`uv run guppi generate` meets an entry of `materialize.yaml` it cannot apply, or one already handled.

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

2026-09-24, `uv run pytest tests/test_generate.py`: 87 passed

## History

- 2026-09-16 created · [[decision-case-201.3]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L29
- 2026-09-17 updated: one line in the Criterion — a recut without method fails alone (case 211.2) · [[decision-case-211.2]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L50
- 2026-09-21 updated: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295) · [[decision-case-295]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L4
- 2026-09-22 updated: no Rule-class branch in generate (case 320) · [[decision-case-320]]
- 2026-09-23 status: pending → failed · raw/2026-09-23/0034/ledger.md#L58
- 2026-09-23 updated: the message of an update with no content as the code prints it since case 320 (case 366) · [[decision-case-366]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L22
- 2026-09-25 updated: the Criterion replaced whole — Given out by the model of case 378, the When and Then as they stood (case 398.2) · [[decision-case-398.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L34
- 2026-09-29 updated: the Criterion replaced whole — a recut without method no longer fails (case 506.5) · [[decision-case-506.5]]
- 2026-09-29 updated: the Criterion replaced whole — an entry that repeats an applied entry of its Case, kind and slug is marked applied, changes no page and prints one line · [[decision-case-514]]
