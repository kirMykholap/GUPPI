---
title: "What a page is called and what kind it is"
type: rule
status: current
authority: page-naming
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[filenames-carry-no-category-prefix]]
tags: [vault, process, retrieval]
---

# What a page is called and what kind it is

The folder set, the naming rule, the form a title takes for each type, and correcting one. Answers "which folder, and what do I call it".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A title corrected in place is not a supersession ([[a-title-corrected-in-place-is-not-a-supersession]])
- An idea lives in `proposals/` with `status: idea` — the folder is the kind, the status is the maturity ([[an-idea-is-a-proposal-with-an-immature-status]])
- Filenames carry no category prefix — the folder and type: already say it ([[filenames-carry-no-category-prefix]])
- The `vault-scripts` page stays a hub, and the gate and its suite get subject pages of their own ([[the-vault-scripts-page-stays-a-hub-and-the-gate-and-its-suite-get-subject-pages]])
- The clause that `concepts` describes the product is struck rather than split ([[the-clause-that-concepts-describes-the-product-is-struck]])
- The folder set is closed, `rules/` joined it on 2026-08-17, and `tasks/` is still not in it ([[the-folder-set-is-closed-and-tasks-is-not-in-it]])
- The title's form follows the record's type: an entity is named, a decision states its claim ([[the-titles-form-follows-the-records-type]])
- What we planned and never did gets a folder, not a status: wiki/proposals/ is a category of its own ([[proposals-are-a-folder-not-a-status]])
- `concepts/` are non-functional requirements and `entities/` are functional, and only there is a shared slug required ([[concepts-are-non-functional-requirements-and-entities-are-functional]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *what a page is called and what kind it is* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is the script's pick and it is served by nothing yet.** `page-naming` is the `authority:` of [[filenames-carry-no-category-prefix]], the earliest-decided member and the page named in `decided_by:`. No `concepts/` or `entities/` page of this family carries a slug — the members are decisions and one proposal — so there was no live page to converge on, and the hook matches nothing here until one is written or an existing page takes the slug. That is the sharper gap in this set: the family answers where a page goes and what it is called, which is a question asked at the moment a page is created and not while an existing one is read.
