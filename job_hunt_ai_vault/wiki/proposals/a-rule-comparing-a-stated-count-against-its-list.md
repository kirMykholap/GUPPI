---
title: "A rule that compares a stated count against the list it heads, where every instance sits in prose a script could reach"
type: proposal
status: current
authority: count-check-design
basis: measurement
sprint: S1
created: 2026-08-15
sources: ["archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", "scripts/vault-check.sh", "log.md"]
decided_by: [[the-audits-findings-are-owed-to-the-owner]]
tags: [vault, testing]
---

# The evidence is already gathered; only the rule is missing

[[a-stated-count-drifts-from-the-list-it-heads]] carries **thirteen measured instances** — three on
2026-08-14, three more the same day inside the store diagnosing the disease, six found by the first
`/vault-lint` on 2026-08-15, and the audit's own arithmetic drifting by one while it was writing
them down. The lesson page ends with *"no such rule exists yet, and writing one is a `/lint`
proposal rather than an ingest's act."* **This is that proposal.**

**Nothing here is decided.**

## What the rule would compare

The failure has one shape: a sentence states a number, and immediately below it stands the thing
counted. The list is edited; the number is not.

| written | followed by |
|---|---|
| "five AST boundary tests" | a table of seven rows |
| "four pairs of pages" | three bullets |
| "18 failing conditions" | a numbered list ending at 18 — the case that passes |

So the mechanical form is: **a cardinal in a line, and a countable block starting within the next
line or two — a markdown table, a bullet list, or a numbered list.** Compare, and report a
mismatch. It would be an advisory rather than an error, at least at first: the false-positive rate
is unknown and a rule that fails a build on prose is a rule people route around.

## Why it is plausible here and not in general

Two properties of this corpus make it tractable, and both are already relied on by other rules:

- **the pages are markdown with a small grammar** — `vault-catalogue.sh` already parses tables and
  `vault-units.sh` already classifies a line as heading, bullet, numbered item or paragraph
  opener, so the block detector exists in two scripts already ([[vault-scripts]]);
- **one `awk` pass over the corpus is the established budget.** The check runs after every write
  and must stay cheap enough to actually be run, which is why `vault-check.sh` reads frontmatter in
  a single pass rather than grepping per field per page.

## What is open

- **False positives, which are the whole risk.** "Three instances were found on 2026-08-14 alone"
  heads a table of three — good. "Six pages said what the repository no longer does" heads nothing
  at all — a number with no list is not a defect, and the rule must ignore it silently or it
  reports half the corpus.
- **Numbers written as words.** *"five"*, *"seven"*, *"thirteen"* are the actual spelling in most
  of the thirteen instances, so a digit-only rule catches the minority.
- **Whether it belongs in `vault-check.sh` at all.** The alternative is an item of `/vault-lint`,
  run once a sprint by a librarian, which needs no parser and finds the word-spelled cases for
  free — against a cost of one dispatch ([[agent-round-trip-cost]]).
- **The cheaper half nobody has argued against.** The measured discipline already works:
  **"N at `<commit>`" was right every time and "it is now N" wrong every time.** A rule that merely
  flagged present-tense counts would catch the drift class without counting anything.

## What it would oblige

If it lands in `vault-check.sh`, it is a rule that reads every page — so it will break unrelated
selftest cases the day it is added, and the fix belongs in the harness
([[a-rule-over-every-page-makes-every-test-fragile]]). It also owes its own selftest cases, because
a check never observed failing is not known to check anything
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

And it would need to survive its own first run: the corpus contains counts today, on the very page
that argues for it.
