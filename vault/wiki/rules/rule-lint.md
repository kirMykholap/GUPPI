---
type: rule
kind: Leaf
purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
status: built
enforcement: check
implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]
parent: rule-harness
estimates: [estimate-lint-catches]
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Purpose

Prevents a page that breaks its schema, points at nothing, or claims a status its
Estimates do not support from sitting in the vault unnoticed. Pages are written by hand
until the generator exists and by script after; both drift, and nothing else reads the
whole graph at once. `make lint` runs it after `render --check` and `index --check` over the four index files; all
three only report, so the Makefile's rule — no target writes to the tree — holds.

`parent: rule-harness` names the MOC of the harness tools: lint runs with the renderer and the indexes, in no phase of the session.

## How it works

`uv run guppi lint` reads every live page against its category's `schema.yaml`:
required fields and sections, legal statuses, `origin` as a grep target in `raw/`,
every ref (`parent`, `target`, `children`, `estimates`, `insight`) as an existing page,
orphans, a `built` page with an Estimate not `passed`, the two Method classes of
case 26.2. A decision page: at least one of `create`, `update`, `delete`, `defer`, each a list of slugs, and neither `kind` nor `target_slug`; every slug with a category prefix a live or archived page; every slug in `deferred_by` an existing decision page; a `[[decision-…]]` wikilink in a History line resolves to a page. A lesson needs no `estimates`; an estimate whose `target` is not an entity or a rule is a finding. It reports and exits 1 on any
finding, 0 with no output on a clean vault.

## Estimates

- [[estimate-lint-catches]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/lint.py`
- `tests/test_lint.py`
- `Makefile`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-09 updated: the Method check, a Leaf names a test file, a MOC a make target · raw/2026-09-09/ledger.md#case-26.2
- 2026-09-10 updated: the Method check, a MOC over hand-read children says by hand · raw/2026-09-10/ledger.md#case-28
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: the classes listed; decision pages: kind and target_slug of equal length, every vault target_slug an existing page · [[decision-case-52.1]]
- 2026-09-11 updated: deferred_by: every slug an existing decision page · [[decision-case-52.3]]
- 2026-09-11 updated: a History wikilink resolves to a page · [[decision-case-52.4]]
- 2026-09-11 updated: lessons: estimates not required; an estimate whose target is not an entity or rule is a finding · [[decision-case-53.1]]
- 2026-09-11 updated: index --check over four files · [[decision-case-53.4]]
- 2026-09-12 updated: decision pages checked on the four kind lists; a target resolves against live and archived pages (case 59.4) · [[decision-case-59.4]]
