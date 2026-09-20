---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: sprint, once it wrote sprint.md and exits 0, ticks the guppi sprint lines of every Spec under raw/ whose yaml is applied whole
method: pytest tests/test_sprint.py, plus one reading of this session's spec.md and the 1957 Spec after the librarian's run
checked: 2026-09-18
origin: raw/2026-09-18/2054/ledger.md#case-250.2
sprint: migration
created: 2026-09-18
tags: [harness, sprint]
---

## Criterion

Given:
`guppi sprint` without a flag writes `vault/wiki/sprint.md` and exits 0, or writes nothing and exits 1.
**＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied` or `superseded_by` and none `failed` (case 250.1); `carry.md` marks a carried-over unit.
**＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.

When:
`guppi sprint` without a flag wrote the file and exits 0.

Then:
In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi sprint` becomes `- [x]`; nothing else changes.
**－** A line where `guppi sprint` sits in a later code span — a `read` line, a description — is not ticked.
**－** `--check` ticks nothing; exit 1 ticks nothing.
**－** A unit without a yaml, with an unapplied or `failed` entry, or marked by `carry.md`, is not touched.

## Result

2026-09-18, pytest tests/test_sprint.py (3 tests of the tick, 429 green) and the librarian's `uv run guppi sprint` of commit 3e1251f: the `uv run guppi sprint` lines 37, 103, 137 of the 1957 Spec — a yaml with two `superseded_by` entries — and line 94 of the 2054 Spec ticked; the `read` line that names the command later, the page lines and the render lines untouched; `--check` and exit 1 tick nothing in the tests

## History

- 2026-09-18 created · [[decision-case-250.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-18/2253/ledger.md#L4
