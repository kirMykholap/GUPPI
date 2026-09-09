---
title: "A wikilink written outside the `.md` sweep reaches nothing and reddens nothing"
type: lesson
status: archived
authority: link-sweep-file-class
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md", "scripts/vault-check.sh", "wiki/decisions/_schema.yaml"]
tags: [vault, harness, testing]
---

# What happened, 2026-08-21

**Rule 4 of the gate sweeps `.md` for broken wikilinks.** The `_schema.yaml` files are `.yaml`, so a
slug cited in one is checked by nothing.

**A slug written into `wiki/decisions/_schema.yaml` from memory rather than from the tree pointed at
no page.** It reached nothing and reddened nothing. **It surfaced only because the librarian copied
it onto a page**, where the sweep does run — which is luck dressed as a process.

**The same blind spot has a second instance the same day.** `authority.md` contains the literal
`[[wikilinks]]` inside a code span, in the very sentence forbidding wikilinked slugs. It is harmless
today because that file is deliberately outside the sweep — a register that linked every page would
make every page reachable and the orphan rule would prove nothing
([[authority-becomes-the-index-and-is-required-outside-rules]]) — and it is named here because **the
day the file is admitted to the sweep, it reddens.**

# Why this is the dangerous direction

**The instrument fails towards nothing-to-do.** A broken link in a page is printed; a broken link in a
schema is silence, and silence is indistinguishable from correctness
([[an-instrument-that-fails-towards-nothing-to-do]]).

**And the schemas are exactly where a citation is most load-bearing.** They are read by the gate as
its own input and are edited by sessions rather than by the librarian
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]],
[[the-per-folder-frontmatter-schema]]), so their citations are written by the party that does not
hold the corpus in front of it.

# The rule that follows, which is cheaper than widening the sweep

**Cite from the tree, never from memory, in any file the sweep does not read.** That instruction is
now written into `wiki/decisions/_schema.yaml` itself, beside the block that carried the broken
slug.

**Widening rule 4 to `.yaml` was not done and is not obviously right**: the schemas are few and their
citations are rare, and the register must stay out of the sweep for a reason that has nothing to do
with cost. **A file class is pinned after it costs something**, which is how this project has ruled
on the same question for line endings ([[a-file-class-is-pinned-after-it-costs-something]]).
