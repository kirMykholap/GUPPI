---
title: "The `sources:`-path-existence verdict has no rule number of its own, and the pages that give it one disagree"
type: lesson
status: archived
authority: verdict-number-drift
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check.sh"]
tags: [vault, harness, retrieval]
---

# What the code says

**It is emitted inside rule 2's single frontmatter pass**, at `scripts/vault-check.sh:453`. It is
not a rule of its own and it has no number.

# What the corpus says

Three pages call it **rule 5** — [[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]],
[[a-path-detector-for-prose-references]], [[moving-raw-into-a-dated-archive]] — and two call it
**rule 11** — [[raw-holds-testimony-and-artefacts-are-frozen]],
[[fidelity-to-a-source-and-fidelity-to-the-tree]].

**The numbering drifted when rule 9 was retired on 2026-08-17**
([[a-rule-over-every-page-makes-every-test-fragile]]). Every page written before that day used one
scheme and every page after it used another, and nothing renumbered anything.

# The resolution, and it is the schema's own

**The script wins on `basis`.** A page whose basis is `code` loses to the code
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]). None of the five pages is
edited to say otherwise; they are wrong about a label and right about the behaviour, which is the
distinction that matters here.

# The rule that follows

**Acceptance for anything keys on the verdict STRING, never on the number.** A rule number is an
ordinal in a file that gets rules added and retired; a verdict's text is what the check actually
prints and what a `grep` can find. This is the same argument that made every sprint criterion name
its command rather than its expectation ([[a-sprint-closes-on-its-goal]]).

**And a number written into prose is a copy.** Five copies, drifting in two directions, is the
signal the store already has a repair for: delete the copy rather than correct it
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).
