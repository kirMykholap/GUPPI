---
type: rule
kind: Leaf
purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
status: built
enforcement: check
implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]
parent: "[[rule-harness]]"
estimates: ["[[estimate-lint-catches]]"]
deferred_by: ["[[decision-case-182]]"]
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Purpose

Prevents a page that breaks its schema, points at nothing, or claims a status its
Estimates do not support from sitting in the vault unnoticed. Pages are written by hand
until the generator exists and by script after; both drift, and nothing else reads the
whole graph at once. `make lint` runs it after `render --check`; both only report, so the Makefile's rule — no target writes to the tree — holds (case 147.7).

`parent: rule-harness` names the MOC of the harness tools: lint runs with the renderer, in no phase of the session.

## How it works

`uv run guppi lint` reads every live page against its category's `schema.yaml`:
required fields and sections, legal statuses, `origin` as a grep target — `raw/<date>/ledger.md#…` at `vault/raw/<date>/ledger.md` or `vault/archive/*/<date>/raw/ledger.md`, `raw/<date>/<HHMM>/ledger.md#…` at `vault/raw/<date>/<HHMM>/ledger.md` or `vault/archive/*/<date>/<HHMM>/raw/ledger.md`; in neither place or in both a finding (case 103.5) —
every ref (`parent`, `target`, `children`, `estimates`, `insight`) as an existing page, a `[[…]]` in a body as a live or archived page, or as a file under `vault/wiki/` by its stem (`brief`, `index`, `glossary`, `case-schema`, `sprint`, `tags`, `log`) or its path (`rules/schema`) (case 149.3),
orphans (a live entity, rule or estimate no other live page names in its frontmatter; a lesson is a record and an Insight names it or not; an Insight owns its children through `children` and is named by no live page once they are archived — neither is one, case 156), a `built` page with an Estimate not `passed`, the two Method classes of case 26.2 — for a MOC's Estimate the `make <target>` is looked for first and a Method that names one passes whatever else it says; "by hand" is judged only when no target is named (case 112.1). A decision page: at least one of `create`, `update`, `delete`, `defer`, each a list of slugs, and neither `kind` nor `target_slug`; every slug with a category prefix a live or archived page; every slug in `deferred_by` an existing decision page; a `[[decision-…]]` wikilink in a History line resolves to a page; `## When` is not required (case 72.6), and every link under `## Criterion` resolves to an Estimate page. An Estimate's `## Criterion` may hold `### case N` blocks; each `case N` names an existing decision page. A lesson needs no `estimates`; an estimate whose `target` is not an entity or a rule is a finding. It reports and exits 1 on any
finding, 0 with no output on a clean vault.

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
- 2026-09-12 updated: no When required on a decision page; Criterion links and ### case N blocks resolve (case 72.6) · [[decision-case-72.6]]
- 2026-09-13 updated: origin resolves in raw/ or the archive (case 100.3, superseded by 103.5 which carries the wording) · [[decision-case-100.3]]
- 2026-09-13 updated: both forms of origin resolve in raw/ or vault/archive/; archived slugs come from vault/archive/ outside raw/ folders; supersedes case 100.3 (case 103.5) · [[decision-case-103.5]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: the Method check of a MOC's Estimate looks for the make target before the words by hand (case 112.1) · [[decision-case-112.1]]
- 2026-09-14 deferred · [[decision-case-146]]
- 2026-09-14 updated: make lint has two steps; no index --check (case 147.7) · [[decision-case-147.7]]
- 2026-09-14 updated: a body wikilink may name a hub file under wiki/ by stem or path (case 149.3) · [[decision-case-149.3]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 defer by decision-case-146 superseded · [[decision-case-156]]
- 2026-09-15 updated: an Insight is never an orphan: its owners are its children, named in its own children field, live or archived; supersedes case 146 (case 156) · [[decision-case-156]]
- 2026-09-15 status: draft → built · cascade
- 2026-09-16 deferred · [[decision-case-182]]
