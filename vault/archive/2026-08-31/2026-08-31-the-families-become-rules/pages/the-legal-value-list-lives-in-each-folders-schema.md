---
title: "The legal value list lives in every folder's own `_schema.yaml`, copied rather than inherited"
type: decision
status: archived
authority: schema-value-location
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "job_hunt_ai_vault/wiki/concepts/_schema.yaml", "job_hunt_ai_vault/CLAUDE.md"]
tags: [record-schema, harness, vault]
---

# The ruling, 2026-08-19

> **owner: the legal value list lives in `values:` in each `_schema.yaml`**, one copy per folder,
> **cited from the vault's own `CLAUDE.md`.**

**Rejected, and the alternatives were named:** a shared or core schema the folders inherit from, and
a list written inside `scripts/vault-check.sh`.

## The reason is the store's own preference, stated as such

**The copied shape was already accepted for the frontmatter core** — the same key set stands in
every folder's schema ([[the-per-folder-frontmatter-schema]],
[[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]). Minting an inheritance mechanism for
the value half would mean this store has one form for keys and another for values, and **one form is
worth more here than being right more often**: the owner takes fewer exceptions to remember over a
design that is technically tighter. The drift the copy invites is real
([[a-copied-list-drifts-and-a-sweep-cannot]]) and is knowingly paid.

**A list inside the check was rejected for the reason the key set was.** The gate is the reader, not
the register. A schema states what is decided; a script states how it is verified, and merging them
puts the decision where no page can cite it ([[the-index-reads-and-the-schema-writes]]).

## What it obliges

- **A change to a value set is made in every folder's file.** The mitigation for the drift is the
  check itself: a page carrying a value one folder allows and another forbids reddens on the folder
  that forbids it, so the two copies cannot silently disagree about a page that exists.
- **The vault's `CLAUDE.md` cites the schemas rather than restating the list.** Its `basis` table
  explains what each value means; the legal set is read from the schema, which is the session's file
  to write ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).
- **The header rule of a `_schema.yaml` still binds.** A value moves in or out when a decision says
  so, and the decision names the page it is written on — a schema is not a place to reason from the
  corpus.

## The direction this page does not oblige, met 2026-08-20

**A field newly ADMITTED to a second folder is not obliged by anything to bring its `values:` list.**
This page obliges the reverse — a change to an existing set is made in every folder's file — and
says nothing about admission.

**The gap has a cost and it was measured rather than argued.** Without the copy, `render: banana`
passes rule 2 on a `concepts/` page while failing on a `rules/` one, **and the injector cannot cover
for it**: it reads `render` only after skipping every page with no `governs:`, so a nonsense value on
a page with neither is seen by nothing
([[the-injector-reads-render-only-after-it-has-skipped-a-page-without-governs]]).

**The copy was made anyway, as an inference**, and it is written down on the ruling that needed it
([[an-absent-render-is-red-on-a-page-that-renders]]). **Whether it becomes a rule is open and is the
owner's** — it is the same trade this page already names, one exception to remember against being
right more often.

**He answered it on 2026-08-26 and no rule is written**
([[no-rule-is-written-against-a-copy-of-a-schemas-values-list]]). The drift is left to the gate,
which reddens a page carrying a value outside its folder's list; the direction the gate cannot see —
a copy that is *missing* a value the schema has — costs one red run the first time somebody uses it.
