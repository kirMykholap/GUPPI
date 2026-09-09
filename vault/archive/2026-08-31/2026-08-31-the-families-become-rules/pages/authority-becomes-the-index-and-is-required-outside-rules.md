---
title: "`authority:` becomes the index a claim is looked up in, and is required on every page outside `wiki/rules/`"
type: decision
status: archived
authority: authority-index
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["scripts/vault-authority.sh", "scripts/vault-check.sh", "wiki/concepts/_schema.yaml", "CLAUDE.md"]
tags: [vault, retrieval, process]
binding: prohibition
---

# The field stops being a label and becomes a job

**Decided 2026-08-21, in the same ruling as [[occams-razor-is-the-ground-rule-for-the-vault]] and
because of it.** The admission rule is decided by looking a candidate up
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]), so the corpus needs an index a
lookup can read *before* a page is opened. `authority:` is that index. It used to be a rank a page
could claim — the vault's schema said pages not claiming sole ownership of a question simply omit
it — and that sentence is withdrawn.

**Required on every page outside `wiki/rules/`, where it stays forbidden.** A rule answers with
`governs:`; carrying both would make the decision and the rule stating it share a slug and read as
a contradiction ([[authority-beside-governs-is-forbidden-on-any-page]]).

**Measured the day it was decided: 423 pages carry the field and every value is distinct; 56 carry
none.** Of those 56, 24 are `proposals/`, 13 `decisions/`, 5 `lessons/`, 2 `entities/`, 2
`concepts/` and 10 `rules/`. The rules are correct to have none. The rest are the hole.

# Why an optional index is worse than no index at all

**A lookup that returns nothing reads exactly like a question nobody has answered.** That is the
whole argument, and it is about the direction of the failure rather than about tidiness.

Under an optional field, `--near <slug>` returning an empty family has two meanings and the reader
cannot tell them apart: either the claim is genuinely new, or the page that owns it declined to
declare itself. The first licenses a new page; the second forbids one. **The rule the lookup
decides therefore fails towards creating**, which is the exact failure the ruling was taken to
stop — the store would go on multiplying entities while running a check that says it is not.

An index with no holes can be wrong about a *family*. An index with holes is wrong about
*existence*, silently, and only in the permissive direction.

# The one folder where the schema still says `optional`, and why that is not an exemption

**`concepts/`.** A concept page may carry `governs:`, and two do —
`a-retrospective-is-a-sessions-end-not-a-sprints-ritual` and
`the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint`. For those,
[[authority-beside-governs-is-forbidden-on-any-page]] applies, so the requirement cannot be
unconditional in that folder: the honest statement is *required unless `governs:` is present*, and
a per-folder schema has no grammar for it — its two blocks say `required` and `optional` about a
key and say nothing about another key's presence.

**So the condition lives in the gate.** Rule 13 of `vault-check.sh` asks it by running
`bash scripts/vault-authority.sh --orphans`, which excludes exactly those pages, so what counts as
a page nothing can look up is defined once and in one place — rule 12's shape, and the same reason
it has it ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). Measured 2026-08-21: 46
non-rule pages carry no `authority:` and the advisory names 44, the difference being the two
concepts that answer with `governs:` instead.

**That arrangement is not new here.** `paths` already has it in `wiki/rules/_schema.yaml`: optional
in the schema because it is meaningless under `render: region`, and reported by the injector on a
`render: whole` page carrying none ([[paths-lives-on-the-vault-page-and-is-written-widest]]). The
conditional requirement is stated by the instrument that can evaluate it.

**The remaining folders hold `optional` for exactly as long as the back-fill runs, and that is an
ordering fact rather than a doubt about the field.** A key in neither schema block is rejected
outright, and `required` ahead of the corpus turns the gate red — which the librarian lock reads as
a refusal to dispatch the writer that would clear it ([[the-librarian-lock-hook]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). Promoted as the last step of the
session that fills them. It is the same sequence [[a-decision-declares-whether-it-binds]] is following, and
for the same reason.

# Rejected: derive the families mechanically from the words in a slug

The obvious alternative, and it is what `--near` falls back to when a slug is in no family yet.

**Refused as the design.** `ledger-retention` and `ledger-archive` share a word and belong
together; `map-admission` and `where-things-are` share none and answer the same question. Word
overlap sees the first pair and is blind to the second, and the second is the case the lookup
exists for — a librarian about to write a page has already chosen words that feel new to it. The
grouping is a judgement about what a question *is*, and the librarian makes it incrementally, about
fifteen slugs per ingest, rather than over the whole register at once.

**Vectors would answer the same objection and are already deferred with a reason**
([[vectors-are-deferred-not-rejected]]). Nothing here reopens that.

# Why `authority.md` is hand-written and not generated

This is the point [[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]] would otherwise
refuse outright, so it is argued rather than assumed.

**Which slugs exist is in the tree and needs no file.** `--list` prints it from frontmatter in one
pass. **Which slugs answer the same question is nowhere and cannot be derived** — it is not in the
frontmatter, not in the folder, not in the words. A file is the only place it can live. That is
exactly the standing of `tags.md`, where the definitions and the Russian aliases are the half no
sweep could produce ([[aliases-carry-the-question-across-languages]],
[[a-field-with-no-register-produces-unique-values-by-default]]).

**The half that IS derivable is the half that drifts**, which is why the register is never trusted:
`bash scripts/vault-authority.sh --check` compares it against the tree in **both** directions — a
slug in the register with no page, and a page whose slug no family names. The derivable half is
audited on every run rather than maintained by hand and hoped for.

# Why the register names slugs as plain text and never as wikilinks

**A register that linked every page would join the link sweep of rule 5, and then no page in this
vault could ever be an orphan again.** The orphan rule would run, pass, and prove nothing — it
would be measuring the register's completeness instead of the corpus's reachability.

That is not hypothetical: it is the trap the generated catalogue carried, and part of why the
catalogue was replaced by a query ([[the-index-is-a-map-not-a-catalogue]]). The plain-text spelling
is load-bearing and is not a formatting preference.

# What this ruling does to a standing claim about `proposals/`

**[[an-authority-register-on-the-model-of-the-tag-dictionary]] says the opposite about one folder:**
*"`proposals` carry no `authority`, and that is correct rather than accidental. Two competing
proposals about one problem are legitimate; flagging them as a contradiction would be wrong."*
That page is `basis: inference`, written 2026-08-17; this ruling is `basis: human`, taken
2026-08-21 with the measurement in front of the owner, and the ranking settles which one a reader
follows.

**The objection underneath it is not settled, and it is recorded here rather than answered.** If two
proposals genuinely compete over one problem, requiring each to declare a distinct slug either
forces a false distinction or trips rule 3. Nothing was decided about that case on 2026-08-21, no
such pair exists in the corpus today, and the first one to arrive is the owner's call rather than a
librarian's.

# Two claims that lived only on the design page, landed here — 2026-08-21

**Written during the `authority` back-fill of 2026-08-21, so that
[[an-authority-register-on-the-model-of-the-tag-dictionary]] no longer holds anything found nowhere
else. That page is not retired: retiring it is a judgement about the corpus and the owner's
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]). What is removed is the reason it
cannot be.**

**A rejected candidate slug is recorded as an alias in `authority.md`.** Stated on that page of
2026-08-17 as the third of the tag dictionary's three parts, and stated about `authority:` nowhere
else — `tags.md` carries the same obligation about *tags*, which is a different field
([[aliases-carry-the-question-across-languages]]). It is the same argument in both places: the word
a librarian reached for and put down is the word a future grep will hit, and it is how a question
asked in Russian reaches a page written in English.

**That page predicted a register would make `authority:` "rare rather than universal", and this
ruling falsified it.** Written 2026-08-17 on `basis: inference`; the ruling of 2026-08-21 made the
field required on every page outside `wiki/rules/`, which is the opposite of rare, and it did so on
the argument above — an index a page may omit is an index with holes in it, and the holes are
invisible in the permissive direction. Recorded rather than corrected in place, because what the
prediction was wrong about is the reason the field exists: it was read as a *rank* a page claims and
is a *job* the index does ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

# The back-fill finished the same day, and three sections above are dated by it — 2026-08-21

**The register exists and is full.** `authority.md` holds **51 families over 470 slugs**, in 543
lines and 41,782 bytes; none is left over and none is in two families;
`bash scripts/vault-authority.sh --check` exits 0 in both directions and `--orphans` reports that
every page outside `wiki/rules/` carries an `authority:`. **Five pages were written and 220
back-filled**, and the field was promoted from `optional` to `required` in every folder's schema as
the last step of the session, in the order the argument above sets out.

**The section *The one folder where the schema still says `optional`* is spent.** The exception it
describes was removed rather than moved: a page that renders its text into another file **is** a
rule, so both `concepts/` pages carrying `governs:` moved into `wiki/rules/` and the field left the
folder with them ([[governs-is-a-property-of-wiki-rules-alone]]). `authority:` now has no exception
anywhere outside `wiki/rules/`, and the conditional requirement that no per-folder schema could
express has nothing left to range over. **Rule 13 still asks by running the tool**, and that is
unchanged.

**The measurement in the opening section is superseded by the end state**: 423 pages carrying the
field became 470, and the 56 that carried none became the 13 rules pages that are correct to have
none.

**The objection about `proposals/` got its first test and it did not fire.** Across **24 proposals
there is no competing pair** — and in three of the four near-pairs the pages say so themselves. The
objection is not thereby settled: what was measured is that the corpus does not contain the case
yet, which is the state the section above already describes as the owner's to decide when it
arrives.

**Eight families hold eleven slugs against a ceiling of about ten.** Twenty were at the ceiling
before this work, so the overflow is arithmetic rather than a design fault, and **rebalancing is a
judgement about the corpus** — raised for the owner rather than taken here.

**[[an-authority-register-on-the-model-of-the-tag-dictionary]] is now retirable and was deliberately
not retired.** Both claims that lived only on it are landed here; what remains is the owner's
judgement ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

## The overflowing family goes to `/vault-lint` — 2026-08-22

**Owner selected: rebalancing is `/vault-lint` work**, the ritual that exists for judgements about
the corpus, rather than something an ingest does on its way past.

**The occasion is *the hooks that stand around a session*, which reached eleven slugs against a
ceiling of about ten** when `dispatch-record-hook` joined it ([[the-dispatch-record-hook]]).

**Rejected: raising the ceiling.** Ten is a property of the reader — what a reader will open for one
question — so moving it to fit the corpus is how a measurement stops saying anything
([[measure-before-optimising-and-count-processes-not-pages]]).

**Nothing is read off this here**, and which slugs move where is a judgement about the corpus and so
is his ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

# The objection that `proposals/` should not carry `authority:` was put and refused — 2026-08-26

**The field stays required in every folder but `wiki/rules/`.** *(the owner selected it, against
dropping it in `proposals/`.)*

**The objection:** a proposal is a design rather than an answer, so it claims no question solely and
the field says nothing about it.

**The price he chose against is a hole in the index.** The lookup is what the admission rule is
decided by, and a folder that may omit the field is a folder the lookup skips silently — a proposal
carrying a finished design is exactly what a candidate page needs to find before it is written.

**The case was on the record the same day**: [[a-generated-harness-map]] held a ready design and was
not found, and a page was nearly written over it.

# The ceiling this page argues from is struck — 2026-08-26

**"About ten to a family" is deleted from `authority.md`**, on the owner's ruling of that date, after
going unapplied since it was written at 666 slugs in 15 families
([[the-authority-registers-family-ceiling-is-deleted]]).

**The rebalancing-is-`/vault-lint`-work clause above is unaffected**: what is struck is the number,
not who decides how the register is grouped.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
