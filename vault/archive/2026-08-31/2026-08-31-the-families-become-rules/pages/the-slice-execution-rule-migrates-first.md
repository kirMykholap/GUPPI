---
title: "The slice-execution rule migrates first, because no test can ever hold it"
type: decision
status: archived
authority: first-migrant
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
tags: [harness, process, vault]
---

# Decided by the owner on 2026-08-17, on the admission test

Of the four rules in the repository's `CLAUDE.md` that could not wait for a question, **the one about
how a slice is executed went first** ([[the-owner-decides-how-a-slice-is-executed]]).

**The test he chose it on:** a paragraph becomes a rule page if it is imperative and **not enforced by
a test**; where a test holds the rule, the test is the rule
([[the-harness-is-compiled-not-maintained]]). Of the four, **this is the only one no test can ever
hold**:

| Rule | What holds it besides the prose |
|---|---|
| never run the suite against the production database | `tests/conftest.py` and the `TEST_DATABASE_URL` fixture |
| fix an AST boundary failure at its cause | the AST boundary tests themselves |
| our JavaScript does not choose which rows are on screen | an owed test, named and not yet written |
| **how a slice is executed is the owner's** | **nothing, ever** — it is a fact about who decides, and no test can assert it |

**Rejected: migrating the cheapest one first**, or all four at once. The first migration is when a
region can land in the wrong file, so it was deliberately the one whose loss would cost most — the
rule *another document will actively argue you out of*.

## What it obliges

- **The fifth verdict went in before this migration, not after.** That ordering was the owner's and it
  was not a preference ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).
- **The slug is not `how-a-slice-is-executed`.** That basename belongs to the decision page behind the
  rule, and two pages sharing one would make every wikilink to either ambiguous. A rule answers with
  `governs:` and never with `authority:`, so the pair does not read as a duplicate claim
  ([[rules-becomes-a-type-of-its-own]]).
- **The other three followed within the day**, and five more blocks after them
  ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).
