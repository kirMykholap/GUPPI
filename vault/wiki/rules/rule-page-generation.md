---
type: rule
kind: Leaf
purpose: Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified
status: built
enforcement: check
implementation_ref: [guppi/generate.py, tests/test_generate.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-generate-writes]]", "[[estimate-generate-walks-dates]]"]
deferred_by: ["[[decision-case-191]]"]
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Purpose

Prevents a ratified decision from ending the session without a page, or a page from
carrying a field nobody ratified. The script is the only writer to `wiki/`. It lays
the content of `materialize.yaml` into schema fields, derives what is derivable and
writes nothing else. A page is always created, even incomplete: red lint is an
accurate signal of debt, a decision with no page is the ledger and the vault
disagreeing silently. A slug collision is an error, never a rename — with one exception: a `create` whose slug is a placeholder page, `status: draft` and no `kind`, fills that page (case 101.1).

## How it works

`uv run guppi generate [--date]` applies the entries of every `materialize.yaml` under `raw/` — the date-level one of a date first, then `raw/<date>/<HHMM>/materialize.yaml` per session in folder order, dates ascending (case 103.3) — each in order, the Decision page of a Case written before the first entry of its lines, and marks each applied entry `applied: <time>` in the yaml and drops a `failed` mark an earlier run left on it, so a rerun writes nothing and no reader of the yaml sees a failure that is over. Without `--date` it walks every `raw/<date>/` that holds a yaml, in
date order; a date with no unapplied entry changes nothing; a failure on one date is
reported and the walk goes on, with exit 1 at the end. An `update`, `estimate`, `delete` or `defer` whose slug is not under `wiki/` reaches the page under `vault/archive/` (`raw/` folders excluded) and edits it there; with a `status` other than `archived` in the same entry, `cleanup` brings it back (case 105.3). An entry that fails — a collision, a `ref` naming no page, a
`replace` whose text is absent or not unique, a field whose shape the script does not
expect, any exception raised while applying it — is reported on stderr, marked
`failed` and skipped; the rest apply; the exit code is 1. No entry ends the run. An entry with `superseded_by` is not applied — a later Case did its work — and leaves no line; its Case's Decision page is still written, `superseded`, and archived by the cascade (case 151). An entry with `failed` and no `kind` — a line `materialize` could not lift (case 142.1) — is skipped with its mark kept and one stderr line, `generate: line N: not lifted by materialize; <message>`; the exit code is 1 (case 142.2).

Initial `status` by category: entity and rule `draft`, estimate `pending`, lesson
`new`, insight `open`, decision `current`. `sprint` is the first `## <id>` heading
of `sprint.md`; `created` is the yaml's date; History lines and `log.md` lines carry
the date of the run. A ref field — `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, and on a Decision page `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by` — is written as a quoted wikilink, `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`, so Obsidian's graph, backlinks and Bases see the structure; a slug without a category prefix (a Rule-class file in a Decision list) stays bare. `pages.read_page` and `materialize.page_estimates` strip the brackets on read, so every reader sees the slug; a page written without brackets reads the same (case 148.1, restated by 172 without the body sections). Body sections follow the order of the category's `schema.yaml`: `Purpose` from `sections` or the `purpose` line; `Render`, `How it works`, `Context`, `Criterion`, `Method`, `Result`, `Trigger`, `Root cause`, `Pattern`, `Proposal` from `sections` or the estimate's fields. No section is derived from a ref field: `estimates`, `children`, `parent`, `implementation_ref`, `code_ref`, `insight` and `addressed_by` are the link, seen by Obsidian since 148.1, and a section a page still carries is left as it is (case 166.2). A field or section the entry lacks is not written: lint names it.

History lines: `created`, `updated: <change>`, `status: a → b`, `deleted`, `deferred`, `child <slug> added`, `estimate <slug> added`, each `· [[decision-case-N]]` when the entry belongs to a Case and `· <origin>` (the ledger pointer) when it is a reading or a lesson;
`log.md` gets the same line with `<category>/<slug>` in front, appended after each
entry, so a run that stops leaves the feed level with the pages. A `create` with `ref` appends the slug to the parent's `children` (order kept) or, for an estimate, to the target's `estimates`; a lesson's `insight` field is its one link to its Insight, and the cascade derives no section from it (case 166.3, supersedes 114); an `update` that sets `addressed_by` writes the field, and an `update` that sets `status: actioned` goes as any update, the cascade of the same run archiving the `clustered` children and recounting `severity` (case 124.2); a derived Estimate create (case 72.3) writes the page `pending` with Context, Criterion and Method and no Result, and is listed on its target the same way. An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace-collapsed match, exactly one occurrence), and appends History; an update carrying `criterion_block` appends the block to `## Criterion`, History `criterion: case N added`; a `remove_criterion` entry deletes the `### case N` block, History `criterion: case N removed` (case 72.4). An `estimate` entry sets `status`, overwrites `## Result` and appends History, whatever the page held before: a reading always lands, and reruns are held off by the `applied` marks alone. A `delete` sets `status: archived`
with History `deleted`; there is no `deleted` status. A `delete` whose slug is neither
a category prefix nor a Rule-class file (`category: unknown` in the yaml) names
something outside the vault: it is printed on stdout as `outside the vault, nothing to
archive` and marked applied, no page is written; a `delete` with a category and no
page fails. A `defer` with a page appends History `deferred` and the decision slug to its `deferred_by` — a Rule, an Entity or an Insight (case 124.2); without one it writes a placeholder page, `status: draft`, with only the fields the Case gave and `deferred_by`. Either way the entry's `purpose` is written to the Case's Decision page under `## Deferred`, so the body of a deferred decision is never dropped (case 186.1). A later `create` of that slug fills the placeholder: fields and sections as for a new page, `origin` the create's, `created` and `deferred_by` kept, History `created over placeholder`; its Estimate is made from `method` as for any Leaf. Any other existing page is a collision (case 101.1). A `create` in `insights/` from a ledger line is refused — an Insight is made by the librarian, never by a decision; a `create` the librarian appended at synthesis, marked `librarian`, applies as any create, its `origin` the lesson line it grew from; a `delete` of an Insight is refused always: the cascade archives it (case 171, the text of 164; supersedes 124.2).

A lesson entry writes the lesson only: a lesson is a recorded fact and has no Estimate. A missing `source` is not invented; lint names it.

One Decision page per Case, `decisions/decision-case-<N>.md`: `case`, `status: current`, one list per kind present among the Case's ledger lines — `create`, `update`, `delete`, `defer`, in that order, each the slugs of those lines in ledger order (the category is derived from the slug prefix or the Rule-class map, never written), `source` when a line carries one, `supersedes`, `origin`, `sprint`, `created`, `tags` (the union of the targets' tags); body `Context`, `Problem`, `Given` from `case_text`, `Criterion` — one `[[estimate-x]] § case N` line per Estimate the Case shaped — when the entry carries `criterion`, and `Deferred` — one `### [[slug]]` heading per target of the Case's `defer` lines, in that order, each followed by that target's `purpose` verbatim, however long, and written for a defer with a `ref` and for a placeholder alike (case 186.1); no `When` (case 72.4; pages written before keep theirs). A `supersedes` sets the earlier page `status: superseded`, appends the new slug to its `superseded_by`, and removes the earlier decision's slug from the `deferred_by` of every target in its `defer` list; an empty `deferred_by` is dropped. A decision page that exists is
skipped. A `create` marked `exists` writes no page and no History; its decision
page is still written.

After all entries: an entity or rule whose Estimates are all `passed` becomes
`built`, a `built` one with an Estimate not passed returns to `draft`, both with a
History line; a decision page with `status: superseded` — the one a supersedes just set, or any met in the walk — becomes `archived` with the History `archived · superseded`, its `superseded_by` and `deferred_by` untouched (case 104.1); the `severity` of every insight is recounted, the status of a child read from its page under `wiki/lessons/` or, failing that, under `vault/archive/` the way `find` reaches a page, a child with no page anywhere counted live (case 110); every `clustered` child of an `actioned` insight becomes `archived` with the History `archived · insight actioned`, the insight's `children` unchanged (case 104.2); an `open` insight whose recounted `severity` is 0 becomes `archived` with the History `archived · no live child`, its `children` kept; an `actioned` one at 0 stays, kept for the recurrence (case 104.3). A tag declared in
`new_tags` is appended to `tags.md` with its meaning and aliases; a tag used but not
declared and not registered is reported on stderr and left on the page.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 estimate estimate-generate-writes added · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: draft → built · cascade
- 2026-09-10 updated: without --date the script walks every raw/<date> with a yaml, applying what is not yet applied · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 estimate estimate-generate-walks-dates added · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: built → draft · cascade
- 2026-09-10 updated: an entry fails alone whatever the cause; log.md is appended per entry; History and log carry the run's date, created the yaml's · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 estimate estimate-generate-rejects-shape-alone added · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 estimate estimate-generate-logs-per-entry added · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 estimate estimate-generate-dates-history-by-run added · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 updated: a delete of something outside the vault (category unknown) applies with a stdout line; a delete of a missing page still fails · raw/2026-09-10/ledger.md#case-48
- 2026-09-10 estimate estimate-generate-passes-delete-outside-vault added · raw/2026-09-10/ledger.md#case-48
- 2026-09-11 updated: a decision page carries kind and target_slug lists and the sections Context, Problem, Given, When from case_text · [[decision-case-52.1]]
- 2026-09-11 updated: a defer with a page appends the decision slug to deferred_by; a placeholder is born with it; a supersedes removes the superseded decision from the list · [[decision-case-52.3]]
- 2026-09-11 updated: the decision page of a Case is written before its entries; History and log lines end with `· [[decision-case-N]]` when a decision exists, else the ledger pointer · [[decision-case-52.4]]
- 2026-09-11 status: draft → built · cascade
- 2026-09-11 updated: a lesson entry writes the lesson only; no paired Estimate · [[decision-case-53.1]]
- 2026-09-11 updated: an estimate entry always sets status, overwrites Result and appends History; no skip · [[decision-case-53.2]]
- 2026-09-11 updated: an entry that applies loses a failed mark left by an earlier run · [[decision-case-53.3]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-11 estimate estimate-generate-rejects-shape-alone archived · cleanup
- 2026-09-11 estimate estimate-generate-logs-per-entry archived · cleanup
- 2026-09-11 estimate estimate-generate-dates-history-by-run archived · cleanup
- 2026-09-11 estimate estimate-generate-passes-delete-outside-vault archived · cleanup
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: a decision page names its targets by kind — one list per kind present — instead of two lists aligned by position (case 59.4) · [[decision-case-59.4]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 updated: the derived Estimate page, the criterion block appended or removed, the decision page's Criterion links and no When (case 72.4) · [[decision-case-72.4]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-13 updated: a create over a placeholder fills it; any other existing page stays a collision (case 101.1) · [[decision-case-101.1]]
- 2026-09-13 updated: the walk covers the yaml of every session folder as well as the date-level yaml (case 103.3) · [[decision-case-103.3]]
- 2026-09-13 updated: a superseded decision is archived by the cascade (case 104.1) · [[decision-case-104.1]]
- 2026-09-13 updated: the clustered lessons of an actioned Insight are archived by the cascade (case 104.2) · [[decision-case-104.2]]
- 2026-09-13 updated: an open Insight with no live child is archived by the cascade; supersedes case 97 (case 104.3) · [[decision-case-104.3]]
- 2026-09-13 updated: an update reaches an archived page in the archive, so a restore and its fix are one entry (case 105.3) · [[decision-case-105.3]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 updated: the cascade reads a child's status in the archive too, so an archived child is not counted live (case 110) · [[decision-case-110]]
- 2026-09-14 updated: the cascade derives the ## Insight section of every clustered lesson from its insight field (case 114) · [[decision-case-114]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: a defer marks an Insight deferred_by like a Rule, and the Addressed by section of an Insight is derived from addressed_by (case 124.2) · [[decision-case-124.2]]
- 2026-09-14 updated: the literal decision-case-N of the History line of 2026-09-11 and of the Given of decision-case-112.1–112.6 quoted by hand, a one-off migration; entry 112.6 superseded (case 130.1) · [[decision-case-130.1]]
- 2026-09-14 updated: the History line of case 114, `updated: the`, completed by hand to name the derived ## Insight section — a one-off migration (case 131) · [[decision-case-131]]
- 2026-09-14 updated: an entry materialize failed is skipped, its failed mark kept (case 142.2) · [[decision-case-142.2]]
- 2026-09-14 updated: ref fields written as quoted wikilinks; read through the brackets; one migration over wiki/ and archive/ (case 148.1) · [[decision-case-148.1]]
- 2026-09-14 updated: an entry with superseded_by is skipped without a line; its Decision page still written (case 151) · [[decision-case-151]]
- 2026-09-15 updated: no derived section on any write; the Addressed by derivation of 124.2/164 removed; the migration over wiki/ and archive/; supersedes 164 (case 166.2) · [[decision-case-166.2]]
- 2026-09-15 updated: the cascade step of 114 removed: no ## Insight derived on lessons; supersedes 114 (case 166.3) · [[decision-case-166.3]]
- 2026-09-15 updated: the sentence of 164 on the librarian's create and the refusals, carried by 171 since 164 is superseded before it applies; supersedes 124.2 (case 171) · [[decision-case-171]]
- 2026-09-15 updated: block 148.1 restated without the body sections; supersedes 148.1 (case 172) · [[decision-case-172]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
- 2026-09-16 deferred · [[decision-case-182]]
- 2026-09-16 updated: a defer writes its purpose to the decision page under · [[decision-case-186.1]]
- 2026-09-16 defer by decision-case-182 superseded · [[decision-case-191]]
- 2026-09-16 deferred · [[decision-case-191]]
