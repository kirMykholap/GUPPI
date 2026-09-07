---
title: "A register row is stale only when no page anywhere carries the slug, and the other direction still asks about `wiki/`"
type: concept
status: current
authority: authority-check-staleness
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-authority.sh", "authority.md"]
tags: [vault, retrieval, harness]
---

# What `--check` asks now

**`bash scripts/vault-authority.sh --check` compares the register against the tree in both directions,
and the two directions read different trees:**

- **Register → tree.** A row is **stale** only when no page in **`wiki/` or `archive/`** carries the
  slug. An archived page keeps its row.
- **Tree → register.** Only pages under **`wiki/`** are required to be in a family. An archived page is
  not required to be grouped.

**It agreed with the tree at 507 slugs** after the sweep of 2026-08-29 and the repeal that followed it.

# Why the change was made in one direction only

**The repeal made an archived page a legitimate row-holder.** A page moving into `archive/` keeps its
`authority:` and keeps its row, so the old test — which asked `wiki/` alone — reddened on all 239 pages
the sweep moved ([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]).

**Widening the *other* direction would have reddened the corpus's own history.** Pages retired between
2026-08-22 and 2026-08-29 had their rows deleted while the repealed rule stood, so requiring an
archived page to be grouped would light up every one of them at once, on work that was correct when it
was done ([[the-authority-check-asymmetry-created-by-the-repeal-is-left-standing]]).

# What the field is for, and why an archived page still has a claim on it

**The register does not answer *which slugs exist*, which is in the tree.** It answers **which slugs
answer the same question**, and an archived page still answers its question — what it asserts is
frozen, and how it is found is live
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**Deleting the row removed the archived page from the one lookup that could reach it**, which is why
the rule requiring the deletion did not survive its first real test.

**Rule 3 of the gate is unaffected**, and it is the one that matters for contradictions: it compares
`authority:` between **`current` pages only**, so a slug worn by one live page and one archived page is
not a collision ([[authority-becomes-the-index-and-is-required-outside-rules]]).

# What still does not reach `archive/`

**`--near`, `--group` and `--list` read `wiki/` alone.** Whether they should is open and deliberately
unbuilt: they share a cached corpus walk, so widening it changes four subcommands at once.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
