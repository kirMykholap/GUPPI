---
title: "The frontmatter core is fixed, `updated` joins it, and which fields owe a check"
type: decision
status: archived
authority: frontmatter-core
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "CLAUDE.md"]
tags: [vault, testing]
---

# Decided 2026-08-16: the core every page carries, and what each field is for

**The core is `title`, `type`, `status`, `created`, `sources`, `tags`, `sprint` — and the new
`updated`.** Each was put through the admission test rather than kept by habit:
[[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]].

Two of them survive on the checksum half rather than on a reader: `type` and `status` restate what
the folder already asserts, which catches a page filed into the wrong folder by an unattended
writer. Two are weak and were kept with the weakness written down — `created`, which git records
better, and `sprint`, which has no consumer but the catalogue's printer and is therefore **labelled
documentation in the schema**, because a field with no consumer that looks like an index eventually
becomes one, and then a query for the current sprint returns only recent knowledge.

**`updated` is new, stamped by a script from the diff, and lays no obligation on any writer.** What
it is for and what it must never be allowed to mean is
[[a-staleness-detector-from-updated-against-a-pages-sources]].

## Per type, above the core

- **`decided` stays** on decisions. Only 8 decision pages of 58 carry the date in their H1, so for
  fifty of them the field is the sole carrier, and git dates the writing rather than the deciding.
  **Rejected: dropping it** — batching widens the gap between deciding and writing, and every
  decision of a sprint would look taken on the day of its retrospective
  ([[ingest-runs-after-handoff-at-the-end-of-a-session]]). Owed a check: `decided <= created`.
- **`supersedes` stays and gains a symmetry rule.** The schema demands the link in both directions
  and explains why — *a deprecated page that does not name its successor is a dead end* — and
  **nothing checks it**: `A supersedes B` with `B` silent passes today, which breaks the chain the
  field exists to keep.
- **`proposals` are left as they stand, with a mark to revisit** —
  [[the-proposal-status-cannot-tell-built-from-refused]].
- **`lessons` and `concepts` get nothing above the core.**

## Three checks the schema now owes

1. **`basis` gets an enumeration check.** It is the only field conflict resolution rests on — a
  page on `human` outranks one on `inference` — and today `basis: banana` passes.
2. **`decided <= created`**, and `created` neither in the future nor before the first commit.
3. **The `supersedes` / `superseded_by` symmetry**, in both directions.

None of them exists. They belong to the same build as everything else here
([[what-the-harness-build-waits-on]], [[vault-scripts]]).

## Where the core is now read from, and the `basis` question this raised — 2026-08-19

**The core is no longer restated in `vault-check.sh`.** Each `wiki/` folder carries a `_schema.yaml`
naming its own required and optional keys, and the check reads it
([[the-per-folder-frontmatter-schema]],
[[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]). Each file cites this page for the seven
it encodes. **The script had been enforcing six** — `title type status created sources tags` — against
the seven decided here, and that gap closed with the change.

**`basis` is carried by 321 of 321 pages and is declared core by nothing**, including by this page,
which names it as *"the only field conflict resolution rests on"*. The schemas leave it `optional:`,
deliberately: a field carried by every page is not thereby required, and reasoning from the corpus to
the schema is exactly how `quantity:` entered the store
([[a-declaration-that-silences-a-check-must-expire-or-be-re-derived]]).

**The omission looks like an oversight rather than a decision, and the ruling is the owner's.** Either
`basis` belongs in the core and this page should say so, or it is genuinely optional and every page
carries it out of habit. **One line either way**, and the six schema files can change in the same
minute.

## The ruling this page asked for: `basis` is core — owner, 2026-08-19

> **owner: `basis` is core.** It moves from `optional:` to `required:` in all six `_schema.yaml`.

**Rejected: leaving it `optional:` and saying so here.** *Why:* this page already calls `basis` *"the
only field conflict resolution rests on"*, and **a field conflict resolution rests on cannot be one a
page may omit.**

**The argument runs from the decision and explicitly not from the corpus.** Reasoning from what every
page happens to carry is how `quantity:` entered this store, around the admission procedure
([[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]],
[[a-declaration-that-silences-a-check-must-expire-or-be-re-derived]]). The corpus figure below is
**corroboration and was not the reason**, and the distinction was stated when the ruling was taken.

**Executed the same turn**, with a three-line comment above the key in each file naming the ruling and
citing this page — which is what the schemas' own header rule demands of any such move
([[the-per-folder-frontmatter-schema]]).

**Measured after the change:** `bash scripts/vault-check.sh` exits 0 and **no page reddens**. `basis` is
on **329 of 329** pages in `wiki/`, in five values — `human` 167, `code` 94, `measurement` 55,
`inference` 11, `external` 2. *(The brief's figure of 321 was the pre-ingest count.)*

**So the core is eight fields**, and this page's title is left as written: it names `updated` because
`updated` is what joined it when the page was created, and a title corrected in place would not record
that a second field joined later ([[a-title-corrected-in-place-is-not-a-supersession]]).

### The first of the three checks below is still owed, and it is now load-bearing

**`basis: banana` passes today**, on a field that now decides every conflict. The owner **was offered the
enumeration check in the same question as the promotion and took the narrower option** — the promotion
without it.

*Consequence, stated rather than assumed:* the gate enforces that the key is **present** and says nothing
about its **value**, so a typo in the one field that ranks pages against each other is invisible to
everything. The other two checks on this page — `decided <= created`, and the `supersedes` symmetry — are
unmoved.
