---
title: "`asserts:` would be a closed predicate set with a flat, line-oriented syntax"
type: proposal
status: current
authority: asserts-field-design
basis: human
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "scripts/vault-check.sh"]
decided_by: [[what-the-harness-build-waits-on]]
tags: [harness, testing]
---

# The half of the harness that keeps the tree honest

Where a marked region keeps the harness **saying** what the vault holds, `asserts:` keeps the tree
**being** what a rule claims ([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]). It is
the field that would catch *"four types where five folders exist"* and a path a file move made
false.

**Two properties, and both are forced rather than chosen.**

**Closed**, because the pages are written unattended ([[the-librarian-writes-unattended]]). An
arbitrary shell predicate in a page's frontmatter would let the store **execute what an agent
wrote** — the gate would run it on every check, in the repository, with whatever the agent typed.
**An unknown predicate name is itself a failure**, which is what makes the set closed in fact rather
than in wording.

**Flat and line-oriented**, because there is no YAML parser available here: PyYAML is absent, the
standard library has none, and every existing script parses frontmatter line-wise in `awk`
([[vault-scripts]]). A nested structure would mean writing a parser before writing the first
predicate.

## What is open, and it blocks everything

**Four predicates are sketched; the full set and the rule for growing it are not agreed.** This is
the item with the largest blast radius on [[what-the-harness-build-waits-on]] — nothing downstream
can be written without it, including the entity pages about the application
([[entities-describe-the-application-once-the-detector-exists]]).

The growth rule matters as much as the set: a closed set that anybody may extend is an open set
with extra steps, and the cost of adding a rule that applies to every page is already measured
([[a-rule-over-every-page-makes-every-test-fragile]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).
