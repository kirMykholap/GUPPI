---
title: "A copy of a list drifts"
type: rule
status: current
authority: derived-register-proof
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]
tags: [vault, harness, process]
---

# A copy of a list drifts

Why a duplicated list is repaired by deleting it rather than extending it, and where a copy has already gone stale here. Answers "should I write this list down a second time".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A copy that keeps drifting is repaired by deleting it, not by adding the missing row ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]])
- The librarian stops writing the *Compiled from* signature, because `sources:` already carries it ([[the-librarian-stops-writing-the-compiled-from-signature]])
- The page list is a query, and the conclusion of the generated catalogue outlived its mechanism ([[the-page-list-is-a-query-not-a-generated-file]])
- `record-schema` is dropped from the live trim candidates, and the advisory still prints ([[record-schema-is-dropped-from-the-trim-candidates]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *a copy of a list drifts* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `drifting-copy-repair`, whose decision leaves for `archive/`. The slug carried instead is `derived-register-proof`, which [[a-printed-register-cannot-drift-and-a-maintained-one-always-has]] carries and keeps: that concept states the family's claim in general — a copy of a list is what drifts, and a derived one cannot — where the other live candidate, `mapping-location`, is one instance of obeying it. `decided_by:` still names a member decision, which is what this folder requires.
