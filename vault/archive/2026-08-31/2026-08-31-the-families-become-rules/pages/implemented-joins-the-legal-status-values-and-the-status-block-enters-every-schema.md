---
title: "`implemented` joins the legal `status` values, and a `status:` block enters every folder's `_schema.yaml`"
type: decision
status: archived
authority: status-value-set
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["scripts/vault-check.sh", "job_hunt_ai_vault/wiki/proposals/_schema.yaml", "job_hunt_ai_vault/CLAUDE.md"]
tags: [record-schema, harness, vault]
---

# The ruling, 2026-08-23

**`status` gains a third value, `implemented`, and it is legal in `wiki/proposals/` alone.** It is
the mark an implemented proposal carries as it leaves direct view
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

**And the legal value list for `status` stops living inside the gate.** The pair is hardcoded in
`scripts/vault-check.sh` — the test at line 468 as the file stood today, its message at line 496,
*"the schema has only current and deprecated"* — while no `_schema.yaml` declares values for
`status` at all, though the generic `values:` mechanism exists and already carries `basis`, `render`
and `binding`.

**Rejected: adding a third word to the list inside the script.** That alternative was already ruled
against on 2026-08-19, in the words this page is bound by —
[[the-legal-value-list-lives-in-each-folders-schema]]: *"The gate is the reader, not the register. A
schema states what is decided; a script states how it is verified, and merging them puts the
decision where no page can cite it."* That page also says a value moves in or out **when a decision
says so, and the decision names the page it is written on**. This is that decision, and this is the
page.

**The schemas and the script are the session's to write, not the librarian's**
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]). This page is the decision they
carry out; it makes no claim that either has been changed.

# The block goes into every folder's file, and leaving one out fails silently

**This is the correctness point and it is the reason the decision is written out rather than left
as *add the value*.** The `badvalue` check at `scripts/vault-check.sh:391` iterates the fields a
folder **declares** values for, and judges nothing else:

```
vn = split(valfields[folder], vf, " ")
```

**So a folder with no `status:` block in its `values:` has no status check at all.** Today the
hardcoded pair covers all six folders. Remove it and write the block into `proposals/` alone, and
five folders — `decisions/`, `concepts/`, `entities/`, `lessons/`, `rules/` — silently lose the
verdict, in the direction of passing, with the gate green.

**The obligation therefore reads: a `status:` block is written into all six `_schema.yaml` files** —
five carrying `[current, deprecated]`, `proposals/` carrying `[current, deprecated, implemented]` —
**in the same change that removes the hardcoded pair.** That is the same obligation the page above
already states in general terms: *"A change to a value set is made in every folder's file."*

**The copy is knowingly paid for.** One form for keys and values beats being right more often, the
drift a copied list invites is real ([[a-copied-list-drifts-and-a-sweep-cannot]]), and the
mitigation is the check itself: a page carrying a value one folder allows and another forbids
reddens on the folder that forbids it, so the two copies cannot silently disagree about a page that
exists ([[a-value-outside-the-schemas-list-is-red]]).

**`built` is not admitted by this decision.** Only `implemented` lands; the middle state waits on
`wiki/tasks/` and on S4, and admitting a value with no test and no page that may carry it is
admitting a word to be misused
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

# A consequence, recorded as a consequence and not as a task

**`scripts/vault-inject.sh` tests positively for `current`**, at line 250 as the file stood today:

```
grep -qE '^status:[[:space:]]*current[[:space:]]*$' "$page" && current_status=1
```

**A page carrying any third value is therefore not-current to the injector**, and a rule page in
that state does not render — the injector removes what it generated and says so. No proposal renders
anything today, so nothing is broken by this on the tree as it stands; the reader of a positive test
is what makes a *third* value a different thing from a second one, and the same shape has already
caught this store out where `render` is read only after a page without `governs:` has been skipped
([[the-injector-reads-render-only-after-it-has-skipped-a-page-without-governs]]).

**It is S3 phase B2 and it is named here so it is not found later.**

# Why this is a page of its own and not a section of the disposition ruling

**They are one change and two questions.** The disposition ruling says where an implemented proposal
lives; this one says what values `status:` may carry and where that list is declared.

**The register settles it.** `authority:` is the question a page is the sole answer to, and a slug
belongs to exactly one family. `built-proposal-disposition` is in *retiring a page*;
`bash scripts/vault-authority.sh --near status-value-set` returns *the per-folder schema*, whose
members are `frontmatter-core`, `schema-value-location`, `schema-value-enforcement`,
`schema-value-parsing` and the rest — a family a reader arrives at from the gate, never from
`proposals/`. **Folding the two into one page would leave the value-set question with no row in the
register**, which is the hole the register exists to close
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

**And the reach differs.** This decision obliges an edit to five folders that hold no proposal at
all, and names a reader inside `scripts/vault-inject.sh`. None of that is a statement about where a
proposal lives.
