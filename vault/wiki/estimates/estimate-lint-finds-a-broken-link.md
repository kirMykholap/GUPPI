---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: A link, an origin or a Decision list that names nothing, and a page nothing names, are findings of lint
method: uv run pytest tests/test_lint.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-401.2
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

Then:
`ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
**＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
**＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate; a `### case N` block under an Estimate's `## Criterion` with no live or archived `decision-case-N`.
**＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
**＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug`; a slug of its lists with a category prefix that no live or archived page carries.
**＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.

## Result

2026-09-24, `uv run pytest tests/test_lint.py`: 69 passed

## History

- 2026-09-25 created · [[decision-case-401.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L43
