---
title: "A governed file carrying no region is an advisory, and red is reserved for markup that is broken"
type: decision
status: archived
authority: region-absence-verdict
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [harness, testing]
---

# Decided by the owner on 2026-08-17: advisory

Rule 11 of `vault-check.sh` goes **red** for markup that is broken — an unclosed marker, a close
with no open, a close carrying the wrong slug, nesting, one slug marking two regions in a file, a
marker not alone at column zero, a region whose `wiki/rules/<slug>.md` is absent, and an
unterminated code fence. A governed file carrying **no** region prints **one advisory line** and
fails nothing.

**Rejected: red on absence, with an exemption list.**

## Why the stricter rule could not have been written

**Markup is gradual and starts at zero.** A rule that fails a governed file with no region would
have been born failing on every governed file in the tree — thirteen of them — and would have
needed its exemption list written **before a single region existed**. That list could only have
been guessed at, and a guessed exemption list is the artefact this project has watched go stale
fastest ([[a-copied-list-drifts-and-a-sweep-cannot]]).

The advisory instead reports a number that shrinks as markup proceeds: **`0 of 13` on the day it
was built**, over a denominator that is swept rather than listed
([[the-governed-set-is-swept-and-markdown-by-property]]).

## The blocker it removed, and how

*Which files may be exempt from "no region means red"* was **one of the three items blocking the
harness build** ([[what-the-harness-build-waits-on]], [[marked-regions-and-the-prose-outside-them]]).
It was not answered. **The design changed so that the question stopped existing** — a distinction
worth keeping, and it has its own page: [[a-blocker-can-be-dissolved-instead-of-answered]].

## The shape of the advisory is itself decided

One line, with the names sorted — not one line per file
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

# The advisory now asks a wider question — 2026-08-20

**A governed file satisfies the coverage reading by carrying a region *or* by carrying the
generation marker**, on the owner's rewording of the criterion
([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]]). The advisory line reads
`a region or whole generation covers 2 of 15`.

**The marker is counted in the pass that already reads every governed file**, not by a grep per
file — the same discipline the value enumeration follows
([[a-fields-legal-values-live-beside-its-legal-keys]]).

**Nothing about the verdict's severity moved.** Absence is still an advisory and red is still
reserved for markup that is broken; the argument above — that a stricter rule would have been born
failing on every governed file, needing an exemption list guessed at before a single region existed
— is untouched.

**What changed is that a member arrived which could never satisfy the narrower question.** A file
generated whole carries a marker and not a paired region by construction, so the criterion had
acquired a case it could not describe ([[the-generated-ast-boundaries-rule-file]],
[[hiding-a-file-from-a-denominator-is-weaker-than-counting-it-as-handled]]).

# The interim state of a half-finished landing is red, and it is not this advisory — 2026-08-22

**A rule page written before its destinations carry markers makes `bash scripts/vault-check.sh` exit
1.** Rule 12 asks its question by **running the injector**, and an unlanded rule makes the injector
print `note` lines, which are red ([[a-check-asks-by-running-the-writer-it-checks]]).

**This page governs the other verdict.** Rule 11's *absence* verdict — a governed file carrying no
region — is the advisory, and it never fails a run. **They are different questions about the same
half-finished state**, and the difference is which end is missing: a governed file with no rule page
is an advisory, a rule page with no region in its destination is red.

**A session told to expect an advisory reads the non-zero exit as a defect.** It happened on this
date: the librarian's own note said to expect the advisory, and the run exited 1 for the other reason
while the landing was half-done. **The state clears the moment the markers are placed and the
injector runs**, which is a step of the landing rather than a repair
([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]).
