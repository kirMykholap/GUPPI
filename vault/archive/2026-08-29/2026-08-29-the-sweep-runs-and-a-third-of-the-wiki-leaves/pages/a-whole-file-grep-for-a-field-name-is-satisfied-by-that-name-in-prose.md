---
title: "A whole-file grep for a field name is satisfied by that name in prose"
type: lesson
status: archived
authority: field-presence-grep
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "wiki/proposals/links-is-filled-by-a-script-from-the-bodys-wikilinks.md"]
tags: [vault, record-schema, process]
---

# The incident

**A guard asked *does this page already carry `decided_by:`* by grepping the whole file.** It hit the
phrase in the body of `wiki/proposals/links-is-filled-by-a-script-from-the-bodys-wikilinks.md:84`,
concluded the field was present, and aborted a back-fill at page eighteen of twenty-six.

**Repaired by narrowing the guard to the frontmatter block**, which is the only place the question
has a meaning.

# The family

**The same class as [[an-example-inside-a-code-block-satisfies-a-search]], one level down.** There
the searched-for thing was quoted inside a fence; here it is a field name used as ordinary English
in a page about that field.

**A corpus that documents its own schema will always have this problem**: every field name appears
in prose somewhere, because the pages explaining the fields are in the corpus.

# The rule that follows

**A question about frontmatter is asked of the frontmatter.** Presence of a key is a structural
question and the structure is delimited — the block between the first two `---` lines — so there is
never a reason to ask it of the whole file.
