---
title: "`decided_by:` is a field of its own, not a line in `sources:` and not a link in the body"
type: decision
status: archived
authority: decided-by-field
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "job_hunt_ai_vault/sprint.md"]
tags: [vault, record-schema, process]
---

# The ruling, 2026-08-23

**owner selected: новое поле `decided_by: [[страница]]`** — a page names the decision that caused
it, in a field of its own.

**A selection and not an utterance.** The wording of the option is this session's; he chose it from
a menu the session composed, so the ruling ranks as his and the sentence carrying it ranks as the
session's. It is written as a label, unquoted and unsigned
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

# What it was chosen against, and both alternatives were measured

| the alternative | what it was measured at | why it lost |
|---|---|---|
| write the causing page into `sources:` | the field stands on 305 pages | the field would carry two meanings — *what this was compiled from* and *what caused this* — and a reader could not tell which a given entry was |
| leave the link in the body | 62 pages already carry such a link in prose | no machine separates *the decision that caused this page* from *a decision this page happens to mention* |

**The shape of the losing arguments is the same as the one that split `Links:` off `sources:` on
the same day**: a field that means two things cannot be read by a script, and a link in prose has
no detector ([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]],
[[a-path-detector-for-prose-references]]).

# What it obliges

- **The field is legal in every folder's `_schema.yaml`** — the same all-six obligation that the
  `status:` block carries, and for the same reason: the gate iterates the fields a folder
  **declares**, so a folder left out loses the verdict silently and in the direction of passing
  ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]],
  [[a-fields-legal-values-live-beside-its-legal-keys]]).
- **The count of pages lacking it prints under `--lint`, and the gate stays green.** It is
  acceptance criterion 3 of S3, and the criterion asks for the field to be legal and the shortfall
  to be counted — **not for the back-fill**, which is 314 pages and is explicitly deferred.
- **It is `[[wikilink]]`, not a path.** The thing named is a page in this store, so it is addressed
  the way this store addresses a page.

# It is not built

**No schema declares it, no page carries it, and nothing counts the shortfall.** The schemas are
the session's to write ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

**And nothing here says what a page does when its cause is not a decision page.** A lesson learned
from an incident, an entity that simply exists — neither has a deciding page, and whether the field
is then absent or names something else was not asked.

# Corrected later on 2026-08-23: the folder set narrowed to two, and one argument above is false

**The first bullet of *What it obliges* went false hours after it was written, in the next session
of 2026-08-23, and is left standing above.** The
field is legal in `wiki/proposals/` and `wiki/rules/` and in no other folder; in `wiki/rules/` it
becomes required, and in `wiki/proposals/` it stays optional. The owner took that by approving a
plan he read in Russian, on the ground that **a decision produces a proposal or a rule and nothing
else** — anything further down names what it descends from in `sources:`
([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**This page is not superseded and its own claim is untouched.** What it decides is *which field
carries the cause* — a field of its own, rather than a line in `sources:` or a link in prose — and
that stands whole. The folder set is a second question and it has a page of its own, which is what
the register asked for ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]). The second
bullet is untouched and still owed: the count of pages lacking the field prints under `--lint`, and
what it counts is now the pages of those two folders. The back-fill stays deferred.

**And the reason that bullet gave is wrong, which is the part a later reader would have
inherited.** *The gate iterates the fields a folder declares, so a folder left out loses the verdict
silently and in the direction of passing* is true of a `values:` block and false of a **key**. It
was transplanted from
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]], where it is
about legal values and is correct. For a key, `scripts/vault-check.sh:382` does the opposite: a key
appearing in neither `required:` nor `optional:` makes the page carrying it **red**, by name
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]). **A
folder left out of a key declaration therefore fails towards refusing**, which is what makes the
narrowing mechanically safe. The two obligations are different in kind, and the correction is
argued in full on the narrowing page rather than restated here.
