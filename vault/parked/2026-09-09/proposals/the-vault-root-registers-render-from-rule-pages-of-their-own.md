---
title: "The vault-root registers render from `wiki/rules/` pages of their own"
type: proposal
status: current
authority: register-rendering-design
basis: human
sprint: S3
created: 2026-08-29
decided_by: "[[the-vault-root-registers-do-not-count-as-citers]]"
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-inject.sh", "authority.md"]
tags: [vault, retrieval, harness]
---

# What it would be

**owner:** «в идеале эти реестры должны рендерится. То есть иметь свою страницу rule в vault, которая
рендерить их полностью или частично. В таком случае упоминание будет идти на страницу, а не на реестр.»

**Each vault-root register gets a `wiki/rules/` page carrying its text**, and `scripts/vault-inject.sh`
renders that page into the register file — wholly or into a marked region of it. The registers in scope
are `index.md`, `tags.md`, `sprint.md` and `log.md`.

**The point is where a mention lands.** Today a page mentioned in a register is mentioned in a file that
is not a page: it has no `authority:`, it is in nobody's family, and the archiver refuses to treat it as
a citer for good reason ([[the-vault-root-registers-do-not-count-as-citers]]). Rendered from a page, the
mention would land on a page.

# What it would take

**`governs:` already points from a rule into a file it renders**, and the injector already writes marked
regions and whole files — `render: whole` with `paths:` exists
([[governs-is-a-property-of-wiki-rules-alone]], [[the-governed-set-is-swept-and-markdown-by-property]]).

**Rules 11 and 12 of the gate already ask both ends of the relation**, so a register that fell out of
step with its page would redden ([[vault-scripts]]).

**A `wiki/rules/` page carries `decided_by:` and never `authority:`**, so each of the four would need a
decision naming it — which is four decisions that do not exist.

# What is open

**Which of the four are `render: whole` and which take a region.** `index.md` is short and hand-written;
`log.md` is append-only and thousands of lines, and rendering it whole from a page would mean the page
is the append target — which is the same file with an extra hop.

**And `log.md` is the one with a conflicting ruling in flight.** It is to be filled **mechanically** and
rotated at the sprint close, which is a different answer to *who writes this file*
([[log-md-is-filled-mechanically-and-rotates-when-the-sprint-closes]]). **The two designs have not been
put beside each other**, and doing that is the first thing anyone building either should do.

**Whether it would make the registers citers at all.** A rendered region is a copy; the archiver counts
pages under `wiki/`, and the rule page would be under `wiki/rules/` — so the mention would count, which
reopens the objection the narrow ruling was made on: `sprint.md` names half the corpus
([[a-citation-is-not-a-test-in-a-corpus-this-densely-linked]]).

**Recorded, not built.** His idea, in his own words, on the day it was said.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
