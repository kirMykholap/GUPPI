---
title: "The gate advisory on a live link into a deprecated page is ordered built, and the refusal of it is overturned"
type: decision
status: archived
authority: archive-citation-advisory
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
supersedes: [[the-live-to-archive-citation-advisory-is-refused-in-full]]
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-check.sh"]
tags: [vault, harness, retrieval]
---

# The ruling, 2026-08-28

*(the owner selected it, from the session's proposal.)*

**The gate keys on the target's `status:`** — a live page links a slug whose page carries
`status: deprecated` — **and prints an advisory, never a red.**

**It does not classify the kind of citation.** A vocabulary-keyed test inverts on the
retirement-policy pages themselves: they are the pages that talk about deprecation, so the words a
classifier would key on occur there for the opposite reason. **What kind of citation it is, is the
reading agent's work** ([[the-decisions-agent-reads-only-and-runs-at-every-ingest]]).

# What this overturns, and what it leaves standing

**Overturned: the refusal of 2026-08-26**, «я вообще не вижу смысла добавлять такое в гейт …
Ничего не строим дополнительно», which refused the class rather than a size of it
([[the-live-to-archive-citation-advisory-is-refused-in-full]]).

**Left standing: a live page citing a deprecated one is still legal.** An advisory names it; nothing
forbids it. That is why the verdict is an advisory and not red, and it is the same asymmetry the
filename half of rule 10 carries ([[a-live-page-can-argue-from-a-deprecated-one]]).

# The measurement the reversal was taken against — 2026-08-28

**Over the whole of `wiki/`: 42 slugs carrying `status: deprecated` in `archive/`, 424 link
occurrences, 332 distinct page-target pairs, 210 distinct live pages.**

**Classified by hand, reading all 424 sentences**: about 197 occurrences on about 140 pages lean on
the target **as if it were live**; about 109 are supersession references; about 108 are historical;
about 10 are unclear. The bounds on that split are plus or minus ten per cent.

**Two named cases, and one of them is the most expensive rule here.**
`wiki/rules/the-suite-never-runs-against-the-production-database.md` carries
`decided_by: [[claude-md-is-a-map-and-four-rules]]`, and that target is deprecated in `archive/`;
`an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test` has the same defect.
`moving-a-rule-into-claude-rules-with-a-paths-scope` is cited 13 times across 12 live pages, none of
them marked, and it is the criterion other pages decide by whether a rule may move.

**The earlier figure of 76 pages over 24 targets was a reading of `wiki/decisions/` alone**
([[a-figure-measured-over-one-folder-was-reported-as-a-reading-of-the-corpus]]).

# Not built

**No code exists.** It is the third of three build items and the owner stopped the session after the
first ([[the-archiving-sweep-and-the-dead-link-advisory-move-to-the-next-session]]). The design is a
proposal ([[the-gate-advisory-naming-a-live-link-into-a-deprecated-page]]).
