---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: glossary, once it wrote glossary.md and exits 0, ticks the guppi glossary lines of every Spec under raw/ whose yaml is applied whole
method: pytest tests/test_glossary.py, plus one reading of this session's spec.md after the librarian's run
origin: raw/2026-09-22/0014/ledger.md#case-306.6
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

Given:
`rule-sprint`: a `check` rule with `governs`; the script writes the file from a page, `--check` compares in memory, writes nothing, exit 1 on a difference; once it wrote the file it ticks its Spec lines (250.2).
**＋** `rule-governed-files-hook` refuses a hand edit of `governs`.
**＋** Case 240.1: a MOC is a thing whose parts the person named as built; a Leaf is not, and a Leaf carries `parent`. Case 240.2: the guard of an Entity is a separate Rule — the edge `applies_to` (305).
**＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole.
**＋** `tests/test_glossary.py` fixes the behaviour on a temp vault.

When:
`uv run guppi glossary` wrote the file and exits 0.

Then:
In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi glossary` becomes `- [x]`; `--check` and an exit 1 tick nothing.
**＋** The Case schema names the fourth ticker and the form of the line `- [ ] `uv run guppi glossary``.

## Result

2026-09-22, uv run pytest tests/test_glossary.py, 8 passed: the plain run ticks the unticked task lines opening with a code span holding guppi glossary in the spec.md of an applied unit, leaves a read line naming the command later, a sprint line and an unapplied unit alone; --check ticks nothing; the live reading of this session's spec.md after the librarian's run not taken

## History

- 2026-09-22 created · [[decision-case-306.6]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L63
