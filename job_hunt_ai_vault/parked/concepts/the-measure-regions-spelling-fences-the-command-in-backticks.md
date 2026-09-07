---
title: "The measure region's spelling fences the command in backticks, and the reading follows the last one"
type: concept
status: current
authority: measure-region-spelling
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-measure.py", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# The spelling

**`<!-- measure -->` … `<!-- /measure -->`, one line per number, the role first.** The grammar was
ruled on 2026-08-25 ([[the-measure-section-grammar-is-one-line-per-number]]); what this page carries
is the byte-level spelling that grammar is written in, which the ruling did not settle and which
`scripts/vault-measure.py` parses.

**A gauge line names its subject and its command, the command fenced in backticks, and the reading
follows the last backtick.** Testimony carries its value and the conditions it was taken under.

# The backticks are not decoration

**A separator character would have to be one that cannot appear inside a shell command, and there is
none.** This is not a hypothetical constraint: **the first gauge this project writes names a command
containing a pipe.** So the delimiter has to be a paired fence rather than a single character, and
the reading has to start after the *last* closing backtick rather than after the first.

# Why this is written down at all

**It is load-bearing for a script rather than for a reader.** 59 selftest cases and one gate rule
stand on it ([[vault-measure-py]],
[[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]), and until
2026-08-26 no page in this store stated it — the spelling existed only in the script that reads it
and in the session that wrote both. **A format with one implementation and no description is a
format nobody else can write into**, which is the position the librarian is in every time it fills a
region.

# Its standing, and how it came to have one

**The owner selected it rather than designing it** — 2026-08-26. The session wrote the spelling
while building the script, put it to him afterwards, and he let it stand and ruled that the
librarian write it onto a page. **The vault had decided one line per number, the role first, and no
value on a gauge; it had not decided the spelling**, so this is the gap being closed rather than a
second answer to a settled question.
