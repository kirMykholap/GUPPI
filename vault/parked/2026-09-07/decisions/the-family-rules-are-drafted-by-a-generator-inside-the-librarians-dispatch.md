---
title: "The family rules are drafted by a generator, and it runs inside the librarian's dispatch"
type: decision
status: current
authority: family-rule-authorship
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-31
created: 2026-08-31
target_kind: action
target: build-family-rules-py-is-run-by-the-librarian-and-its-output-read-whole
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "scripts/build-family-rules.py", ".claude/hooks/lock-the-librarian.ps1", "scripts/vault-check.sh"]
tags: [vault, harness, agents]
---

# Context

**The librarian is the only writer of `wiki/` and of the registers**, and a family rule page is a
`wiki/rules/` page. **The clauses are already machine content**: a family rule's clause is the title of
one decision, lifted out of frontmatter, because only two of the 295 prohibitions the cleanup surveyed
carried a written `# The rule text` section of their own
([[a-family-rules-clauses-are-drafted-from-titles-because-a-title-names-its-claim]]).

**Writing nineteen such pages by hand is transcription**, and doing it for the harness-facing families
later would be transcription again.

**Files and pages this touches:** `scripts/build-family-rules.py`,
`.claude/hooks/lock-the-librarian.ps1`, `scripts/vault-check.sh`, `job_hunt_ai_vault/index.md`,
[[the-steward-is-scripts-that-run-after-the-librarian]],
[[hand-edits-of-the-wiki-are-a-recorded-divergence]].

# The question

**Does the librarian author the family rule pages by hand, or does a generator draft them?**

# How it works after

**A generator drafts them, under the librarian's dispatch.** `scripts/build-family-rules.py` writes one
page per vault-facing family and refuses outright to write a title carrying a measurable quantity. **The
librarian reads the output whole, repairs it, and answers for it** — which is what keeps the one-writer
clause meaning something. On the day it ran, four repairs were applied to all eighteen drafts and a
nineteenth page was written by hand.

**The generator must run *inside* the dispatch, and that is a property of the mechanism rather than a
preference.** Both orders redden the gate:

- **pages first** — rules 4 and 5 build the linked set from `wiki/`, `archive/`, `index.md`, `tags.md`
  and `sprint.md`, and nothing points at a page just created, so eighteen orphans;
- **`index.md` lines first** — nineteen wikilinks resolving to nothing.

**A red gate locks the librarian out through `.claude/hooks/lock-the-librarian.ps1`, and the librarian
is the only party who may write `index.md`.** So neither order can be split across two dispatches: one
party has to hold both writes, and that party is the librarian
([[one-page-written-into-the-wiki-reaches-the-register-deadlock]]).

**This works around the one-writer clause by permission rather than by argument**, which is why it is
written down. It is not a widening: the pen stays the librarian's and the generator is a drafting tool
it runs, in the same relation as `scripts/vault-inject.sh`. What would move the clause is a generator
run by anyone else, and nothing here permits that.

# Recommendation

**The session recommended the librarian author them by hand** and the owner chose the generator, having
heard that the clauses are machine content already. **Rejected: hand-authoring nineteen pages of lifted
titles.**

**Rejected by mechanism rather than by choice: running the generator outside the dispatch.** The
session tried it, produced eighteen orphan pages, reddened the gate, and was locked out of the file
that would have cleared them. It reverted and re-ran correctly.

# Ratification

**owner selected, 2026-08-31: «генератором».** Put to him as a recommendation against a generator, and
he took the other option.

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
