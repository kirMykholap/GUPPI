---
title: "Where a rule's text is sent"
type: rule
status: current
authority: rule-delivery-modes
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[governs-is-a-path-from-the-repository-root]]
tags: [harness, vault, record-schema]
---

# Where a rule's text is sent

`governs:` and `paths:` — the destination, how it is resolved, who may carry it, and what the governed set is. Answers "which file does this rule end up in".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- The JavaScript rule leaves `wiki/rules/` for `decisions/` with `binding: prohibition`, and the region goes in the same change as `governs:` ([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]])
- The `governs:` destination-uniqueness verdict is removed, and uniqueness moves onto the file-and-slug pair ([[governs-uniqueness-is-removed-and-the-pair-carries-it]])
- The `ruleclaim` verdict widens to any page carrying `authority:` beside `governs:`, and `nogoverns` stays rules-only ([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]])
- The conditional-delivery gate covers any departure from unconditional delivery, wherever the rule goes ([[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]])
- The feedback region leaves `vault-ask`, and that destination leaves the rule page's `governs:` list ([[the-feedback-region-leaves-vault-ask-and-the-destination-leaves-the-rules-governs-list]])
- The feedback rule's extra destination is withdrawn, on the page that forbids governing a file the ritual empties ([[the-feedback-rules-extra-destination-is-withdrawn]])
- The governed set is swept rather than listed, and it is markdown by a property ([[the-governed-set-is-swept-and-markdown-by-property]])
- The owner-block rule gains the repository's `CLAUDE.md` as a destination ([[the-owner-block-rule-gains-the-repository-claude-md-as-a-destination]])
- The rule about rules is served by the hook on a touch of `wiki/rules/`, and is rendered into no file ([[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]])
- `authority:` beside `governs:` is forbidden on any page, not only inside `wiki/rules/` ([[authority-beside-governs-is-forbidden-on-any-page]])
- `governs:` is a path from the repository root, and the vault's name is fixed from now on ([[governs-is-a-path-from-the-repository-root]])
- `governs:` is a property of `wiki/rules/` alone, and a page that renders is a rule ([[governs-is-a-property-of-wiki-rules-alone]])
- `governs:` takes a bare path or an inline list, and the block form is red rather than silent ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]])
- `paths:` is required where it is read, and nowhere else ([[paths-is-required-where-it-is-read-and-nowhere-else]])
- `paths:` lives on the vault page, the injector syncs it, and it is written with the widest true pattern ([[paths-lives-on-the-vault-page-and-is-written-widest]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *where a rule's text is sent* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, which here is `governs-path-resolution` — a decision about how one path is spelled, and a page that leaves for `archive/`. Six live concepts of this family were available; the slug carried is `rule-delivery-modes`, which
[[a-rule-reaches-a-session-by-several-routes-and-only-one-transition-had-a-gate]] carries and keeps. That concept is the family's question at its widest — by what route a rule's text reaches anyone — while the other five each answer one route or one verdict inside it. `decided_by:` still names a member decision, which is what this folder requires.

**One slug of this family is deliberately not taken here.** `rule-about-rules-delivery` belongs to
[[a-rule-page-carries-a-family-slug-and-the-decision-that-caused-it]], the rule about rules, which the same family produced and which is a page of its own.
