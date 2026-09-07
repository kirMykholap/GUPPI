---
title: "The marker becomes `<!-- [type]: slug -->`, with the script substituting the record's type"
type: decision
status: archived
authority: marker-type
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check.sh"]
tags: [harness, record-schema, vault]
---

# Decided by the owner on 2026-08-17. Not built.

`<!-- rule: some-slug -->` becomes `<!-- entity: some-slug -->`, `<!-- concept: some-slug -->` and so
on, with the type taken from the page rather than typed by hand. **His argument: once a non-rule can
render, the word `rule` in the marker is a lie** ([[governs-becomes-a-property-of-any-page]]).

**The session objected first and then withdrew the objection**, and the withdrawal is the part worth
keeping. The objection was that this puts a *mutable field* into an *address*, which is the shape that
makes a rename expensive. The answer: **the type is the folder, and pages do not move between
folders** — so the marker becomes a **complete** address into the vault, `<!-- entity: some-slug -->`
resolving to exactly one path, which *removes* the cross-folder lookup the field-driven design would
otherwise need ([[a-marker-with-its-type-is-a-complete-address]]).

**Rejected: keeping `rule:` as a fixed word for every record type.** It reads as a claim about the
record and would be false on most of them.

## Two conditions the owner attached

1. **The type is validated against the closed six-type set**, not matched as any word. A loose
   `<!-- foo: slug -->` must be *malformed*, not *a marker for a type nobody has heard of* — the
   detector is generous, the judge is not
   ([[a-marker-is-detected-loosely-and-judged-strictly]]).
2. **A marker whose type disagrees with its page gets its own verdict.** `<!-- entity: x -->` where
   `wiki/decisions/x.md` is the page is a wrong address that still resolves, which is the class the
   fifth verdict already exists for at the file level
   ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

## What it obliges

- **Every existing region has to be rewritten**, which is a rewriter-and-detector pair rather than a
  find-and-replace ([[a-rewriter-must-be-paired-with-a-detector]]). Nine regions carry `rule:` today
  ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).
- **The check's `rule:` pattern, the injector's two extractors and the selftest's sandbox all read the
  literal word** and all three change together
  ([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]).

The whole design, with the two new verdicts and what each costs to omit, is
[[the-marker-carries-a-type-and-governs-is-read-as-a-field]].

# The type word is the SINGULAR — closed by the owner, 2026-08-18, and built at `e83ce28`

*(The heading above says **not built**; it is left standing as the state on 2026-08-17.)*

**owner: singular.** `<!-- concept: some-slug -->` resolves to `wiki/concepts/some-slug.md`.
**Rejected: the folder name** (`<!-- concepts: x -->`), which reads worse and was priced as the
cheaper option on a claim that turned out to be false.

**The design's argument for the folder spelling did not survive measurement.** It said the singular
*"needs a pluralisation the check does not currently do anywhere"* — the check already does exactly
that mapping at `scripts/vault-check.sh:176`, folder to singular, with one special case for
`entitie`, and the inverse is the same line read backwards. **And the mapping cannot be avoided by
the folder spelling anyway**, because the verdict comparing a marker's type against a page's `type:`
needs the same bridge in either direction.

**The singular owes no rewrite at all.** All nine live `<!-- rule: slug -->` markers were already in
the target form, so the rewriter-and-detector row in the obligations above belonged to the *folder*
spelling only ([[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]]).

## What replaced the two conditions

**Condition 1 — validation against the closed six-type set — is met by derivation instead.** The
type words are swept off `wiki/` as `singular:plural` pairs and a marker's type is legal because its
folder exists, which rule 1 already checks
([[the-type-words-are-swept-off-the-tree-and-never-listed]]). The judge stays strict: an unknown word
is **malformed**, by name and line ([[a-marker-is-detected-loosely-and-judged-strictly]]).

**Condition 2 — a verdict for a marker whose type disagrees with its page — was dropped as
unreachable and replaced** by one that names the folder a slug is actually in
([[the-unreachable-verdict-is-dropped-and-replaced]]).

**What it obliges now:** the type↔folder correspondence is derived **in one place per script** and
never listed anywhere.

# Pages do move between folders, and the injector reads the folder — 2026-08-21

**The design's argument above rests on *"the type is the folder, and pages do not move between
folders"*. Two pages moved on 2026-08-21**, out of `concepts/` and into `wiki/rules/`, on the
owner's ruling that a page which renders its text into another file is a rule
([[governs-is-a-property-of-wiki-rules-alone]]).

**The sentence is left standing and dated rather than struck**, because what it was *for* held: the
marker stayed a complete address through the move. What it got wrong is only that folder membership
is stable.

**The injector derives the type word from the folder the page sits in, not from anything the page
says**, so a move changes what every marker for that page must say. **Four markers in the
repository's `CLAUDE.md` were retyped** from `<!-- concept: … -->` to `<!-- rule: … -->`, and until
they were, the injector reported no region for those pages and rule 12 was red — the expected state
of a half-finished move ([[a-check-asks-by-running-the-writer-it-checks]]).

**A brief asserted the opposite before anyone read the injector**, and that is on its own page as a
claim reasoned from what the page carries rather than read from the tool
([[a-presence-test-cannot-answer-an-identity-question]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
