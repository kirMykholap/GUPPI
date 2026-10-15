---
type: rule
kind: Leaf
purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
status: built
enforcement: check
implementation_ref: [.guppi/guppi/lint.py, .guppi/guppi/check.py, .guppi/tests/test_lint.py, .guppi/tests/test_check.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-lint-catches]]", "[[estimate-lint-finds-a-broken-link]]", "[[estimate-lint-checks-the-statuses]]", "[[estimate-lint-checks-the-method]]", "[[estimate-lint-catches-a-broken-fence]]", "[[estimate-lint-runs-every-step]]", "[[estimate-lint-reports-a-method-tied-to-a-one-off-moment]]"]
deferred_by: ["[[decision-case-838]]"]
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
core: true
---

## Purpose

Prevents a page that breaks its schema, points at nothing, claims a status its
Estimates do not support, or waits for a reading nobody took from sitting in the vault
unnoticed. Pages are written by the generator;
both drift, and nothing else reads the whole graph at once. Red is a signal, not a
gate: a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again (cases 182, 799); a placeholder is red with the count of its defers (case 186.3).
`uv run --project .guppi guppi check` runs it after `guppi render --check`, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds (case 807.2). Where the command `ship` is missing, as in a project that installed GUPPI, it prints one line that it skips that step and runs the other five (case 820). All six only report, so no step writes to the tree (cases 147.7, 227). It runs every step even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red (case 587). It needs no tool but `uv`, so a project runs it on any machine (case 820). `parent: rule-harness` names the
MOC of the harness tools: lint runs with the renderer, in no phase of the session. Where the module of the command `ship` stands, as in the repository that builds the clean version of GUPPI, `guppi lint` also reports each rule or entity with `core: true` that is `draft`, since `guppi ship` builds no clean version while one stands; a project that installed GUPPI gets no such line (case 822). The
classes and their order live in the docstring of `.guppi/guppi/lint.py`.

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
- 2026-09-16 updated: a placeholder earns one deferred finding with its count instead of the schema and orphan findings (case 186.3) · [[decision-case-186.3]]
- 2026-09-16 defer by decision-case-182 superseded · [[decision-case-191]]
- 2026-09-16 deferred · [[decision-case-191]]
- 2026-09-16 updated: Purpose carries unread, deferred and unmigrated; How it works dropped by hand, the classes in the docstring of guppi/lint.py (case 202) · [[decision-case-202]]
- 2026-09-16 defer by decision-case-191 superseded · [[decision-case-203.2]]
- 2026-09-18 updated: make lint has three steps — sprint --check between render --check and lint (case 227) · [[decision-case-227]]
- 2026-09-22 updated: make lint runs glossary --check too (case 306.5) · [[decision-case-306.5]]
- 2026-09-22 updated: no page is written by hand (case 320) · [[decision-case-320]]
- 2026-09-23 updated: the class `markers` — a Render not wrapped in the page's own markers, and a closing marker line for a child in a full page (case 325.2) · [[decision-case-325.2]]
- 2026-09-23 updated: a reading in `method` has one spelling, `by hand`; the constant READING is gone (case 330.1) · [[decision-case-330.1]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 updated: the class schema reads properties.single — a field holding a list where one value is its shape (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: draft → built · cascade
- 2026-09-25 estimate estimate-lint-finds-a-broken-link added · [[decision-case-401.2]]
- 2026-09-25 estimate estimate-lint-checks-the-statuses added · [[decision-case-401.3]]
- 2026-09-25 estimate estimate-lint-checks-the-method added · [[decision-case-401.4]]
- 2026-09-25 estimate estimate-lint-counts-the-unmigrated added · [[decision-case-401.5]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 status: draft → built · cascade
- 2026-09-27 updated: make lint runs backlog --check (case 451.5) · [[decision-case-451.5]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-09-29 estimate estimate-lint-catches-a-broken-fence added · [[decision-case-487.2]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 updated: the unmigrated count gone from the Purpose (case 506.2) · [[decision-case-506.2]]
- 2026-09-29 estimate estimate-lint-counts-the-unmigrated archived · cleanup
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: a Decision page with children and no kind list, and the origin of a parent Case found by a line of its sub-case, are no findings (case 544.9) · [[decision-case-544.9]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 status: draft → built · cascade
- 2026-10-02 updated: make lint runs every step and exits non-zero when any is red (case 587) · [[decision-case-587]]
- 2026-10-02 estimate estimate-lint-runs-every-step added · [[decision-case-587]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-03 estimate estimate-lint-reports-a-method-tied-to-a-one-off-moment added · [[decision-case-613.1]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-13 updated: a pending Estimate whose method waits for a later moment is no longer red; a failed one still is (case 799) · [[decision-case-799]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: make lint runs guppi ship --check as its last step (case 807.2) · [[decision-case-807.2]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: guppi check runs the six vault checks, and skips guppi ship --check where the command ship is missing · [[decision-case-820.1]]
- 2026-10-15 updated: every live rule, entity and Estimate names guppi check in place of the target lint of the Makefile · [[decision-case-820.7]]
- 2026-10-15 updated: lint reports a draft page with core: true where the module of ship stands · [[decision-case-822.9]]
- 2026-10-15 status: built → draft · cascade
- 2026-10-15 deferred · [[decision-case-838]]
- 2026-10-15 status: draft → built · cascade
