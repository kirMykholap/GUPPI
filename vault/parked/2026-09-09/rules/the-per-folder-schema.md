---
title: "The per-folder schema"
type: rule
status: current
authority: per-folder-frontmatter-schema
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[the-type-words-are-swept-off-the-tree-and-never-listed]]
tags: [record-schema, vault, harness]
---

# The per-folder schema

Where the legal keys and values live, how the gate learns them, and in what order a schema change lands. Answers "is this frontmatter legal, and who says so".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A `sources:` path inside the vault is vault-relative, and one outside it is written from the repository root ([[a-sources-path-inside-the-vault-is-vault-relative]]) — **the corpus disagrees with this clause and the clause is what is right**: measured 2026-08-31, `authority.md` is cited from the repository root on **29** pages and vault-relative on **24**. The pages written from 2026-08-31 follow the rule; the 29 are a sweep nobody has scheduled, and a reader who copies the wrong neighbour copies the wrong form
- A conditional requirement is refused by the script that moves the page, not by the gate ([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]])
- A frontmatter value outside its schema's list is red, not an advisory ([[a-value-outside-the-schemas-list-is-red]])
- No rule is written against a copy of a schema's `values:` list, and the drift is left to the gate ([[no-rule-is-written-against-a-copy-of-a-schemas-values-list]])
- The `idea` and `decided_by:` verdict is built narrowed to a cause that is not a deferral ([[the-idea-and-decided-by-verdict-is-built-narrowed-to-a-non-deferral-cause]])
- The gate learns the legal frontmatter keys from a yaml per folder, rather than from a list inside itself ([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]])
- The legal value list lives in every folder's own `_schema.yaml`, copied rather than inherited ([[the-legal-value-list-lives-in-each-folders-schema]])
- The type words are swept off the tree as `singular:plural` pairs and listed nowhere ([[the-type-words-are-swept-off-the-tree-and-never-listed]])
- `implemented` joins the legal `status` values, and a `status:` block enters every folder's `_schema.yaml` ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *the per-folder schema* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `type-word-source`, whose decision leaves for `archive/`. The slug carried instead is `per-folder-frontmatter-schema`, which [[the-per-folder-frontmatter-schema]] carries and keeps: that entity **is** the `_schema.yaml` this family is about, so opening one of those files' description hands over the rule that governs writing them. `decided_by:` still names a member decision, which is what this folder requires.
