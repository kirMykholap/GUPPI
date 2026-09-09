---
title: "The measure section's grammar is one line per number, and a gauge line names the command instead of a value"
type: decision
status: archived
authority: measure-section-grammar
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# The ruling, 2026-08-25

> **owner:** «ТВое предложение принмаиется»

**A line per number, and the line opens with the role.** Testimony or gauge — the split ruled the
day before, now written into the grammar rather than left to a reader
([[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]]).

**A gauge line names the command that prints it and carries no value of its own.** The value is
written beside it by the script that runs the command
([[a-gauge-is-written-by-a-script-that-runs-the-command]]).

**The spelling this grammar is written in was not decided here and has a page of its own** — the
paired comment markers, and the command fenced in backticks with the reading after the last one
([[the-measure-regions-spelling-fences-the-command-in-backticks]], owner selected it 2026-08-26).

**The check rides the gate's existing shared pass rather than a per-page script.** The shared pass
already visits every page and already detects a body marker on a `wiki/` page — the
`slicenogoverns` verdict fires on a `<!-- text -->` slice on a page carrying no `governs:` — so a
measure region is a second customer of a pass that exists
([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]]).

# The section it is a grammar for was decided a day earlier

**The section itself is settled**: a marked region, legal in any folder, required nowhere, with no
frontmatter flag ([[the-measure-section-is-a-marked-region-legal-in-any-folder-and-required-nowhere]]).
What was explicitly left undesigned then was the grammar, and this is that half
([[the-measure-section-carries-a-numbers-role-and-its-grammar-is-not-designed]]).

# The two grammars fit without a translator

**The destination bracket carries the role.** A `measure:` line written in chat names `[slug]` for
testimony and `[gauge:slug]` for a gauge, so the librarian never re-decides the kind at the ingest;
the region's opening word says the same thing on the page. They were designed a day apart
([[a-measure-line-names-its-destination-in-brackets-after-the-kind]]).

# What the parser sees today, and it is nothing

**Rule 11's marker word map is built from the folder set**, so a word that is not a folder can never
be a legal marker: `<!-- measure: subject -->` in a harness file is `malformed` and red, while
`<!-- measure -->` carries no colon and is invisible to the parser. **The escape is an accident of
spelling** — exactly like the generated-file marker that was later recognised explicitly in the same
rule ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

**And rule 11 walks the harness sweep alone** — both `CLAUDE.md` files plus every `*.md` under
`.claude/` — so a marked region inside a `wiki/` page is checked by nothing today.

# Not done

**No region exists, no grammar is parsed, and no verdict reads one.** The corpus holds pages with
`basis: measurement` and a log full of `measure:` lines, and none of them is written in this shape.
