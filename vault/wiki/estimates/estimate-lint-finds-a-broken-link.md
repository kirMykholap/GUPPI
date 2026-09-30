---
type: estimate
kind: QA
status: pending
target: "[[rule-lint]]"
purpose: A link, an origin or a Decision list that names nothing, and a page nothing names, are findings of lint
method: uv run pytest tests/test_lint.py
checked: 2026-09-29
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
**＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate.
**＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
**＋** An `origin` `#case-N` of a Case that has no ledger line of its own is found by a line of one of its sub-cases, `[case N.M]`.
**＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer` and no `children`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
**＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
**－** A `### case N` line under an Estimate's `## Criterion` is not read as a link.

## Result

2026-09-29, uv run pytest tests/test_lint.py: 78 passed; make lint of Work Mode in session 1432 prints one link-class finding, the orphan rule-spec-box, a live rule no other page names, and no ref, origin or decision finding

## History

- 2026-09-25 created · [[decision-case-401.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L43
- 2026-09-27 updated: the Criterion replaced whole — the prefixes of a Decision list are judged by category_of of guppi/materialize.py, decision- included (case 460.3) · [[decision-case-460.3]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L20
- 2026-09-29 updated: the Criterion replaced whole — no ### case N block of an Estimate followed (case 506.4) · [[decision-case-506.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L26
- 2026-09-30 updated: the Criterion replaced whole — the page of a parent Case: children in place of the kind lists, its origin found by a line of a sub-case (case 544.9) · [[decision-case-544.9]]
