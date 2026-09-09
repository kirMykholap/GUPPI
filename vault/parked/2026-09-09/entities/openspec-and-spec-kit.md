---
title: "openspec and spec-kit, the published toolkits this store was read against"
type: entity
status: current
authority: external-spec-toolkits
basis: external
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md"]
tags: [harness, vault, process]
---

# What they are, and why they are in this store at all

**Two published toolkits for spec-driven development, read on 2026-08-23 against this vault.** No
page in the corpus named either before this one.

**Both are feature pipelines rather than knowledge stores.** Their unit of work is one feature or
one change: a spec is written, a change is executed, the change is closed. **Four of this
project's six categories have no destination in either** — `lessons/`, `entities/`, `rules/` and
the standing half of `decisions/` describe things that outlive a feature, and a pipeline whose
records close with a change has nowhere to put them.

**So they are not an alternative to this store and were not read as one.** What they are is the
nearest published prior art, which makes them the only external check available on whether this
project has invented something odd ([[the-vault-is-compiled-not-retrieved]]).

# What they have that this does not

- **A packaging and distribution system for the method itself.** spec-kit has extensions, presets
  and bundles; openspec has forkable schemas and a beta *Stores* — the extract-the-method-as-a-
  product move, already shipping. **This project's method is a directory of hand-written files with
  no way to hand it to anybody**, which is the same finding as the harness being invisible to its
  owner, seen from outside ([[the-harness-is-no-longer-visible-to-its-owner]]).
- **A documented machine surface**: a diagnostic envelope and defined exit codes. This project's
  gate has exit codes and no envelope, and reshaping its messages is a rewrite of its own selftest
  ([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).
- **A command that checks the artefacts against the codebase** — `/speckit.converge` and
  `/opsx:verify`. **This is the most directly relevant of the three.** This project's gate checks
  the corpus against itself: rule 5 resolves a `sources:` path, rule 12 asks whether a region agrees
  with its page, and nothing anywhere asks whether a page's claim about the code is still true
  ([[fidelity-to-a-source-and-fidelity-to-the-tree]]). A proposal for such a check was asked for
  early on 2026-08-23 and not written.

# On the disposition of a built change they disagree, and both state why

**openspec folds a completed change into a living spec**, because it maintains a second corpus that
has to stay current — the spec is the artefact, so the change has to be absorbed into it.

**spec-kit names this project's policy *flow-forward*, endorses it for auditability, and names its
one risk**: duplication and fragmented lineage, requiring naming and linking habits. **That risk is
already mechanised here** — the `authority:` uniqueness constraint is exactly a naming-and-linking
habit turned into a verdict, and rule 3 of the gate fails on two `current` pages claiming the same
question ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**Read against the ruling of the same day, this is an outside witness rather than an argument.**
The owner ruled that `archive/` is history and `wiki/` is the source of truth, which is
flow-forward stated in his own words
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]). Neither toolkit
was consulted before that ruling and neither caused it.

# What is worth taking, and one thing that is refused

**Worth taking: the injector's lifecycle hooks.** spec-kit runs its injection on lifecycle events
rather than leaving it to be remembered, and *remembering to inject* is a known gap here — rule 12
catches a page edited and not injected, but only when somebody runs the gate
([[a-check-asks-by-running-the-writer-it-checks]]).

**Refused: a written list of governed destinations.** spec-kit's injector carries one; here it is
already ruled against, because the governed set is swept off the property rather than listed
([[the-governed-set-is-swept-and-markdown-by-property]],
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# The boundary of this reading, and it is narrower than the claims above

**Documentation only** — no source code, no GitHub code search. Every claim above that one toolkit
*lacks* a feature rests on its published navigation tree, which is the weakest kind of negative
evidence this store admits ([[a-claim-asserted-from-prose-rather-than-from-the-file]]). The claims
about what they *have* are stronger, because a documented feature is documented.
