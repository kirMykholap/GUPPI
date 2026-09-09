---
title: "Admitting a frontmatter field"
type: rule
status: current
authority: field-admission-test
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-decision-declares-whether-it-binds]]
tags: [vault, process, record-schema]
---

# Admitting a frontmatter field

What a new field has to earn before it exists, what a self-declaration costs, and the fields that were admitted or withdrawn. Answers "may I add a field for this".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A `decided_by:` pointing into `archive/` is kept as it stands, and becomes a candidate for a lesson ([[a-decided-by-target-in-the-archive-is-kept-and-becomes-a-lesson-candidate]])
- A decision declares whether it binds, and `binding:` is required in `decisions/` ([[a-decision-declares-whether-it-binds]])
- A proposal keeps an absent `decided_by:` rather than a false `idea` mark ([[a-proposal-keeps-an-absent-decided-by-rather-than-a-false-idea-mark]])
- The English-migration proposal keeps its `sources:` line beside its `decided_by:` field ([[the-english-migration-page-keeps-its-sources-line-beside-its-decided-by-field]])
- The `Links:` field and the script that would have filled it are refused, on the owner's reading of his own graph ([[the-links-field-and-the-script-that-would-fill-it-are-refused]])
- The `decided_by:` back-fill is read off each page's sources, and `status: idea` is set only where no decision exists ([[the-decided-by-back-fill-is-read-off-each-page-and-never-swept]])
- `authority:` becomes the index a claim is looked up in, and is required on every page outside `wiki/rules/` ([[authority-becomes-the-index-and-is-required-outside-rules]])
- `decided_by:` is a field of its own, not a line in `sources:` and not a link in the body ([[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]])
- `decided_by:` is legal in `wiki/proposals/` and `wiki/rules/` alone, and required in `wiki/rules/` ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *admitting a frontmatter field* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `decision-binding` — which is about one admitted field rather than about admission, and whose decision leaves for `archive/`. The slug carried instead is `field-admission-test`, which [[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]] carries and keeps: that concept is the test this family exists to state. The other live candidate, `silencing-declaration`, is what a bad admission costs and not what decides one. `decided_by:` still names a member decision, which is what this folder requires.
