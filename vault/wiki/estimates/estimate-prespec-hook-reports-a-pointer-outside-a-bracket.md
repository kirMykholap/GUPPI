---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: "Whether the check of the plan finds a pointer to a case, a decision or a session that stands outside a bracket of its own in the new text of a page with core: true, or of an Estimate whose target carries core: true, its method and its new Criterion included"
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k pointer
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, ci]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

Then:
It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
**＋** It prints the same finding for an item of an Estimate whose target, the `ref` of a `create` or the `target` of the live page, carries `core: true` on the live page or as the plan leaves it: in its `purpose`, its `method`, each `sections` value it writes and its new `## Criterion`.
**＋** The new `## Criterion` of such an Estimate is the one the item writes under `sections`, else the `when` and `then` of its Case, for a `create` and for an `update` that names no part of the page, read by the one function of `.guppi/guppi/prespec.py` by which the note on a Criterion line not carried reads it.
**＋** The finding names the Case, the page and the pointer.
**＋** It judges each text by `outside` of `.guppi/guppi/pointers.py`, imported.
**－** A pointer inside such a bracket, a code span or a fenced block is no finding.
**－** An item for a page without `core: true` that is no such Estimate, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
