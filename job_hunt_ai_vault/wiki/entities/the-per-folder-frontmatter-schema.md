---
title: "The `_schema.yaml` a folder carries, and the verdicts the gate reads off it"
type: entity
status: current
authority: per-folder-frontmatter-schema
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "job_hunt_ai_vault/wiki/decisions/_schema.yaml", "scripts/vault-check.sh"]
tags: [record-schema, harness, vault]
---

# What it is

**Every folder under `wiki/` carries a file named `_schema.yaml`**, landed 2026-08-19 at `6abd1a2`
and read by the gate at `bd7cb1f`. Each one names, for a page in that folder, the frontmatter keys
it **must** carry and the keys it **may** carry — and nothing else in the repository restates the
list.

```yaml
type: decision
required:  [title, type, status, created, sources, tags, sprint, decided]
optional:  [authority, basis, updated, supersedes, superseded_by]
```

The bodies differ only where the folder does: `decisions/` requires `decided:`, `rules/` requires
`governs:` and drops `authority:` from the optional block entirely, `concepts/` alone lists
`governs:` as optional because a concept may render
([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]). The rest is the core of
2026-08-16 ([[the-frontmatter-core-is-fixed-and-updated-joins-it]]).

**They are not templates.** A template is copied; this is read. The decision behind that separation
is [[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]].

# The header is the rule they were built on

Each file opens with the same comment block, and its second paragraph is the load-bearing one:

> **THIS FILE ENCODES WHAT IS DECIDED, NOT WHAT IS OBSERVED.** A field carried by every page today
> is not thereby required: that is how `quantity:` entered this store, around the admission
> procedure, and it took a day to remove.

**That is why `basis` sits in `optional:` on all six** while 321 of 321 pages carry it. Reading the
corpus and promoting the field would be exactly the reasoning that admitted the escape hatch
([[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]]). The field's
status is an open question for the owner, and it is recorded on the decision page rather than
settled here.

# The verdicts the check takes from them

`scripts/vault-check.sh` sweeps `wiki/*/` for these files before it reads a single page, and there
are three ways to go red:

| Condition | Message |
|---|---|
| a page carries a key in neither block | `frontmatter key 'X' is in neither the required nor the optional list of <folder>/_schema.yaml` |
| a folder carries no `_schema.yaml` | `no _schema.yaml - the check reads the folder's key set from it and cannot judge a page without it` |
| a schema parses to no `required:` keys | `no required: keys parsed - a schema that yields nothing would let every key through` |

**The second and third exist because the failure to design around is a permissive one.** A missing
or unparseable schema would otherwise mean *every key is fine*, silently and in the direction of
passing — the shape [[a-denominator-is-walked-off-the-input-list]] describes. The folder-with-no-
schema verdict prints once by folder name and not once per page, so the line that matters is not
buried under sixty.

**A folder with a schema is judged per page; a folder without one is judged once and its pages are
not read for keys at all.** That is deliberate: reporting sixty missing-field lines for one missing
file tells a reader about the wrong thing.

# What it closed, and what it did not

**Two prose-only rules were retired by a mechanism written for neither.** `quantity:` can no longer
be written onto a page — measured, a page carrying it now reddens with the undeclared-key message
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]) — and the `basis`/`authority`
key set is now enforced rather than described. The other half of the standing
`authority:`-beside-`governs:` alarm closed the same night by a different route
([[authority-beside-governs-is-forbidden-on-any-page]],
[[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]).

**The parser is guarded against a schema that yields nothing and not against one that yields a
wrong set.** A key misspelled inside a `_schema.yaml` would reject every page carrying the correct
spelling: loud rather than silent, and a confusing morning. That is a known and accepted gap, named
here so the first reader of a wall of red checks the yaml before the pages.

**`empty_vault()` in the selftest now mirrors these files off the pristine copy** — the third thing
in that one function which has to be swept rather than listed
([[vault-scripts]], [[a-fixture-must-materialise-what-the-subject-reads]]).

**`*.yaml` is not pinned in `.gitattributes`**, so these six files convert to CRLF on the next
checkout. Measured 2026-08-19: the `awk` parse is CR-clean on this host and the gate stays correct,
so the class is not pinned ([[a-file-class-is-pinned-after-it-costs-something]]).

# `basis` moved to `required:` in all six — 2026-08-19

**The open question this page recorded is answered.** The owner ruled `basis` core, and it sits in
`required:` in every one of the six files, with a three-line comment above it naming the ruling and
citing the page it is written on
([[the-frontmatter-core-is-fixed-and-updated-joins-it]]).

```yaml
  # Promoted from optional on 2026-08-19, owner's ruling: the field conflict
  # resolution rests on cannot be one a page may omit.
  # [[the-frontmatter-core-is-fixed-and-updated-joins-it]]
  - basis
```

**The header rule was obeyed on both of its clauses**, which is the part worth reading here: a field
moves when **a decision** says so, and the comment **names the page** the decision is written on. The
section above explains why the corpus figure — every page carrying the field — was explicitly not the
argument.

**Measured after the change: the gate exits 0 and no page reddens**, `basis` being on 329 of 329 pages
in `wiki/`.

**These files were edited by the session and that is now legal.** What the gate reads as its own input is
the session's to write, with the owner reading the diff before the commit
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]) — so the six schemas and the vault's
`CLAUDE.md` are outside the one-writer rule and no divergence is recorded for editing them.

**Still not enforced: the value.** The schema says `basis` must be present; nothing says it must be one
of the five. `basis: banana` passes.

# The value half landed, and two of this page's closing lines are spent — 2026-08-19

**`values:` joined the six files.** It names a field and the values it may carry, and the gate builds
the set in the same `awk` pass that reads the key set
([[a-fields-legal-values-live-beside-its-legal-keys]]).

```yaml
values:
  basis:
    - human
    - code
    - measurement
    - external
    - inference
```

**A value outside the list is red, not advisory** ([[a-value-outside-the-schemas-list-is-red]]), and
**a `values:` header that parses to nothing is red too** — the same permissive-failure argument the
missing-schema verdict was written on. **So *"`basis: banana` passes"* above is false as of
2026-08-19**, and it is left standing as the state that produced the ruling.

**The list lives in each folder's file rather than in a shared schema or in the check**
([[the-legal-value-list-lives-in-each-folders-schema]]). The copy is knowingly paid: one form for
keys and values is worth more here than an inheritance mechanism that is right more often.

**And `*.yaml` is pinned now**, so *"these six files convert to CRLF on the next checkout"* above is
also spent. It happened — a `git stash push` / `pop` turned all six CRLF and an edit script's LF
anchors matched nothing, which is exactly the cost the pinning policy waits for
([[the-yaml-class-is-pinned-to-lf]], [[a-file-class-is-pinned-after-it-costs-something]]).

**The reason the earlier measurement looked like a safety argument is worth keeping**: no carriage
return reaches `awk` on this host, so the parse really was CR-clean here and really was not in the
container ([[no-cr-reaches-awk-on-this-host-and-the-container-is-where-it-bites]]).

**One loader asymmetry is left and reported**: the value loader strips `\r`, the `required:` and
`optional:` loaders do not, and the page pass does. With the pin in place they cannot be reached
from the checkout direction — a reason to leave them rather than a reason they are right.

**`render:` is required in `wiki/rules/_schema.yaml` from 2026-08-19**, which is the first field
this store has admitted on a re-entry condition a refusal named for itself
([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]).

# The `concepts/` asymmetry is withdrawn — 2026-08-21

**The sentence *"`concepts/` alone lists `governs:` as optional because a concept may render"* is
false from this date.** A concept may not render. The owner ruled at the retro of 2026-08-21 that
a page carrying `governs:` **is** a rule, so the field belongs to `wiki/rules/` and to no other
folder ([[governs-is-a-property-of-wiki-rules-alone]]). The sentence is left where it stands as the
reading of 2026-08-19, and this section is the correction rather than a rewrite of it.

**`render:` goes out with it.** It was admitted to `concepts/_schema.yaml` on 2026-08-20 only so
that a concept page which renders would have to name its delivery mode, and the asymmetry between
the two files was written up here as *the decision rather than an oversight*
([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]],
[[an-absent-render-is-red-on-a-page-that-renders]]). With no such page left, the field has nothing
in that folder to discriminate.

**`authority:` becomes required in `concepts/` with them, which is what makes the withdrawal a
simplification rather than a swap.** That folder was the one place the schema still said `optional`,
and it was not an exemption — it was a condition a per-folder schema cannot express, *required
unless the page carries `governs:`*, which therefore lived in the gate and in
`bash scripts/vault-authority.sh --orphans` instead
([[authority-becomes-the-index-and-is-required-outside-rules]]). With the condition's other half
gone the rule reads straight: **required outside `wiki/rules/`, forbidden inside it**, with no third
case ([[authority-beside-governs-is-forbidden-on-any-page]]).

**The three edits to `concepts/_schema.yaml` are the session's to write** — the file is what the
gate reads as its own input ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]) —
and the header rule is obeyed on both clauses as usual: the fields move because a decision says so,
and the decision names the page it is written on.

**After that edit the confinement is mechanical and not remembered.** `governs` already appears in
neither the `required:` nor the `optional:` block of `decisions/`, `entities/`, `lessons/` and
`proposals/`, and a key in neither block is rejected outright, so `concepts/` was the last folder
where the gate would have accepted it ([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]).

# A citation written into one of these files is checked by nothing — 2026-08-21

**Rule 4 of the gate sweeps `.md` for broken wikilinks and these files are `.yaml`.** A slug written
into `wiki/decisions/_schema.yaml` from memory rather than from the tree reached no page and reddened
nothing; it surfaced only because the librarian copied it onto a page
([[a-wikilink-outside-the-md-sweep-is-invisible-to-the-gate]]).

**The instruction now stands in the schema itself, beside the block that carried the broken slug:
cite from the tree here.** Widening the sweep to `.yaml` was considered and not done.

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# The rules schema documents the list form of `governs:` — 2026-08-21

**`job_hunt_ai_vault/wiki/rules/_schema.yaml` now says that the field takes a bare path or an inline
list, and why the block form is refused.** The entry is documentation beside a key that was already
legal: no key moved between the blocks, and nothing became required
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

**It is a session's file rather than the librarian's**, and it was edited by the session with the
owner reading the diff — the clause of 2026-08-19, not a divergence
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# The objection carried in `wiki/proposals/_schema.yaml` was answered on 2026-08-24, and the objection was kept

**The comment holding the case against pairing `status: idea` with `decided_by:` is left exactly as
it stood**, and its answer is appended beneath it. **The objection is what the build had to answer,
not a mistake to tidy away**: a fully designed proposal no decision produced would have to assert an
immaturity it does not have, and a half-thought produced by a deferral could not be an `idea` at all.

**The answer is the owner's narrowing**: a page is red only when it carries `status: idea` and names
a cause whose `binding:` is not `deferral`
([[the-idea-and-decided-by-verdict-is-built-narrowed-to-a-non-deferral-cause]]).

**The file was edited by the session and not by the librarian**, under the clause that what the gate
reads as its own input is the session's to write
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

## The state of `wiki/proposals/` after the back-fill, read 2026-08-24

**27 of 34 pages carry `decided_by:`, and exactly one page carries `status: idea`** — the first page
in the corpus ever to hold that value, minted on 2026-08-23. **Seven pages carry no cause**: one is
the `idea`, and six are pages whose ruling existed and had never been compiled
([[a-proposal-keeps-an-absent-decided-by-rather-than-a-false-idea-mark]],
[[the-missing-decision-pages-are-written-by-the-nearest-ingest]]).

**This is a gauge and it is dated where it stands.** The command that answers it is
`bash scripts/vault-check.sh --lint`, which names every page lacking the field
([[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]]).

# Two values entered on 2026-08-28, and they entered differently

**`archived` is declared in all six files.** It is written by a sweep as it moves a page, so finding
it under `wiki/` means the move did not finish
([[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]]).

**`processed` is declared in `wiki/decisions/_schema.yaml` alone** and is red in the other five,
which is the protection rather than an oversight — the arrangement `implemented` already has in
`wiki/proposals/` ([[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]]).

**Neither has a writer yet.** `archived` waits on a sweep that does not exist and `processed` waits
on the reading agent that would name its pages
([[the-archive-sweep-that-walks-each-folder-and-collects-its-refusals]],
[[the-decisions-agent-reads-only-and-runs-at-every-ingest]]).

**The comment blocks in `wiki/decisions/_schema.yaml` and `wiki/proposals/_schema.yaml` carry the
full reasoning for both**, written by the session that added them, which is the arrangement the
schemas were given when they stopped being the librarian's to edit
([[the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own]]).

# `wiki/rules/_schema.yaml` carries a criterion that named no decision, and now there is one — 2026-08-29

**It holds a folder-specific archival criterion — `deprecated` plus a decision behind the overturn —
and it named no decision page.** That is against these files' own header rule, which says a field or a
criterion moves on a decision **and the decision names the page it is written on**. It is the only
folder-specific archival paragraph of the six.

**Surfaced by `/pre-task` against plan decision 10 on 2026-08-29**, and the decision it was missing
exists now ([[a-rules-page-leaves-only-on-a-decision-and-a-deprecated-mark]]).

**The schema file itself was not edited by this ingest.** These files are the session's to write, not
the librarian's ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]); what is owed is
one citation added to that paragraph.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# Four readings off the schemas and the gate — 2026-08-29

**`unknownkey` is a schema question, not a script question.** `scripts/vault-check.sh:422` reports it
for any frontmatter key not in the folder's `required:` or `optional:` list, and
`wiki/entities/_schema.yaml`'s `optional:` holds only `updated`, `supersedes`, `superseded_by` and
`Links`. **So `decided_by:` on an entity or concept page is red today and would go legal the moment the
schema changed — no script change needed**, because the gate reads the schema rather than a hardcoded
list. That is the mechanical half of a widening the owner reversed
([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**`processed` was already a legal `status:` value in `wiki/decisions/_schema.yaml`** alongside
`current`, `deprecated` and `archived`, and `scripts/vault-archive.sh` already selected on it in
`sweep_candidates()`. **Zero of the live pages carried it**, because no librarian had ever been asked to
set one. The machinery existed and had never been used
([[the-librarian-sets-processed-when-it-writes-decided-by-and-the-archiver-reads-each-field]]).

**`wiki/rules/` held 16 pages, nine rendering into `CLAUDE.md` and the rest into skills, agents and
hooks, against 15 governed harness markdown files — all 16 carrying `decided_by:`.** So the relation *a
rule names the decision behind it* existed for 16 of 263 prohibitions. **It does not mean `rules/` could
hold the rest**: each rule needs a destination file and a rendered slice, and most decisions have
neither.

**`wiki/decisions/` held 295 — 263 `prohibition`, 32 `deferral`, 0 `divergence`.** The zero is the
sweep's doing, and it is why a new divergence page written today would be taken by the archiver on
sight.

**All four are readings of 2026-08-29 and each is decided by a command rather than by this page.**

# The schema files stopped describing frontmatter alone on 2026-08-30

**Three new block kinds entered these files, and none of them is a frontmatter key.**

| block | what it declares | read by |
|---|---|---|
| `sections:` | the `# ` headings a page in this folder carries | rule 16 |
| `lifecycle_from:` | the date from which those obligations apply | rule 16 |
| `required_from:` | the keys that become obligatory on that date | rule 16 |

**`wiki/decisions/_schema.yaml`** gained `target_kind:` and `target:` as **optional** keys with a
closed five-value list, `lifecycle_from: 2026-08-30`, a `sections:` block of five headings and a
`required_from:` block naming both keys. **Its `processed` entry is marked repealed and stays legal
until the one live page carrying it leaves**
([[processed-is-struck-from-the-schema-once-no-page-carries-it]]).

**`wiki/proposals/_schema.yaml`** gained the same date and a one-heading `sections:` block.
**`wiki/rules/_schema.yaml`** gained `status: repealed`.

**The other four folders carry the mechanism and no sections**, which is the owner's own staging:
«Мы описываем механизм для всех старниц, но сами разделы прописываем сейчас только для decisions»
([[the-body-sections-are-declared-in-every-schema-and-filled-where-they-are-written]]).

**Rule 16 checks the schema against itself**: a key named in `required_from:` must also appear under
`required:` or `optional:`, or the rule would oblige a key that the `unknownkey` verdict then reddens
— and no page in the folder could be written correctly. **Two lists of one set drift, so the check is
mechanical rather than trusted to whoever edits the file.**

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`, extended 2026-08-30.)*
