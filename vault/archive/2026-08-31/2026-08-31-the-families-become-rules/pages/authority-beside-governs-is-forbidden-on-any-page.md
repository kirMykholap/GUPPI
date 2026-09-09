---
title: "`authority:` beside `governs:` is forbidden on any page, not only inside `wiki/rules/`"
type: decision
status: archived
authority: authority-beside-governs
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh"]
tags: [record-schema, harness, vault]
supersedes: [[authority-beside-governs-on-a-non-rule-page-is-unruled]]
---

# Decided by the owner on 2026-08-18: a page that renders does not also own a question

> **owner: `authority:` beside `governs:` on a non-rule page is forbidden.**

The prohibition already existed for `wiki/rules/`, on a rule-specific argument: a decision and the
rule stating it share a slug, so a rule claiming an `authority:` reads as a contradiction against
the decision it renders ([[rules-becomes-a-type-of-its-own]],
[[governs-uniqueness-is-removed-and-the-pair-carries-it]]). Since `governs:` became a property of
any page ([[governs-becomes-a-property-of-any-page]]) the same shape was expressible outside that
folder and nothing ruled on it.

**Rejected: allowing it.** The cost of allowing it was written down before the ruling — the
duplicate-`authority:` check would have to tolerate the decision-and-record pair for some pages and
not others, which is a rule with an exception nobody can apply from the outside.

**The owner's ground was not the check.** Both non-rule renderers had already done without the field
and neither lost anything by it ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]), and **leaving it unruled costs a
question every time** — every page that renders would have to reason it out again, and reasoning it
out from inside the vault is how a question gets answered by accident.

## What it obliges, and what is not yet built

- **A rendering page carries `governs:` and no `authority:`.** The question it would have owned goes
  to the decision or the concept behind it, which is the split both existing renderers already made.
- **The check does not enforce this yet.** The `ruleclaim` branch of `vault-check.sh` is gated on
  `folder == "rules"` and was left that way on purpose, so the question would stay askable
  ([[the-governs-branch-widens-and-the-others-stay-rules-only]]). It has been answered, so the gate
  is now narrower than the rule — a work item with a selftest case owed, and until it lands this
  page is prose that nothing stops an agent from breaking
  ([[no-rule-reads-a-harness-file]], [[knowing-a-rule-is-not-a-mechanism]]).

## The gate now exists, 2026-08-19

**The last clause above — *"the check does not enforce this yet"* — stopped being true on
2026-08-19.** The `ruleclaim` branch of `vault-check.sh` no longer asks what folder a page is in; it
fires on **any** page carrying `authority:` beside `governs:`
([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]). The owed selftest case
landed with it, proved against the pre-change script.

**So this page is no longer prose that nothing stops an agent from breaking.** The paragraph above is
left standing as the reading of 2026-08-18, which is what it was
([[a-title-corrected-in-place-is-not-a-supersession]]).

**One instance was found while the rule was still prose**, and it is the vault's own schema file: the
frontmatter example in `job_hunt_ai_vault/CLAUDE.md` carries both fields under `type: concept`. It is
a field catalogue rather than a page, its comments state the exclusion in words, and the gate does not
read it — but it is a block written to be copied, and a page copied from it would have landed outside
the old branch. Named here rather than repaired, because it belongs to whoever next edits that file
([[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]]).
