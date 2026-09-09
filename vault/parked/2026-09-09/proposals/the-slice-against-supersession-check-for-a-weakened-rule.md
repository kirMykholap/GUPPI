---
title: "The slice-against-supersession check: a rule's text changed and no supersession came with it"
type: proposal
status: current
authority: rule-weakening-detector
basis: inference
sprint: S3
created: 2026-08-25
decided_by: [[the-ask-before-weakening-rule-gets-a-claude-rules-file-and-the-owner-as-its-watcher]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# What it would be

**Weakening a rule has a mechanical signature the store already defines**: the `<!-- text -->` slice
of a rule page changed, and no supersession accompanied the change
([[what-travels-from-a-rule-page-is-a-marked-slice]], [[a-deprecated-rule-does-not-render]]).

**The observing half is a `git diff` of the slice against `HEAD`, per changed rule page.** Whether a
page changed is a diff rather than a judgement, which is what makes it something a script can ask.

# What it does not cover, and the gaps are the reason it is not the rule

- **It is coarser than the rule.** A typo inside the slice fires it.
- **It covers the text half alone.** Working around a rule in code leaves no slice diff at all, and
  that is the larger half of what the rule forbids
  ([[ask-before-weakening-or-working-around-a-rule]]).

# Its status

> **owner:** «Наблюдать буду пока что я сам»

**Deferred, not refused.** The delivery half of the rule is being built as a `.claude/rules/` file
and the owner is the watcher until this exists.

# What it would oblige

**A verdict that fires on a correct edit needs an exit**, and none is designed: nothing says how a
legitimate slice correction is declared. **That is the open question a build starts from**, and the
answer must not be a page declaring itself exempt
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).
