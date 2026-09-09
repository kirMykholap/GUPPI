---
title: "A deferral with a proposal behind it, and the decision nobody compiled"
type: rule
status: current
authority: missing-decision-compilation
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[the-missing-decision-pages-are-written-by-the-nearest-ingest]]
tags: [vault, process, record-schema]
---

# A deferral with a proposal behind it, and the decision nobody compiled

The rulings that produced a proposal and were never written as a page, and the proposals that therefore named no cause. Answers "who ruled on this proposal, and when".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A deferral repeated again names the sprint it happens in, or it is refused ([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]])
- The missing decision pages behind the empty `decided_by:` fields are written by the nearest `/ingest` ([[the-missing-decision-pages-are-written-by-the-nearest-ingest]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *a deferral with a proposal behind it, and the decision nobody compiled* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is the script's pick and it is served by nothing yet.** `missing-decision-compilation` is the `authority:` of [[the-missing-decision-pages-are-written-by-the-nearest-ingest]], the earliest-decided member and the page named in `decided_by:`. Six of this family's eight slugs are carried by no live page at all and the remaining two are decisions, so there was nothing to converge on; the hook matches nothing here until a page outside `decisions/` takes one of these slugs.
