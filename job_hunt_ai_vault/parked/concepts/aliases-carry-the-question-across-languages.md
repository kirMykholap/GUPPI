---
title: "A tag's aliases are how a Russian question reaches an English page"
type: concept
status: current
authority: alias-purpose
basis: human
sprint: S0
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md"]
tags: [retrieval, vault]
---

# Aliases carry the question across the language gap

The corpus is written in English. **The questions are asked in Russian.** Retrieval is grep. Those
three facts do not fit together, and `tags.md` is where they are made to.

A tag entry is three parts, and each does separate work:

- **the tag** — what the page is about;
- **the definition** — why the dictionary is not merely a second copy of the tags in the
  frontmatter. It cannot be derived from the files, and without it a librarian arriving with a
  fresh context will within a month attach the same tag to three different kinds of thing;
- **the aliases** — every word a real question is likely to use for this subject, in either
  language.

## The rule that fills the alias list

**When you consider a new tag and reject it in favour of an existing one, record the rejected word
as an alias.** It costs one line at the moment you already have the word in your hand, and it is
what a future grep will hit.

## It has already paid, once, measurably

The vault's first recorded miss was word-shaped: no alias reached the JavaScript and React pages,
and two Russian questions landed only because those English words happen to appear in filenames.
One dictionary entry — the `frontend` tag — closed it the same day.

## Four runs in, the entry point has never been an alias

Measured across the acceptance runs of 2026-08-13 and 2026-08-14. **Russian reaches this corpus
only through `tags.md`, and only for vocabulary someone thought of in advance** — and so far the
questions that landed did not need it:

- Q3 and Q4 of 2026-08-14 were asked in Russian and landed because *JavaScript* and *React* survive
  untranslated into Russian speech **and appear in filenames**. The filename answered the grep and
  hid the gap;
- the words the questions were actually made of — `вид`, `браузер`, `клиентский`, `остров`,
  `переписать` — **reached nothing at all** before the run. The agents widened the `frontend`
  aliases in response, which is the rule above working exactly as designed, one question too late;
- that is the **third and fourth consecutive run whose entry point was a filename rather than the
  alias list**.

The reading to take from it is not that aliases are unnecessary. It is that **an English word which
survives into Russian speech masks the failure**, so the alias list is never exercised by the
questions most likely to be asked — and a subject with no such word (the database, before `schema`
was minted) fails silently and completely.

**That is also the recall gap that motivates vectors**, closed here by a line of text rather than
by an index; see [[vectors-are-deferred-not-rejected]], which records what a multilingual
embedding would and would not supersede. The definitions and the split rule it would not: those
are the discipline of classification, not search.

The counterweight, because a tag can fail by growing as well as by proliferating: a tag on more
than ~15–20 pages is a split candidate. That rule has already fired twice —
`collection` at 17 of 29 pages and `web` at 22 of 56 — and **three tags now stand over it and are
not being split by an ingest**: `process` 32, `vault` 31, `testing` 23, of 95 pages on 2026-08-14
([[lint-waits-for-an-open-sprint]]). **Re-measured 2026-08-15: `vault` 42, `process` 40, `testing`
26, of 108 — the corpus grew 14% and `vault` 35%**, with the per-tag table and the reasoning in
[[dynamic-tag-classification-by-a-skill]]. The figures above are kept as the 2026-08-14 reading;
what they were is the evidence for the rate.

**The counterweight itself was corrected on 2026-08-16, and the paragraph above is kept as what
was believed.** A tag is no longer measured over the whole corpus: it is measured **inside one
folder of `wiki/`**, and the number is **ten**, the ceiling a reader opens for one question. Both
readings above — the 2026-08-14 one and the 2026-08-15 one — were counts over the corpus, and a
count over the corpus tracks the project's age rather than a tag's power to classify. Measured per
folder at `2036d98`, `testing` is **5 of 47 pages in `decisions/`** and **13 of 19 in `lessons/`**:
the same tag, healthy in the folder where it was accused and useless in one other. The two firings
this page records, `collection` at 17 of 29 and `web` at 22 of 56, were both real and both would
still fire; what changes is that a third firing now names the folder it is about
([[the-folder-is-the-first-narrowing]],
[[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**And the alias rule at the top of this page is what feeds the tag it then has to split.** `vault`
was extended five times in `tags.md` at `2036d98`, and every extension carries the same trigger in
its own words: a Russian word reached nothing, so the word was added to the widest tag's alias
list. Each such fix improves recall and permanently degrades the classifier, because an entry can
only attach a word to a tag. The design that would break that coupling — letting an entry point at
a page or a folder — was written down on 2026-08-16 and **not taken**:
[[an-alias-may-point-at-a-page-not-only-at-a-tag]] carries it, with the three reasons against.

Where this sits in retrieval as a whole: [[the-index-is-a-map-not-a-catalogue]], and the narrowing
the aliases now run inside: [[the-folder-is-the-first-narrowing]].

## Both registers have a checked half and an unchecked half, and the aliases are the unchecked one — 2026-08-21

**`authority.md` was argued for on retrieval grounds and the half that argument rests on is read by
no instrument at all.** `bash scripts/vault-authority.sh --check` parses `slugs:` and compares it
against the tree in both directions; **`definition:` and `aliases:` are checked by nothing.** So a
missing or wrong Russian alias fails silently and forever, in the permissive direction — a lookup
that returns nothing reads exactly like a question nobody has answered
([[authority-becomes-the-index-and-is-required-outside-rules]]).

**`tags.md` has had exactly this standing since it was written**, so it is not a regression; it is a
gap nobody had named. **It is also unavoidable in principle for this half**: which slugs exist is
derivable and is therefore audited, while whether the right Russian word is on the list is a
judgement about a reader, and no sweep produces it
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**The instrument that would test it is use.** An alias is verified when a question asked in Russian
lands on the page, which is what the feedback loop records
([[the-measurement-is-whether-the-vault-changed-what-a-session-did]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
