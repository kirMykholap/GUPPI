---
title: "The no-quantity rule"
type: rule
status: current
authority: title-check-mechanism
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-title-names-what-is-counted-instead-of-counting-it]]
tags: [vault, retrieval, harness]
---

# The no-quantity rule

Why a title and a filename carry no measurable quantity, which words count, and what the check does about it. Answers "may this number be in the title".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A title carries no measurable quantity, and names what is counted instead of counting it ([[a-title-names-what-is-counted-instead-of-counting-it]])
- Ordinals count in a title and in a filename, `first` does not, and every word in the list is a promise ([[ordinals-count-and-first-does-not]])
- The `quantity:` field is rejected, the rule stays unconditional, and the corpus is cleaned before the check is tightened ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]])
- The length of a title is deliberately unbounded, and no check measures it ([[the-length-of-a-title-is-unbounded-and-no-check-measures-it]])
- The no-quantity rule extends to filenames, and the renames wait on the rewriter-and-detector pair ([[the-title-rule-extends-to-filenames]])
- The no-quantity rule reads the title and the filename, and never the body: a counting subheading is prose ([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *the no-quantity rule* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `title-quantities`, whose decision leaves for `archive/`. The slug carried instead is `title-check-mechanism`, which [[the-title-check-asks-and-the-answer-is-a-retitle]] carries and keeps — the one live `concepts/` or `entities/` page in this family, and the half of the family's own definition that asks "what the check does about it". `decided_by:` still names a member decision, which is what this folder requires.
