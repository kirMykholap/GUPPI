---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
checked: 2026-09-16
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Context

Lint is the first reader of the whole graph. The unit cases seed one page per defect
class and pin the finding each produces; the live reading is the first pass over the
pages written by hand since Slice 0, whose findings are the debt the brief carries.

## Criterion

Given:
`guppi lint` reads every live page of `wiki/<category>/` against the category's `schema.yaml` and writes nothing.
**＋** `estimates/schema.yaml` (193): `purpose`, `method`, `checked` are optional fields; `## Context`, `## Method` optional sections; `## Result` required on `passed` and `failed`.
**＋** The tests in `tests/test_lint.py` fix the behaviour, one per class; the live reading is `make lint` in the librarian's run of this session.
**－** `render --check` and the Makefile do not change.

When:
`uv run guppi lint` reads the live pages of the vault.

Then:
Every live page is checked against the `schema.yaml` of its category; one line per finding, `<category>/<slug>: <class>: <what>`; exit 1 on any finding, 0 and no output on a clean vault; nothing is written.
**＋** `schema`: a missing required field or section, a value outside the list, a conditional not met; `## When` is never required on a Decision page; `schema-prose`: `schema.md` and `schema.yaml` naming different fields or sections.
**＋** `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by` or in a History wikilink that no live or archived page carries; a `[[…]]` in a body may name a hub file under `wiki/` by stem or path; a `[[slug]]` under a Decision page's `## Criterion` that is no Estimate; a `### case N` block of an Estimate with no decision page.
**＋** `origin`: both forms resolve in `raw/` or in `vault/archive/`; in neither, or in both, a finding.
**＋** `path`: a file of `implementation_ref` or `governs` that does not exist.
**＋** `orphan`: a live entity, rule or estimate that no live page's frontmatter names; a lesson and an Insight never.
**＋** `status`: `built` with an Estimate not `passed`, `draft` with every one `passed`; an Estimate `passed` or `failed` without `## Result`; an Estimate whose target is not an entity or a rule, or does not list it in `estimates`.
**＋** `unread`: every Estimate `pending` or `failed` — one finding each, `unread: <status>`; red between a change of a promise and its reading, by design.
**＋** `method`: the `method` field, or on a page of the old shape the `## Method` section; for a MOC's Estimate a named `make <target>` of the Makefile passes whatever stands beside it, without one `by hand` passes only when the Estimates of every child are by hand; for a Leaf's Estimate a `tests/` file that exists, the word `pytest`, a `make <target>` of the Makefile or a reading (`by hand`, `reading`); else a finding.
**＋** `decision`: a decision page with none of the four lists, or with `kind`/`target_slug`; a listed slug with a category prefix and no page.
**＋** `deferred`: a placeholder earns one finding `deferred: <N> times since case <M>` in place of its `schema` and `orphan` findings; a page with `deferred_by` whose fields are in place earns none.
**＋** `unmigrated`: one line, `estimates: unmigrated: <N> pages in the shape before case 193` — the live Estimates without a `method` field, or with `## Context`, `## Method` or a `### case N` block; no line at zero.
**－** `make lint` runs it after `render --check`; neither writes.
**－** The checks of the old shape — `## Method` as a section, the `### case N` blocks — leave by a separate `update` of this rule once the counter reads zero; not this Case.

## Method

pytest in `tests/test_lint.py`, one test per defect class; the live reading once by hand,
written into the estimate line.

## Result

2026-09-16, `pytest tests/test_lint.py`: 54 green — unread on pending and failed, the method field read with a test path, pytest, a make target or a reading passing, the ## Method section read on a page of the old shape, unmigrated as one line and none at zero; live, `make lint`: 77 findings — 62 of Cases 1–28, 2 deferred, 10 unread, 1 method (estimate-plan-mode-names-its-estimates says by hand while estimate-spec-capture-offers-the-fork names a test file — new, the MOC rule of 112.1 now reads the field), `estimates: unmigrated: 42 pages in the shape before case 193`; the body [[slug]] finding on estimate-generate-writes leaves with its recut

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-09 updated: criterion gains the two Method defect classes · raw/2026-09-09/ledger.md#case-26.2
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: the classes of cases 52 and 53 seeded; a lesson without estimates is clean; pending until the suite · [[decision-case-57]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L69
- 2026-09-12 updated: the decision classes of case 59.4 replace those of 52.1 in the criterion · [[decision-case-59.4]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L98
- 2026-09-12 updated: the two shapes of case 72.6 join the criterion; pending until the unit reading · [[decision-case-72.6]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L159
- 2026-09-13 criterion: case 100.3 added · [[decision-case-100.3]]
- 2026-09-13 criterion: case 103.5 added · [[decision-case-103.5]]
- 2026-09-13 criterion: case 100.3 removed · [[decision-case-103.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/0652/ledger.md#L2
- 2026-09-14 criterion: case 112.1 added · [[decision-case-112.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L47
- 2026-09-14 criterion: case 149.3 added · [[decision-case-149.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L1
- 2026-09-15 criterion: case 156 added · [[decision-case-156]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L24
- 2026-09-16 status: passed → passed · raw/2026-09-16/1651/ledger.md#L38
- 2026-09-16 updated: the Criterion replaced whole by case 202 — the head and the blocks 103.5, 112.1, 149.3, 156 recut into one, with unread, the method field and unmigrated (case 202) · [[decision-case-202]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L32
