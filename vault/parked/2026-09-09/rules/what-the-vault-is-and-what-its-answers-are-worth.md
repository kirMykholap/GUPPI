---
title: "What the vault is and what its answers are worth"
type: rule
status: current
authority: vault-artefacts
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[the-handoff-splits-into-a-handoff-and-a-knowledge-base]]
tags: [vault, process, architecture]
---

# What the vault is and what its answers are worth

Why the store exists, its root principle, what ranks one page's claim against another's, and how a claim from it has already been misread. Answers "how much may I lean on this page".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A wrong record is acceptable and an invisible one is not, which is the principle under the whole store ([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]])
- The handoff splits: it stays a handoff, and everything that outlives a session becomes a knowledge base ([[the-handoff-splits-into-a-handoff-and-a-knowledge-base]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *what the vault is and what its answers are worth* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `vault-origin`, whose decision leaves for `archive/`. Three live pages of this family were available; the slug carried is `vault-artefacts`, which [[journal-vault-brief-each-artefact-has-one-owner]] carries and keeps. Both clauses here are about what the store is and what it is for, which is that concept's own question; `fidelity-axes` answers the other half of the family name — what an answer is worth — and `vault-location` is about the directory. `decided_by:` still names a member decision, which is what this folder requires.
