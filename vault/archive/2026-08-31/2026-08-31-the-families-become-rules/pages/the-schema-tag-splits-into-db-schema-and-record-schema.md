---
title: "The `schema` tag splits into `db-schema` and `record-schema`, and the bare word stays an alias on each"
type: decision
status: archived
authority: schema-tag-split
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["tags.md", "log.md", "scripts/vault-check.sh"]
tags: [retrieval, vault]
---

# Decided 2026-08-19: rename each half, keep the general word out of the tag position

`schema` named the database as a structure from 2026-08-13. From 2026-08-17 the corpus was also
tagging pages about the shape of a **page** with it — `governs:`, the marker's type word, the
frontmatter core, the rejection of `quantity:`. `tags.md` recorded that on 2026-08-18 as owed to
the next `/vault-lint`, and the owner took it here.

**The word is retired from the tag position on each half.** The database pages carry `db-schema`,
the record pages carry `record-schema`. Neither keeps the bare word, and no page anywhere is
tagged `schema` any more.

# What the tag was rejected for, and it is not density

**Rejected: keeping `schema` on the database half and minting only `record-schema`.** It is the
cheaper edit — the database aliases and the mint date stay attached to the same word, and only
the newer meaning pays for the rename.

**It was rejected because that arrangement has already been tried here and failed.** The
2026-08-13 definition opens with *"the database as a structure"* and names tables, columns and
Alembic revisions; the drift happened against that text, in the same store, read by the same
librarian. A general word sitting in the tag position is decided by whoever types it next, and a
prose clause telling him which of the meanings is the real one is the exact defence that was in
place while the drift ran for two days. Repeating it would be repeating the experiment and
expecting the other result. The general word only becomes safe when there is nothing general left
to attach to it.

**The prose defence is what failed, so the fix is structural.** Both new words carry their half in
the word itself: nothing about `db-schema` invites a frontmatter page, and nothing about
`record-schema` invites a migration.

# The bare word stays an alias on each entry, and that is a different position

`схема` and `schema` are aliases on `db-schema` **and** on `record-schema`.

Retiring the word from the tag position and retiring it from the alias list are separate acts,
because the positions do different work. **A tag is written by a librarian classifying a page, and
that is where an ambiguous word does its damage** — one word, two meanings, no reader present to
notice the choice being made. **An alias is read by a librarian looking for a page**, and it does
not classify anything: no page is ever tagged with an alias, so a word duplicated across the
alias lists cannot reproduce the drift.

Putting it on one entry only would have re-created the asymmetry a layer down: a question
containing "schema" would reach the database and silently miss the records, which is the shape of
the original fault with the arrow reversed. Putting it on neither would reproduce the failure the
tag was minted for — `schema` was created on 2026-08-13 precisely because
`rg -il "колонк|таблиц|миграц|схем"` over the wiki returned nothing at all, and dropping `схема`
would hand the same stem back the same emptiness for the larger half of the corpus.

On each entry, an ambiguous word lands where ambiguity is supposed to be settled: in the
dictionary, in front of a reader who has both definitions on the screen and can pick. The Latin
`schema` would in fact survive by accident — it is a substring of each new tag name, so
`rg -i schema tags.md` finds both entries whatever the alias lists say — but the Cyrillic `схема`
would not, and an alias that works by accident is not one this store relies on.

# The measurement, recorded because a reader will otherwise re-derive it

The proposal that reached the owner said the split should happen **before the density counter
forced it**. That premise was wrong, and the correction is the useful part of the work.

`vault-check.sh` prints a per-folder advisory when a tag selects more than ten pages in one
folder. Measured before the rename, `decisions/` alone carried `harness` at 54 pages, `process` at
60 and `vault` at 78, and the run printed eighteen such lines across the corpus. `schema` in
`decisions/` stood at ten — one page short. **So the counter was never a forcing function here:
crossing it would have added the nineteenth line to a list of eighteen that already stand
unactioned** ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

The honest reading runs the other way. An advisory prints against a folder count, and splitting a
tag lowers each new count below the old one — so a split can only ever *remove* advisories, and
this one removed none, because there was none to remove. **The split is happening on the meaning
seam alone.**

This does not overturn [[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]].
That decision refused a **density-driven** split and holds unchanged; the measurement above is what
shows this is not one.

# What the rename touched, and what it did not

Sixteen pages under `wiki/` — six to `db-schema`, ten to `record-schema` — and three more in
`archive/`, all on the record side. The archived pages were taken because the rename would
otherwise be incomplete in a way nothing mechanical would report: rule 6 of `vault-check.sh` reads
tags from `wiki/` only, so three archived pages carrying a word that `tags.md` no longer defines
would have passed the gate in silence.

Every touched page had its tag count checked and unchanged — a rename substitutes a word and moves
no count, and each page stayed inside the schema's 2-to-4.

**No page was renamed and no `updated:` was written.** Only the one word inside `tags:` moved, so
no address moved with it and nothing had to be swept ([[a-page-rename-is-sed-and-verify]] is about
the other operation and was not needed).

# What is still owed

**The corpus sweep is deferred to `/vault-lint`,** on the owner's decision the same day. Seven
pages carry record-schema subject matter without the tag, and the boundary of that sweep is what
the `wiki/<folder>/_schema.yaml` files are about to settle — they landed this session and have not
stabilised, so sweeping against them now would be sweeping against a moving line.

**Three pages keep `record-schema` on a loose fit and go on that same list**:
[[a-definition-may-render-into-the-repository-claude-md]],
[[the-governs-branch-widens-and-the-others-stay-rules-only]] and
[[the-marker-carries-the-records-type]]. Each was flagged as a candidate for trimming rather than
renaming, and nothing here removes a tag without a word from the owner: the rename carried them
across unchanged so that the trim is a decision taken on its own evidence and not a side effect of
this one.
