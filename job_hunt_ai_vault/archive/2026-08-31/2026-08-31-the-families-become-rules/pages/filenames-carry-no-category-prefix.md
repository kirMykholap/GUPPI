---
title: "Filenames carry no category prefix — the folder and type: already say it"
type: decision
status: archived
authority: page-naming
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md"]
tags: [vault, retrieval]
---

# A page is named for its subject, and nothing else

**Decided by the owner on 2026-08-15.** `kebab-case`, descriptive, no dates — and **no
`[category]-` prefix**, which is what his instructions note had asked for:
`[category]-[short-description].md`
([[the-owners-instructions-note-and-what-was-built-from-it]]). No page in this vault has ever
carried one; from 2026-08-15 that is a decision rather than a divergence.

**Rejected: the prefix.** Three reasons, his, in the order he gave them:

- **the category is already written twice** — by the folder the page sits in and by its `type:`
  field, and `vault-check.sh` rule 2 fails a page where those two disagree. A prefix would be a
  third copy of the same fact, and third copies drift like second ones;
- **the filename is search surface.** Retrieval starts at `rg --files … | rg -i <term>`, so a name
  beginning with a word a third of the corpus shares is worse to grep than one beginning with its
  subject: `decision-` would prefix forty-odd files here and match on every one of them. The rule
  the naming serves is that a filename is part of what a question can hit
  ([[the-index-is-a-map-not-a-catalogue]]);
- **renaming now would break every `[[wikilink]]` and every `sources:` entry that names a page.**
  Rules 4 and 5 would go red across the corpus at once, which is the same shape of cost that
  killed archiving handoffs at a sprint close ([[a-sprint-closes-on-its-goal]]).

*(The title read "Filenames carry no category prefix — the folder and type: already say it twice"
until 2026-08-18, and the first bullet above is where the duplication is described. **The "twice"
counted the sayers, not a population**, and the title had already named both of them — the folder
and `type:` — so the word added nothing a reader could not see. That reasoning stood in a
`quantity:` line until the field was rejected and the rule made unconditional over titles and
filenames alike ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), which
withdrew the only way a page had to declare itself exempt; naming what is counted instead of
counting it here cost one word
([[a-title-names-what-is-counted-instead-of-counting-it]]). The bullets keep the word, which is the
argument and not the claim. Not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## The owner's other note had already said so

`auth-module-redesign.md` is the method note's own example of a filename, and it carries no prefix
([[the-owners-method-note-and-what-was-built-from-it]]). So the two notes disagreed with each
other and the build followed one of them; what was recorded on 2026-08-14 as a divergence from the
owner was a choice between two things the owner wrote. Why nobody noticed:
[[summarised-sources-lose-the-disagreement-between-them]].

## What it obliges

The naming rule stays where it is, in `index.md`, and it stays one line long. **A new page starts
with its subject** — the word a reader would search for, not the kind of page it is. What the kind
is remains answerable in two ways, both mechanical: the folder, and `catalogue.md`, which lists
every page by category and is generated ([[the-catalogue-is-generated-not-maintained]]).
