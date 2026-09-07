---
title: "What the owner said, and what was put in his mouth"
type: rule
status: current
authority: retro-ratification
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]]
tags: [process, vault, harness]
---

# What the owner said, and what was put in his mouth

How a line comes to be attributed to the owner, what separates his own words from a session's paraphrase of them, and the mechanisms that check the difference. Answers "is this sentence his, and may I reason from it as his". Added 2026-08-22, after a rule he had never given stood for three days as a quotation stamped `basis: human` and decided three things. Separate from "how the owner is asked", which is about putting a question to him: this family is about what comes back and how it is written down.

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A paraphrase that survived ratification keeps `basis: human` and is not downgraded to `inference` ([[a-paraphrase-that-survived-ratification-keeps-basis-human]])
- A ratification sweep may run inside a session when the list is assembled in advance and shown whole ([[a-sweep-may-run-inside-a-session-when-the-list-is-assembled-in-advance-and-shown-whole]])
- Every line of a plan's ratification list carries its source ([[every-line-of-a-plans-ratification-list-carries-its-source]])
- The `owner:` signature is removed where the words are not his, and the block is rewritten in the session's voice ([[the-owner-signature-is-removed-where-the-words-are-not-his]])
- The alphabet test behind the owner-block advisory is overturned, and the ratification step carries the weight ([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]])
- The ratification is one decision over a list shown whole, and not a signature per block ([[the-ratification-is-one-decision-over-a-shown-list-and-not-a-signature-per-block]])
- The retro ratifies every line before it is attributed to the owner ([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]])
- The retro records a ruling chosen from a menu, and ratifies decisions rather than utterances ([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]])
- The retro's verdicts are set by the session and brought to the owner as one block ([[the-retro-verdicts-are-set-by-the-session-and-brought-as-one-block]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *what the owner said, and what was put in his mouth* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is the script's pick and it is served by nothing yet.** `retro-ratification` is the `authority:` of [[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]], the earliest-decided member and the page named in `decided_by:`. No `concepts/` or `entities/` page of this family carries a slug at all — every member is a decision or a proposal — so there was no live page to converge on, and the hook matches nothing here until one is written or an existing page takes the slug.
