---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec refuses an item that writes a Render without the page's own markers
method: pytest in tests/test_prespec.py — a create and an update with an unwrapped Render, a wrapped one clean
checked: 2026-09-22
origin: raw/2026-09-22/1724/ledger.md#case-325.1
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

Given:
`check_form` already reads the items of the plan's `then` blocks and knows `live_page` and `read_category`: it can read the target page.
**＋** In a `create` the fields `enforcement` and `render_mode` stand in the item itself; in an `update` they are read from the page.
**＋** The check judges only the text the item itself writes, and does not simulate the Spec in entry order.
**＋** `rule-prespec` carries `enforcement: render` and renders `.claude/skills/pre-spec/SKILL.md`; the new finding belongs in its Render.

When:
`uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

Then:
An item of a `then` block carrying `sections: Render`, whose target is a page with `enforcement: render`, whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->`, gives one line: `case N: <create|update> <slug>: Render is not wrapped in <!-- slug --> … <!-- /slug -->`.
**＋** A target without `enforcement: render` gives no finding.
**＋** A wrapped text is silent; exit 0 on a clean plan stands.
**－** The child's marker line in the parent is not checked here: its true value is known only after every item of the Spec is applied.

## Result

2026-09-22, uv run pytest tests/test_prespec.py -k "markers or wrapped": 3 passed — an update writing an unwrapped Render on a page with `enforcement: render` gives `case 1: update rule-x: Render is not wrapped in <!-- rule-x --> … <!-- /rule-x -->`, a create carrying the field in the item itself gives the same for its own slug, a wrapped text and a target that does not enforce by render are both clean

## History

- 2026-09-23 created · [[decision-case-325.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-22/2046/ledger.md#L34
