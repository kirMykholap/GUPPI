---
title: "The handoff template moves out of `raw/`, loses its numbers, and gains a `Harness` section last"
type: decision
status: current
authority: handoff-template-form
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "archive/handoffs/TEMPLATE.md"]
tags: [vault, process, harness]
---

# Decided 2026-08-16: four changes to the form, none of them written to disk yet

**It lives at `.claude/templates/handoff.md`.** Not in `raw/`, which becomes an inbox that is empty
between sessions and where the template was already an exception `vault-coverage.sh` had to skip
([[archive-is-dated-by-session-and-holds-what-left-the-working-set]]). **Both skills point at it**
rather than carry a copy: a pointer is checkable and a copy is not.

**The numbers are dropped and the cut is by heading text.** The numbers coupled the template to the
harness — `/ingest` says in so many words that *section 7* goes to `log.md` — so inserting a
section meant renumbering everything that referred to a number. A name does not move.

**One new section, `Harness`, and it goes last.** Everything above it is an account of the session;
it is a work queue, and the two are different genres. It carries the marked lines drained from
[[vault-feedback-file]], and `/ingest` cuts it on the section boundary
([[a-harness-change-is-recorded-when-it-is-decided]]).

**The owner's corrections are a marked token in place, not a section of their own.** Sections do
not map onto folders one for one in any case, so a section would have bought no consistency. **A
marker written by a human is authorship rather than classification**, and it keeps the correction
beside the claim it corrects instead of ten sections away behind a reference. The librarian is told
that a marked unit is the owner's testimony and outranks its neighbour; the `basis: human` it earns
lands on whichever page the unit reaches, and the field keeps the meaning it already had.

## What it obliges

- **The section-set check reads the list from the template**, never from a hard-coded copy — the
  same shape as `catalogue.md`: regenerate and compare rather than compare against a list somebody
  wrote down ([[the-catalogue-is-generated-not-maintained]], [[vault-scripts]]).
- **`Anything else worth keeping` stays, with its default written down:** its units are `skip:`
  unless the librarian finds them a category. A catch-all is more honest than forcing a
  classification, but a verdict chosen by taste is a hole in *there is no fifth option*
  ([[ingest-is-units-and-verdicts]]).
- **The template stops being advice and gets a rule in the check.** With the cut running on
  headings, a renamed or missing one breaks compilation silently, which is this project's signature
  failure.

## It supersedes nothing yet

[[the-handoff-template-maps-onto-the-categories]] describes the template **as it stands on disk**,
numbers and all, and its mapping is what this ingest was performed against. This page describes what
the template becomes; the retirement belongs to the session that performs the change, not to the one
that recorded the intention — the same shape as
[[the-repository-claude-md-becomes-a-dispatch-table]]. **The final form is designed and not written
to disk**, which is the first of the items on [[what-the-harness-build-waits-on]].
