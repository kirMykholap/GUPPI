---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec refuses an item that writes a Render without the page's own markers
method: pytest in .guppi/tests/test_prespec.py — a create and an update with an unwrapped Render, a wrapped one clean
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks that carry `sections: Render`.

Then:
An item whose target is a page with `enforcement: render`, and whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->` of its own slug, gives one line `case N: <create|update> <slug>: Render is not wrapped in`, followed by the two markers of that slug.
**＋** In a `create` the `enforcement` of the target is read from the item itself, and in an `update` from the page.
**＋** The check judges only the text the item itself writes, and does not simulate the Spec in entry order.
**＋** A target without `enforcement: render` gives no finding.
**＋** A wrapped text is silent; exit 0 on a clean plan stands.
**－** The child's marker line in the parent is not checked here: its true value is known only after every item of the Spec is applied.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
