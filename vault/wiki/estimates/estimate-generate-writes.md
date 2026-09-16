---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Every page of the vault comes through this script from Slice 3 on. A derived field computed wrong, or a ratified one dropped, is corrupted everywhere at once.

## Criterion

Against a temp vault from one yaml: a MOC rule create, a Leaf child create with ref
and its nested estimate yield three pages that pass their schema.yaml, the parent's children in order and the target's estimates, no section derived from either (case 174); a derived Estimate create yields a pending page with Context, Criterion as a ### case N block and Method, listed on its target; an update carrying a criterion block appends it to ## Criterion and sets pending, a removal deletes the block, each with its History line; an update with set, sections, replace and change changes the field, the section, the
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

### case 142.2

When:
`guppi generate` reaches an entry with `failed` and no `kind`.

Then:
The entry is skipped: not applied, `failed` kept as `materialize` wrote it, one line on stderr `generate: line N: not lifted by materialize; <message>`; exit 1; the other entries apply.
**－** An entry with `kind` and a stale `failed` of an earlier run is as today (53.3): applied, the mark dropped.

### case 151

When:
`guppi generate` reaches an entry with `superseded_by`.

Then:
The action of the entry is not done, stderr is empty, the exit code is not changed; the Decision page of its Case is written when it does not exist yet (`superseded`, the cascade — `archived`); `failed` and `superseded_by` on the entry stay as they are.
**＋** The rule's text: "An entry with `superseded_by` is not applied — a later Case did its work — and leaves no line; its Case's Decision page is still written, `superseded`, and archived by the cascade (case 151)."
**＋** Tests: an entry `failed` + `superseded_by` — no stderr, exit 0, the Decision page exists, the target untouched; an entry `superseded_by` without `applied` in one yaml with the superseding one — both Decision pages, the earlier `superseded`.
**＋** The librarian's run of this session: `generate` over `0747` is silent; 112.6 is out of the Flags.
**－** `materialize`, `archive`, `cleanup` do not change.

### case 166.2

When:
`guppi generate` writes a page of any category, or applies a yaml entry whose target is a page of `insights/`.

Then:
Neither at `create`, nor at `update`, nor in `save` does `generate` write `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code`, `## Insight` or `## Addressed by`; a section a page still carries is neither touched nor derived again on a write; `SECTION_ORDER` does not know them.
**＋** A `create` with `ref` still appends the slug to the parent's `children` or to the target's `estimates`, History `child <slug> added` / `estimate <slug> added`; an `update` with `set` on a field writes the field.
**＋** A `create` in `insights` marked `librarian` writes the page as any `create`: `status: open`, `severity` from the count of `children`, the entry's `origin`, `## Pattern` and `## Proposal` from the fields; History `created · <origin>`.
**＋** A `defer` with an Insight as its target appends the decision slug to its `deferred_by`; a `supersedes` removes it through `clear_deferred_by`.
**＋** An `update` with `set: {addressed_by: decision-case-N}` writes the field — and only the field.
**＋** An `update` with `set: {status: actioned}` goes as any `update`; the cascade of the same run archives the `clustered` children and recounts `severity`.
**－** A `create` in `insights` without the `librarian` mark is refused; a `delete` of an Insight is refused always.

### case 166.3

When:
The cascade of `guppi generate` runs after all entries.

Then:
The cascade does not walk the lessons for `## Insight`; a lesson's `insight` field is its one link to its Insight; the History line `insight section derived` is written no more.
**－** The other steps of the cascade — `built`/`draft`, the archive of a superseded decision, `severity`, the children of an `actioned` Insight, an Insight with no live child — as today.

### case 172

When:
`guppi generate` or `guppi cleanup` writes a page; a script reads a page through `pages.read_page` or `materialize.page_estimates`.

Then:
In the written frontmatter every value of a ref field that carries a category prefix is `"[[slug]]"`, a list `["[[a]]", "[[b]]"]`; the fields: `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by`; a slug without a category prefix stays as it was.
**＋** `read_page` and `page_estimates` strip `[[`/`]]` from these fields; a page without brackets reads the same.
**＋** In Obsidian the backlinks of an Insight are its lessons and its Decision; the backlinks of a Rule are its children, Estimates and Decisions; `unresolved` is empty.
**－** No CLI probe.

## Method

pytest in tests/test_generate.py against a temp vault; the live reading once by hand

## Result

2026-09-16, `pytest tests/test_generate.py`: 47 green, 186.1 — a defer with a purpose writes ## Deferred on the Decision page, one ### [[slug]] heading per target in the order of the defer list, the purpose verbatim and a multi-line one not collapsed, before ## History; a placeholder still gets its purpose field; a defer without a purpose writes no section; the one-off over decision-case-182, 183 and 185 from raw/2026-09-15/2225/materialize.yaml wrote 5, 2 and 1 headings

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
- 2026-09-14 criterion: case 142.2 added · [[decision-case-142.2]]
- 2026-09-14 criterion: case 148.1 added · [[decision-case-148.1]]
- 2026-09-14 criterion: case 151 added · [[decision-case-151]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L58
- 2026-09-15 criterion: case 124.2 removed · [[decision-case-164]]
- 2026-09-15 criterion: case 166.2 added · [[decision-case-166.2]]
- 2026-09-15 criterion: case 166.3 added · [[decision-case-166.3]]
- 2026-09-15 criterion: case 114 removed · [[decision-case-166.3]]
- 2026-09-15 criterion: case 172 added · [[decision-case-172]]
- 2026-09-15 criterion: case 148.1 removed · [[decision-case-172]]
- 2026-09-15 updated: head Criterion: no ## Children, no ## Estimates — the text of 166.2 (case 174) · [[decision-case-174]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L9
- 2026-09-16 status: passed → passed · raw/2026-09-16/1651/ledger.md#L37
