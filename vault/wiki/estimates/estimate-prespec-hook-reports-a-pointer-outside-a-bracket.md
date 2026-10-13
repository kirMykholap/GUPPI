---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: "Whether the check of the plan finds a pointer to a case, a decision or a session that stands outside a bracket of its own in the new text of a page with core: true"
method: uv run pytest tests/test_prespec.py -k pointer
origin: raw/2026-10-13/2118/ledger.md#case-807.4
sprint: plugin
created: 2026-10-13
tags: [harness, ci]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

Then:
It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
**＋** The finding names the Case, the page and the pointer.
**＋** It judges each text by the judgment that `guppi ship` runs over the files it writes, imported from `guppi/ship.py`.
**－** A pointer inside such a bracket, a code span or a fenced block is no finding.
**－** An item for a page without `core: true`, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

## Result

2026-10-14, uv run pytest tests/test_prespec.py -k pointer: 6 passed — a pointer outside a bracket in a replace new, a sections value and a set purpose of a core page is a finding naming the Case, the page and the pointer; prespec.outside is ship.outside; a bracket, a code span and a fence give none; a page without core, set core false and the change line are not judged; the context of a Case is not judged and --check prints the one finding

## History

- 2026-10-14 created · [[decision-case-807.4]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L23
