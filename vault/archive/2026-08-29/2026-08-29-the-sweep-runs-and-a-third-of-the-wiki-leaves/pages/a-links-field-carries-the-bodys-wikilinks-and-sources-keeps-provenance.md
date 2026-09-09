---
title: "A `Links:` field carries the body's wikilinks, and `sources:` keeps provenance alone"
type: decision
status: archived
authority: links-field
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "scripts/vault-archive.sh", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# What he opened with, and it was a proposal to merge the two

> **owner: поле "sources" работает плохо. Я предлагаю проверять скриптом все `[[викиссылки]]` внутри
> записи и выставлять их в "sources". Тогда поле sorces будет правильно нести все ссылки и мы можем
> проверять по нему, а не всему тексту. А также скрипт делает этот процесс точным, в отличие от
> работы агента.**

*(His `[[викиссылки]]` is written here inside a code span and is otherwise untouched. The gate's
link sweep reads `[[...]]` as an address and strips code spans, so a quotation naming a wikilink
reddens the tree unless it is marked as the identifier it is.)*

**Three separate claims are in there and only one of them was in dispute.** That the field should
be filled *by a script rather than by an agent* — not disputed. That a check should read a field
rather than the whole text — not disputed. That the links should be written **into `sources:`** —
this is the one the session put back to him.

# The collision that was put to him

**`sources:` means provenance and it holds paths.** It names what a page was compiled from: a
journal in `raw/`, a file in the repository, a note. Rule 5 of the gate resolves every repository
path on that line and reddens one that does not exist, and `scripts/vault-archive.sh` rewrites the
line on a move on exactly that assumption — on a `sources:` line a path is an address by
construction and can be nothing else ([[a-sources-path-inside-the-vault-is-vault-relative]],
[[vault-archive-sh]]).

**Filling it with the body's wikilinks destroys that meaning.** A page would then cite as its
provenance every page it merely mentions, the archive rewriter would have two kinds of thing to
rewrite on one line, and no reader — human or script — could tell *what this was written from* from
*what this points at*.

# The ruling

> **owner: да, тогда вводим отдельное поле Links, согласен.**

**So there are two fields and each keeps one meaning.** `sources:` stays provenance: paths, written
by whoever compiles the page. `Links:` is new: the `[[wikilinks]]` that occur in the body, written
by a script and never by hand.

**What it obliges, and it binds before the field exists:**

- **Nothing may be added to `sources:` in order to make a link countable.** That is the exact move
  the new field exists to prevent, and it is available today.
- **A check that wants the links reads `Links:`**, once the field exists — not the whole text, and
  not `sources:`.
- **The field is filled mechanically.** His last sentence is the reason the ruling is a ruling
  rather than a preference: *скрипт делает этот процесс точным, в отличие от работы агента*. A
  field an agent fills by reading its own page is a field that drifts
  ([[knowing-a-rule-is-not-a-mechanism]]).

**Rejected: one field carrying both meanings** — his own first proposal, refused by him once the
collision was named.

# It is not built, and what waits on it

**No schema declares `Links:`, no script writes it, and no check reads it.** Admitting a field is a
change to every `_schema.yaml` that may carry it, and the schemas are the session's
([[the-per-folder-frontmatter-schema]], [[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).
The design is [[links-is-filled-by-a-script-from-the-bodys-wikilinks]].

**The nearest thing waiting on it is the archive precondition**, which today matches a slug as a
plain string anywhere in a live page because there is no field to read
([[vault-archive-sh]], [[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]).
That match is safe on a measurement rather than by construction, and a field would make it exact.
