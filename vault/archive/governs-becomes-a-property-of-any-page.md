---
title: "`governs:` becomes a property any page may carry, rather than a mark of one folder"
type: decision
status: deprecated
authority: governs-scope
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, record-schema, vault]
superseded_by: [[governs-is-a-property-of-wiki-rules-alone]]
---

# Decided by the owner on 2026-08-17. Not built.

**Any page may name a destination it renders into.** Today only a page in `wiki/rules/` can:
`scripts/vault-inject.sh` globs that one folder, and every `governs:` branch in `scripts/vault-check.sh`
is gated on `folder == "rules"` ([[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]]).

**What forced the question:** the owner ruled that a factual record may render into the repository's
`CLAUDE.md` ([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]). The project
description is such a record and it is not a rule, so under the present mechanism it has nowhere to
render from.

## Two alternatives rejected, each on a test the project already had

**A seventh folder for renderable records.** Rejected: the folder set was closed the day before
([[the-folder-set-is-closed-and-tasks-is-not-in-it]]), and its admission test refuses a folder whose
description goes stale on its own — which a folder holding *"facts about the tree"* would.

**Putting the project description in `rules/`.** Rejected: it would empty the admission test that
folder stands on — *imperative and not enforced by a test*
([[the-harness-is-compiled-not-maintained]]). A description is not imperative, and admitting it makes
`rules/` mean nothing.

## What it obliges

- **The field must become either a rendering or a refusal, everywhere.** Silence outside `rules/` is
  a green that examined nothing, which is this project's most-repeated failure shape
  ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
- **The marker has to carry the record's type**, or the word `rule` in it becomes a lie the moment a
  non-rule renders ([[the-marker-carries-a-type-and-governs-is-read-as-a-field]]).
- **Three records are waiting on this and have nowhere to live until it lands**: the project
  description, the definition of *retrospective*, and the map
  ([[the-map-in-claude-md-and-its-admission-test]]).

**Nothing of it is built.** The design is agreed in full and is on
[[the-marker-carries-a-type-and-governs-is-read-as-a-field]]; the cost of waiting is on
[[what-the-harness-build-waits-on]].

# Built at `e83ce28`, and the paragraph above is the old state

*(Corrected 2026-08-18. The heading and the closing paragraph both said **not built**; they are left
standing as what was true on 2026-08-17 and the correction is here rather than in place.)*

**`scripts/vault-inject.sh` walks `wiki/*/*.md`, pre-filtered by `grep -l '^governs:'`, and takes the
destination from the field.** The three obligations above are discharged, each in a way worth
naming:

- **The field became a rendering, and the silence moved rather than vanished.** Absent `governs:` is
  now a legal skip, because most of the corpus delivers nothing by design; the red went to the
  inverse — a `<!-- text -->` slice on a page that names no destination
  ([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]).
- **The marker carries the record's type**, as the singular word
  ([[the-marker-carries-the-records-type]], [[a-marker-with-its-type-is-a-complete-address]]).
- **One of the three waiting records is built** — the map
  ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]). The project description and
  the definition of *retrospective* are still waiting, and both are now unblocked by mechanism and
  blocked by nothing but a session ([[a-definition-may-render-into-the-repository-claude-md]],
  [[what-the-harness-build-waits-on]]).

**Only one of the three `folder == "rules"` branches dropped**, not the gate
([[the-governs-branch-widens-and-the-others-stay-rules-only]]), and one of the two approved verdicts
was replaced by a reachable one ([[the-unreachable-verdict-is-dropped-and-replaced]]).

# Overturned by the owner on 2026-08-21, and retired

**`governs:` is a property of `wiki/rules/` alone.** The owner reversed this ruling at the retro of
2026-08-21, in his own words: *"Странная формулировка governs у concepts. Если у концепта
появляется governs — Он становится правилом. Поэтому authority = required в concepts. А governs из
concepts уходит."* The successor is [[governs-is-a-property-of-wiki-rules-alone]].

**The paragraphs above are left standing as what was decided on 2026-08-17 and built at `e83ce28`.**
Read them for why the field was widened, which is still the honest account of the problem: three
records had been licensed to render into the repository's `CLAUDE.md` and none of them was an
imperative, so under the mechanism of that week none of them had anywhere to render from.

**What survives the reversal is the mechanism, and it is most of what this page obliged.** The
injector still walks `wiki/*/*.md`, the field is still read as a field rather than as a mark of a
folder, and the marker still carries the record's type. What is withdrawn is the permission it gave
a page outside `wiki/rules/` to carry the field.

**What the reversal rests on is this page's own admission argument, applied the other way.** The two
alternatives rejected above were refused because `wiki/rules/` admits *imperative and not enforced
by a test*, and a description is not imperative. The owner replaced that admission test with one
about delivery: a page that renders is a rule, whatever its grammatical mood. The two `concepts/`
pages this decision made possible were moved into `wiki/rules/` on 2026-08-21.
