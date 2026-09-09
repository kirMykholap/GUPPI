---
title: "The authority register groups the corpus, and the family is the unit of a cleanup rather than the page"
type: concept
status: current
authority: authority-family-grouping
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/authority.md", "scripts/vault-authority.sh"]
tags: [vault, retrieval, process]
---

# What it turned out to be

**`authority.md` was built on 2026-08-21 as the index a claim is looked up in before a page is
written** ([[authority-becomes-the-index-and-is-required-outside-rules]]). It was written for
admission — *does this claim already have a page* — and it grouped the corpus as a side effect.

**Read as a grouping on 2026-08-30:**

- **282 prohibitions sit in 53 of its 63 families, with no slug left over.** Median five per family,
  largest fourteen, and the largest twenty-eight families cover 214 pages.
- **187 pages of `concepts/` and `entities/` sit in 51 families**, of which **24 already hold both a
  concept and an entity** (88 + 38), 22 hold concepts alone (54 pages), and five hold entities alone
  (seven pages).
- **61 families carry at least one live page**; seven of them are about the product and hold twenty
  prohibitions of the 282 and 24 concepts of the 142. **The five largest families are all about the
  machinery of this store** and hold 59 prohibitions between them.

# Why that changes what a cleanup costs

**The unit of a decision becomes a family, not a page: 99 verdicts rather than 469.** A reviewer
reading 53 prohibition families and 46 concept/entity groups is answering a question a person can
answer; a reviewer reading 469 pages is not.

**And the grouping is the half that cannot be derived.** Which slugs exist is in the tree and needs no
file; which slugs answer the same question is nowhere else, which is why this register is hand-written
and audited in both directions by `bash scripts/vault-authority.sh --check` rather than generated.

**What the numbers do not say** is that a family is the right unit of *judgement*. They say a grouping
exists and costs one pass to read. Whether a family should become one rule, several, or none is the
owner's verdict and those verdicts do not exist yet.

# The review table is derived and lives outside the store

**`docs/vault-cleanup-families.md` carries the 53 prohibition families with the title of every page in
each, and the 46 concept/entity groups — 1,819 lines, verdict columns empty.** It was generated from
this register plus the corpus frontmatter by a one-off script that lives in a scratchpad, and it says
in its own first paragraph that it is regenerated rather than edited.

**It is not a page of this vault and does not become one.** It exists so the owner reads the families
before anything is swept, and the next sweep stands on the verdicts he writes into it.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
