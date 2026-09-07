---
title: "How a measurement is written down"
type: rule
status: current
authority: measure-region-spelling
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-measure-line-names-its-destination-in-brackets-after-the-kind]]
tags: [vault, record-schema, process]
---

# How a measurement is written down

Whether a number is testimony for a claim or a gauge of how much now, where each lives, and the marked section they are written in. Answers "this number — where does it go".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A `measure:` line names its destination in brackets straight after the kind ([[a-measure-line-names-its-destination-in-brackets-after-the-kind]])
- A measurement is testimony or a gauge, and the role of the number decides where it lives ([[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]])
- The measure section's grammar is one line per number, and a gauge line names the command instead of a value ([[the-measure-section-grammar-is-one-line-per-number]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *how a measurement is written down* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `measure-destination-syntax`, whose decision leaves for `archive/`. Two live pages of this family were available; the slug carried is `measure-region-spelling`, which [[the-measure-regions-spelling-fences-the-command-in-backticks]] carries and keeps. Every clause here is about the written form of a measurement, which is that concept's own subject; `measure-writer-script` is the tool that fills a gauge and answers a different question. `decided_by:` still names a member decision, which is what this folder requires.
