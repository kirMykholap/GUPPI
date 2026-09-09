---
title: "A rule page and the slice that travels"
type: rule
status: current
authority: rules-folder-inventory
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[rules-becomes-a-type-of-its-own]]
tags: [vault, harness, process]
---

# A rule page and the slice that travels

What makes a page a rule, what part of it is rendered elsewhere, and how rules are numbered and ordered. Answers "should this be a rule, and what of it leaves the page".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A definition may render into the repository's `CLAUDE.md`, not only an imperative or a sourced assertion ([[a-definition-may-render-into-the-repository-claude-md]])
- A migrating rule leaves the numbered list for a block of its own, and ships no ordinal ([[a-rule-leaves-the-numbered-list-and-carries-no-ordinal]])
- A retired rule number is never reused, because the corpus cites rules by number ([[a-retired-rule-number-is-never-reused]])
- A rule ships one piece of text or it is more than one rule, which is why `## Language` is one page ([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]])
- The slice-execution rule migrates first, because no test can ever hold it ([[the-slice-execution-rule-migrates-first]])
- What travels from a rule page is a marked slice, and everything outside the mark stays home ([[what-travels-from-a-rule-page-is-a-marked-slice]]) — **narrowed permanently on 2026-08-31 to the rendering modes**: a page under `render: authority` renders into no file, so it carries no slice and none is owed ([[the-cleanup-suspends-the-rules-that-would-refuse-it]])
- `rules` becomes a type of its own, and a script injects each rule where it governs ([[rules-becomes-a-type-of-its-own]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *a rule page and the slice that travels* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, which here is `rules-type` and belongs to a decision that leaves for `archive/`. The slug carried instead is `rules-folder-inventory`, which [[wiki-rules-holds-the-rules-of-the-repository-claude-md]] carries and keeps: that entity is the description of this folder, so anyone reading what `wiki/rules/` holds is handed the rule about what a page in it must be. `decided_by:` still names a member decision, which is what this folder requires.
