---
title: "The region a rule renders into"
type: rule
status: current
authority: region-form
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-governed-file-with-no-region-is-an-advisory]]
tags: [harness, vault, testing]
---

# The region a rule renders into

The markers, their form, their placement, and the verdicts that read them. Answers "what does the rendered block look like, and where does it go".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A `[[wikilink]]` inside a rendered slice is red rather than an advisory ([[a-wikilink-inside-a-rendered-slice-is-red]])
- A governed file carrying no region is an advisory, and red is reserved for markup that is broken ([[a-governed-file-with-no-region-is-an-advisory]])
- The address verdict joins the rule that already holds every region, instead of becoming a rule of its own ([[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]])
- The injector writes the paragraph separator, and it goes inside the region ([[the-injector-writes-the-separator-inside-the-region]])
- The marker becomes `<!-- [type]: slug -->`, with the script substituting the record's type ([[the-marker-carries-the-records-type]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *the region a rule renders into* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, which here is `region-absence-verdict` — one verdict about one absence, and a page that leaves for `archive/`. Four live concepts of this family were available; the slug carried is `region-form`, which [[a-region-is-a-paired-comment-named-for-a-rule]] carries and keeps. That concept is what the family is about — what a region looks like and where it goes — while the other three each describe how a marker is detected or judged. `decided_by:` still names a member decision, which is what this folder requires.
