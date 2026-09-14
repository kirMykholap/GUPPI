---
type: estimate
kind: QA
status: passed
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Every page of the vault comes through this script from Slice 3 on. A derived field computed wrong, or a ratified one dropped, is corrupted everywhere at once.

## Criterion

Against a temp vault from one yaml: a MOC rule create, a Leaf child create with ref
and its nested estimate yield three pages that pass their schema.yaml, the parent's
children and ## Children in order, the target's estimates and ## Estimates; a derived Estimate create yields a pending page with Context, Criterion as a ### case N block and Method, listed on its target; an update carrying a criterion block appends it to ## Criterion and sets pending, a removal deletes the block, each with its History line; an update with set, sections, replace and change changes the field, the section, the
text and appends History; a replace absent or not unique fails that entry alone,
exit 1; a delete sets archived with History; a defer without a page writes a
placeholder with only the Case's fields and deferred_by, a defer with a page appends
the decision slug to its deferred_by, and a supersedes removes it; an estimate entry
sets status and overwrites ## Result whatever the page held; a lesson entry writes
the lesson and no Estimate; one decision page per Case with one list per kind present —
create, update, delete, defer, the slugs in ledger order — and the sections Context, Problem, Given, and Criterion links when the Case shaped an Estimate, no When, written before
the entries of its lines, and supersedes marks the earlier page superseded; History
and log lines of a Case's entries end with the decision wikilink, a reading's or a
lesson's with the ledger pointer; the cascade sets built; a declared new tag lands
in tags.md, an undeclared one is reported; log.md gains one line per write.
**＋** An entry whose field has a shape the script does not expect, or in which any
exception is raised, is marked failed, reported on stderr and skipped; the rest
apply; exit 1.
**＋** After each applied entry its lines are in log.md; a run that stops at entry N
leaves the feed level with the pages up to N.
**＋** History lines and log.md lines carry the date of the run; created carries the
yaml's date.
**＋** A delete whose slug is neither a category prefix nor a Rule-class file is
printed on stdout as outside the vault and marked applied; a delete of a missing
page with a category fails.
Applied entries are marked, a stale failed mark left by an earlier run is dropped on apply, and a rerun writes nothing; a create colliding with a
page not marked exists fails. Live: the yaml of the session's librarian run; the
reading records pages created per category, make lint afterwards against the
known-false list, and git diff --stat.

### case 101.1

When:
`uv run guppi generate` applies a `create` whose slug is a live page without `kind` and with `status: draft`.

Then:
The page is filled from the entry: fields and sections as for a new page, `origin` the create's, `created` kept, `deferred_by` kept (empty after the supersedes), History gains `created over placeholder · [[decision-case-N]]`.
**＋** The Estimate from `method` is created and written into `estimates`, as for any Leaf create.
**＋** Any other existing page is a collision, as today.
**＋** `estimate-generate-writes` gets a `### case 101.1` block, `pending`.

### case 104.1

When:
`uv run guppi generate` sets `superseded` on a decision page, or meets a decision with `status: superseded` in the cascade.

Then:
The page's status is `archived`; `superseded_by` and the History `superseded by [[X]]` as today, plus the History `archived · superseded`; `cleanup` takes it under the session of the run.
**＋** The cascade walks every decision page: the 24 `superseded` of today leave at the first run.
**＋** `estimate-generate-writes` gets a `### case 104.1` block, `pending`.
**－** `deferred_by`, the History wikilinks and the `supersedes` chain do not change: the slug is known in the archive.

### case 104.2

When:
In the cascade `generate` meets an Insight with `status: actioned`.

Then:
Every child of it with `status: clustered` gets `status: archived`, History `archived · insight actioned`; the Insight's `children` does not change.
**＋** A lesson synthesis adds later, returning the Insight to `open`, stays live; the children archived before stay archived.
**＋** `estimate-generate-writes` gets a `### case 104.2` block, `pending`.

### case 104.3

When:
In the cascade `generate` recounts the `severity` of an Insight with `status: open`.

Then:
`severity` 0 — every child `archived` — gives `status: archived`, History `archived · no live child`; `children` keeps the slugs.
**＋** `severity` 1 or more: as it is; the Insight stands on one live child.
**＋** `estimate-generate-writes` gets a `### case 104.3` block, `pending`.
**－** An `actioned` Insight with `severity` 0 is not archived: it is kept for the recurrence.

### case 105.3

When:
`uv run guppi generate` applies an `update` (or `estimate`, `delete`, `defer`) to a slug that is not under `wiki/`.

Then:
`find` looks for `<slug>.md` under `vault/archive/`, `raw/` folders excluded, and edits the page there: `set`, `sections`, `replace`, History — as for a live page.
**＋** `set: {status: <not archived>}` in the same entry — `cleanup` then brings the page back to `wiki/<category>/` with the History `restored · cleanup`.
**＋** `estimate-generate-writes` gets a `### case 105.3` block, `pending`.
**－** A slug in neither place: "no such page", as today.

### case 114

When:
`generate` writes a lesson page, or its cascade runs after all entries.

Then:
A lesson whose `insight` field is set gets `## Insight` holding `- [[<insight>]]`, rebuilt from the field on every write, before `## History`; a lesson without the field has no such section.
**＋** In the cascade every live lesson with `insight` set and no `## Insight` section, or one that names another slug, is rewritten with the section and History `insight section derived`; the 22 pages are filled at the next librarian run.
**＋** `estimate-generate-writes` gets a `### case 114` block, `pending`; a test in `tests/test_generate.py`: an `update` with `set: {status: clustered, insight: insight-x}` yields the section; a live lesson with the field and no section gets it in the cascade.
**＋** `guppi lint` after the run shows the 22 `## Insight` findings gone.
**－** `{supersedes:case 108}`: `decision-case-108` is superseded, `rule-synthesis` loses `deferred_by`.

### case 124.2

When:
`guppi generate` applies a yaml entry whose target is a page of `insights/`.

Then:
A `defer` with an Insight as its target appends the decision slug to its `deferred_by`, as for a Rule; `KEY_ORDER["insights"]` gains `deferred_by` after `addressed_by`; a `supersedes` removes it through the same `clear_deferred_by`.
**＋** An `update` with `set: {addressed_by: decision-case-N}` writes the field, and on every write of an Insight page the `## Addressed by` section is derived from the field — `- [[decision-case-N]]` — as a lesson's `## Insight` is from `insight` (114); without the field there is no section.
**＋** An `update` with `set: {status: actioned}` goes as any `update`; the cascade of the same run archives the `clustered` children (104.2) and recounts `severity`.
**＋** `estimate-generate-writes` gets a `### case 124.2` block, `pending`; the test: a `defer` on an insight → `deferred_by` written and shown in `insights-index.md`; an `update` with `addressed_by` and `status: actioned` → `## Addressed by` with the link, the children `archived`; a `supersedes` clears `deferred_by`.
**－** An Insight is neither created nor deleted through the yaml: a `create` or `delete` with an Insight as its target is a `generate` error, as today.

## Method

pytest in tests/test_generate.py against a temp vault; the live reading once by hand

## Result

block 124.2 against tests/test_generate.py: a defer on an insight writes deferred_by and insights-index.md shows it; an update with addressed_by and status actioned writes ## Addressed by with the link and the cascade archives the clustered child, severity 0; a supersedes clears deferred_by; a create or delete of an insight is an error

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L71
- 2026-09-11 updated: the criteria of the four Estimates of Cases 47–48 folded in; no skip, no paired estimate, the decision-page shape and deferred_by of Case 52; pending until the End of Work reading · [[decision-case-53.2]]
- 2026-09-11 updated: criterion: a stale failed mark is dropped on apply (case 53.3) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L76
- 2026-09-12 updated: the decision page's four lists replace the aligned pair in the criterion (case 59.4) · [[decision-case-59.4]]
- 2026-09-12 updated: the derived Estimate page and the decision page's Criterion links join the criterion (case 72.4); pending until the unit reading · [[decision-case-72.4]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L167
- 2026-09-13 criterion: case 101.1 added · [[decision-case-101.1]]
- 2026-09-13 criterion: case 104.1 added · [[decision-case-104.1]]
- 2026-09-13 criterion: case 104.2 added · [[decision-case-104.2]]
- 2026-09-13 criterion: case 104.3 added · [[decision-case-104.3]]
- 2026-09-13 criterion: case 105.3 added · [[decision-case-105.3]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L1
- 2026-09-14 criterion: case 114 added · [[decision-case-114]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L46
- 2026-09-14 criterion: case 124.2 added · [[decision-case-124.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L33
